from django.urls import path

app_name = 'pages'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]