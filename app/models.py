from django.db import models

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
