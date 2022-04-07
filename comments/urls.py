
from django.urls import path
from .views import leave_comment

app_name = 'comment'

urlpatterns = [
    path('<int:pk>/comment', leave_comment, name='leave_comment')
]