from django.shortcuts import render
from films.models import FilmModel
from django.views.generic import TemplateView, ListView


class HomePageView(ListView):
    model = FilmModel
    template_name = 'main/index.html'
    context_object_name = 'films'
