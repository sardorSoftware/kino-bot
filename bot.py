import os
import django
import telebot

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from movies.models import Movie

BOT_TOKEN = "8419632249:AAE52t-l4s3LyTaXk8uSpUkecxalSZifeEk"

bot = telebot.TeleBot(BOT_TOKEN)

# START
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "🎬 Kino botga xush kelibsiz!\n\nKino kodini yozing (masalan: kino9)"
    )

# VIDEO FILE_ID OLISH (VAQTINCHA)
@bot.message_handler(content_types=['video'])
def get_file_id(message):
    bot.send_message(
        message.chat.id,
        f"FILE_ID:\n{message.video.file_id}"
    )

# KINO QIDIRISH
@bot.message_handler(func=lambda message: True)
def send_movie(message):
    code = message.text.lower().strip()

    movie = Movie.objects.filter(code=code).first()

    if movie:
        movie.views += 1
        movie.save()

        bot.send_video(
            message.chat.id,
            movie.file_id,
            caption=f"🎬 {movie.title}\n👁 {movie.views} marta ko‘rilgan"
        )
    else:
        bot.send_message(message.chat.id, "❌ Bunday kino topilmadi")

print("Bot ishga tushdi...")
bot.infinity_polling()
