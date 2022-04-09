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

while True:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    screen.fill((150, 150, 255))
    pygame.display.update()