import pandas

df = pandas.read_csv("morse.csv")
library_dict = df.to_dict("list")
on = True

letter =library_dict["letter"]
morse = library_dict["morse"]

morse_word = []

print("""

  ______      __         _          __  ___                        ______          __        ______                           __           
 /_  __/_  __/ /__  ____( )_____   /  |/  /___  _____________     / ____/___  ____/ /__     / ____/___  ____ _   _____  _____/ /____  _____
  / / / / / / / _ \/ ___/// ___/  / /|_/ / __ \/ ___/ ___/ _ \   / /   / __ \/ __  / _ \   / /   / __ \/ __ \ | / / _ \/ ___/ __/ _ \/ ___/
 / / / /_/ / /  __/ /    (__  )  / /  / / /_/ / /  (__  )  __/  / /___/ /_/ / /_/ /  __/  / /___/ /_/ / / / / |/ /  __/ /  / /_/  __/ /    
/_/  \__, /_/\___/_/    /____/  /_/  /_/\____/_/  /____/\___/   \____/\____/\__,_/\___/   \____/\____/_/ /_/|___/\___/_/   \__/\___/_/     
    /____/                                                                                                                                 
""")
while on:
    to_convert = str(input("Enter a word or phrase to convert: ").upper())
    for n in to_convert:
        if n in letter:
            morse_row = letter.index(n)
            morse_word.append(morse[morse_row])

    print(f'"{to_convert.capitalize()}" in morse code is: {"   ".join(morse_word)}\n')
    con = input("Would you like to continue? Y/N?").lower()
    print(con)
    if con == "yes" or con == "y":
        on = True
        morse_word = []
    else:
        on = False
print("Thanks for using Tyler's Decoder!")