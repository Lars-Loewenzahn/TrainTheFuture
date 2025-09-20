from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton, 
    QListWidget, 
    QVBoxLayout, 
    QHBoxLayout )

app = QApplication([])
win = QWidget()
btn_dir = QPushButton("Folder")
lw_files = QListWidget()

col1 = QVBoxLayout()
col1.addWidget(btn_dir)
col1.addWidget(lw_files)

btn_left = QPushButton("Left") 
btn_right = QPushButton("Right") 
btn_flip = QPushButton("Mirror")
btn_sharp = QPushButton("Sharpness")
btn_bw = QPushButton("B&W")

row_tools = QHBoxLayout()
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)

lb_image = QLabel("Image")

col2 = QVBoxLayout()
col2.addWidget(lb_image, 95)
col2.addLayout(row_tools, 5)

row = QHBoxLayout()
row.addLayout(col1, 20)
row.addLayout(col2, 80)

win.setWindowTitle("Easy Editor")
win.resize(700, 400)
win.setLayout(row)
win.show()
app.exec()