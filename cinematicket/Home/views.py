from django.http import JsonResponse
from .models import Movie

def movie_lst(request):
    query = request.GET.get('query', None)
    if query:
        movies = Movie.objects.filter(title=query)
    else:
        movies = Movie.objects.all()

    data = {
        'movies': list(movies.values('title', 'category', 'description', 'director', 'rating'))
    }
    return JsonResponse(data)