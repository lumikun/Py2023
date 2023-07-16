# Implementation of Conway's Game of Life.
# https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life (EN)
# https://lv.wikipedia.org/wiki/Dz%C4%ABve_(sp%C4%93le) (LV)
# The Game of Life, also known simply as Life, is a cellular automaton
# devised by the British mathematician John Horton Conway in 1970.


# 3) All other live cells die in the next generation. Similarly,
# all other dead cells stay dead.

import pygame
import numpy as np
import time


col_bg = (0, 0, 0)
col_grid = (50, 50, 50)
col_alive = (255, 255, 255)
col_dead = (175, 175, 175)
#####################################
#   All Values are pixels           #
#####################################
W = 80  # Widht of the Window
H = 60  # Height of the Window
K = 10  # Constant for changing the window size
CS = 10  # The Cell size scaled to the window size.


# TODO figure out why all the cells die within a short time.
def update(window, cells, with_progress=False):
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))
    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
        color = col_bg if cells[row, col] == 0 else col_alive

        if cells[row, col] == 1:
            if alive < 2 or alive > 3:
                if with_progress:
                    color = col_dead
                elif 2 <= alive <= 3:
                    updated_cells[row, col] = 1
                    if with_progress:
                        color = col_alive
        else:
            if alive == 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = col_alive
        pygame.draw.rect(window, color, (col * CS, row * CS, CS-1, CS-1))
    return updated_cells


def init(x, y):
    cells = np.zeros((y, x))
    pattern = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0,
                            1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0,
                            1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0,
                            1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0,
                            0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0,
                            0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    pos = (3, 3)
    cells[pos[0]:pos[0]+pattern.shape[0], pos[1]          :pos[1]+pattern.shape[1]] = pattern
    return cells


def main():

    pygame.init()
    window = pygame.display.set_mode(((W*K), (H*K)))
    pygame.display.set_caption("Conway's Game of Life")
    window.fill(col_grid)

    running = False

    cells = init(W, H)
    update(window, cells)
    pygame.display.flip()
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(window, cells)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // CS, pos[0] // CS] = 1
                update(window, cells)
                pygame.display.update()

        # window.fill(col_grid)
        # pygame.display.update()

        if running:
            cells = update(window, cells, with_progress=True)
            pygame.display.update()

        time.sleep(0.01)


if (__name__ == "__main__"):
    main()
