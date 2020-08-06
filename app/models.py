from django.db import models
from datetime import datetime

# Create your models here.
class Team(models.Model):

    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    profile = models.TextField()
    photo = models.ImageField(upload_to='photos/team')
    email = models.CharField(max_length=100, blank=True)
    rank = models.IntegerField()
    is_consultant = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    requirements = models.TextField()
    posted = models.DateField(default=datetime.now)
    closing = models.DateField()
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title