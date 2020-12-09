# calss card
# hold a card
# matched or not
# location
# __eq__
# __str__

class Card:
    def __init__(self, word, location):
        self.card = word
        self.location = location
        self.matched = False

    # check if the card is matched
    def __eq__(self, other):
        return self.card == other.card
    
    # convert o bject into string
    def __str__(self):
        return self.card

# import card class into game class
if __name__ == '__main__':
        card1 = Card('egg', 'A1')
        card2 = Card('egg', 'D1')
        card3 = Card('hut', 'A4')

        print(card1 == card2)
        print(card1 == card3)
        print(card1)
