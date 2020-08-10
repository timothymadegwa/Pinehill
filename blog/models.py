from django.db import models
from app.models import Team
from ckeditor.fields import RichTextField
from datetime import date

class BlogPost(models.Model):
    author = models.ForeignKey(Team, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='blogs/images')
    body = RichTextField()
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