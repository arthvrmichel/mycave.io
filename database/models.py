from django.db import models

# Create your models here.
class Platform(models.Model):
    name = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=10)
    
class Game(models.Model):
    name = models.CharField(max_length=200)
    platform = models.ManyToManyField(Platform)