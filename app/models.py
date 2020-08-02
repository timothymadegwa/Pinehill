from django.db import models
from datetime import datetime

# Create your models here.
class Team(models.Model):

    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    profile = models.TextField()
    photo = models.ImageField(upload_to='photos/team')
    email = models.CharField(max_length=100)
    rank = models.IntegerField()
    is_consultant = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Contact(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField()


    def __str__(self):
        return self.first_name + ' ' + self.last_name
