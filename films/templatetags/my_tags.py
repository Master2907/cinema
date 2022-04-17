from django import template

from films.models import SavedFilmsModel
from films.models import FilmModel

register = template.Library()


@register.filter
def is_saved(film, user):
    return SavedFilmsModel.objects.filter(user=user, film=film).exists()
