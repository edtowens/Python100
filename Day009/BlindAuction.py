import os
from art import logo

print(logo)
add_bids = True
bidders = {}
highest_bid = 0.0
winner = ""
while add_bids:

    name = input("Please enter your name\n")
    bid = float(input("Please enter your maximum bid\n"))
    
    bidders[name] = bid
    
    AddMoreBids = input("Are there other users who want to bid? y for yes, n for no\n").lower()
    if AddMoreBids == "n":
        add_bids = False
    else:
        os.system('clear')

for bidder in bidders:
    if bidders[bidder] > highest_bid:
        winner = bidder
        highest_bid = bidders[bidder]
        
print(f"The winner is {winner} with a bid of ${highest_bid}")