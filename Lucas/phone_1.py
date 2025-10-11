import pygame as pg 
from pygame.locals import *
from pygame.version import PygameVersion
import os

pg.init()

# Constants
WINDOW_SIZE = (500, 750)
GameWindow = pg.display.set_mode(WINDOW_SIZE)
pg.display.set_caption('Bank Account Simulater')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

#Button Colliders
UpBT2_Collider_Pressed = False
MiddleBT5_Collider_Pressed = False
DownBT8_Collider_Pressed = False
LeftBT4_Collider_Pressed = False
RightBT6_Collider_Pressed = False
TopLeftBT1_Collider_Pressed = False
TopRightBT3_Collider_Pressed = False
BottomLeftBT7_Collider_Pressed = False
BottomRightBT9_Collider_Pressed = False
BottomBT0_Collider_Pressed = False

class Main_UI:
    def __init__(self):
        self.window_size = WINDOW_SIZE
        self.image = None
        self.visible = False
    def Phone_Draw(self):
        # Get current directory and construct proper path
        current_dir = os.path.dirname(os.path.abspath(__file__))
        bg_path = os.path.join(current_dir, "suggestion1", "background.png")
        self.PhoneImage = pg.image.load(bg_path)
        # Use WINDOW_SIZE directly as a fallback in case self.window_size is not set
        window_size = getattr(self, 'window_size', WINDOW_SIZE)
        self.PhoneImage = pg.transform.scale(self.PhoneImage, (window_size[0], window_size[1]))
        GameWindow.blit(self.PhoneImage, (0, 0))
    def Collider_Draw(self):
        self.HomeBT_Collider = pg.draw.rect(GameWindow, GRAY, (200, 400, 100, 100), 1)
        self.UpBT2_Collider = pg.draw.rect(GameWindow, GRAY, (200, 515, 100, 50), 1)
        self.MiddleBT5_Collider = pg.draw.rect(GameWindow, GRAY, (200, 575, 100, 50), 1)
        self.DownBT8_Collider = pg.draw.rect(GameWindow, GRAY, (200, 635, 100, 50), 1)
        self.LeftBT4_Collider = pg.draw.rect(GameWindow, GRAY, (50, 575, 100, 50), 1)
        self.RightBT6_Collider = pg.draw.rect(GameWindow, GRAY, (350, 575, 100, 50), 1)
        self.TopLeftBT1_Collider = pg.draw.rect(GameWindow, GRAY, (50, 515, 100, 50), 1)
        self.TopRightBT3_Collider = pg.draw.rect(GameWindow, GRAY, (350, 515, 100, 50), 1)
        self.BottomLeftBT7_Collider = pg.draw.rect(GameWindow, GRAY, (50, 635, 100, 50), 1)
        self.BottomRightBT9_Collider = pg.draw.rect(GameWindow, GRAY, (350, 635, 100, 50), 1)
        self.BottomBT0_Collider = pg.draw.rect(GameWindow, GRAY, (200, 695, 100, 50), 1)

    def Collider_Check(self):
        if self.HomeBT_Collider.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
            print("Home Button Pressed")
            HomeBT_Collider_Pressed = True
        if self.UpBT2_Collider.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
            print("2Up Button Pressed")
            UpBT2_Collider_Pressed = True
        if self.MiddleBT5_Collider.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
            print("5Middle Button Pressed")
            MiddleBT5_Collider_Pressed = True
        if self.DownBT8_Collider.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
            print("8Down Button Pressed")
            DownBT8_Collider_Pressed = True
        if self.LeftBT4_Collider.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
            print("4Left Button Pressed")
            LeftBT4_Collider_Pressed = True
        if self.RightBT6_Collider.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
            print("6Right Button Pressed")
            RightBT6_Collider_Pressed = True
        if self.TopLeftBT1_Collider.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
            print("1TopLeft Button Pressed")
            TopLeftBT1_Collider_Pressed = True
        if self.TopRightBT3_Collider.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
            print("3TopRight Button Pressed")
            TopRightBT3_Collider_Pressed = True
        if self.BottomLeftBT7_Collider.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
            print("7BottomLeft Button Pressed")
            BottomLeftBT7_Collider_Pressed = True
        if self.BottomRightBT9_Collider.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
            print("9BottomRight Button Pressed")
            BottomRightBT9_Collider_Pressed = True
        if self.BottomBT0_Collider.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
            print("0Bottom Button Pressed")
            BottomBT0_Collider_Pressed = True


