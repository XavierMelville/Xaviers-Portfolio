class Card(object):
    """This class contains the values and functions related to a single card
    It should be kept generic and reusable when possible

    """
    card_author = ("Unassigned card author")
    text = ("unassigned card text")
    adult = (False)
    card_type = ("Unassigned card type")

    # construct the card from provided details
    def __init__(self, card_author, text, adult, card_type):
        self.card_author = card_author
        self.text = text
        self.adult = adult
        self.card_type = card_type
