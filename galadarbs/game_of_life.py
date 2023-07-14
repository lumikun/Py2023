# Implementation of Conway's Game of Life.
# https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life (EN)
# https://lv.wikipedia.org/wiki/Dz%C4%ABve_(sp%C4%93le) (LV)
# The Game of Life, also known simply as Life, is a cellular automaton 
# devised by the British mathematician John Horton Conway in 1970.

# 1) Any live cell with two or three live neighbours survives.
# 2) Any dead cell with three live neighbours becomes a live cell.
# 3) All other live cells die in the next generation. Similarly, all other dead cells stay dead.

# STUB testing pygame
import pygame

pygame.init()

screen = pygame.display.set_mode([500, 500])

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False
    
    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    pygame.display.flip()

pygame.quit()