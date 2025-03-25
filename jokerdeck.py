from card import Card
from carddeck import CardDeck

class Game:
    def start(self):
        print("starting...")

class JokerDeck(CardDeck, Game):

    def _make_deck(self):
        super()._make_deck()  # d'oh!!!
        for joker_number in 1, 2:
            card = Card(f"JOKER-{joker_number}", "** JOKER **")
            self._cards.append(card)

if __name__ == "__main__":
    j = JokerDeck()
    j.shuffle()
    j.start()
    print(j.cards)
    for i in range(5):
        print(j.draw())
    print(f"{JokerDeck.mro() = }")
    
