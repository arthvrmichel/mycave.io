from django.db import models

# Create your models here.
class Platform(models.Model):
    name = models.CharField(max_length=200)
    abbreviation = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return self.name

class Version(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name
    
class Game(models.Model):
    name = models.CharField(max_length=200)
    platforms = models.ManyToManyField(Platform)

    def __str__(self) -> str:
        return self.name
