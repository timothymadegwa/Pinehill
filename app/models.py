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
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    requirements = models.TextField()
    posted = models.DateField(default=datetime.now)
    closing = models.DateField()
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class JobApplication(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    cover = models.FileField(upload_to='jobs/covers')
    cv = models.FileField(upload_to='jobs/cv')

    def __str__(self):
        return self.first_name + self.last_name


    