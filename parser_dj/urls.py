from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('anime/', views.AnimeView.as_view(), name='naruto'),
    path('parser/', views.ParserAnimeView.as_view(), name='parser'),
    # path('jutsu1/', views.SerialView.as_view(), name='serial'),
    # path('jutsu2/', views.ParserJutsuView.as_view(), name='jutsuparser'),
]