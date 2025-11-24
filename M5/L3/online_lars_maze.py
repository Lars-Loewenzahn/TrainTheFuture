from turtle import speed
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (55,55))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def refresh(self):
        window.blit(self.image, (self.rect.x ,self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.side = "left"

    def update(self):
        if  self.rect.x <= 470:
            self.side = "right"
        if self.rect.x >= win_width-85:
            self.side = "left"
            
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed






win_width = 700
win_height = 500
window = display.set_mode((win_width , win_height))
display.set_caption("Maze")
background = transform.scale(image.load("M5/L2/background.jpg"), (win_width, win_height))

packman = Player('M5\L2\hero.png', 5, win_height - 80, 4)
monster = Enemy("M5/L2/cyborg.png", win_width - 80, 280, 2)

FPS = 60
game = True
clock = time.Clock()

mixer.init()
mixer.music.load("M5\L2\jungles.ogg")
mixer.music.play()

while game:
    window.blit(background, (0,0))

    events = event.get()
    for e in events:
        if e.type == QUIT:
            game = False
    packman.update()
    monster.update()
    packman.refresh()
    monster.refresh()
        

    # keys_pressed = key.get_pressed()
    # # SPRTIE 1
    # if keys_pressed[K_UP] and y1 > 0:
    #     y1 -= speed
    # if keys_pressed[K_DOWN] and y1 < 395:
    #     y1 += speed
    # if keys_pressed[K_LEFT] and x1 > 0:
    #     x1 -= speed
    # if keys_pressed[K_RIGHT] and x1 < 595:
    #     x1 += speed


    display.update()
    clock.tick(FPS)