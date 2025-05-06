from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
import random

app = QApplication([])

main_win = QWidget()
main_win.setWindowTitle('Winner Generator')
main_win.resize(400, 200)
main_win.move(0,0)

text = QLabel("Push the button to generate a winner")
winner = QLabel("?")
button = QPushButton("Generate")


layout = QVBoxLayout()
layout.addWidget(text, alignment= Qt.AlignCenter)
layout.addWidget(winner, alignment= Qt.AlignCenter)
layout.addWidget(button, alignment= Qt.AlignCenter)
main_win.setLayout(layout)

def button_click():
    winner.setText(str(random.randint(1, 100)))

button.clicked.connect(button_click)

main_win.show()
app.exec_()
