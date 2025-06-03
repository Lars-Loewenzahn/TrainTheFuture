from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel)
from random import shuffle

class Question:
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []   
q1 = Question("Wann kommt GTAVI raus?", "2032", "2022", "bald", "Nichts")
question_list.append(q1)
q2 = Question('The national language of Brazil', 'Portuguese', 'Brazilian', 'Spanish', 'Italian')
question_list.append(q2)
q3 = Question("Was ist die Hauptstadt von Australien?", "Canberra", "Sydney", "Melbourne", "Perth")
question_list.append(q3)

q4 = Question("Wie viele Planeten hat unser Sonnensystem?", "8", "9", "7", "10")
question_list.append(q4)

q5 = Question("Wer malte die Mona Lisa?", "Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Claude Monet")
question_list.append(q5)

q6 = Question("Was ist die chemische Formel von Wasser?", "H2O", "O2", "CO2", "H2SO4")
question_list.append(q6)

q7 = Question("Wie heißt das größte Säugetier der Welt?", "Blauwal", "Elefant", "Giraffe", "Nilpferd")
question_list.append(q7)

q8 = Question("Welches Land hat die meisten Einwohner?", "China", "Indien", "USA", "Russland")
question_list.append(q8)
q9 = Question("Was ist die Quadratwurzel von 81?", "9", "8", "7", "6")
question_list.append(q9)

q10 = Question("Wer schrieb 'Faust'?", "Johann Wolfgang von Goethe", "Friedrich Schiller", "Heinrich Heine", "Thomas Mann")
question_list.append(q10)

q11 = Question("Welches Element hat das chemische Symbol 'Fe'?", "Eisen", "Blei", "Fluor", "Zink")
question_list.append(q11)

q12 = Question("Wie viele Bundesländer hat Deutschland?", "16", "14", "18", "12")
question_list.append(q12)

q13 = Question("Welcher Planet ist der Sonne am nächsten?", "Merkur", "Venus", "Erde", "Mars")
question_list.append(q13)

q14 = Question("In welchem Jahr fiel die Berliner Mauer?", "1989", "1991", "1987", "1990")
question_list.append(q14)

q15 = Question("Was ist die Hauptstadt von Kanada?", "Ottawa", "Toronto", "Vancouver", "Montreal")
question_list.append(q15)

q16 = Question("Welches Tier legt Eier?", "Ente", "Hund", "Katze", "Kuh")
question_list.append(q16)

q17 = Question("Wie heißt der höchste Berg der Erde?", "Mount Everest", "K2", "Kilimandscharo", "Mont Blanc")
question_list.append(q17)

q18 = Question("Was ist das Ergebnis von 7 * 8?", "56", "54", "64", "58")
question_list.append(q18)

q19 = Question("Wie viele Kontinente gibt es?", "7", "6", "8", "5")
question_list.append(q19)

q20 = Question("In welcher Einheit wird elektrische Spannung gemessen?", "Volt", "Ampere", "Ohm", "Watt")
question_list.append(q20)

q21 = Question("Wer war der erste Mensch auf dem Mond?", "Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "John Glenn")
question_list.append(q21)

q22 = Question("Welche Farbe entsteht durch Mischen von Blau und Gelb?", "Grün", "Lila", "Orange", "Braun")
question_list.append(q22)


app = QApplication([])
btn_OK = QPushButton('Answer') 
lb_Question = QLabel('The most difficult question in the world!')


RadioGroupBox = QGroupBox("Answer options") 
rbtn_1 = QRadioButton('Option 1')
rbtn_2 = QRadioButton('Option 2')
rbtn_3 = QRadioButton('Option 3')
rbtn_4 = QRadioButton('Option 4')


RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) 


RadioGroupBox.setLayout(layout_ans1) 


AnsGroupBox = QGroupBox("Test result")
lb_Result = QLabel('are you correct or not?')
lb_Correct = QLabel('the answer will be here!')


layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)


layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()


layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() 


layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) 
layout_line3.addStretch(1)

layout_card = QVBoxLayout()


layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)


def show_result():
    ''' show answer panel '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Next question')


def show_question():
    ''' show question panel '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Answer')
    RadioGroup.setExclusive(False) 
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) 


answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


def ask(q: Question):
    ''' the function writes the value of the question and answers into the corresponding widgets while distributing the answer options randomly'''
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer) 
    show_question() 


def show_correct(res):
    ''' show result - put the written text into "result" and show the corresponding panel '''
    lb_Result.setText(res)
    show_result()


def check_answer():
    ''' if an answer option was selected, check and show answer panel '''
    if answers[0].isChecked():
        show_correct('Correct!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Incorrect!')

def next_question():
    q = question_list[window.curr]
    show_question()
    ask(q)
    window.curr += 1
    if window.curr >= len(question_list):
        window.curr = 0

def click_OK():
    if btn_OK.text() == "Answer":
        check_answer()
    else:
        next_question()

window = QWidget()
window.curr = 0
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
ask(q1)
btn_OK.clicked.connect(click_OK) 


window.show()
app.exec()
