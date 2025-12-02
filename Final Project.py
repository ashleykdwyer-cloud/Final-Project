card_suits = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
card_list = {'A': 1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}

deck = []

for suit in card_suits:
    for card, value in card_list.items():
        deck.append([suit, card, value])

for card in deck:
              print(card)
