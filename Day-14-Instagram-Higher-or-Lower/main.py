import art
from replit import clear
from game_data import data
import random

SCORE = 0
CONT = True
new_a = {}


def select_a():
  """Selects a random acc from data. Prints details and returns insta count. If not first turn a = old b"""
  if SCORE == 0:
    a_raw = random.choice(data)
  else: 
    a_raw = new_a
  data.remove(a_raw)
  a_list = []
  for key in a_raw:
    a_list.append(a_raw[key])
  print(f"\nCompare A: {a_list[0]}, a {a_list[2]}, from {a_list[3]}.")
  return a_list[1] 
  
def select_b():
  """Selects a random acc from data. Prints details and returns insta count."""
  b_raw = random.choice(data)
  global new_a
  new_a = b_raw
  b_list = []
  for key in b_raw:
    b_list.append(b_raw[key])
  print(f"\nAgainst B: {b_list[0]}, a {b_list[2]}, from {b_list[3]}.")
  return b_list[1]

def guess(): 
  guess_input = input("Who has more Instagram Followers? Type 'A' or 'B': ").lower()
  if a_count > b_count:
    return guess_input == "a"
  else:
    return guess_input == "b"




print(art.logo)


while CONT:
  
  a_count = select_a() 
  print(art.vs)
  b_count = select_b()
  answer = guess()
  
  if answer:
    SCORE += 1
    clear()
    print(art.logo)
    print(f"You're right! Current score: {SCORE}.") 
    CONT = True
  else:
    clear()
    print(art.logo)
    print(f"Sorry that is wrong. Final score: {SCORE}.")
    CONT = False