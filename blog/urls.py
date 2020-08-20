from django.urls import path

from . import views

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('<str:slug>', views.blog, name='blog')

]