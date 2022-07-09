from game_data import data
from random import choices, choice

def char_choices(num_of_choices):
    char=choices(data,k=num_of_choices)
    return char

def game(game_continue):
    while game_continue:
        char=char_choices(2)
        charA=char[0]
        charB=char[1]
        print(f"Compare A: {charA['name']}, {charA['description']} from {charA['country']}\n\nto\n\nB: {charB['name']}, {charB['description']} from {charB['country']}\n")
        user_ansewr = input("Who has more instagram followers? Type 'A' or 'B': ").upper()
        if charA['follower_count']>charB['follower_count']:
            correct_ansewr = 'A'
        else:
            correct_ansewr = 'B'
        if user_ansewr!=correct_ansewr:
            print(f"\nYou lost!\n\n{charA['name']} has {charA['follower_count']} followers and {charB['name']} has {charB['follower_count']} followers")
            game_continue=False
        else:
            print("\nVery good, keep going!\n")

print("Welcome to the high lower game! The objective of the game is to guess which celebrity has more instragram followers!")
start = input("Press S to start: ")
if start=='S':
    game_continue=True
    game(game_continue)
else:
    print("I guess you don't want to play rigth now. See you latter!")