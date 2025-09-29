import os
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QListWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QFileDialog
)


app = QApplication([])
win = QWidget()
win.setWindowTitle("Easy Editor")
win.resize(700, 400)

btn_dir = QPushButton("Folder")
lw_files = QListWidget()
btn_left = QPushButton("Left")
btn_right = QPushButton("Right")
btn_flip = QPushButton("Mirror")
btn_sharp = QPushButton("Sharpen")
btn_bw = QPushButton("B&W")
lb_image = QLabel("Image")

col1 = QVBoxLayout()
col2 = QVBoxLayout()
row = QHBoxLayout()
row_tools = QHBoxLayout()

col1.addWidget(btn_dir)
col1.addWidget(lw_files)

row.addLayout(col1, 20)

col2.addWidget(lb_image)
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)

col2.addLayout(row_tools, 80)
row.addLayout(col2)
win.setLayout(row)

def showFileNameList():
    extensions = [".jpg", ".png" , ".bmp", ".svg", ".ips"]
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    filenames = os.listdir(workdir)
    filter(filenames, extensions)



def filter(filenames, extensions):
    filtered_filenames = []
    for filename in filenames:
        print(filename[-4:])
        for extension in extensions:
            if filename[-4:] == extension:
                filtered_filenames.append(filename)
    return filtered_filenames



win.show()
app.exec()

