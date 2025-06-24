def del_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        field_text.clear()
        list_tags.clear()
        list_notes.addItems(notes)
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, ensure_ascii=False, indent=2)
        print("Note deleted:", key)
    else:
        print("No note selected.")