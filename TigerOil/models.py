from __future__ import unicode_literals

from django.db import models

# Create your models here.

#The database of noun cards
class NounCard(models.Model):
    #author = models.ForeignKey('auth.User', default ='xavier')
    cardAuthor = models.CharField(max_length=50, default="Xavier Melville")
    text = models.CharField(max_length=30)
    adult = models.BooleanField(default=False)
    cardType = models.CharField(max_length=50, default="Noun")

    def __str__(self):
        return self.text

#The database of customer cards
class CustomerCard(models.Model):
    #author = models.ForeignKey('auth.User',default='xavier')
    cardAuthor = models.CharField(max_length=50, default="Xavier Melville")
    text = models.CharField(max_length=30)
    adult = models.BooleanField(default=False)
    cardType = models.CharField(max_length=50, default="Customer")
    def __str__(self):
        return self.text

# a single player
class Player(models.Model):
    player_name = models.CharField(max_length=50, default="") #add constriant to be unique
    #game = Game()

# the database of ongoing games
class Game(models.Model):
    game_name = models.CharField(max_length=50) #add constraint to be unique
    #time_created = models.Time()
    #players = models.Player[]
