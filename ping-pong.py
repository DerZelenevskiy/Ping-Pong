import pygame

width, height = 800, 600
fps = 60

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

while True:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    screen.fill((150, 150, 255))
    pygame.display.update()