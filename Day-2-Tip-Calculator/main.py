print("Welcome to the tip calculator! o/\n")
bill = float(input("What was the total bill?\n £"))
tip = float("1."+(input("What percentage of tip would you like to give?\n")))
split = int(input("How many people are splitting the bill?\n"))
total = round((bill / split) * tip,2) 

print(f"Each person should pay £{total}")
