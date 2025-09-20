from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

app = QApplication([])
main_window = QWidget()

main_window.setGeometry(100, 100, 300, 200) # (x, y, width, height)
main_window.setWindowTitle('Einfaches PyQt Beispiel')

button = QPushButton('Klick mich!', main_window)
button.setGeometry(100, 80, 100, 30) # (x, y, width, height)

def on_button_click():
  """Eine einfache Funktion, die aufgerufen wird, wenn die Schaltfläche geklickt wird."""
  print("Schaltfläche wurde geklickt!")

button.clicked.connect(on_button_click)

main_window.show()

app.exec()