class Home_Screen:
    def __init__(self):
        self.window_size = WINDOW_SIZE
        self.image = None
        self.visible = False
    def Collider_Draw(self):
        self.App_Bank_Collider = pg.draw.rect(GameWindow, GRAY, (73, 142, 68, 50))
        self.App_Email_Collider = pg.draw.rect(GameWindow, GRAY, (73+80, 142, 68, 50))
        self.App_WorldMap_Collider = pg.draw.rect(GameWindow, GRAY, (73+80+80, 142, 68, 50))
        self.App_LinkedIn_Collider = pg.draw.rect(GameWindow, GRAY, (73+80+80+80, 142, 68, 50))
        self.App_Internet_Collider = pg.draw.rect(GameWindow, GRAY, (73, 142+53, 68, 50))
        self.App_Appspace1_Collider = pg.draw.rect(GameWindow, GRAY, (73+80, 142+53, 68, 50))
        self.App_Appspace2_Collider = pg.draw.rect(GameWindow, GRAY, (73+80+80, 142+53, 68, 50))
        self.App_Appspace3_Collider = pg.draw.rect(GameWindow, GRAY, (73+80+80+80, 142+53, 68, 50)) 
        self.App_Appspace4_Collider = pg.draw.rect(GameWindow, GRAY, (73, 142+53+53, 68, 50))
        self.App_Appspace5_Collider = pg.draw.rect(GameWindow, GRAY, (73+80, 142+53+53, 68, 50))
        self.App_Appspace6_Collider = pg.draw.rect(GameWindow, GRAY, (73+80+80, 142+53+53, 68, 50))
        self.App_Appspace7_Collider = pg.draw.rect(GameWindow, GRAY, (73+80+80+80, 142+53+53, 68, 50))
    def App_Selecter_Draw(self):
        self.App_Selecter = pg.draw.rect(GameWindow, WHITE, (73, 142, 68, 50))
    def App_Selecter_Movement(self):
        if UpBT2_Collider_Pressed:
            if self.App_Selecter.y >= 142:
                self.App_Selecter.y -= 142
        if DownBT8_Collider_Pressed:
            if self.App_Selecter.y <= 692:
                self.App_Selecter.y += 692
        if LeftBT4_Collider_Pressed:
            if self.App_Selecter.x >= 73:
                self.App_Selecter.x -= 73
            else:
                self.App_Selecter.x -= 80
        if RightBT6_Collider_Pressed:
            if self.App_Selecter.x <= 313:
                self.App_Selecter.x -= 313
            else:
                self.App_Selecter.x += 80
            
    def App_Selecter_Check(self):
        if self.App_Selecter.collidepoint((self.App_Bank_Collider.x, self.App_Bank_Collider.y)):
            print("Bank App Selected")
        if self.App_Selecter.collidepoint((self.App_Email_Collider.x, self.App_Email_Collider.y)):
            print("Email App Selected")
        if self.App_Selecter.collidepoint((self.App_WorldMap_Collider.x, self.App_WorldMap_Collider.y)):
            print("World Map App Selected")
        if self.App_Selecter.collidepoint((self.App_LinkedIn_Collider.x, self.App_LinkedIn_Collider.y)):
            print("LinkedIn App Selected")
        if self.App_Selecter.collidepoint((self.App_Internet_Collider.x, self.App_Internet_Collider.y)):
            print("Internet App Selected")
        if self.App_Selecter.collidepoint((self.App_Appspace1_Collider.x, self.App_Appspace1_Collider.y)):
            print("Appspace1 App Selected")
        if self.App_Selecter.collidepoint((self.App_Appspace2_Collider.x, self.App_Appspace2_Collider.y)):
            print("Appspace2 App Selected")
        if self.App_Selecter.collidepoint((self.App_Appspace3_Collider.x, self.App_Appspace3_Collider.y)):
            print("Appspace3 App Selected")
        if self.App_Selecter.collidepoint((self.App_Appspace4_Collider.x, self.App_Appspace4_Collider.y)):
            print("Appspace4 App Selected")
        if self.App_Selecter.collidepoint((self.App_Appspace5_Collider.x, self.App_Appspace5_Collider.y)):
            print("Appspace5 App Selected")
        if self.App_Selecter.collidepoint((self.App_Appspace6_Collider.x, self.App_Appspace6_Collider.y)):
            print("Appspace6 App Selected")
        if self.App_Selecter.collidepoint((self.App_Appspace7_Collider.x, self.App_Appspace7_Collider.y)):
            print("Appspace7 App Selected")
        

#defining objects
Main_UI = Main_UI()
Home_Screen = Home_Screen()
GameClock = pg.time.Clock()

#Drawing Colliders
Main_UI.Collider_Draw()


#Rememeber to always draw UI over the Box Colliders
#Drawing the UI
Main_UI.Phone_Draw()

Home_Screen.Collider_Draw()
Home_Screen.App_Selecter_Draw()



running = True
while running:
    GameClock.tick(60)
    UpBT2_Collider_Pressed = False
    MiddleBT5_Collider_Pressed = False
    DownBT8_Collider_Pressed = False
    LeftBT4_Collider_Pressed = False
    RightBT6_Collider_Pressed = False
    TopLeftBT1_Collider_Pressed = False
    TopRightBT3_Collider_Pressed = False
    BottomLeftBT7_Collider_Pressed = False
    BottomRightBT9_Collider_Pressed = False
    BottomBT0_Collider_Pressed = False
    
    # Handle events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
           Main_UI.Collider_Check()
           Home_Screen.App_Selecter_Movement()
        
    Home_Screen.App_Selecter_Draw()
    pg.display.update()