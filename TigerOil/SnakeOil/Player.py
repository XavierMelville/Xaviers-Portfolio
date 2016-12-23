import Card


class Player:
    """Contains the objects and functions visible to or doable by a player

    should be kept generic enough to be reused with no or minimal changes.

    stackoverflow on how to append/extend lists
    http://stackoverflow.com/questions/3653298/concatenating-two-lists-difference-between-and-extend
    """


    # constructor that initializes only with player's name and sets points to 0
    # will likely need updating once game becomes properly online
    def __init__(self, player_name):
        self.player_name = player_name
        self.points = 0
        self.hand = []
        self.active_cards = []

    #get cards dealed from the deck
    def recieve_cards(self, cards):
        self.hand.append(cards)

    #returns the current amount of cards left in hand
    def get_hand_size(self):
        return len(self.hand)

    # play their turn, one card at a time
    def play_cards(self, cards_to_play):
        count = 0
        while (count < cards_to_play):
            self.active_cards.append(self.play_one_card())
            count+=1

    # clear active_cards and return them to the discard pile
    def discard_played_cards(self):
        discarded_cards = []
        for card in self.active_cards:
            index_of_card = self.active_cards.index(card)
            discarded_cards.append(self.active_cards.pop(index_of_card))
        return discarded_cards

    # get the player's choice of card, remove it from their hand, and return it
    def play_one_card(self):
        choice = self.get_player_card_selection()
        return self.hand.pop(0)

    # player won the round, add a point
    def win_round(self):
        self.points+=1

# interactions with client
    # return the player's choice of card
    def get_player_card_selection(self):
        return 0 #Stubbed out. will later interface with interface logic

    # get the player's choice of winner for the round
    def choose_winner(self, player_list):
        this_players_index = player_list.index(self)
        if(this_players_index!=0):
            return 0 # stubbed out
        else:
            return 1
