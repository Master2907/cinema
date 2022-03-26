from django.shortcuts import render
from films.models import FilmModel, BannerModel, TagModel, GenreModel
from django.views.generic import TemplateView, ListView
from datetime import datetime


class HomePageView(ListView):
    model = FilmModel
    template_name = 'main/index.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(HomePageView, self, *args, **kwargs).get_context_data()
        context['banners'] = BannerModel.objects.all()
        context['adventure'] = FilmModel.objects.all().filter(genre__name='Adventure')
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

        return context

    def get_queryset(self):
        qs = FilmModel.objects.all().filter(movie_type='film')
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

        return context

    def get_queryset(self):
        qs = FilmModel.objects.all().filter(movie_type='cartoon')
        return qs
