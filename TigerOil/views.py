from django.shortcuts import render
from .models import NounCard
from .models import CustomerCard

# how to import files from subdirectories from
# http://stackoverflow.com/questions/1260792/python-import-a-file-from-a-subdirectory
# how to fis nodeule object is not callable
# http://stackoverflow.com/questions/4534438/typeerror-module-object-is-not-callable
from SnakeOil.Card import Card
from SnakeOil.Deck import Deck
from SnakeOil.Game import Game
from SnakeOil.Player import Player

#sort and concatenating pattern from stackoverflow
#http://stackoverflow.com/questions/431628/how-to-combine-2-or-more-querysets-in-a-django-view
from itertools import chain
from operator import attrgetter


# return a list of all the noun and customer cards in the database
def card_list(request):
    #Concatenate both tables with chain
    #Then sort them alphabettically by text with sorted and attrgetter
    orderedAllCardList = sorted(
        chain(CustomerCard.objects.all(), NounCard.objects.all()),
        key=attrgetter('text'))
    return render(request, 'tigeroil/card_list.html', {'cards':orderedAllCardList})

# see the current state of the game
def game(request):

    # generate 4 fake players
    players = []
    players.append(Player("Player 1"))
    players.append(Player("Player 2"))
    players.append(Player("Player 3"))
    players.append(Player("Player 4"))

    # start a new game
    game = Game(players)

    print('Game successfully completed itself')
    # return the game object containing all the details of the game
    return render(request, 'tigeroil/game.html', {'game':game})
