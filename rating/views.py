from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import RatingModel
from films.models import FilmModel
from .forms import RatingForm


def rating_view(request, pk):
    film = get_object_or_404(FilmModel.objects.all().filter(id=pk))

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            user = request.user
            is_liked = request.POST.get('is_liked')
            if is_liked == 'True':
                if RatingModel.objects.filter(user=user, film=film, is_liked=True).exists():
                    RatingModel.objects.filter(user=user, film=film, is_liked=True).delete()
                else:
                    if RatingModel.objects.filter(user=user, film=film, is_liked=False).exists():
                        RatingModel.objects.filter(user=user, film=film, is_liked=False).delete()
                    RatingModel.objects.create(user=user, film=film, is_liked=True)
            else:
                if RatingModel.objects.filter(user=user, film=film, is_liked=False).exists():
                    RatingModel.objects.filter(user=user, film=film, is_liked=False).delete()
                else:
                    if RatingModel.objects.filter(user=user, film=film, is_liked=True).exists():
                        RatingModel.objects.filter(user=user, film=film, is_liked=True).delete()
                    RatingModel.objects.create(user=user, film=film, is_liked=False)
    return HttpResponseRedirect(reverse('pages:watch', args=[str(pk)]))
