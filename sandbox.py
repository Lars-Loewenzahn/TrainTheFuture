import json 

with open("neues_json.json", 'r') as f:
    notes = json.load(f)
print(notes["interessen"][1])