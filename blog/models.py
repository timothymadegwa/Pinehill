from django.db import models
from app.models import Team
from datetime import date

class BlogPost(models.Model):
    author = models.ForeignKey(Team, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    paragraph_1 = models.TextField(blank=False, null=False)
    image_1 = models.ImageField(upload_to='photos/blogs', null=True, blank=True)
    caption_1 = models.CharField(max_length=100, blank=True, null=True)
    paragraph_2 = models.TextField(blank=True, null=True)
    image_2 = models.ImageField(upload_to='photos/blogs', null=True, blank=True)
    caption_2 = models.CharField(max_length=100, blank=True, null=True)
    paragraph_3 = models.TextField(blank=True, null=True)
    image_3 = models.ImageField(upload_to='photos/blogs', null=True, blank=True)
    caption_3 = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(default=date.today)
    views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class ExternalBlog(models.Model):

    title = models.CharField(max_length=100)
    date = models.DateField()
    author = models.CharField(max_length=100, blank=True)
    is_published = models.BooleanField(default=True)
    link = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.title

class Video(models.Model):

    title = models.CharField(max_length=100)
    is_published = models.BooleanField(default=True)
    link = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.title