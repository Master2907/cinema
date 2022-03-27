from django.urls import path
from .views import HomePageView, FilmsPageView, CartoonPageView, SearchPageView, FilmDetailView

app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('films/', FilmsPageView.as_view(), name='films'),
    path('cartoons/', CartoonPageView.as_view(), name='cartoon'),
    path('search/', SearchPageView.as_view(), name='search'),
    path('<int:pk>/watch/', FilmDetailView.as_view(), name='watch'),

]