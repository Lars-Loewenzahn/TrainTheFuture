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



# Spieler 1
player_1 = transform.scale(image.load("M5/L1/sprite1.png"), (55,55))
player_1_x, player_1_y = 50, 50
player_1_vel = 5


# Spieler 2
player_2  =GameSprite("M5/L1/sprite2.png", 5, (50, 300))

window = display.set_mode((700, 500))
display.set_caption("Catch")

background = transform.scale(image.load("M5/L1/background.png"), (700, 500))

clock = time.Clock()

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (0 ,0))
    window.blit(player_1, (player_1_x, player_1_y))
    player_2.draw()

    keys_pressed = key.get_pressed()
    if keys_pressed[K_UP] and player_1_y > 5:
        player_1_y-= player_1_vel
    if keys_pressed[K_DOWN] and player_1_y < 440:
        player_1_y += player_1_vel
    if keys_pressed[K_LEFT] and player_1_x > 5:
        player_1_x -= player_1_vel
    if keys_pressed[K_RIGHT] and player_1_x < 640:
        player_1_x += player_1_vel

    display.update()
    clock.tick(60)