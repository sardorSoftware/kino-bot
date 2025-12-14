import requests
import telebot

BOT_TOKEN = "BOT_TOKEN_BU_YERGA"
API_URL = "https://USERNAME.pythonanywhere.com/api/movie/"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "🎬 Kino bot\nKino kodini yozing (masalan: kino9)"
    )

@bot.message_handler(func=lambda message: True)
def send_movie(message):
    code = message.text.strip().lower()

    r = requests.get(API_URL, params={'code': code})
    data = r.json()

    if data['status'] == 'ok':
        bot.send_video(
            message.chat.id,
            data['file_id'],
            caption=f"🎬 {data['title']}\n👁 {data['views']} marta ko‘rildi"
        )
    else:
        bot.send_message(message.chat.id, "❌ Kino topilmadi")
bot.infinity_polling()
