from django.shortcuts import render
from django.http import HttpResponse

def blog(request):
    return HttpResponse('<h1>this is the blog page</h1>')
