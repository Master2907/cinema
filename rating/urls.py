
from django.urls import path
from .views import rating_view

app_name = 'rating'

urlpatterns = [
    path('<int:pk>/rate', rating_view, name='rate_view')
]