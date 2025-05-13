from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,
 QHBoxLayout, QVBoxLayout,
  QGroupBox, QRadioButton, 
  QPushButton, QLabel)


app = QApplication([])
window = QWidget()

answer_button = QPushButton('Answer')
answer_button.setStyleSheet("background-color : yellow")
info_text = QLabel('The most difficult question in the world!')

layout_line1 = QVBoxLayout()

line1 = QLabel("Are you correct or not?")
line2 = QLabel("the answer will be here!")

layout_ans1 = QVBoxLayout()

layout_ans1.addWidget(line1, alignment=Qt.AlignLeft)
layout_ans1.addWidget(line2, alignment=Qt.AlignCenter)

RadioGroupBox = QGroupBox("Test result")
RadioGroupBox.setLayout(layout_ans1)

layout_line1.addWidget(info_text, alignment=Qt.AlignCenter)
layout_line1.addWidget(RadioGroupBox)
layout_line1.addWidget(answer_button)

window.setWindowTitle('Memo Card')
window.setLayout(layout_line1)
window.show()
app.exec()