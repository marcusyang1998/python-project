from cards import Card
import random


class Game:
    def __init__(self):
        self.size = 4
        self.card_options = ['add', 'boo', 'Cat', 'Dev', 'Egg', 'Far', 'Gum']
        self.columns = ['A', 'B', 'C', 'D']
        self.cards = []
        self.locations = []
        for column in self.columns:
            for num in range(1, self.size + 1):
                print(f'{column}{num}')


# grid size
# card options
# column
# method
# method:
    # create cards
    # create grid
    # check for matches
    # check game won
    # run the game
# dunder main:
if __name__ == '__main__':
    Game()
    # create game instance
    # call start game
