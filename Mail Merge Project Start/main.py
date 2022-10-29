with open("./input/Names/invited_names.txt") as letter:
    names = (letter.readlines())

with open("./input/letters/starting_letter.txt") as letter:
    letter_contents = letter.read()


for name in range(len(names)):
    current_name = names[name]
    naked_name = current_name.strip()
    new_letter = letter_contents.replace("[name]", naked_name)
    with open(f"./Output/ReadyToSend/letter_for_{naked_name}.", mode="w") as letter:
        letter.write(new_letter)

