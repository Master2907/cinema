from django.forms import ModelForm
from .models import RatingModel


class RatingForm(ModelForm):
    class Meta:
        model = RatingModel
        fields = '__all__'
        exclude = ('user', 'film')
