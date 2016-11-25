from Card import Card
from random import shuffle
"""
    This is a deck class for an implementation of snake oil
    This is where cards will be pulled from the database and stored for use by the Game class
"""

class Deck(object):

    # debugging variables
    total_cards_count = 0

    maximum_deck_size = 0

    # the list of cards still available to be played
    cards = []

    # the list of discarded cards available to be shuffled back in
    discarded_cards = []

    # what type of card the deck will hold. not sure how to refactor this
    # this is used in create_card to determine where to pull cards from
    card_type = "Unassigned Card Type"

    # constructor to set the deck size and type, as well as fill the deck with cards
    def __init__(self, maximum_deck_size, card_type):
        self.maximum_deck_size = maximum_deck_size
        self.card_type = card_type
        self.fill_deck()

    # fill the deck until it's the maximum size.
    def fill_deck(self):
        count = 0
        while (count < self.maximum_deck_size):
            self.cards.append(self.create_card())
            count += 1
            self.total_cards_count +=  1

    # grab the next card from the deck
    def next_card(self):
        if(len(self.cards)==0):
            self.shuffle_discard_pile()
        return self.cards.pop()

    # send a card(s) to a discard pile
    def discard_cards(self, discarded_cards):
        if(isinstance(discarded_cards,list)):
            self.discarded_cards.extend(discarded_cards)
        else:
            self.discarded_cards.append(discarded_cards)

    # shuffle the discarded cards back into the active deck
    def shuffle_discard_pile(self):
        self.cards.extend(self.discarded_cards)
        shuffle(self.cards)

    # create and return a card of the deck's type
    # currently stubbed out until database interface is implemented
    def create_card(self):
        if(self.card_type=="Noun"):
            return self.create_default_noun_card()
        elif(self.card_type=="Customer"):
            return self.create_default_customer_card()
        elif(self.card_type=="Unassigned Card Type"):
            raise ValueError("Deck's card type not assigned")
            return Card("Xavier", "Error", False, "Error")
        else:
            raise ValueError("%s card type is not implemented" % (card_type))
            return Card("Xavier", "Error", False, "Error")


    # create and return a default noun card for a snake oil deck
    def create_default_noun_card(self):
        return Card("Xavier", "Body", False, "Noun")

    # create and return a default customer card for a snake oil deck
    def create_default_customer_card(self):
        return Card("Xavier", "Therapist", False, "Customer")

# old implementation that included both decks in one deck class
"""
    # the list of noun and customer cards.
    # when played, cards will be placed in the discard pile or 'used'
    # to later be shuffled back into the deck
    noun_cards = Card[]
    used_noun_cards = Card[]

    customer_cards = Card[]
    used_customer_cards = Card[]

    def __init__(self, cards_per_deck, ):
"""
