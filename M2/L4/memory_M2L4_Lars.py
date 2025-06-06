from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QButtonGroup, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,  
        QPushButton, QLabel)
from random import shuffle

app = QApplication([])

btn_OK = QPushButton('Answer')

lb_Question = QLabel('The most difficult question in the world!')
RadioGroupBox = QGroupBox("Answer options")

rbtn_1 = QRadioButton('Option 1')
rbtn_2 = QRadioButton('Option 2')
rbtn_3 = QRadioButton('Option 3')
rbtn_4 = QRadioButton('Option 4')
rbtns = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1) # two answers in the first column
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # two answers in the second column
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2) 
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1) 

# Create a results panel
AnsGroupBox = QGroupBox("Test result")
lb_Result = QLabel('Are you correct or not?') # “Correct” or “Incorrect” text will be here
lb_Correct = QLabel('the answer will be here!') # correct answer text will be written here 

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()

# Place all the widgets in the window:
layout_line1 = QHBoxLayout() # question
layout_line2 = QHBoxLayout() # answer options or test result
layout_line3 = QHBoxLayout() # “Answer” button

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
# Put both panels in the same line; one of them will be hidden and the other will be shown:
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
 #RadioGroupBox.hide() # We’ve already seen this panel; let’s hide it and see how the answer panel turned out 

layout_line3.addStretch(1)	
layout_line3.addWidget(btn_OK, stretch=2) # the button should be large
layout_line3.addStretch(1)

# Now let’s put the lines we’ve created one under one another:
layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)

layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # spaces between content

def show_result():
    check_answer()
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText("Next question")

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_OK.setText("Answer")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(False)
    
def switch_between_q_and_a():
    if btn_OK.text() == "Answer":
        show_result()
    else:
        show_question()

btn_OK.clicked.connect(switch_between_q_and_a)

def ask(question, right, wrong1, wrong2, wrong3):
    lb_Question.setText(question)
    lb_Correct.setText(right)
    answer_list = [right, wrong1, wrong2, wrong3]
    shuffle(answer_list)
    rbtn_1.setText(answer_list[0])
    rbtn_2.setText(answer_list[1])
    rbtn_3.setText(answer_list[2])
    rbtn_4.setText(answer_list[3])

def check_answer():
    for rbtn in rbtns:
        if not rbtn.isChecked():
            continue
        if rbtn.text() == lb_Correct.text():
            lb_Correct.setText("Correct")
        else: 
            lb_Correct.setText("Incorrect")



ask("What is 5?", "1", "2", "3", "4")

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')
window.show()
app.exec()