#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import LOGO
import random
from replit import clear

chosen_number = random.randint(1,101)
guess = 0
lives = 10


def difficulty():
  dif_input = input("Choose a difficulty. Type 'Easy' or 'Hard': ").lower()
  return dif_input

def guess_input():
  g_num = int(input("Make a guess: "))
  return g_num

def hot_or_cold():
  if guess > chosen_number:
    print("Too high.")
    return lives - 1
  elif guess < chosen_number:
    print("Too low.")
    return lives -1
  elif guess == chosen_number:
    print(f"\nBoom! You got it, the answer was: {chosen_number}")
    return lives + 1

 


# print(f"The chosen num is {chosen_number}.")

print(LOGO)
print("Welcome to tjh's Guess The Number!\n")
print("I am thinking of a number between 1 and 100.")

if difficulty() == "hard":
  lives -= 5
clear()
print(LOGO)


while lives > 0 and chosen_number != guess:
  print(f"You have {lives} guesses remaining to guess the number.")
  guess = guess_input()
  lives = hot_or_cold()

if lives == 0:
  print(f"\nYou ran out of lives :(. The answer was {chosen_number}.")
  

  
