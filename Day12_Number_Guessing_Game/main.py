from random import randint

def choose_number():
    choice = randint(1,100)
    return choice

def check_number(guess,number,attempts):
    if guess==number:
        print("That is right. You win!")
        attempts=-1
    if number > guess:
        print("Too low.")
        attempts-=1
    elif number < guess:
        print("Too high.")
        attempts-=1
    return attempts

difficulty = input("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100.\nChoose a difficulty to start. Type 'easy', 'medium' or 'hard': ")

difficulty_choice = False 

while not difficulty_choice:
    if difficulty=='easy':
        attempts = 10
        difficulty_choice = True
    elif difficulty=='medium':
        attempts = 7
        difficulty_choice = True
    elif difficulty=='hard':
        attempts = 5
        difficulty_choice = True
    else:
        print("Please type a valid difficulty to start!")
        difficulty = input("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100.\nChoose a difficulty to start. Type 'easy', 'medium' or 'hard': ")
num = choose_number()
while attempts>0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess= int(input("Make a guess: "))
    attempts = check_number(guess,num,attempts)
if attempts==0:
    print("You lost!")
print(f"The number is {num}")
print("End of game")