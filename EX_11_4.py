import random


class Card:
    def __init__(self, value, figure):
        self.value = value
        self.figure = figure


class Deck:
    def __init__(self, card_list):
        self.card_list = card_list
        self.full_list = []

    def shuffle(self):
        pass

    def deal(self):
        pass


def main():

    fig = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J ', 'Q', 'K']
    col = ['Diamond', 'Clubs', 'Spades', 'Hearts']
    deck1 = Deck([])
    print(deck1.full_list)
    print(deck1.card_list)


if __name__ == "__main__":
    main()
