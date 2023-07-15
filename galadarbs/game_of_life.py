# Implementation of Conway's Game of Life.
# https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life (EN)
# https://lv.wikipedia.org/wiki/Dz%C4%ABve_(sp%C4%93le) (LV)
# The Game of Life, also known simply as Life, is a cellular automaton 
# devised by the British mathematician John Horton Conway in 1970.

# 1) Any live cell with two or three live neighbours survives.
# 2) Any dead cell with three live neighbours becomes a live cell.
# 3) All other live cells die in the next generation. Similarly, all other dead cells stay dead.

# STUB testing pygame
import argparse
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
W = 64      #    Widht of the Window 
H = 48      #    Height of the Window
K = 10      #    Constant for changing the window size
CS = 10      #    The Cell size scaled to the window size.

def update_frame(window, cur):
    frame = np.zeros((cur.shape[0], cur.shape[1]))
    for row, col in np.ndindex(cur.shape):
        num_alive = np.sum(cur[row-1:row+2, col-1:col+2]) - cur[row, col]
        
        if (cur[row, col] == 1 and num_alive < 2 or num_alive > 3):
            c = col_dead
        elif ((cur[row, col] == 1 and  2 <= num_alive <= 3) or (cur[row, col] == 0 and num_alive == 3)):
            frame[row, col] = 1
            c = col_alive
        
        c = c if cur[row, col] == 1 else col_bg
        pygame.draw.rect(window, c, (col*CS, row*CS, CS-1, CS-1))
        
    return frame

def init(width, height):
    cells = np.zeros((width, height))
    # pattern = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        # [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        # [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                        # [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                        # [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        # [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        # [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        # [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        # [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]);
    pattern = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]);
    pos = (3, 3)
    cells[pos[0]:pos[0]+pattern.shape[0], pos[1]:pos[1]+pattern.shape[1]] = pattern
    return cells

def main():
    parse = argparse.ArgumentParser(description="Implementation of Conway's Game of Life")

    pygame.init()
    window = pygame.display.set_mode(((W*K), (H*K)))
    pygame.display.set_caption("Conway's Game of Life")

    cells = init(W*K, H*K)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            window.fill(col_grid)
            cells = update_frame(window, cells)
            pygame.display.flip()
            time.sleep(0.001)

if (__name__ == "__main__"):
    main()