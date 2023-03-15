from django.views.generic.base import View
from django.shortcuts import render
from .models import Movie

# Create your views here.


class MovieView(View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'movie/movies.html', {'movie_list': movies})
