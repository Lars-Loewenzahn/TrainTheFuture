def show_note():
    key = list_notes.selectedItems()[0].text()
    field_text.setText(notes[key]["text"])
    list_tags.clear()
    list_tags.addItems(notes[key]["tags"])