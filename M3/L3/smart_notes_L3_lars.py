from dataclasses import field
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout


import json


app = QApplication([])


'''Notes in json'''
notes = {
    "Welcome!" : {
        "text" : "This is the best note taking app in the world!",
        "tags" : ["good", "instructions"]
    }
}
with open("notes_data.json", "w") as file:
    json.dump(notes, file, ensure_ascii=False)




'''Application interface'''
#application window parameters
notes_win = QWidget()
notes_win.setWindowTitle('Smart Notes')
notes_win.resize(900, 600)


#application window widgets
list_notes = QListWidget()
list_notes_label = QLabel('List of notes')


button_note_create = QPushButton('Create note') #a window appears with the field "Enter note name"
button_note_del = QPushButton('Delete note')
button_note_save = QPushButton('Save note')


field_tag = QLineEdit('')
field_tag.setPlaceholderText('Enter tag...')
field_text = QTextEdit()
button_add = QPushButton('Add to note')
button_del = QPushButton('Untag from note')
button_search = QPushButton('Search notes by tag')
list_tags = QListWidget()
list_tags_label = QLabel('List of tags')


#arranging widgets by layout
layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)


col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)
row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)


col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)
row_3 = QHBoxLayout()
row_3.addWidget(button_add)
row_3.addWidget(button_del)
row_4 = QHBoxLayout()
row_4.addWidget(button_search)


col_2.addLayout(row_3)
col_2.addLayout(row_4)


layout_notes.addLayout(col_1, stretch = 2)
layout_notes.addLayout(col_2, stretch = 1)
notes_win.setLayout(layout_notes)


'''Application functionality'''
def show_note():
    #get the text from the note with the title highlighted and display it in the edit field
    key = list_notes.selectedItems()[0].text()
    print(key)
    field_text.setText(notes[key]["text"])
    list_tags.clear()
    list_tags.addItems(notes[key]["tags"])

def add_note():
    note_name, ok = QInputDialog.getText(notes_win, "Add note", "Note name:")
    if ok and note_name != "":
        notes[note_name] = {"text":"", "tags": []}
        list_notes.addItem(note_name)
        list_tags.clear

button_note_create.clicked.connect(add_note)

def show_note():
    key = list_notes.selectedItems()[0].text()
    field_text.setText(notes[key]["text"])
    list_tags.clear()
    list_tags.addItems(notes[key]["tags"])

list_notes.itemClicked.connect(show_note)


def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]["text"] = field_text.toPlainText()
        with open("M3/L3/notes_data.json", "w") as file:
            json.dump(notes, file, ensure_ascii=False, indent=2)
    else:
        print("no item selected")
button_note_save.clicked.connect(save_note)


def del_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tags.clear()
        field_text.clear()
        list_notes.addItems(notes)
        with open("M3/L3/notes_data.json", "w") as file:
            json.dump(notes, file, ensure_ascii=False, indent=2)
    else:
        print("No item selected")
button_note_del.clicked.connect(del_note)

def add_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = field_tag.text()
        if tag and tag not in notes[key]["tags"]:
            notes[key]["tags"].append(tag)
            list_tags.addItem(tag)
            field_tag.clear()
            with open("M3/L3/notes_data.json", "w") as file:
                json.dump(notes, file, ensure_ascii=False, indent=2)
        print("Tag added", tag)
    else:
        print("No item selected")
button_add.clicked.connect(add_tag)


def del_tag():
    if list_tags.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = list_tags.selectedItems()[0].text()
        notes[key]["tags"].remove(tag)
        list_tags.clear()
        list_tags.addItems(notes[key]["tags"])
        with open("M3/L3/notes_data.json", "w") as file:
                json.dump(notes, file, ensure_ascii=False, indent=2)
        print("Tag removed", tag)
    else:
        print("No item selected")
button_del.clicked.connect(del_tag)

def search_tag():
    tag = field_tag.text()
    if tag and button_search.text() == "Search notes by tag":
        list_notes.clear()
        list_tags.clear()
        button_search.setText("Reset search")
        filtered_notes = {}
        for key, value in notes.items():
            if tag in value["tags"]:
                filtered_notes[key] = value
        list_notes.addItems(filtered_notes)
    else:
        field_tag.clear()
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes)
        button_search.setText("Search notes by tag")

button_search.clicked.connect(search_tag)


'''Run the application'''
notes_win.show()


with open("notes_data.json", "r") as file:
    notes = json.load(file)
list_notes.addItems(notes)


app.exec_()



