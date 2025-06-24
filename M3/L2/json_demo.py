notes = {
    "Note1" :
    {
    "text" : "Very important note text",
    "tags" : ["draft", "thoughts"]
    },
    "Note2" :
    {
    "text" : "Very important secound note text",
    "tags" : ["draft", "thoughts", "note"]
    }
}

import json

print(notes["Note2"]["text"])

with open("M3/L2/notes_data.json", "w") as file:
    json.dump(notes, file)