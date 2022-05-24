from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from django.contrib.auth import get_user_model
from config.helpers import UploadTo
from django.contrib.auth.forms import forms
UserModel = get_user_model()

m_type = (
    ("film", "film"),
    ("cartoon", "cartoon"),
)

f_age = (
    ("6+", "6+"),
    ("8+", "8+"),
    ("12+", "12+"),
    ("16+", "16+"),
    ("18+", "18+"),
)


class YearModel(models.Model):
    year = models.PositiveIntegerField(unique=True, default=int(datetime.now().year), verbose_name=_('year'))

    def __str__(self):
        return str(self.year)

    class Meta:
        verbose_name = 'year'
        verbose_name_plural = 'years'


class GenreModel(models.Model):
    name = models.CharField(max_length=25, verbose_name=_("name"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "genre"
        verbose_name_plural = "genres"


class TagModel(models.Model):
    name = models.CharField(max_length=25, verbose_name=_("name"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created at"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "tag"
        verbose_name_plural = "tags"


class FilmModel(models.Model):
    name = models.CharField(max_length=30, verbose_name=_("name"))
    image = models.ImageField(upload_to=UploadTo('film-image'), verbose_name=_("image"))
    film_video = models.FileField(upload_to=UploadTo('film-video'), verbose_name=_("film video"))
    description = models.TextField(max_length=3000, verbose_name=_("description"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created at"))
    genre = models.ManyToManyField(GenreModel, verbose_name=_("genre"))
    tag = models.ManyToManyField(TagModel, verbose_name=_("tag"))
    year = models.ForeignKey(YearModel, on_delete=models.CASCADE, null=True, verbose_name="year")
    movie_type = models.CharField(max_length=20, choices=m_type, default=1, verbose_name=_("movie type"))
    age = models.CharField(max_length=3, choices=f_age, verbose_name=_('age'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('film')
        verbose_name_plural = _('films')

class BannerModel(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    banner_img = models.ImageField(upload_to=UploadTo('banners'), verbose_name=_('banner img'))
    film = models.ForeignKey(FilmModel, on_delete=models.PROTECT, verbose_name=_('film'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "banner"
        verbose_name_plural = "banners"


class SavedFilmsModel(models.Model):
    film = models.ForeignKey(FilmModel, on_delete=models.CASCADE, verbose_name=_('film'))
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name=_('user'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return f'{self.film}'

    class Meta:
        verbose_name = 'saved film'
        verbose_name_plural = 'saved films'
