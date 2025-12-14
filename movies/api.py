from django.http import JsonResponse
from .models import Movie

def get_movie(request):
    code = request.GET.get('code', '').lower().strip()

    if not code:
        return JsonResponse({'status': 'error'})

    movie = Movie.objects.filter(code=code).first()
    if not movie:
        return JsonResponse({'status': 'not_found'})

    movie.views += 1
    movie.save()

    return JsonResponse({
        'status': 'ok',
        'title': movie.title,
        'file_id': movie.file_id,
        'views': movie.views
    })
