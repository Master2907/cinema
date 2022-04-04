from django.urls import path
from .views import HomePageView, FilmsPageView, CartoonPageView, SearchPageView, film_watch, like_view, dislike_view

app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('films/', FilmsPageView.as_view(), name='films'),
    path('cartoons/', CartoonPageView.as_view(), name='cartoon'),
    path('search/', SearchPageView.as_view(), name='search'),
    path('<int:pk>/watch/', film_watch, name='watch'),
    path('<int:pk>/like', like_view, name='like_film'),
    path('<int:pk>/dislike', dislike_view, name='dislike_film')
]