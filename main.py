import pygame
from settings import *
from player import Player
import math
from map import world_map

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.movement()
    screen.fill(BLACK)

    pygame.draw.circle(screen, GREEN, player.pos, 12)
    pygame.draw.line(screen, GREEN, player.pos, (player.x + WIDTH * math.cos(player.angle), player.y + WIDTH * math.sin(player.angle)))
    
    for x,y in world_map:
        pygame.draw.rect(screen, DARKGRAY, (x, y, TILE, TILE), 2)

    pygame.display.flip()
    clock.tick(FPS)