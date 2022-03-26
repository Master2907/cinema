from django.shortcuts import render
from films.models import FilmModel, BannerModel
from django.views.generic import TemplateView, ListView


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
    paginate_by = 24

    def get_queryset(self):
        film = FilmModel.objects.all().filter(movie_type='film')
        return film


