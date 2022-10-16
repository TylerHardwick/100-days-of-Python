from art import logo
from replit import clear
#Calculator Functions

#Add
def add(n1, n2):
  """Adds one number to another."""
  return n1 + n2

#Subtract
def subtract(n1, n2):
  """Takes one number from another."""
  return n1 - n2

#Multiply
def multiply(n1, n2):
  """Times one number by another."""
  return n1 * n2

#Divide
def divide(n1, n2):
  """divide one number by another."""
  return n1 / n2

maths_operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide,
 
}



def calculator():
  print(logo)
  
  #num1 and last answer
  num1 = float(input("What is the first number?: "))
  
  #print symbols:
  for symbol in maths_operations:
    print(symbol)
  
  #Continue:
  cont = True
  
  while cont:
     
    op_select = input("Pick an operation: ")
    next_num = float(input("What is the next number?: "))
    answer = maths_operations[op_select](num1, next_num)
    
    print(f"{num1} {op_select} {next_num} = {answer}")
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
      num1 = answer
      clear()
      print(logo)
      print(answer)
    else:
      cont = False
      clear()
      calculator()


calculator()

