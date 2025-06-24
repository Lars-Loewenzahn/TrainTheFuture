
def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]["text"] = field_text.toPlainText()
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, ensure_ascii=False, indent=2)
        print("Note saved:", key)
    else:
        print("No note selected.")