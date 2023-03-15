from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Movie

# Create your views here.


class MovieView(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(DetailView):
    model = Movie
    slug_field = 'url'
