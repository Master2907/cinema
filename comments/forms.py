from django.forms import ModelForm
from .models import CommentModel


class CommentForm(ModelForm):
    class Meta:
        model = CommentModel
        fields = '__all__'
        exclude = ('user', 'film')
