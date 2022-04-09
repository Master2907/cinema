from django.db import models
from django.contrib.auth import get_user_model
from films.models import FilmModel

UserModel = get_user_model()


class RatingModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name='user')
    film = models.ForeignKey(FilmModel, on_delete=models.CASCADE, verbose_name='film')
    is_liked = models.BooleanField(verbose_name='is liked')

    def likes_count(self):
        return self.is_liked.count()

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = 'rating'
        verbose_name_plural = 'ratings'
