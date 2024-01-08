import pandas

alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row["letter"]: row["code"] for (index, row) in alphabet_data.iterrows()}

def generate_phonetic():
    user_input = input().upper()

    try:
        phonetic_code_list = [alphabet_dict[item] for item in user_input]

    except KeyError:
        print("Sorry, your input must contain only latin letters.")
        generate_phonetic()

    else:
        print(phonetic_code_list)

generate_phonetic()