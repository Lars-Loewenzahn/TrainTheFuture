from pygame import *

' ' 'Required classes' ' '

#parent class for sprites 
class GameSprite(sprite.Sprite):
    #class constructor
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
 
        #every sprite must store the image property
        self.image = transform.scale(image.load(player_image), (55, 55))
        self.speed = player_speed
 
        #every sprite must have the rect property – the rectangle it is fitted in
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#heir class for the player sprite (controlled by arrows)
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

#heir class for the enemy sprite (moves by itself)
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

#class for obstacle sprites
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
 
        #wall image – a rectangle of the required size and color
        self.image = Surface([self.width, self.height])
        self.image.fill((color_1, color_2, color_3))
 
        #every sprite must store the rect – rectangular property
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
 
    def draw_wall(self):
        draw.rect(window, (self.color_1, self.color_2, self.color_3), (self.rect.x, self.rect.y, self.width, self.height))

#Game scene:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("M5/L3/background.jpg"), (win_width, win_height))

#Game characters:
packman = Player('M5/L3/hero.png', 5, win_height - 80, 4)
monster = Enemy('M5/L3/cyborg.png', win_width - 80, 280, 2)
final = GameSprite('M5/L3/treasure.png', win_width - 120, win_height - 80, 0)

w1 = Wall(154, 205, 50, 100, 20 , 450, 10)
w2 = Wall(154, 205, 50, 100, 480, 350, 10)
w3 = Wall(154, 205, 50, 100, 20 , 10, 380)
w4 = Wall(154, 205, 50, 200, 130, 10, 350)
w5 = Wall(154, 205, 50, 450, 130, 10, 360)
w6 = Wall(154, 205, 50, 300, 20, 10, 350)
w7 = Wall(154, 205, 50, 390, 120, 130, 10)
walls =[w1, w2, w3, w4, w5 ,w6, w7]

# You win!
font.init()
font = font.Font(None, 70)
win = font.render("You win!", True, (255, 215 , 0))
lose = font.render("You lose!", True, (255, 0 , 0))

game = True
finish = False
clock = time.Clock()
FPS = 60

mixer.init()
mixer.music.load('M5/L3/jungles.ogg')
mixer.music.play()

money = mixer.Sound('M5/L3/money.ogg')
kick = mixer.Sound('M5/L3/kick.ogg')

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.blit(background,(0, 0))
        packman.update()
        monster.update()
        
        packman.reset()
        monster.reset()
        final.reset() 

        for wall in walls:
            wall.draw_wall()
            if sprite.collide_rect(packman, wall):
                finish = True
                kick.play()
                window.blit(lose, (200, 200))

        if sprite.collide_rect(packman, final):
            finish = True
            money.play()
            window.blit(win, (200, 200))

        if sprite.collide_rect(packman, monster):
            finish = True
            kick.play()
            window.blit(lose, (200, 200))

    display.update()
    clock.tick(FPS)




