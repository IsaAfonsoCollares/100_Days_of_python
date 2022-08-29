import pandas as pd


file = pd.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = pd.DataFrame(file)

user_word = input("What do you want to translate into the NATO Alphabet?: ").upper()

phonetic_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}

result = [phonetic_dict[letter] for letter in user_word]

[print(result)]
