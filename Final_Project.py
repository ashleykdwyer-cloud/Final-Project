import random
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

def check_blackjack(hand):
    return len(hand) == 2 and totals(hand) == 21
         
def bet(money):
    while True:
        try:
            bet_amount = float(input("Bet amount: "))
        except ValueError:
            print("Invalid bet input. Enter valid number.\n")
            continue
        
        if bet_amount < 5:
            print("Bet must be a min of $5 and max of $1000. Try again!\n")
            continue
        elif bet_amount > 1000:
            print("Bet must be a max of $1000 and min of $5. Try again!\n")
            continue
        elif bet_amount > money:
            print(f"You do not have enough money. You have ${money}, try again!\n")
            continue
        else:
            return bet_amount

def dealer_totals(deck, dealer_hand):
    while totals(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    return dealer_hand


def totals(hand):
    total = sum(card[2] for card in hand)
    aces = sum(1 for card in hand if card[1] == 'A')
    while total > 21 and aces:
        total -= 10
        aces -=1
    return total


def money_balance(money):
    if money < 5:
        chips= input(f"Your balance is {money}, would you like to buy more chips? (y/n): ").lower()
        if chips == 'y':
            amount = float(input("Enter the amount you would like to buy: "))
            money += amount
            db.write_money(money)
            print(f"New balance: {money}")
            return money
        else:
            return None


def play_game(deck, dealer_hand, player_hand, money):
    money = money_balance(money) or money
    bet_amount = bet(money)
    print()
    print("DEALER'S SHOW CARD:")
    dealer_card = dealer_hand[0]
    print(f"{dealer_card[1]} of {dealer_card[0]}\n")
    print("YOUR CARDS:")
    for card in player_hand:
        print(f"{card[1]} of {card[0]}")
      
    player_blackjack = check_blackjack(player_hand)
    dealer_blackjack = check_blackjack(dealer_hand)
    if player_blackjack or dealer_blackjack:
        print("\nDEALER'S CARDS:")
        for card in dealer_hand:
            print(f"{card[1]} of {card[0]}")

            if player_blackjack:
                print("\nBLACKJACK! You win!!")
                money += bet_amount * 1.5
                money = round(money, 2)
                print(f"Money: ${money}")
                return money
            elif dealer_blackjack:
                print("\nDealer has blackjack, you lose!")
                money -= bet_amount
                print(f"Money: ${money}")
                return money
            elif player_blackjack and dealer_blackjack:
                print("You both have blackjack, it is a tie!")
                print(f"Money: ${money}")

    while True:
        print()
        hit_stand = input("Hit or stand? (hit/stand): ").lower()
        if hit_stand == 'hit':
            card = deck.pop()
            player_hand.append(card)
            print("\nYOUR CARDS:")
            for card in player_hand:
                print(f"{card[1]} of {card[0]}")
            if totals(player_hand) > 21:
                break
        elif hit_stand== 'stand':
            break
    
    player_total = totals(player_hand)
    if player_total > 21:
        print("\nPlayer Bust!")
        money -= bet_amount
        print(f"Money: ${money}")
        return money
    else:
        dealer_hand = dealer_totals(deck, dealer_hand)

    dealer_total = totals(dealer_hand)
    print("\nDEALER'S CARDS:")
    for card in dealer_hand:
        print(f"{card[1]} of {card[0]}")
    print(f"\nYOUR POINTS:\t",player_total)
    print(f"DEALER'S POINTS:",dealer_total)
    
    if dealer_total > 21:
        print("\nDealer Bust! You Win!")
        money += bet_amount
    elif player_total > dealer_total:
        print("\nYou Win!!")
        money += bet_amount
    elif player_total < dealer_total:
        print("\nSorry. You lose.")
        money -= bet_amount
    else:
        print("It is a tie!")
    print(f"Money: ${money}")
    return money


    
def main():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2\n")
    money = db.read_money()
    play_again = 'y'
    while True:
        deck = deck_cards()
        dealer_hand, player_hand = hands(deck)
        money = play_game(deck, dealer_hand, player_hand, money)
        db.write_money(money)
        play_again = input("\nPlay again? (y/n): ")
        print()
        if play_again != 'y':
            break
    print("\nCome back soon!\nBye!")
       


if __name__ =="__main__":
    main()
