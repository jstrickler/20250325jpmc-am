"""
Non-OOP version of CardDeck class
"""
import random

CLUB = '\u2663'
DIAMOND = '\u2662'
HEART = '\u2661'
SPADE = '\u2660'

RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

def create_deck(dealer):
    deck = {'dealer': dealer, 'cards': []}
    for suit in CLUB, DIAMOND, HEART, SPADE:
        for rank in RANKS:
            card = rank, suit
            deck['cards'].append(card)
    return deck

def draw_card(deck):
    return deck['cards'].pop()

def shuffle_deck(deck):
    random.shuffle(deck['cards'])

def get_cards_in_deck(deck):
    return ','.join([f"{c[0]}-{c[1]}" for c in deck['cards']])

