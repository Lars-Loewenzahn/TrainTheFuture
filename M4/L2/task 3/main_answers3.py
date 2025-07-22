import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QFileDialog, QLabel,
    QPushButton, QListWidget, QHBoxLayout, QVBoxLayout
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PIL import Image

########### Task 1. Creating the interface #########
app = QApplication([])
win = QWidget()
win.resize(700, 500)
win.setWindowTitle('Easy Editor')

lb_image = QLabel("Image")
lb_image.setAlignment(Qt.AlignCenter)

btn_dir = QPushButton("Folder")
lw_files = QListWidget()

btn_left = QPushButton("Left")
btn_right = QPushButton("Right")
btn_flip = QPushButton("Mirror")
btn_sharp = QPushButton("Sharpness")
btn_bw = QPushButton("B/W")

row = QHBoxLayout()          # Main layout
col1 = QVBoxLayout()         # Left column (buttons and list)
col2 = QVBoxLayout()         # Right column (image and tools)

col1.addWidget(btn_dir)      # Folder selection button
col1.addWidget(lw_files)     # File list

col2.addWidget(lb_image, 95) # Image display

row_tools = QHBoxLayout()    # Tool button row
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)
col2.addLayout(row_tools)

row.addLayout(col1, 20)
row.addLayout(col2, 80)
win.setLayout(row)
win.show()

########### Task 2. Displaying a list of graphic file names #########
workdir = ''  # Global variable for current working directory

def filter(files, extensions):
    result = []
    for filename in files:
        for ext in extensions:
            if filename.lower().endswith(ext):
                result.append(filename)
    return result

def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def showFilenamesList():
    extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    chooseWorkdir()
    filenames = filter(os.listdir(workdir), extensions)
    lw_files.clear()
    for filename in filenames:
        lw_files.addItem(filename)

btn_dir.clicked.connect(showFilenamesList)

########### Task 3. Creating the ImageProcessor class #########
class ImageProcessor:
    def __init__(self):
        self.image = None
        self.filename = None

    def loadImage(self, directory, filename):
        self.filename = filename
        full_path = os.path.join(directory, filename)
        self.image = Image.open(full_path)

    def showImage(self):
        if self.image:
            self.image.thumbnail((lb_image.width(), lb_image.height()))
            self.image.save("temp_preview.png")  # Workaround: save thumbnail
            lb_image.setPixmap(QPixmap("temp_preview.png"))

workimage = ImageProcessor()

########### Task 4. Showing image preview when file is selected #########
def showChosenImage():
    if lw_files.currentRow() >= 0:
        filename = lw_files.currentItem().text()
        workimage.loadImage(workdir, filename)
        workimage.showImage()

lw_files.currentRowChanged.connect(showChosenImage)

app.exec()
