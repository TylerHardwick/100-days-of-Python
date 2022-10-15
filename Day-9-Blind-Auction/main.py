from replit import clear
from art import logo

print(logo)
print("Welcome to the Tyler's Secret Auctions.\n")

all_bids = {}
cont_bidding = True

def find_highest_bidder(all_bids):
  
  highest_bid = 0
  highest_bidder = ""
  
  for bidders in all_bids:
    current_bid = all_bids[bidders]
    if current_bid > highest_bid:
      highest_bid = current_bid
      highest_bidder = bidders
    clear()
    print(logo)    
    print(f"The winner is {highest_bidder} with a bid of £{highest_bid}.")
    print("\nCongratulations!")

while cont_bidding:

  name = input("What is your name?: ")
  bid = int(input("What is your bid?: £"))
  
  all_bids[name] = bid
  more_bidders = input("\nAre there any other bidders? Type 'yes' or 'no': ").lower()

  if more_bidders == "no":
    cont_bidding = False      
    find_highest_bidder(all_bids)
                  
  else:
    clear()
    print(logo)



