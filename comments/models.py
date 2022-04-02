from django.db import models
from django.contrib.auth import get_user_model
from films.models import FilmModel
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()


class CommentModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name=_('user'))
    film = models.ForeignKey(FilmModel, on_delete=models.CASCADE, verbose_name=_('film'))
    comment = models.TextField(max_length=1000, verbose_name=_('comment'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
