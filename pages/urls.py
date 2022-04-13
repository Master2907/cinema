from django.urls import path
from .views import *

app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('films/', FilmsPageView.as_view(), name='films'),
    path('cartoons/', CartoonPageView.as_view(), name='cartoon'),
    path('search/', SearchPageView.as_view(), name='search'),
    path('<int:pk>/watch/', film_watch, name='watch'),
    path('<int:pk>/comment', leave_comment, name='leave_comment'),
    path('liked/', LikedFilmsView.as_view(), name='liked-films'),
    path('<int:pk>/save', save_view, name='save-film'),
    path('saved/', SavedView.as_view(), name='saved-films')
]
