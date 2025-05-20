import turtle

class SnackautomatAnimation:
    def __init__(self, betriebssystem_callback=None):
        self.screen = turtle.Screen()
        self.screen.setup(600, 600)
        self.screen.title('Snackautomat')
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.speed(0)
        self.betriebssystem_callback = betriebssystem_callback
        self.products = [
            ('Chips', 1),
            ('Cola', 2),
            ('Schokoriegel', 3),
            ('Kaugummi', 4),
            ('Wasser', 5)
        ]
        self.coins = [0.5, 1, 2]
        self.draw_automat()
        self.draw_products()
        self.draw_coins()
        self.draw_screen()
        self.draw_keypad()
        self.screen.listen()

    def draw_automat(self):
        # Automat-Gehäuse
        self.t.penup()
        self.t.goto(-120, 150)
        self.t.pendown()
        self.t.fillcolor('#888')
        self.t.begin_fill()
        for _ in range(2):
            self.t.forward(240)
            self.t.right(90)
            self.t.forward(400)
            self.t.right(90)
        self.t.end_fill()
        self.t.penup()

    def draw_products(self):
        start_y = 100
        for idx, (name, num) in enumerate(self.products):
            y = start_y - idx * 40
            self.t.goto(-90, y)
            self.t.pendown()
            self.t.fillcolor('#ffe680')
            self.t.begin_fill()
            for _ in range(2):
                self.t.forward(120)
                self.t.right(90)
                self.t.forward(30)
                self.t.right(90)
            self.t.end_fill()
            self.t.penup()
            self.t.goto(-80, y+5)
            self.t.color('black')
            self.t.write(f"{num}. {name}", font=("Arial", 14, "normal"))
            self.t.penup()
        self.t.color('black')

    def draw_coins(self):
        # Münzen unter dem Automaten
        x = -60
        for val in self.coins:
            self.t.goto(x, -280)
            self.t.pendown()
            self.t.fillcolor('#ffd700')
            self.t.begin_fill()
            self.t.circle(20)
            self.t.end_fill()
            self.t.penup()
            self.t.goto(x, -310)
            self.t.write(f"{val}€", align='center', font=("Arial", 12, "bold"))
            x += 60
        self.t.penup()

    def draw_screen(self):
        # Bildschirm
        self.t.goto(-80, -120)
        self.t.pendown()
        self.t.fillcolor('#222')
        self.t.begin_fill()
        for _ in range(2):
            self.t.forward(160)
            self.t.right(90)
            self.t.forward(40)
            self.t.right(90)
        self.t.end_fill()
        self.t.penup()
        self.t.goto(-75, -115)
        self.t.color('lime')
        self.t.write('Willkommen!', font=("Arial", 16, "bold"))
        self.t.color('black')
        self.t.penup()

    def draw_keypad(self):
        # Zahlenfeld
        start_x = -60
        start_y = -180
        for i in range(1, 10):
            x = start_x + ((i-1)%3)*40
            y = start_y - ((i-1)//3)*40
            self.t.goto(x, y)
            self.t.pendown()
            self.t.fillcolor('#bbb')
            self.t.begin_fill()
            for _ in range(4):
                self.t.forward(30)
                self.t.right(90)
            self.t.end_fill()
            self.t.penup()
            self.t.goto(x+10, y-25)
            self.t.write(str(i), font=("Arial", 14, "bold"))
        # 0 Taste
        self.t.goto(start_x+40, start_y-120)
        self.t.pendown()
        self.t.fillcolor('#bbb')
        self.t.begin_fill()
        for _ in range(4):
            self.t.forward(30)
            self.t.right(90)
        self.t.end_fill()
        self.t.penup()
        self.t.goto(start_x+50, start_y-145)
        self.t.write('0', font=("Arial", 14, "bold"))
        self.t.penup()

    def run(self):
        self.screen.mainloop()

# Test (entfernen, wenn mit betriebssystem verbunden)
if __name__ == '__main__':
    anim = SnackautomatAnimation()
    anim.run()
