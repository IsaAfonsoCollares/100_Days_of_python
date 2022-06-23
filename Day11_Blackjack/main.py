############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can as 1.
## Use the following list as the deck of cards:
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo, cards
from random import choice
from os import system
from time import sleep

keys=list(cards.keys())


def choose_card():
    card=choice(keys)
    return card

def get_value(card):
    card_value=int(cards[card])
    return card_value

def add_card_value(card, card_value, player):
    if player == "dealer":
        dealer_cards.append(card)
        dealer_values.append(card_value)
        return dealer_cards, dealer_values
    elif player =="user":
        user_cards.append(card)
        user_values.append(card_value)
        return user_cards, user_values


again="yes"
print("Welcome to blackjack land")
start = input("Type any key to start:")
while again=='yes':
    system("cls")
    print(logo)
    dealer_cards = []
    dealer_values=[]
    user_cards = []
    user_values=[]
    num_cards=2
    dealer_turn = True
    for i in range (0,num_cards):
        game_cards=choose_card()
        value=get_value(game_cards)
        add_card_value(game_cards, value, "user")
    print("".join(user_cards))
    print(f"Your total score is:{sum(user_values)}")
    another_card = input("Would you like another card?\nType 'yes' to continue or 'no' to stop: ")
    while another_card=='yes':
        system("cls")
        game_cards=choose_card()
        value=get_value(game_cards)
        add_card_value(game_cards, value, "user")
        print("".join(user_cards))
        print(f"Your total score is:{sum(user_values)}")
        if sum(user_values)<21:
            another_card = input("Would you like another card?\nType 'yes' to continue or 'no' to stop: ")
        if sum(user_values)==21:
            break
        else:
            break
    if sum(user_values)==21:
        print("Game over\n\nYOU WON!!!")        
    elif sum(user_values)>21:
        print("Game over\n\nTHE COMPUTER WON")
    else:
        print(f"Your total score is:{sum(user_values)}")
        print("Now is the Dealer turn.\n") 
        for i in range (0,num_cards):
            game_cards=choose_card()
            value=get_value(game_cards)
            add_card_value(game_cards, value, "dealer")
        print("".join(dealer_cards))
        print(f"The dealer total score is:{sum(dealer_values)}")
        if sum(dealer_values)>=19 and sum(dealer_values)<21:
            dealer_turn=False
        while dealer_turn:
            system("cls")
            print("".join(user_cards))
            print(f"Your total score is:{sum(user_values)}")
            game_cards=choose_card()
            value=get_value(game_cards)
            add_card_value(game_cards, value, "dealer")
            print("".join(dealer_cards))
            print(f"The dealer total score is:{sum(dealer_values)}")
            if sum(dealer_values)>=19 and sum(dealer_values)<21:
                dealer_turn=False
            if sum(dealer_values)==21:
                break
            elif sum(dealer_values)>21:
                break
        if sum(dealer_values)==21:
            print("Game over\n\nTHE COMPUTER WON")
        elif sum(dealer_values)>21:
            print("Game over\n\nYOU WON!!!")
        else:
            if sum(dealer_values)<sum(user_values):
                print("Game over\n\nYOU WON!!!")
            elif sum(user_values)<sum(dealer_values):
                print("Game over\n\nTHE COMPUTER WON")
            elif sum(user_values)==sum(dealer_values):
                print("Its a drawn")
    again = input("Would you like to play again?: Type yes or no: ")

print("Goodbye")
