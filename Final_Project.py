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


def play_game(deck, dealer_hand, player_hand, money):
    bet = float(input("Bet amount: "))
    print()
    print("DEALER'S SHOW CARD:")
    dealer_card = dealer_hand[0]
    print(f"{dealer_card[1]} of {dealer_card[0]}\n")
    print("YOUR CARDS:")
    for card in player_hand:
        print(f"{card[1]} of {card[0]}")
    while True:
        print()
        hit_stand = input("Hit or stand? (hit/stand): ").lower()
        if hit_stand == 'hit':
            card = deck.pop()
            player_hand.append(card)
            print("\nYOUR CARDS:")
            for card in player_hand:
                print(f"{card[1]} of {card[0]}")
        elif hit_stand== 'stand':
            dealer_hand = dealer_totals(deck, dealer_hand)
            print("\nDEALER'S CARDS:")
            for card in dealer_hand:
                print(f"{card[1]} of {card[0]}")
            break
    player_total = totals(player_hand)
    dealer_total = totals(dealer_hand)
    print(f"\nYOUR POINTS:\t",player_total)
    print(f"DEALER'S POINTS:",dealer_total)
    if player_total > 21:
        print("\nPlayer Bust!")
        money -= bet
    elif dealer_total > 21:
        print("\nDealer Bust! You Win!")
        money = money - bet + bet *1.5
    elif player_total > dealer_total:
        print("\nYou Win!!")
        money = money - bet + bet *1.5
    elif player_total < dealer_total:
        print("\nSorry. You lose.")
        money -= bet
    else:
        print("It is a tie!")
    print(f"Money: ${money}")
    return money

def totals(hand):
    total = sum(card[2] for card in hand)
    aces = sum(1 for card in hand if card[1] == 'A')
    while total > 21 and aces:
        total -= 10
        aces -=1
    return total

def dealer_totals(deck, dealer_hand):
    while totals(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    return dealer_hand



def main():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2\n")
    money = db.read_money()
    deck = deck_cards()
    dealer_hand, player_hand = hands(deck)
    money = play_game(deck, dealer_hand, player_hand, money)
    db.write_money(money)
   


if __name__ =="__main__":
    main()
