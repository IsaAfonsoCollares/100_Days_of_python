import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
lizard = '''
  _______ ___ 
 /   ____)___)
/   /    /  /
\   \___/  /             
 \        /   
  |      |  
'''
spock ='''
  __      __ 
 _\ \    / /_  
 \ \ \  / / /
  \ \ \/ / /
   \      / 
    |    |
'''
bye ='''
 #####                                           
#     #  ####   ####  #####  #####  #   # ###### 
#       #    # #    # #    # #    #  # #  #      
#  #### #    # #    # #    # #####    #   #####  
#     # #    # #    # #    # #    #   #   #      
#     # #    # #    # #    # #    #   #   #      
 #####   ####   ####  #####  #####    #   ###### 
'''
#Write your code below this line 👇
n=1
version = int(input("Welcome to Rock, paper, scissor. Would you like to play:\n1-classic game\nor\n2-Sam Kass' version?\nType 1 or 2: "))
while n==1:
  if version ==1 :
    option = [scissors, paper, rock]
    user_choice = int(input("\nWhat do you choose? Type 0 for scissors, 1 for paper or 2 for rock: "))
    print(f"You chose{option[user_choice]}")
    comp_choice = random.choice(option)
    print(f"Computer choose:\n{comp_choice}")
    if option[user_choice]==comp_choice:
      print("It's a draw")
    else:
      if (option[user_choice]==scissors and comp_choice==paper) or (option[user_choice]==paper and comp_choice==rock) or (option[user_choice]==rock and comp_choice==scissors):
        print("The computer lose. You won!")
      else:
        print("The computer won. You lose!")
    n=int(input("\nWould you like to play again?\n1-Yes\n2-No\n"))
  if version ==2 :
    option = [scissors, paper, rock, lizard, spock]
    user_choice = int(input("\nWhat do you choose?\nType 0 for scissors\n1 for paper\n2 for rock\n3 for lizard\n4 for spock: "))
    print(f"You chose {option[user_choice]}")
    comp_choice = random.choice(option)
    print(f"Computer choose:\n{comp_choice}")
    if option[user_choice]==comp_choice:
      print("It's a draw")
    else:
      if option[user_choice]==scissors:
        if comp_choice==paper or comp_choice==lizard:
          print("The computer lose. You won!")
        else:
          print("The computer won. You lose!")
      elif option[user_choice]==paper: 
        if comp_choice==rock or comp_choice== spock:
          print("The computer lose. You won!")
        else:
          print("The computer won. You lose!")
      elif option[user_choice]==rock: 
        if comp_choice==scissors or comp_choice==lizard:
          print("The computer lose. You won!")
        else:
          print("The computer won. You lose!")
      elif option[user_choice]==lizard:
        if comp_choice==spock or comp_choice==paper:
            print("The computer lose. You won!")
        else:
          print("The computer won. You lose!")
      elif option[user_choice]==spock:
        if comp_choice==scissors or comp_choice==rock:
          print("The computer lose. You won!")
        else:
          print("The computer won. You lose!")
    n=int(input("\nWould you like to play again?\n1-Yes\n2-No\n"))
print(f"\nThanks for playing, see you soon!\n{bye}")