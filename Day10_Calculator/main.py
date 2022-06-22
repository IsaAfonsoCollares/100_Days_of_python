from art import logo
from os import system

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

close_application = 1
while close_application == 1:
    repeat = 0
    print(logo)
    print("Welcome to the Python Calculator")
    if repeat ==1 :
        first_number=result
        print(f"First number = {first_number}")
    else:
        first_number =float(input("Please enter the first number: "))
    operator=input("What operation would you like to perform?\nType: + to add\n      - to subtract\n      * to multiply\n      / to divide\n")
    second_number=float(input("Please enter the second number: "))
    if operator=="+":
        result = add(first_number, second_number)

    elif operator=="-":
        result = subtract(first_number, second_number)

    elif operator=="*":
        result = multiply(first_number, second_number)

    elif operator=="/":
        result = divide(first_number, second_number)

    print(f"{first_number} {operator} {second_number} = {result}")
    next=int(input(f"Type 1 to continue operations with {result}, 2 to start a new calculation or 0 to close the calculator: "))
    if next == 1:
        repeat=1
    elif next == 2:
        system("cls")
    else:
        break
print("Thank you for using the Python Calculator See you soon!")