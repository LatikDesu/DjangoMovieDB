from django.contrib import admin
from .models import Category, Genre, Movie, Movie_shots, Actor, Rating, RatingStar, Reviews
# Register your models here.

admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Movie_shots)
admin.site.register(Actor)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews)
