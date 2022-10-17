
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


from art import logo
from replit import clear
import random

player_cards = []
pc_cards = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_score = 0
pc_score = 0
chips = 100
ng = True
buy_in = 10
draw_another = False

def chips_remaining():
  """Displays chips and buy in"""
  print(f"Chips remaining: £{chips}      Stake: £{buy_in}")


def random_card():
  """Deals a random card"""
  return random.choice(cards)
  
  
def new_card():
  """Draws a new card"""
  player_cards.append(random_card())
  

def check_score(list):
  """Adds all items in a list together. If Blackjack will return 0."""
  score = sum(list)
  if score == 21 and len(list) == 2:
    return 0
  elif score > 21 and 11 in list:
    list.remove(11)
    score -= 10
    list.append(1)
  return score





print(logo)
ng_input = input(f"Would you like to start a new game? Enter 'y' or 'n'. ").lower()
bet = int(input(f"You have £{chips}. How much would you like to bet?: £"))
if ng_input == "n":
  ng = False
  print("Didn't want to play with you either.")
  
  
  
while ng:
  clear()
  print(logo)
  player_cards.clear()
  pc_cards.clear()
  buy_in = bet
  chips -= buy_in
  chips_remaining()

  
  player_cards.extend([random_card(), random_card()])
  pc_cards.extend([random_card(), random_card()])
  
  player_score = check_score(player_cards)
  pc_score = check_score(pc_cards)

  
    
  
  print(f"\nYour cards: {player_cards}, current score {player_score}.")
  print(f"Computer's first card: {pc_cards[0]}")

  
  
  if player_score == 0 or pc_score == 0:
    draw_another = False
    print("BJ!")
  else:
    hit_or_stick = input("\nType 'y' to get another card, type 'n' to stick: ").lower()
    if hit_or_stick == "y":
      draw_another = True
    
    

  while draw_another:
    clear()
    print(logo)
    chips_remaining()
    player_cards.append(random_card())
    player_score = check_score(player_cards)
    
    print(f"\nYour cards: {player_cards}, current score {player_score}.")
    print(f"Computer's first card: {pc_cards[0]}")

    if player_score > 21:
      #bust
      draw_another = False
      
    else:   
      hit_or_stick = input("\nType 'y' to get another card, type 'n' to stick: ").lower()
      if hit_or_stick == "y":
        draw_another =  True
      else:
        draw_another = False
        
     

  while pc_score != 0 and  pc_score < 17:
      pc_cards.append(random_card())
      pc_score = check_score(pc_cards)
  
  print(f"\nYour final hand: {player_cards}, final score {player_score}.")
  print(f"Computer's final card: {pc_cards}, final score {pc_score}.\n") 
  if pc_score == 0:
    print("Dealer got Blackjack. You lose.")
  elif player_score == 0:
    print("Bj! Bj! You win.")
    chips += (buy_in * 2)
  elif player_score > 21:
    print("Bust, you lose.")
  elif pc_score > 21:
    print("Dealer bust. You win!")
    chips += (buy_in * 2)
  elif player_score > pc_score:
    print("Nice! You win.")
    chips += (buy_in * 2)
  elif player_score == pc_score:
    print("It's a draw.")
    chips += buy_in
  else:
    print("You lose.")
  
  if chips <= 0:
    print("You are out of Money. You lose.")
    ng = False
  else:
    ng_input = input(f"\nWould you like to buy in a new game? Enter 'y' or 'n'. ").lower()
                  
    if ng_input == "y":
      ng = True
      bet = int(input(f"You have, £{chips} much would you like to bet?: "))
    else:
      ng = False
      print(f"You walk away with £{chips}.")
    

      

  

