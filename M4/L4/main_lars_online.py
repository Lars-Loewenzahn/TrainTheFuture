import os
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QListWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QFileDialog,
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PIL import Image
from PIL import ImageFilter

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
btn_blur = QPushButton("Blur")
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
row_tools.addWidget(btn_blur)

col2.addLayout(row_tools, 80)
row.addLayout(col2)
win.setLayout(row)

class ImageProcessor():
    def __init__(self):
        self.image = None
        self.filename = None
        self.save_dir = "Modified/"

    def loadImage(self, dir, filename):
        self.filename = filename
        self.dir = dir
        image_path = os.path.join(dir, filename)
        self.image = Image.open(image_path)


    def showImage(self, path):
        lb_image.hide()
        pixmapimage = QPixmap(path)
        w, h = lb_image.width(), lb_image.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        lb_image.setPixmap(pixmapimage)
        lb_image.show()

    def do_bw(self):
        self.image = self.image.convert("L")
        self.saveImage()
        global workdir
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_flip(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveImage()
        global workdir
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        global workdir
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    
    def do_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.saveImage()
        global workdir
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    
    def do_sharpen(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.saveImage()
        global workdir
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.saveImage()
        global workdir
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)


    def saveImage(self):
        path = os.path.join(workdir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)

workimage = ImageProcessor()

def showChosenImage():
    if lw_files.currentRow() >= 0:
        filename = lw_files.currentItem().text()
        workimage.loadImage(workdir, filename)
        image_path = os.path.join(workimage.dir, workimage.filename)
        workimage.showImage(image_path)


def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def showFileNameList():
    extensions = [".jpg", ".png" , ".bmp", ".svg", ".ips"]
    chooseWorkdir()
    global workdir
    filenames = os.listdir(workdir)
    filenames = filter(filenames, extensions)
    lw_files.clear()
    for filename in filenames:
        lw_files.addItem(filename)



def filter(filenames, extensions):
    filtered_filenames = []
    for filename in filenames:
        print(filename[-4:])
        for extension in extensions:
            if filename[-4:] == extension:
                filtered_filenames.append(filename)
    return filtered_filenames


btn_dir.clicked.connect(showFileNameList)
lw_files.currentRowChanged.connect(showChosenImage)
btn_bw.clicked.connect(workimage.do_bw)
btn_flip.clicked.connect(workimage.do_flip)
btn_left.clicked.connect(workimage.do_left)
btn_right.clicked.connect(workimage.do_right)
btn_sharp.clicked.connect(workimage.do_sharpen)
btn_blur.clicked.connect(workimage.do_blur)

win.show()
app.exec()
