import pygame

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
    pass

class Racket(GameSprite):
    pass

racket1 = Racket('platform.png', 46, 200, 0, 200)
racket2 = Racket('platform.png', 46, 200, 754, 200)
ball = Ball('ball.png', 50, 50, 375, 275)

while True:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    screen.fill((150, 150, 255))

    racket1.blit(screen)
    racket2.blit(screen)
    ball.blit(screen)

    pygame.display.update()
