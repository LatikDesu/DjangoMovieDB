from django.contrib import admin
from .models import Category, Genre, Movie, Movie_shots, Actor, Rating, RatingStar, Reviews
from django.utils.html import mark_safe

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)


class ReviewsInline(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ('name', 'email')


class MovieShortsInline(admin.TabularInline):
    model = Movie_shots
    extra = 1
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="111"')

    get_image.short_description = "Image"


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'draft')
    list_filter = ('category', 'year')
    search_fields = ('title', 'category__name')
    inlines = [MovieShortsInline, ReviewsInline]
    save_on_top = True
    save_as = True
    list_editable = ('draft',)
    readonly_fields = ('get_image',)
    fieldsets = (
        (None, {
            "fields": (("title", "tagline"),)
        }),
        (None, {
            "fields": ("description", ("poster", 'get_image'))
        }),
        (None, {
            "fields": (("year", "world_premiere", "country"),)
        }),
        ("Actors", {
            "classes": ("collapse",),
            "fields": (("actors", "directors", "genres", "category"),)
        }),
        (None, {
            "fields": (("budget", "fees_in_usa", "fees_in_world"),)
        }),
        ("Options", {
            "fields": (("url", "draft"),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.poster.url}" width="100" height="100"')

    get_image.short_description = "Постер"


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'parent', 'movie', 'id')
    readonly_fields = ('name', 'email')


admin.register(Genre)


class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "url")


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("name", "age", 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="60"')

    get_image.short_description = "Image"


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("ip",)


@admin.register(Movie_shots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ("title", "movie", 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="60"')

    get_image.short_description = "Image"


admin.site.register(RatingStar)


admin.site.site_title = "Movie Database"
admin.site.site_header = "Movie Database"
