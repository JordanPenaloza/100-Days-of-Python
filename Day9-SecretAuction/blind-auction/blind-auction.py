import os
from art import logo

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_bid(name, bid):
  new_bid = {}
  new_bid["name"] = name
  new_bid["bid"] = bid
  bid_list.append(new_bid)

def find_highest_bid(bid_list):
    highest_bid = 0
    winner = ""
    for bidder in bid_list:
        bid_amount = bidder["bid"]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder["name"]
    print(f"The winner is {winner} with a bid of ${highest_bid}")


print(logo)
bid_list = []
Yes = True

while Yes:

    name = input("What is the bidder's name?\n")
    bid = int(input("What is the bidder's bid?\n"))
    add_bid(name, bid)
    decision = input("Is there another bidder? yes/no\n")

    if decision == 'yes':
        clear()
        Yes = True
    else:
        find_highest_bid(bid_list)
        Yes = False
                     
