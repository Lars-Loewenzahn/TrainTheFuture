from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, image_path, player_x, player_y, size_x, size_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(image_path), (size_x, size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



win_width = 700
win_height = 500

display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))

bg_im = image.load("M5/L4/galaxy.jpg")
background = transform.scale(bg_im, (win_width, win_height))

player = GameSprite("M5/L4/rocket.png", 300, win_height - 100 , 80, 100, 10)


run = True
FPS = 20
clock = time.Clock()

while run: 
    for e in event.get():
        if e.type == QUIT:
            run = False
    window.blit(background, (0,0))

    player.draw()


    display.update()
    clock.tick(FPS)