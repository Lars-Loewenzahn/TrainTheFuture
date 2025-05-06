from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,
 QHBoxLayout, QVBoxLayout,
  QGroupBox, QRadioButton, 
  QPushButton, QLabel)


app = QApplication([])
window = QWidget()

answer_button = QPushButton('Answer')
question = QLabel('Question')

layout_line1 = QVBoxLayout()


r1 = QRadioButton("Luis")
r2 = QRadioButton("Lucas")
r3 = QRadioButton("Abdou")
r4 = QRadioButton("Phillip")

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(r1)
layout_ans2.addWidget(r2)
layout_ans3.addWidget(r3)
layout_ans3.addWidget(r4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
layout_ans1.setSpacing(0)

RadioGroupBox = QGroupBox("Answer options")
RadioGroupBox.setLayout(layout_ans1)

layout_line1.addWidget(question, alignment=Qt.AlignCenter)
layout_line1.addWidget(RadioGroupBox)
layout_line1.addWidget(answer_button, stretch=10)

window.setWindowTitle('Memo Card')
window.setLayout(layout_line1)
window.resize(400, 300)
window.show()
app.exec()