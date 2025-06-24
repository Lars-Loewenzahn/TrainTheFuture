def add_note():
    note_name, ok = QInputDialog.getText(notes_win, "Add note", "Note name:")
    if ok and note_name != "":
        notes[note_name] = {"text": "", "tags": []}
        list_notes.addItem(note_name)
        list_tags.clear()
        print(notes)

