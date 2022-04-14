from django.urls import path
from .views import *

app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('films/', FilmsPageView.as_view(), name='films'),
    path('cartoons/', CartoonPageView.as_view(), name='cartoon'),
    path('search/', SearchPageView.as_view(), name='search'),
    path('<int:pk>/watch/', film_watch, name='watch'),
    path('liked/', LikedFilmsView.as_view(), name='liked-films'),
    path('saved/', SavedView.as_view(), name='saved-films')
]
