import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
)

# Funktionen zur Umrechnung
def int_to_roman(num):
    roman_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100,  'C'), (90,  'XC'), (50,  'L'), (40,  'XL'),
        (10,   'X'), (9,   'IX'), (5,   'V'), (4,   'IV'),
        (1,    'I')
    ]
    result = ""
    for value, symbol in roman_map:
        while num >= value:
            result += symbol
            num -= value
    return result

def roman_to_int(s):
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    for char in reversed(s.upper()):
        if char not in roman_map:
            raise ValueError("Ungültiges römisches Zeichen: " + char)
        value = roman_map[char]
        if value < prev_value:
            result -= value
        else:
            result += value
            prev_value = value
    return result

# GUI Klasse
class RomanConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Römische Zahlen Umrechner")

        # Widgets
        self.int_label = QLabel("Arabische Zahl (1–3999):")
        self.int_input = QLineEdit()
        self.to_roman_btn = QPushButton("→ Römisch")

        self.roman_label = QLabel("Römische Zahl:")
        self.roman_input = QLineEdit()
        self.to_int_btn = QPushButton("→ Arabisch")

        self.result_label = QLabel("")
        self.result_label.setStyleSheet("color: red")

        # Layouts
        layout = QVBoxLayout()

        row1 = QHBoxLayout()
        row1.addWidget(self.int_input)
        row1.addWidget(self.to_roman_btn)

        row2 = QHBoxLayout()
        row2.addWidget(self.roman_input)
        row2.addWidget(self.to_int_btn)

        layout.addWidget(self.int_label)
        layout.addLayout(row1)
        layout.addWidget(self.roman_label)
        layout.addLayout(row2)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

        # Verbindungen
        self.to_roman_btn.clicked.connect(self.convert_to_roman)
        self.to_int_btn.clicked.connect(self.convert_to_int)

    def convert_to_roman(self):
        try:
            num = int(self.int_input.text())
            if not 1 <= num <= 3999:
                raise ValueError("Nur Zahlen zwischen 1 und 3999 erlaubt.")
            roman = int_to_roman(num)
            self.roman_input.setText(roman)
            self.result_label.setText("")
        except ValueError as e:
            self.result_label.setText(str(e))

    def convert_to_int(self):
        try:
            roman = self.roman_input.text().strip().upper()
            number = roman_to_int(roman)
            self.int_input.setText(str(number))
            self.result_label.setText("")
        except ValueError as e:
            self.result_label.setText(str(e))


# Start der App
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RomanConverter()
    window.show()
    sys.exit(app.exec_())
