from django.urls import path
from .views import HomePageView, FilmsPageView

app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('films/', FilmsPageView.as_view(), name='films')
]