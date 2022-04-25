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
            is_liked = request.POST.get('is_liked')
            if is_liked == 'True':
                if RatingModel.objects.all().filter(film=film, is_liked=False, user=request.user).exists():
                    dislike = RatingModel.objects.get(film=film, is_liked=False)
                    dislike.user.remove(request.user)
                    if dislike.user.count() <= 0:
                        RatingModel.objects.filter(film=film, is_liked=False).delete()
                    if RatingModel.objects.all().filter(film=film, is_liked=is_liked).exists():
                        rate = RatingModel.objects.get(film=film, is_liked=is_liked)
                        rate.user.add(request.user)
                    else:
                        RatingModel.objects.create(film=film, is_liked=is_liked).user.add(request.user)
                else:
                    if RatingModel.objects.all().filter(film=film, is_liked=is_liked).exists():
                        rate = RatingModel.objects.get(film=film, is_liked=is_liked)
                        if RatingModel.objects.all().filter(film=film, is_liked=is_liked, user=request.user).exists():
                            rate.user.remove(request.user)
                            if rate.user.count() <= 0:
                                RatingModel.objects.filter(film=film, is_liked=is_liked).delete()
                        else:
                            rate.user.add(request.user)
                    else:
                        RatingModel.objects.create(film=film, is_liked=is_liked).user.add(request.user)
            elif is_liked == 'False':
                if RatingModel.objects.all().filter(film=film, is_liked=True, user=request.user).exists():
                    like = RatingModel.objects.get(film=film, is_liked=True)
                    like.user.remove(request.user)
                    if like.user.count() <= 0:
                        RatingModel.objects.filter(film=film, is_liked=True).delete()
                    if RatingModel.objects.all().filter(film=film, is_liked=is_liked).exists():
                        rate = RatingModel.objects.get(film=film, is_liked=is_liked)
                        rate.user.add(request.user)
                    else:
                        RatingModel.objects.create(film=film, is_liked=is_liked).user.add(request.user)
                else:
                    if RatingModel.objects.all().filter(film=film, is_liked=is_liked).exists():
                        rate = RatingModel.objects.get(film=film, is_liked=is_liked)
                        if RatingModel.objects.all().filter(film=film, is_liked=is_liked, user=request.user).exists():
                            rate.user.remove(request.user)
                            if rate.user.count() <= 0:
                                RatingModel.objects.filter(film=film, is_liked=is_liked).delete()
                        else:
                            rate.user.add(request.user)
                    else:
                        RatingModel.objects.create(film=film, is_liked=is_liked).user.add(request.user)

    return HttpResponseRedirect(reverse('pages:watch', args=[str(pk)]))
