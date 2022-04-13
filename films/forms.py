from django.forms import ModelForm
from .models import SavedFilmsModel


class SaveForm(ModelForm):
    class Meta:
        model = SavedFilmsModel
        fields = '__all__'
        exclude = ('user', 'film')
