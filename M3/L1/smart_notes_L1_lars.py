from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, 
    QHBoxLayout, QVBoxLayout,
    QPushButton, QLabel,
    QTextEdit, QListWidget)

app = QApplication([])

window = QWidget()
window.setWindowTitle('Smart Notes')

v1 = QVBoxLayout()
text_field = QTextEdit()
v1.addWidget(text_field)

v2 = QVBoxLayout()
l1  =QLabel()
l1.setText("List of Notes")
v2.addWidget(l1)
list1 = QListWidget()
v2.addWidget(list1)

h1 = QHBoxLayout()
create_notes_button = QPushButton()
create_notes_button.setText("Create note")
h1.addWidget(create_notes_button)
delete_notes_button = QPushButton()
delete_notes_button.setText("Delete note")
h1.addWidget(delete_notes_button)
v2.addLayout(h1)
save_note_button = QPushButton()
save_note_button.setText("Save note")
v2.addWidget(save_note_button)

l2  =QLabel()
l2.setText("List of Tags")
v2.addWidget(l2)
list2 = QListWidget()
v2.addWidget(list2)

h2 = QHBoxLayout()
add_to_note_button = QPushButton()
add_to_note_button.setText("Add to note")
h2.addWidget(add_to_note_button)
untag_button = QPushButton()
untag_button.setText("Untag from note")
h2.addWidget(untag_button)
v2.addLayout(h2)
search_button = QPushButton()
search_button.setText("Search notes by tag")
v2.addWidget(search_button)

h0 = QHBoxLayout()
h0.addLayout(v1, stretch=3)
h0.addLayout(v2, stretch=1)

window.setLayout(h0)

window.show()
app.exec()
                                                                             