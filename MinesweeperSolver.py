import pygame
from pygame.locals import *
import random
import time
from pynput.mouse import Listener

# variables
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
black = (0, 0, 0)
gray = (100, 100, 100)
width = 40
row = 22
col = 22
bomb_num = 100
msai_loop = 0
# initialization of systems
pygame.init()
clock = pygame.time.Clock()
run_game = True
screen = pygame.display.set_mode((880, 880))
font1 = pygame.font.SysFont(None, 25)


# the tile class
class Cube:
    def __init__(self):
        self.combx = False
        self.value = 0
        self.color = gray
        self.visable = False
        self.flag = False
        self.tv = self.value

    # giving the adjacent tiles of a bomb their number
    def im_a_bomb(self, boardY, boardX):
        # self.color = red
        self.value = 0
        loop_adjacent_add_value(boardY, boardX)

    def color_myself(self):
        if self.combx is False:
            self.color = white
        elif self.combx is True:
            self.color = red
        if self.flag is True:
            self.color = blue


# looping through adjacent
def loop_adjacent(y_tile, x_tile):
    adjacent = [y_tile - 1, x_tile - 1], [y_tile - 1, x_tile], [y_tile - 1, x_tile + 1], [y_tile, x_tile - 1], [y_tile,
                                                                                                                x_tile + 1], [
                   y_tile + 1, x_tile - 1], [y_tile + 1, x_tile], [y_tile + 1, x_tile + 1]
    for t in range(8):
        if inbound(adjacent[t][0], adjacent[t][1]):
            print(adjacent[t])
    print("----------------------------------")


# looping through adjacent and making them visible (spreading of 1 click)
def loop_adjacent_visable(y_tile, x_tile):
    adjacent = [y_tile - 1, x_tile - 1], [y_tile - 1, x_tile], [y_tile - 1, x_tile + 1], [y_tile, x_tile - 1], [y_tile,
                                                                                                                x_tile + 1], [
                   y_tile + 1, x_tile - 1], [y_tile + 1, x_tile], [y_tile + 1, x_tile + 1]
    for t in range(8):
        if inbound(adjacent[t][0], adjacent[t][1]) and grid[adjacent[t][0]][adjacent[t][1]].combx is False and \
                grid[adjacent[t][0]][adjacent[t][1]].visable is False:
            grid[adjacent[t][0]][adjacent[t][1]].visable = True
            if grid[adjacent[t][0]][adjacent[t][1]].value == 0:
                loop_adjacent_visable(adjacent[t][0], adjacent[t][1])


# looping through adjacent of a bomb and adding a value to each tile
def loop_adjacent_add_value(y_tile, x_tile):
    adjacent = [y_tile - 1, x_tile - 1], [y_tile - 1, x_tile], [y_tile - 1, x_tile + 1], [y_tile, x_tile - 1], [y_tile,
                                                                                                                x_tile + 1], [
                   y_tile + 1, x_tile - 1], [y_tile + 1, x_tile], [y_tile + 1, x_tile + 1]
    for t in range(8):
        if inbound(adjacent[t][0], adjacent[t][1]) and grid[adjacent[t][0]][adjacent[t][1]].combx is False:
            grid[adjacent[t][0]][adjacent[t][1]].value += 1


# this creates a grid filled with cube objects
grid = [[Cube() for n in range(col)] for r in range(row)]


# checking inbound

def inbound(y, x):
    if 0 <= x < row and 0 <= y < col:
        return True
    else:
        return False


# this creates bombs
for n in range(bomb_num):
    while True:
        y = random.randint(0, row-1)
        x = random.randint(0, col-1)
        if not grid[y][x].combx:
            grid[y][x].combx = True
            grid[y][x].im_a_bomb(y, x)
            break


