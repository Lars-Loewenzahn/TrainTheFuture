
def add_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = field_tag.text()
        if tag and tag not in notes[key]["tags"]:
            notes[key]["tags"].append(tag)
            list_tags.addItem(tag)
            field_tag.clear()
            with open("notes_data.json", "w") as file:
                json.dump(notes, file, ensure_ascii=False, indent=2)
        print("Tag added:", tag)
    else:
        print("No note selected.")