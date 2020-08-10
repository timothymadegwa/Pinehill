from django.shortcuts import render, get_object_or_404
from .models import ExternalBlog, Video, BlogPost
from django.http import HttpResponse

def blogs(request):
    blogs = BlogPost.objects.filter(is_published=True)
    external = ExternalBlog.objects.filter(is_published=True)
    videos = Video.objects.filter(is_published=True)
    context = {
        'blogs' : blogs,
        'external' : external,
        'videos' : videos
    }
    return render(request, "blog/media.html", context)

def blog(request, blog_id):
    blog = get_object_or_404(BlogPost, pk=blog_id)
    blogs = BlogPost.objects
    recent_blogs = blogs.order_by('date').exclude(id=blog_id)[:5]
    popular_blogs = blogs.order_by('views').exclude(id=blog_id)[:5]
    views = blog.views
    blog.views = views + 1
    blog.save()

    context = {
        'blog' : blog,
        'recent_blogs' : recent_blogs,
        'popular_blogs' : popular_blogs
    }
    return render(request, 'blog/blog.html', context)
