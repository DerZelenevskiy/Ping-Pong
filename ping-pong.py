import pygame
from random import choice

width, height = 800, 600
fps = 60

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image, image_x, image_y, x, y):
        self.image = pygame.transform.scale(pygame.image.load(image), (image_x, image_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def blit(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Ball(GameSprite):
    def __init__(self, image, image_x, image_y, x, y):
        self.image = pygame.transform.scale(pygame.image.load(image), (image_x, image_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = choice([5, -5])
        self.speedy = choice([5, -5])

    def move(self, rackets):
        for i in rackets:
            if self.rect.colliderect(i.rect):
                self.speedx = 0 - self.speedx
        if self.rect.x <= 0 or self.rect.x >= 750:
            self.speedx = 0 - self.speedx
        if self.rect.y <= 0 or self.rect.y >= 550:
            self.speedy = 0 - self.speedy
        self.rect.x += self.speedx
        self.rect.y += self.speedy

class Racket(GameSprite):
    def move(self, keys, controller):
        if controller == 'w,s':
            if keys[pygame.K_w] and self.rect.y > 0:
                self.rect.y -= 5
            if keys[pygame.K_s] and self.rect.y < 400:
                self.rect.y += 5
        if controller == 'up,down':
            if keys[pygame.K_UP] and self.rect.y > 0:
                self.rect.y -= 5
            if keys[pygame.K_DOWN] and self.rect.y < 400:
                self.rect.y += 5

racket1 = Racket('platform.png', 46, 200, 0, 200)
racket2 = Racket('platform.png', 46, 200, 754, 200)
ball = Ball('ball.png', 50, 50, 375, 275)

ticks = 300
while True:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    keys = pygame.key.get_pressed()
    screen.fill((150, 150, 255))

    racket1.move(keys, 'w,s')
    racket2.move(keys, 'up,down')
    if ticks == 0:
        ticks = 300
        if ball.speedx > 0:
            ball.speedx += 1
        if ball.speedx < 0:
            ball.speedx -= 1
        if ball.speedy > 0:
            ball.speedy += 1
        if ball.speedy < 0:
            ball.speedy -= 1
    ball.move([racket1, racket2])

    racket1.blit(screen)
    racket2.blit(screen)
    ball.blit(screen)

    pygame.display.update()
    ticks -= 1
