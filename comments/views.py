
from django.urls import reverse
from films.models import FilmModel
from comments.models import CommentModel
from django.shortcuts import get_object_or_404
from .forms import CommentForm
from django.http import HttpResponseRedirect


def leave_comment(request, pk):
    film = get_object_or_404(FilmModel.objects.all().filter(id=pk))
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            user = request.user
            comment = request.POST.get('comment')
            CommentModel.objects.create(film=film, user=user, comment=comment)
    else:
        form = CommentForm()
    return HttpResponseRedirect(reverse('pages:watch', args=[str(pk)]))
