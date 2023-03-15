from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Movie

# Create your views here.


class MovieView(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = 'movie/movies.html'


class MovieDetailView(View):
    def get(self, request, slug):
        movie = Movie.objects.get(url=slug)
        return render(request, 'movie/moviesingle.html', {'movie': movie})
