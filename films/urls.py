from django.urls import path
from .views import *

app_name = 'films'

urlpatterns = [
    path('<int:pk>/save', save_view, name='save-film')
]
