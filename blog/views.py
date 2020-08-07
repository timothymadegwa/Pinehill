from django.shortcuts import render
from .models import ExternalBlog, Video, BlogPost

def blogs(request):
    blogs = BlogPost.objects.all().filter(is_published=True)
    external = ExternalBlog.objects.all().filter(is_published=True)
    videos = Video.objects.all().filter(is_published=True)
    context = {
        'blogs' : blogs,
        'external' : external,
        'videos' : videos
    }
    return render(request, "blog/media.html", context)
