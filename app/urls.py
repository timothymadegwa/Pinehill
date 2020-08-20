from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('team', views.team, name='team'),
    path('investment', views.investment, name='investment'),
    path('strategy', views.strategy, name='strategy'),
    path('research', views.research, name='research'),
    path('risk', views.risk, name='risk'),
    path('capacity', views.capacity, name='capacity'),
    path('media', views.media, name='media'),
    path('careers', views.careers, name='careers'),   
]