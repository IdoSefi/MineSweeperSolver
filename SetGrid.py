from Cube import Cube
import random
def set_grid(col, row, bomb_num):
    # this creates a grid filled with cube objects
    grid = [[Cube() for n in range(col)] for r in range(row)]
    # this creates bombs
    for n in range(bomb_num):
        while True:
            y = random.randint(0, row-1)
            x = random.randint(0, col-1)
            if (not grid[y][x].combx) and x != (row//2) and y != (col//2):
                grid[y][x].combx = True
                grid[y][x].im_a_bomb(y, x, grid)
                break
    grid[col//2][row//2].color = (0, 255, 0)
    return grid