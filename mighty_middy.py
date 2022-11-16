import pygame
import time

TILE_SIZE = 64
pygame.init()


screen = pygame.display.set_mode((
    15 * TILE_SIZE, 15 * TILE_SIZE))
water = pygame.image.load("assets"/water_tile.png)
water_rect = water.get_rect()
screen_rect = screen.get_rect()
num_tiles = screen_rect.width // water_rect.width

for y in range(num_tiles):
    for x in range(num_tiles):
        screen.blit(water, (x * water_rect.width, y * water_rect.height))

print(water_rect)
screen.blit(water, (0, 0))
screen.bit(water, (water_rect.width + 1, 0))
screen.blit(water, (0, water_rect.height + 1))


while True:
    # 1 check for user inputs (keys, mouse)
    for event in pygame.event.get():
        if event.type == 769:
            print("you released a key")
        if event.type == pygame.MOUSEMOTION:
            print("You moved the mouse")
    time.sleep(1)
