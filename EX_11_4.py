from random import shuffle


class Card:
    def __init__(self, value, figure):
        self.value = value
        self.figure = figure

    def __str__(self):
        return f'{self.value}  -  {self.figure}'

    # def __repr__(self):
    #     return f'{self.value} - '


class Deck:
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J ', 'Q', 'K']
    figures = ['Diamond', 'Clubs', 'Spades', 'Hearts']

    def __init__(self) -> None:
        self.full_list = []

    def __str__(self):
        return "".join([str(card) for card in self.full_list])

    def create_deck(self):
        for figure in Deck.figures:
            for value in Deck.values:
                self.full_list.append(Card(value, figure))

    def shuffle(self):
        shuffle(self.full_list)

    def deal(self):
        last = self.full_list.pop()
        return last


def main():

    deck1 = Deck()
    deck1.create_deck()
    print(deck1)
    deck1.shuffle()
    print("______________________________________________________________________________")
    print("______________________________________________________________________________")
    print(deck1.deal())
    print(deck1.deal())
    print(deck1.deal())

if __name__ == "__main__":
    main()
