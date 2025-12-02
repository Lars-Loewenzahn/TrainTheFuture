from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, image_path, player_x, player_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(image_path), (55,55))
        self.speed = speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed

class Enemy(GameSprite):
    side = "left"
    def update(self):
        if self.rect.x <= 470:
            self.side = "right"
        
        if self.rect.x >= win_width - 85:
            self.side = "left"

        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")

background = transform.scale(image.load("M5/L2/background.jpg"), (win_width, win_height))

packman = Player("M5/L2/hero.png", 5, win_height - 80, 4)
monster = Enemy("M5/L2/cyborg.png", win_width - 80, 280, 2)
final = GameSprite("M5/L2/treasure.png", win_width - 120, win_height - 80, 0)

game = True
clock = time.Clock()
FPS = 60


mixer.init()
mixer.music.load("M5/L2/jungles.ogg")
mixer.music.play()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (0 ,0))
    packman.draw()
    packman.update()
    monster.draw()
    monster.update()
    final.draw()

    display.update()
    clock.tick(FPS)
