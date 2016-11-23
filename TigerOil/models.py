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
