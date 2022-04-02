from django.urls import path, include
urlpatterns = [
    path('', include('registration.backends.default.urls'))
]