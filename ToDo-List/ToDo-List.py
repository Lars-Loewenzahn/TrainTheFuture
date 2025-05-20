import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QListWidget, QListWidgetItem, QMessageBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class ToDoList(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ToDo-Liste')
        self.setGeometry(200, 200, 400, 500)
        self.setStyleSheet('background: #f8f8f8;')
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.input = QLineEdit()
        self.input.setPlaceholderText('Neue Aufgabe eingeben...')
        self.input.setFont(QFont('Arial', 14))
        self.input.returnPressed.connect(self.add_task)
        layout.addWidget(self.input)

        self.list_widget = QListWidget()
        self.list_widget.setFont(QFont('Arial', 13))
        self.list_widget.setStyleSheet('background: #fff; border: 1px solid #ddd;')
        self.list_widget.itemDoubleClicked.connect(self.toggle_done)
        layout.addWidget(self.list_widget)

        button_layout = QHBoxLayout()
        self.add_btn = QPushButton('Hinzufügen')
        self.add_btn.clicked.connect(self.add_task)
        self.del_btn = QPushButton('Löschen')
        self.del_btn.clicked.connect(self.delete_task)
        button_layout.addWidget(self.add_btn)
        button_layout.addWidget(self.del_btn)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def add_task(self):
        text = self.input.text().strip()
        if text:
            item = QListWidgetItem(text)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            self.list_widget.addItem(item)
            self.input.clear()
        else:
            QMessageBox.information(self, 'Hinweis', 'Bitte eine Aufgabe eingeben.')

    def delete_task(self):
        selected = self.list_widget.currentRow()
        if selected >= 0:
            self.list_widget.takeItem(selected)
        else:
            QMessageBox.information(self, 'Hinweis', 'Bitte eine Aufgabe auswählen.')

    def toggle_done(self, item):
        if item.checkState() == Qt.Checked:
            item.setCheckState(Qt.Unchecked)
            item.setFont(QFont('Arial', 13, QFont.Normal))
        else:
            item.setCheckState(Qt.Checked)
            font = QFont('Arial', 13, QFont.Normal)
            font.setStrikeOut(True)
            item.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    todo = ToDoList()
    todo.show()
    sys.exit(app.exec_())
