import pygame
from settings import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill(BLACK)

    pygame.draw.circle(screen, GREEN, player_pos, 12)

    pygame.display.flip()
    clock.tick()