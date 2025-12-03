import random
import csv
import db


def deck_cards():
    card_suits = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
    card_list = [('A', 11), ('2',2), ('3',3), ('4',4), ('5',5), ('6',6), ('7',7), ('8',8), ('9',9), ('10',10), ('J',10), ('Q',10), ('K',10)]
    deck = []
    for suit in card_suits:
        for card, value in card_list:
            deck.append([suit, card, value])
    random.shuffle(deck)
    return deck

def hands(deck):
    hands = [[],[]]
    for _ in range(2):
        hands[0].append(deck.pop())
        hands[1].append(deck.pop())     
    dealer_hand = hands[0]
    player_hand = hands[1]
    return dealer_hand, player_hand

def play_game(deck, dealer_hand, player_hand):
    bet = float(input("Bet amount: "))
    print()
    print("DEALER'S SHOW CARD:")
    dealer_card = dealer_hand[0]
    print(f"{dealer_card[1]} of {dealer_card[0]}\n")
    print("YOUR CARDS:")
    for card in player_hand:
        print(f"{card[1]} of {card[0]}")
        
  

def main():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2\n")
    deck = deck_cards()
    money = db.read_money()
    dealer_hand, player_hand = hands(deck)
    play_game(deck, dealer_hand, player_hand)
   


if __name__ =="__main__":
    main()
