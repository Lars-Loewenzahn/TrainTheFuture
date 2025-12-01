from turtle import *
from random import *

# basic setup
penup()
speed(0)        # drawing speed
pensize(1)
hideturtle()
color("blue")


class House():
    def __init__(self, col, size, x,y):
        self.size = size
        goto(x,y)
        pendown()
        setheading(0)
        color(col)
        begin_fill()
        for _ in range(4):
            forward(size)
            right(90)
        end_fill()

        color("brown")
        begin_fill()
        left(60)
        forward(size)
        right(120)
        forward(size)
        end_fill()
        penup()

class Firestation(House):
    def __init__(self, x,y):
        super().__init__("red", 100, x, y)
        setheading(270)
        forward(self.size)
        right(90)
        forward(self.size/2 + 30)
        pendown()
        color("grey")
        right(90)
        begin_fill()
        forward(75)
        right(90)
        forward(60)
        right(90)
        forward(75)
        right(90)
        forward(60)
        right(90)
        end_fill()
        penup()

class Hospital(House):
    def __init__(self, x ,y):
        super().__init__("grey", 150, x,y)
        setheading(270)
        forward(self.size/2)
        right(90)
        forward(self.size/2)
        # Kreuz 100 hoch und breit, Strichstärke 10
        pensize(10)
        color("red")
        pendown()
        forward(50)
        backward(100)
        forward(50)
        left(90)
        forward(50)
        backward(100)
        forward(50)
        pensize(1)
        penup()


colors  = [
    "black", "white", "red", "green", "blue",
    "cyan", "magenta", "yellow",
    "gray", "grey", "lightgray", "darkgray",
    "brown", "orange", "pink",
    "purple", "violet", "navy",
    "skyblue", "turquoise",
    "gold", "silver",
    "lime", "maroon", "olive", "teal",
    "indigo", "coral", "salmon", "chocolate", "sienna"
]

while True:
    for i in range(6):
        h = House(choice(colors), randint(20, 75), randint(-400, 350), randint(-350, 350))
    f = Firestation(randint(-400, 350),randint(-350, 350))
    g = Hospital(randint(-400, 350),randint(-350, 350))

done()
