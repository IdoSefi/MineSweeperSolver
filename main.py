from config import *
#from Cube import Cube
from functions import *
from SetGrid import set_grid
from Solver import *
from tkinter import *
from tkinter import messagebox

grid = set_grid(col, row, bomb_num)
Tk().wm_withdraw() #to hide the main window
messagebox.showinfo('Mine Sweeper Solver','welcome to Mine Sweeper Solver,\n'
                                          'to play press the left mouse on an empty block, if you press on a bomb'
                                          ' you will loose, and will have to retry')
messagebox.showinfo('Mine Sweeper Solver','press the green tile')
run_game = True
while run_game:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx, my = pygame.mouse.get_pos()
            clicked_tile_left(mx, my, width, grid)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            mx, my = pygame.mouse.get_pos()
            clicked_tile_right(mx, my, width, grid)

    # the solver
    if msai_loop <= 5:
        msai(row, col, grid)
    elif msai_loop > 5:
        msai2(row, col, grid)
        msai_loop = 0
    msai_loop += 1

    # drawing
    draw_grid(grid, row, col, screen, width)
    pygame.display.update()
    clock.tick(80)
pygame.quit()
quit()