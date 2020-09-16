from django.shortcuts import render, get_object_or_404
from .models import ExternalBlog, Video, BlogPost
from django.http import HttpResponse

def media(request):
    blogs = BlogPost.objects.filter(is_published=True).order_by('-id')[:3]
    external = ExternalBlog.objects.filter(is_published=True)
    videos = Video.objects.filter(is_published=True)
    context = {
        'blogs' : blogs,
        'external' : external,
        'videos' : videos
    }
    return render(request, "blog/media.html", context)

def all_blogs(request):
    blogs = BlogPost.objects.filter(is_published=True).order_by('-id')
    context = {
        'blogs' : blogs,
    }
    return render(request, "blog/all_blogs.html", context)

def blog(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug)
    blogs = BlogPost.objects
    recent_blogs = blogs.filter(is_published=True).order_by('-id').exclude(slug=slug)[:3]
    popular_blogs = blogs.filter(is_published=True).order_by('-views').exclude(slug=slug)[:3]
    views = blog.views
    blog.views = views + 1
    blog.save()

    context = {
        'blog' : blog,
        'recent_blogs' : recent_blogs,
        'popular_blogs' : popular_blogs
    }
    return render(request, 'blog/blog.html', context)
