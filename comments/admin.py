from django.contrib import admin
from .models import *


@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'film']
    list_display_links = ['id', 'user', 'film']
    search_fields = ['user']
    list_filter = ['created_at']
