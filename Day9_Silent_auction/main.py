from os import system

bids = {}
def add_to_bids(name_bidder , bid_value):
    bids[name_bidder] = bid_value
    return bids

def higher_bidder(bids):
    keys=list(bids.keys())
    values=list(bids.values())
    maximum = max(values)
    ind = values.index(maximum)
    winner=keys[ind]
    print(f"The winner is {winner} with a bid of ${maximum}")

close_auction = False
while close_auction == False:
    name = input("Welcome to the secret auction program.\nWhat is your name?: ")
    bid = input("What's your bid? $")
    bidders = input("Are there any other bidders? Type 'yes' or 'no':\n")
    add_to_bids(name, bid)
    if bidders == "no":
        close_auction = True
    elif bidders == "yes":
        system("cls")
higher_bidder(bids)