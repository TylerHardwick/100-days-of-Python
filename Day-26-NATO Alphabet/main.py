import pandas

user_string = input("Enter text to convert to NATO Phonetic Alphabet: ").upper()

alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter:row.code for (index, row) in alphabet_df.iterrows()}


alphabet_list = [alphabet_dict[letter] for letter in user_string]
print(alphabet_list)

# phonetic_list = [new_item for item in alphabet_dict if item in user_letters]
# print(phonetic_list)
# for (index, row) in alphabet_df.iterrows():
#     if row.letter in user_letters:
#         print(row.code)




#
# print(alphabet_dict)



# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass



#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

