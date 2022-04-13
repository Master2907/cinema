from django.db.models import Count
from django.shortcuts import render
from django.urls import reverse

from films.models import FilmModel, BannerModel, TagModel, GenreModel, YearModel, SavedFilmsModel
from comments.models import CommentModel
from django.views.generic import DetailView, ListView
from django.shortcuts import render, redirect, get_object_or_404
from comments.forms import CommentForm
from films.forms import SaveForm
from django.http import HttpResponseRedirect
from rating.models import RatingModel


class HomePageView(ListView):
    model = FilmModel
    template_name = 'main/index.html'
    saved = False

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(HomePageView, self, *args, **kwargs).get_context_data()
        context['banners'] = BannerModel.objects.all().order_by('-id')[:4]
        context['all_films'] = FilmModel.objects.all().order_by('-created_at')
        context['type_film'] = FilmModel.objects.all().filter(movie_type='film').order_by('-created_at')
        context['type_cartoon'] = FilmModel.objects.all().filter(movie_type='cartoon').order_by('-created_at')
        context['most_rated'] = RatingModel.objects.filter(is_liked=True)
        return context


class FilmsPageView(ListView):
    model = FilmModel
    template_name = 'main/films.html'
    paginate_by = 24
    context_object_name = 'films'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(FilmsPageView, self, **kwargs).get_context_data()
        context['tags'] = TagModel.objects.all()
        context['genres'] = GenreModel.objects.all()
        context['years'] = YearModel.objects.all().order_by('-year')

        return context

    def get_queryset(self):
        qs = FilmModel.objects.all().filter(movie_type='film')

        genre = self.request.GET.get('genre')
        if genre:
            qs = qs.filter(genre__id=genre)

        year = self.request.GET.get('year')
        if year:
            qs = qs.filter(year__year=year)

        tag = self.request.GET.get('tag')
        if tag:
            qs = qs.filter(tag__id=tag)

        rating = self.request.GET.get('rating')
        if rating:
            if rating == '1':
                qs = qs.order_by('-ratingmodel__is_liked')
            if rating == '2':
                qs = qs.order_by('ratingmodel__is_liked')

        return qs


class CartoonPageView(ListView):
    model = FilmModel
    template_name = 'main/cartoons.html'
    paginate_by = 24
    context_object_name = 'films'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CartoonPageView, self, **kwargs).get_context_data()
        context['tags'] = TagModel.objects.all()
        context['genres'] = GenreModel.objects.all()
        context['years'] = YearModel.objects.all().order_by('-year')

        return context

    def get_queryset(self):
        qs = FilmModel.objects.all().filter(movie_type='cartoon')

        genre = self.request.GET.get('genre')
        if genre:
            qs = qs.filter(genre__id=genre)

        year = self.request.GET.get('year')
        if year:
            qs = qs.filter(year__year=year)

        tag = self.request.GET.get('tag')
        if tag:
            qs = qs.filter(tag__id=tag)

        rating = self.request.GET.get('rating')
        if rating:
            if rating == '1':
                qs = qs.order_by('-ratingmodel__is_liked')
            if rating == '2':
                qs = qs.order_by('ratingmodel__is_liked')

        return qs


class SearchPageView(ListView):
    model = FilmModel
    template_name = 'main/search.html'
    paginate_by = 12

    def get_queryset(self):
        qs = FilmModel.objects.all()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(name__icontains=q)
            return qs
        else:
            return qs


def leave_comment(request, pk):
    film = get_object_or_404(FilmModel.objects.all().filter(id=pk))
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            user = request.user
            comment = request.POST.get('comment')
            if CommentModel.objects.filter(user=user, film=film, comment=comment).exists():
                pass
            else:
                CommentModel.objects.create(user=user, film=film, comment=comment)
    else:
        form = CommentForm()
    return HttpResponseRedirect(reverse('pages:watch', args=[str(pk)]))


def film_watch(request, pk):
    films = FilmModel.objects.all()
    film = get_object_or_404(FilmModel.objects.all().filter(id=pk))
    comments = CommentModel.objects.all().filter(film_id=pk).order_by('created_at')
    liked = False
    disliked = False
    if request.user.is_authenticated:
        if RatingModel.objects.filter(user=request.user, film=film, is_liked=True).exists():
            liked = True
        elif RatingModel.objects.filter(user=request.user, film=film, is_liked=False).exists():
            disliked = True

    return render(request, 'main/watch.html', context={
        'film': film,
        'comments': comments,
        'liked': liked,
        'disliked': disliked,
        'total_dislikes': RatingModel.objects.all().filter(is_liked=False, film=film).count(),
        'total_likes': RatingModel.objects.all().filter(is_liked=True, film=film).count(),
        'related': set(FilmModel.objects.all().filter(tag__id__in=film.tag.all(), genre__id__in=film.genre.all()).exclude(id=pk)),
    })


class LikedFilmsView(ListView):
    model = RatingModel
    template_name = 'main/liked-films.html'
    paginate_by = 24

    def get_queryset(self):
        qs = RatingModel.objects.all().filter(user=self.request.user, is_liked=True).order_by('-created_at')

        return qs


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


class SavedView(ListView):
    model = FilmModel
    template_name = 'main/saved-films.html'

    def get_queryset(self):
        qs = SavedFilmsModel.objects.all().filter(user=self.request.user).order_by('-created_at')
        return qs
