def search_tag():
    tag = field_tag.text()
    if button_tag_search.text() == "Search notes by tag" and tag:
        filtered_notes = {k: v for k, v in notes.items() if tag in v["tags"]}
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(filtered_notes)
        button_tag_search.setText("Reset search")
    elif button_tag_search.text() == "Reset search":
        field_tag.clear()
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes)
        button_tag_search.setText("Search notes by tag")