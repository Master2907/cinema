from django.db import models
from django.contrib.auth import get_user_model
from films.models import FilmModel

UserModel = get_user_model()


class RatingModel(models.Model):
    film = models.ForeignKey(FilmModel, on_delete=models.CASCADE, verbose_name='film')
    user = models.ManyToManyField(UserModel, verbose_name='user')
    is_liked = models.BooleanField(verbose_name='is liked')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created at')

    def likes_count(self):
        return self.user.count()

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = 'rating'
        verbose_name_plural = 'ratings'
