#import Player, Deck, Card
from Player import Player
from Deck import Deck
from Card import Card
from enum import Enum

CONST_DECK_SIZE = 200
CONST_POINT_LIMIT = 5
CONST_HAND_SIZE = 5
CONST_CARDS_PLAYED_PER_TURN = 2

class GameState(Enum):
    DealingCards = 0
    PlayersSelectingNounCards = 1
    PlayerMakingPitch = 2
    PlayerSelectingWinner = 3
    RestartingRound = 4

class Game:
    """ Contains the main business logic of the game
    including setting up players, dealing hands, and operating rounds

    player_list = []
    current_customer = Player
    current_customer_card = Card
    noun_deck = Deck
    customer_deck = Deck

    """

    # the game constructor
    # fills out player hands, chooses first customer and begins round loop
    def __init__ (self, player_list):

        # set the state to currently processing the game
        self.game_state = GameState.DealingCards

        # create both decks and fill them with appropriate cards
        self.noun_deck = Deck(CONST_DECK_SIZE, "Noun")
        #print('next noun card is %s' % self.noun_deck.next_card().text)
        #print('noun deck is of type %s' % self.noun_deck.card_type)

        self.customer_deck = Deck(CONST_DECK_SIZE, "Customer")
        #print('next noun card is %s' % self.noun_deck.next_card().text)
        #print('noun deck is of type %s' % self.noun_deck.card_type)


        # store the players and fill their hands
        self.player_list = player_list
        self.give_players_cards()


        while(self.victory_condition() != True):
            self.round()


    # the logic for a single round (all players get one turn)
    # 'sellers' play two cards which starts a timer during which they can talk
    # when all sellers have made their pitch, the customer picks a seller, who gets a point
    def round(self):

        # select the new customer, based on the position of the last customer (or set it to the first customer for turn 1)
        self.determine_customer()

        # select a new customer card from the deck
        self.current_customer_card = self.customer_deck.next_card()

        # loop through each player getting their selection of cards and letting them make their pitch
        # also refill their hand after their turn
        for player in self.player_list:
            if(player!=self.current_customer):
                # player has x seconds for his turn or he can end it manually
                # timer stuff

                # play two cards and store the play in the player
                player.play_cards(CONST_CARDS_PLAYED_PER_TURN)

                # refill cards
                self.give_players_cards()

        # let the customer pick the winner
        winner = self.player_list[self.current_customer.choose_winner(self.player_list)]

        # give the winner their points
        winner.win_round()
        print('winrar: %s as a %s bought a %s %s from %s who has %d points' % (self.current_customer.player_name, self.current_customer_card.text, winner.active_cards[0].text, winner.active_cards[1].text,winner.player_name,  winner.points))

        # recycle all the active cards from each player into the deck, and the customer card
        for player in self.player_list:
            self.noun_deck.discard_cards(player.discard_played_cards())
        self.customer_deck.discard_cards(self.current_customer_card)


    # give each player the correct amount of cards
    def give_players_cards(self):
        for player in self.player_list:
            while (player.get_hand_size() < CONST_HAND_SIZE):
                player.recieve_cards(self.noun_deck.next_card())

    # check each player to see if any have won enough points to win the game
    def victory_condition(self):
        for player in self.player_list:
            if (player.points >= CONST_POINT_LIMIT):
                return True
            else:
                return False

    # determine and select the player who will next play as the CustomerCard
    # if this is the first round, the customer will be the first in the list
    def determine_customer(self):
        try:
            old_customer_index = self.player_list.index(self.current_customer)
            if(old_customer_index >= len(self.player_list)-1):
                self.current_customer = self.player_list[0]
            else:
                self.current_customer = self.player_list[old_customer_index+1]
        except AttributeError:
            self.current_customer = self.player_list[0]
