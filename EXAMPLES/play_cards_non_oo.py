from carddeck_non_oo import create_deck, shuffle_deck, draw_card, get_cards_in_deck

deck = create_deck("Mary")

shuffle_deck(deck)

for i in range(10):
    card = draw_card(deck)
    print(card)
print()

print(deck)

print(get_cards_in_deck(deck))

