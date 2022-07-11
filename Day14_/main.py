drinks = {"espresso": {"water": 50, "coffee": 18, "milk": 0, "price": 1.50},
          "latte": {"water": 200, "coffee": 24, "milk": 150, "price": 2.50},
          "cappuccino": {"water": 250, "coffee": 24, "milk": 100, "price": 3}}

supplies = {"water": 300, "coffee": 100, "milk": 200, "money": 0}

coins = [0.01, 0.05, 0.10, 0.25]


def report():
    print(f"The machine still has:\nWater: {supplies['water']}ml,\nCoffee:"
          f"{supplies['coffee']}g,\nMilk: {supplies['milk']}ml")


def recharge_supplies():
    supplies["water"] = 300
    supplies["coffee"] = 100
    supplies["milk"] = 200
    supplies["money"] = 0
    return supplies


def check_resources(type_of_drink):
    if supplies['water'] >= drinks[type_of_drink]['water']:
        if supplies['coffee'] >= drinks[type_of_drink]['coffee']:
            if supplies['milk'] >= drinks[type_of_drink]['milk']:
                insert_money(type_of_drink)
            else:
                print(f"Sorry! There isn't enough milk to make"
                      f" {type_of_drink}")
        else:
            print(f"Sorry! There isn't enough coffee to make {type_of_drink}")
    else:
        print(f"Sorry! There isn't enough water to make {type_of_drink}")


def insert_money(type_of_drink):
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))
    check_coins(type_of_drink, quarters, dimes, nickles, pennies)


def check_coins(type_of_drink, quarters, dimes, nickles, pennies):
    money = (quarters * coins[3]) + (dimes * coins[2]) + (nickles * coins[1]) \
            + (pennies * coins[0])
    if money >= drinks[type_of_drink]['price']:
        change = money - drinks[type_of_drink]['price']
        make_drink(type_of_drink)
        print(f"Your change is: {change}")
    else:
        print(f"There isn't enough money to make a {type_of_drink}")


def make_drink(type_of_drink):
    supplies['water'] = supplies['water'] - drinks[type_of_drink]['water']
    supplies['coffee'] = supplies['coffee'] - drinks[type_of_drink]['coffee']
    supplies['milk'] = supplies['milk'] - drinks[type_of_drink]['milk']
    print(f"Here is your {type_of_drink}. Enjoy!")


machine_on = True
while machine_on:
    print("Coffee machine operating...")
    options = int(input("What would you like to do?\n Type 1- for drinks and 2 - for system "
                        "options"))
    if options == 1:
        drink = input("What would you like to drink ? The options are: 'espresso', 'latte' or "
                      "'cappuccino': ")
        check_resources(drink)

    elif options == 2:
        conf = input("Your system option are : 'report' to show the supplies on the machine,"
                     "'recharge' to recharge the supplies and 'off' to turn off the machine.\nWhat "
                     "would you like to do?")
        if conf == 'report':
            report()
        elif conf == 'recharge':
            recharge_supplies()
        elif conf == 'off':
            machine_on = False
        else:
            print("Option not valid, please choose again.")
print("Goodbye")
