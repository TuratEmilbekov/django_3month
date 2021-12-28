import requests
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView, FormView
# from django.views.generic.edit import FormView
from . import models, forms, parser

# Create your views here.
class AnimeView(ListView):
    model = models.Film
    template_name = 'anime_list.html'

    def get_queryset(self):
        return models.Film.objects.all()

class ParserAnimeView(FormView):
    template_name = 'anime_parser.html'
    form_class = forms.ParserForm
    success_url = '/anime/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponseRedirect(self.success_url)
        else:
            return super (ParserAnimeView, self).post(request, *args, **kwargs)


# class SerialView(ListView):
#     model = models.Serial
#     template_name = 'jutsu_list.html'

#     def get_queryset(self):
#         return models.Serial.objects.all()

# class ParserJutsuView(FormView):
#     template_name = 'jutsu_parser.html'
#     form_class = forms.ParserForm
#     success_url = '/jutsu1/'

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.parser_data()
#             return HttpResponseRedirect(self.success_url)
#         else:
#             return super (ParserJutsuView, self).post(request, *args, **kwargs)

