from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, TemplateView
from .models import FilmModel, SavedFilmsModel
from .forms import SaveForm


def save_view(request, pk):
    film = get_object_or_404(FilmModel.objects.all().filter(id=pk))
    if request.method == 'POST':
        form = SaveForm(request.POST)
        if form.is_valid():
            user = request.user
            if SavedFilmsModel.objects.filter(user=user, film=film).exists():
                SavedFilmsModel.objects.filter(user=user, film=film).delete()
            else:
                SavedFilmsModel.objects.create(user=user, film=film)
    return redirect(request.GET.get('next', '/'))
