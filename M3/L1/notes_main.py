#start to create smart notes app

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget, 
    QHBoxLayout, 
    QVBoxLayout, 
    QGroupBox, 
    QButtonGroup, 
    QRadioButton, 
    QPushButton,
    QListWidget,
    QTextEdit,
    QLabel)


app = QApplication([])

label_list1 = QLabel("List of notes:")
list1 = QListWidget()
cn_button = QPushButton("Create note")
dn_button = QPushButton("Delete note")
h1_v1 = QHBoxLayout()
h1_v1.addWidget(cn_button)
h1_v1.addWidget(dn_button)
sn_button = QPushButton("Save notes")


label_list2 = QLabel("List of tags:")
list2 = QListWidget()
atn_button = QPushButton("Add to note")
utn_button = QPushButton("Untag from notes")
h2_v1 = QHBoxLayout()
h2_v1.addWidget(atn_button)
h2_v1.addWidget(utn_button)
snbt_button = QPushButton("Search notes by tag")

v1 = QVBoxLayout()
v1.addWidget(label_list1)
v1.addWidget(list1)
v1.addLayout(h1_v1)
v1.addWidget(sn_button)
v1.addWidget(label_list2)
v1.addWidget(list2)
v1.addLayout(h2_v1)
v1.addWidget(snbt_button)


note = QTextEdit()
v2 = QVBoxLayout()
v2.addWidget(note)



mainline = QHBoxLayout()
mainline.addLayout(v2, stretch=2)
mainline.addLayout(v1, stretch= 1)



window = QWidget()
window.resize(800, 600)
window.setLayout(mainline)
window.setWindowTitle('Simple Notes')
window.show()
app.exec()
                                                                             