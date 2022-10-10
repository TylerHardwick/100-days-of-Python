rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

rps = [rock,paper,scissors]

print("Welcome to Rock Paper Scissors!\n")
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))


if choice >=3 or choice < 0:
  print("You lost. Re-run and enter a number between 0 and 2.")
else:
  print(rps[choice])

  pc_rps = random.randint(0,2)
  pc_rps_select = rps[pc_rps]
  
  print(f"\nThe computer chooses:\n {pc_rps_select}")
  
  
  if choice == 0 and pc_rps == 2:
    print("Boom, you win!")
  elif pc_rps == 0 and choice == 2:
    print("You lose.")
  elif choice < pc_rps:
    print("You lose.")
  elif choice > pc_rps:
    print("Boom, you win!")
  else:
    print("It's a draw.")


# print(f"\nThe computer chooses:\n {pc_rps}")
# if user_rps == rock and pc_rps == rock or user_rps == paper and pc_rps == paper or user_rps == scissors and pc_rps == scissors:
#   print("It's a draw.")
# elif user_rps == rock and pc_rps == scissors or user_rps == paper and pc_rps == rock or user_rps == scissors and pc_rps == rock:
#   print("Boom, you win!")
# else:
#   print("You lose.")