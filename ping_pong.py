from pygame import *
from random import randint 
from time import time as timer
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width ,player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 450:
            self.rect.y += self.speed

lost = 0
hop = 0

clock = time.Clock()
FPS = 60

window = display.set_mode((700, 500))
display.set_caption("Понг")
player1 = Player('racket.jpeg',50, 200, 65, 100, 10)
player2 = Player('racket.jpeg',590, 200, 65, 100, 10)
ball = GameSprite('ball.jpeg',320, 200, 70, 70, 8 )

game = True
finish = False
while game:
    
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN and e.key == K_SPACE:
            if num_fire < 5 and rel_time == False:
                num_fire = num_fire + 1
                player.fire()
            if num_fire>=5 and rel_time == False:
                rel_time = True
                last_time = timer()

    if finish != True:
        window.fill((255,250,255))
        player1.reset()
        player1.update_l()
        player2.reset()
        player2.update_r()
        clock.tick(FPS)
        ball.reset()
    display.update()