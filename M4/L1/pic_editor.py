
from PIL import Image




class ImageEditor():
    def __init__(self, filename):
        self.filename = filename
        self.original = None
        self.changed = []

    def open(self):
        try:
            self.original =  Image.open(self.filename)
        except:
            print("File not found")
            return
        self.original.show()
    
    def do_bw(self):
        gray = self.original.convert("L")
        self.changed.append(gray)
        gray.save("M4/L1/gray.jpg")


MyImage = ImageEditor("M4\L1\cute_chick_with_hairy_cat.png")
MyImage.open()
MyImage.do_bw()