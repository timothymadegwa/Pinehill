from django.db import models
from datetime import datetime 

# Create your models here.
class Contact(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=50, default='number')
    message = models.TextField()
    requirements = models.TextField()
    posted = models.DateField(default=datetime.now)

    def __str__(self):
        return self.company

class Team(models.Model):

    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    profile = models.TextField()
    photo = models.ImageField(upload_to='photos/team')
    email = models.CharField(max_length=100, blank=True)
    linkedin = models.CharField(max_length=100, blank=True, null=True)
    hobbies = models.TextField(blank=True, null=True)
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
    closing = models.DateTimeField()
    is_published = models.BooleanField(default=True)
    pdf = models.FileField(upload_to='jobs/pdf', null=True)

    def __str__(self):
        return self.title

class TalentPool(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    cv = models.FileField(upload_to='jobs/talent/cv')

    def __str__(self):
        return self.first_name


class JobApplication(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    cover = models.FileField(upload_to='jobs/covers')
    cv = models.FileField(upload_to='jobs/cv')

    def __str__(self):
        return self.first_name + self.last_name


    