import sys
import os
import django
from django.db import models

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()



class Game(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    raiting = models.IntegerField()
    
class Genre(models.Model):
    name = models.CharField(max_length=50)
    games = models.ManyToManyField(Game, related_name="games")

strategy = Genre.objects.create(name = 'strategy')
horror = Genre.objects.create(name = 'horror')

Silent_Hill = Game.objects.create(name = 'Silent Hill', year = 1999, raiting = 86)
Civilization4 = Game.objects.create(name = 'Civilization4', year = 2005, raiting = 94)