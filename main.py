import pygame
from settings import *
from player import Player

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.movement
    screen.fill(BLACK)

    pygame.draw.circle(screen, GREEN, player.pos, 12)

    pygame.display.flip()
    clock.tick(FPS)