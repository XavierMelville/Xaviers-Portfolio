from django.shortcuts import render
from .models import NounCard
from .models import CustomerCard

#sort and concatenating pattern from stackoverflow
#http://stackoverflow.com/questions/431628/how-to-combine-2-or-more-querysets-in-a-django-view
from itertools import chain
from operator import attrgetter



def card_list(request):
    #Concatenate both tables with chain
    #Then sort them alphabettically by text with sorted and attrgetter
    orderedAllCardList = sorted(
        chain(CustomerCard.objects.all(), NounCard.objects.all()),
        key=attrgetter('text'))
    return render(request, 'tigeroil/card_list.html', {'cards':orderedAllCardList})
