import pandas as pd
data = pd.read_csv('nato_phonetic_alphabet.csv')
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
new_dict = {row.letter: row.code for (index, row) in data.iterrows()}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
input_word = input("Please enter the word: ")
final_list = []
# for letter in input_word.upper(): # SAHER
for letter in input_word.upper():
    olist = [value for key, value in new_dict.items() if key == letter]
    final_list += olist
print(final_list)