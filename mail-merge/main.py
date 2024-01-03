def write_file(name, letter):
    name_for_file = name.lower()
    name_for_file = name_for_file.replace(" ", "_")

    with open(f"./Output/ReadyToSend/letter_for_{name_for_file}.txt", "a") as write_file:
        
        for line in letter:
            write_file.write(line)

with open("./Input/Letters/starting_letter.txt", "r") as letter_file:
    letter_lines = letter_file.readlines()

with open("./Input/Names/invited_names.txt", "r") as invited_names_file:
    invited_names = invited_names_file.readlines()

for name in invited_names:
    name = name.strip("\n")
    current_letter = letter_lines.copy()
    current_letter[0] = current_letter[0].replace("[name]", name)
    write_file(name, current_letter)