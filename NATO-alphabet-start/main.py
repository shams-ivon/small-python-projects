import pandas

alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row["letter"]: row["code"] for (index, row) in alphabet_data.iterrows()}

user_input = input().upper()

phonetic_code_list = [alphabet_dict[item] for item in user_input]

print(phonetic_code_list)