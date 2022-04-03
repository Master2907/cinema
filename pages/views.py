from django.shortcuts import render
from films.models import FilmModel, BannerModel, TagModel, GenreModel, YearModel
from comments.models import CommentModel
from django.views.generic import DetailView, ListView
from django.shortcuts import render, redirect, get_object_or_404
from comments.forms import CommentForm

class HomePageView(ListView):
    model = FilmModel
    template_name = 'main/index.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(HomePageView, self, *args, **kwargs).get_context_data()
        context['banners'] = BannerModel.objects.all().order_by('-id')[:4]
        context['all_films'] = FilmModel.objects.all().order_by('name')
        context['type_film'] = FilmModel.objects.all().filter(movie_type='film')
        context['type_cartoon'] = FilmModel.objects.all().filter(movie_type='cartoon')

        return context


class FilmsPageView(ListView):
    model = FilmModel
    template_name = 'main/films.html'
    paginate_by = 12
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

        return qs


class CartoonPageView(ListView):
    model = FilmModel
    template_name = 'main/cartoons.html'
    paginate_by = 12
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


def film_watch(request, pk):
    film = get_object_or_404(FilmModel.objects.all().filter(id=pk))
    comments = CommentModel.objects.all().filter(film_id=pk)
    # form = CommentForm
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

    return render(request, 'main/watch.html', context={
        'film': film,
        'comments': comments,
        'form': form,
        'related': set(FilmModel.objects.all().filter(tag__id__in=film.tag.all(), genre__id__in=film.genre.all()).exclude(id=pk)),
    })
