alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    # Allows symbols and numbers to encoded/decoded and remain in same place
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    elif char not in alphabet:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}\n")

from replit import clear
from art import logo

restart = True
while restart:
  clear()
  print(logo)
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  #allows for shift numbers over 26 to be entered 
  if shift > 26:
    shift % 26
  
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  #restarts the program if True
  restart_input = input("Would you like to restart the cipher program? Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
  if restart_input == "no":
    restart = False
    print("Goodbye o/")
