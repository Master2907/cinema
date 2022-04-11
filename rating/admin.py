from django.contrib import admin
from .models import *


@admin.register(RatingModel)
class RatingModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'film', 'is_liked']
    list_display_links = ['id', 'user', 'film']
    search_fields = ['user']
