import random
from abc import ABCMeta, abstractmethod
from card import Card

# a b c
class GameBase(metaclass=ABCMeta):
    @abstractmethod
    def start(self):
        pass

class CardDeck(GameBase):
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self):
        self._make_deck()


    def start(self):
        print("starting up")

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)
    
    @property
    def cards(self):
        return self._cards
    
    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()
    
    @classmethod
    def get_ranks(cls):
        return cls.RANKS
    
    def __len__(self):  # works with len(x)
        return len(self.cards)
    
    def __add__(self, other):  # self + other
        my_class = type(self)
        new_deck = my_class()  # new_deck = CardDeck()
        new_deck._cards = self.cards + other.cards
        return new_deck
    
    #  deck[x]
    #  deck ** y


if __name__ == "__main__":
    d1 = CardDeck()
    d2 = CardDeck()
    print(f"{d1.cards = }")
    d1.shuffle()
    print(f"{d1.cards = }")
    for i in range(5):
        card = d1.draw()
        print(card)
    print(d1.get_ranks())
    print(CardDeck.get_ranks())
    print(f"{len(d1) = }")
    
    d3 = d1 + d2
    print(f"{d3 = }")
    print(f"{len(d3) = }")
    print(f"{d3.cards = }")
    