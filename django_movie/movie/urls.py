from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    path('', views.MovieView.as_view(), name='movie_list'),
]
