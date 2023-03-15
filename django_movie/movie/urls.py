from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    path('<slug:slug>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('', views.MovieView.as_view(), name='movie_list'),
    path('review/<int:pk>/', views.AddReview.as_view(), name='add_review')

]
