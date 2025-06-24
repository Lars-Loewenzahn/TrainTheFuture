import json


with open("M3/L2/notes_data.json", "r") as file:
    notes = json.load(file)

input_1 = input("Nenne einen Key")
input_2 = input("Nenne einen Value")

notes[input_1] = input_2


with open("M3/L2/notes_data.json", "w") as file:
    json.dump(notes, file, indent=4)