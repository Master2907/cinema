from django.contrib import admin
from .models import *


@admin.register(TagModel)
class TagModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    list_filter = ['created_at']


@admin.register(GenreModel)
class GenreModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    list_filter = ['created_at']


@admin.register(FilmModel)
class FilmModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'movie_type', 'year', 'age']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'genre', 'tag', 'description']
    list_filter = ['created_at', 'movie_type']


@admin.register(BannerModel)
class BannerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    list_filter = ['created_at']


@admin.register(YearModel)
class BannerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'year']

