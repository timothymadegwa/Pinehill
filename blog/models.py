from django.db import models

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