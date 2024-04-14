from replit import clear

import art
#HINT: You can call clear() to clear the output in the console.

bidders = {}

def add_bidder(name, bid):
    bidders[name] = bid

print(art.logo)
continue_bidding = True

while continue_bidding:
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    add_bidder(name, bid)
    while True:
        more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
        if more_bidders.lower() == "yes":
            clear()
            break
        elif more_bidders.lower() == "no":
            continue_bidding = False
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

winner_bidder = ""
winner_bid = 0
for bidder in bidders:
    if int(bidders[bidder]) > winner_bid:
        winner_bidder = bidder
        winner_bid = int(bidders[bidder])
print(f"The winner is {winner_bidder} with a bid of ${winner_bid}")