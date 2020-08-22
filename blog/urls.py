from django.urls import path

from . import views

urlpatterns = [
    path('', views.media, name='media'),
    path('<str:slug>', views.blog, name='blog'),
    path('all_blogs/', views.all_blogs, name='all_blogs'),

]