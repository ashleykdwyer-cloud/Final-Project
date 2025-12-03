import random
import csv
import db


def deck_cards():
    card_suits = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
    card_list = [['A', 11], ['2',2], ['3',3], ['4',4], ['5',5], ['6',6], ['7',7], ['8',8], ['9',9], ['10',10], ['J',10], ['Q',10], ['K',10]]
    deck = []
    for suit in card_suits:
        for card, value in card_list:
            deck.append([suit, card, value])
    random.shuffle(deck)
    hands = [["Dealer", []],[["Player"],[]]]
    dealer_hand = hands[0][1]
    player_hand = hands[1][1]


def main():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2\n")
    deck_cards()
    money = db.read_money()


if __name__ =="__main__":
    main()
