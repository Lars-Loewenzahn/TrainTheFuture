from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
import random
import sys

class AnnoyingWindow(QWidget):
    def __init__(self, parent, pos_x, pos_y):
        super().__init__()
        self.parent = parent
        
        self.setWindowTitle('Error')
        self.resize(400, 200)
        self.move(pos_x, pos_y)
        
        text = QLabel("An error occurred because your kids are coding!")
        winner = QLabel(f"Error: {random.randint(100, 999)}")
        winner.setStyleSheet("font-size: 36px; color: red; font-weight: bold;")
        button = QPushButton("Close")

        layout = QVBoxLayout()
        layout.addWidget(text, alignment=Qt.AlignCenter)
        layout.addWidget(winner, alignment=Qt.AlignCenter)
        layout.addWidget(button, alignment=Qt.AlignCenter)
        self.setLayout(layout)
        
        button.clicked.connect(self.button_click)
        self.show()

    def button_click(self):
        new_x = random.randint(0, 1200)
        new_y = random.randint(0, 1200)
        #self.move(new_x, new_y)
        self.parent.add_window()
    
    def closeEvent(self, event):
        # Custom code when the window is closed via the red X button
        print("Red X clicked! Adding a new window...")
        self.parent.add_window()
        self.parent.add_window()

        event.accept()


class Parent:
    def __init__(self):
        self.x = 20
        self.y = 20        
        self.windows = []
        self.app = QApplication(sys.argv)
        self.add_window()
        sys.exit(self.app.exec_())

    def add_window(self):
        x, y = random.randint(0, 1200), random.randint(0, 1200)
        self.x += 20
        self.y += 20
        window = AnnoyingWindow(self,x, y)
        self.windows.append(window)

parent = Parent()
