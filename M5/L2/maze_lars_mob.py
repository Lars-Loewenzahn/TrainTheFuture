from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, image_path, speed, pos):
        super().__init__()
        self.image = transform.scale(image.load(image_path), (55,55))
        self.speed = speed

        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")

background = transform.scale(image.load("M5/L2/background.jpg"), (win_width, win_height))


game = True
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (0 ,0))

    display.update()
    clock.tick(60)