from django.shortcuts import render
from .models import ExternalBlog, Video

def blog(request):
    external = ExternalBlog.objects.all().filter(is_published=True)
    videos = Video.objects.all().filter(is_published=True)
    context = {
        'external' : external,
        'videos' : videos
    }
    return render(request, "blog/media.html", context)