# this draws the grid to the screen
def draw_grid(grid):
    for y in range(row):
        for x in range(col):
            if grid[y][x].visable is True:
                grid[y][x].color_myself()
                grid[y][x].flag = False
            pygame.draw.rect(screen, grid[y][x].color, [x * width, y * width, width - 3, width - 3])
            if grid[y][x].value != 0 and grid[y][x].visable is True:
                value_to_screen = font1.render(str(grid[y][x].value), True, black)
                screen.blit(value_to_screen, [x * width + width // 3, y * width + width // 4])


# finding the clicked tile
def clicked_tile_left(mx, my):
    x_tile = mx // width
    y_tile = my // width
    if grid[y_tile][x_tile].flag is False:
        open_a_tile(y_tile, x_tile)



def clicked_tile_right(mx, my):
    x_tile = mx // width
    y_tile = my // width
    #corner(y_tile, x_tile)
    if grid[y_tile][x_tile].tv == 1:
        seacch_1_1_pattern(y_tile, x_tile)
    '''
    find_true_value(y_tile, x_tile)
    if grid[y_tile][x_tile].visable is False and grid[y_tile][x_tile].flag is False:
        flag_em(y_tile, x_tile)
    elif grid[y_tile][x_tile].flag is True:
        grid[y_tile][x_tile].flag = False
        grid[y_tile][x_tile].color = gray
'''

# opening a tile AND spreading visibility
def open_a_tile(boardY, boardX):
    grid[boardY][boardX].visable = True
    if grid[boardY][boardX].value == 0 and grid[boardY][boardX].combx is False:
        loop_adjacent_visable(boardY, boardX)
    elif grid[boardY][boardX].combx is True:
        you_loose()

# flagging a tile
def flag_em(y_tile, x_tile):
    grid[y_tile][x_tile].flag = True
    grid[y_tile][x_tile].color_myself()


def you_loose():
    draw_grid(grid)
    print('------------------------------------------------------')
    #time.sleep(15)
    for y in range(row):
        for x in range(col):
            if grid[y][x].combx is True:
                grid[y][x].visable = True

# the AI AI AI AI AI AI AI AI AI AI AI---------------------------------AI AI AI AI-----------------------------------
def msai():
    for y in range(row):
        for x in range(col):
            if grid[y][x].visable is True and grid[y][x].value !=0:
                corner(y, x)
    for y in range(row):
        for x in range(col):
            if grid[y][x].visable is True and grid[y][x].value !=0:
                find_true_value(y, x)
                open_corner(y, x)

def msai2():
    effective = False
    for y in range(row):
        for x in range(col):
            if grid[y][x].visable is True and grid[y][x].value !=0:
                #seacch_1_1_pattern(y, x)
                if seacch_1_1_pattern(y, x) is True:
                    print("its true baby")
                    return


#corners: if the no. of adjacent hidden tiles = the true value of the tile. the adjacent hidden tile must be flaged!
def corner(y_tile, x_tile):
    adjacent = [y_tile - 1, x_tile - 1], [y_tile - 1, x_tile], [y_tile - 1, x_tile + 1], [y_tile, x_tile - 1], [y_tile,
                                                                                                                x_tile + 1], [
                   y_tile + 1, x_tile - 1], [y_tile + 1, x_tile], [y_tile + 1, x_tile + 1]
    gray_tile = 0
    for t in range(8):
        if inbound(adjacent[t][0], adjacent[t][1]) and grid[adjacent[t][0]][adjacent[t][1]].visable is False:
            gray_tile +=1
    if gray_tile == grid[y_tile][x_tile].value:
        for t in range(8):
            if inbound(adjacent[t][0], adjacent[t][1]) and grid[adjacent[t][0]][adjacent[t][1]].visable is False:
                flag_em(adjacent[t][0], adjacent[t][1])

#indint the TRUE VALUE: it subtract the number of adjacent flagged tile from the value
def find_true_value(y_tile, x_tile):
    adjacent = [y_tile - 1, x_tile - 1], [y_tile - 1, x_tile], [y_tile - 1, x_tile + 1], [y_tile, x_tile - 1], [y_tile,
                                                                                                                x_tile + 1], [
                   y_tile + 1, x_tile - 1], [y_tile + 1, x_tile], [y_tile + 1, x_tile + 1]
    true_value = grid[y_tile][x_tile].value
    for t in range(8):
        if inbound(adjacent[t][0], adjacent[t][1]) and grid[adjacent[t][0]][adjacent[t][1]].flag is True:
            true_value -=1
    grid[y_tile][x_tile].tv = true_value
    open_corner(y_tile, x_tile)


#if the true num is 0, it opens all the adjacent non flagged tiles
def open_corner(y_tile, x_tile):
    if grid[y_tile][x_tile].tv == 0:
        adjacent = [y_tile - 1, x_tile - 1], [y_tile - 1, x_tile], [y_tile - 1, x_tile + 1], [y_tile, x_tile - 1], [y_tile,
                                                                                                                    x_tile + 1], [
                       y_tile + 1, x_tile - 1], [y_tile + 1, x_tile], [y_tile + 1, x_tile + 1]
        for t in range(8):
            if inbound(adjacent[t][0], adjacent[t][1]) and grid[adjacent[t][0]][adjacent[t][1]].flag is False:
                open_a_tile(adjacent[t][0], adjacent[t][1])

def seacch_1_1_pattern(y_tile, x_tile):
    adj = [y_tile - 1, x_tile - 1], [y_tile - 1, x_tile], [y_tile - 1, x_tile + 1], [y_tile, x_tile - 1], [y_tile,
                                                                                                                x_tile + 1], [
                   y_tile + 1, x_tile - 1], [y_tile + 1, x_tile], [y_tile + 1, x_tile + 1]
    a_list = []
    b_list = []
    c_list = []

    for i in range(8):
        if inbound(adj[i][0], adj[i][1]) and grid[adj[i][0]][adj[i][1]].flag is False and grid[adj[i][0]][adj[i][1]].visable is False:
            a_list.append([adj[i][0], adj[i][1]])
    for t in [1, 3, 4, 6]:
        if inbound(adj[t][0], adj[t][1]) and grid[adj[t][0]][adj[t][1]].tv == 1:
            make_gray_list(adj[t][0], adj[t][1], b_list)
            #print('b', b_list)
            if 0 < len(a_list) < 3:
                for r in b_list:
                    if r not in a_list:
                        c_list.append(r)
                print('I am', y_tile, x_tile)
                print('a', a_list)
                print('b', b_list)
                print('c', c_list)
                for l in a_list:
                    if l not in b_list:
                        print('return')
                        return
                for t in range(len(c_list)):
                    print('open', c_list[t])
                    open_a_tile(c_list[t][0], c_list[t][1])
                    b_list.clear()
                    c_list.clear()
                    return True


def make_gray_list(y_tile, x_tile, b_list):
    adj = [y_tile - 1, x_tile - 1], [y_tile - 1, x_tile], [y_tile - 1, x_tile + 1], [y_tile, x_tile - 1], [y_tile,
                                                                                                           x_tile + 1], [
              y_tile + 1, x_tile - 1], [y_tile + 1, x_tile], [y_tile + 1, x_tile + 1]
    b_list.clear()
    for t in range(8):
        if inbound(adj[t][0], adj[t][1]) and grid[adj[t][0]][adj[t][1]].flag is False and grid[adj[t][0]][adj[t][1]].visable is False:
            b_list.append([adj[t][0], adj[t][1]])
    return b_list


# the main game loop--------------MAIN  MAIN  MAIN   MAIN -----------------------------------------------------
while run_game:

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx, my = pygame.mouse.get_pos()
            clicked_tile_left(mx, my)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            mx, my = pygame.mouse.get_pos()
            clicked_tile_right(mx, my)

        # ai
        if msai_loop <= 5:
            msai()
        elif msai_loop > 5:
            print('yo')
            msai2()
            msai_loop = 0
        msai_loop += 1

    # drawing
    draw_grid(grid)
    pygame.display.update()
    clock.tick(25)
pygame.quit()
quit()

# all that is left is adding  flagging. and than AI
