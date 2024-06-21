from functions import *
def msai(row, col, grid):
    for y in range(row):
        for x in range(col):
            if grid[y][x].visable is True and grid[y][x].value !=0:
                corner(y, x, grid)
    for y in range(row):
        for x in range(col):
            if grid[y][x].visable is True and grid[y][x].value !=0:
                find_true_value(y, x, grid)
                open_corner(y, x, grid)

def msai2(row, col, grid):
    effective = False
    for y in range(row):
        for x in range(col):
            if grid[y][x].visable is True and grid[y][x].value !=0:
                #seacch_1_1_pattern(y, x)
                if seacch_1_1_pattern(y, x, grid) is True:
                    return


#corners: if the no. of adjacent hidden tiles = the true value of the tile. the adjacent hidden tile must be flaged!
def corner(y_tile, x_tile, grid):
    adjacent = make_adjacent(y_tile, x_tile)
    gray_tile = 0
    for t in range(8):
        if inbound(adjacent[t][0], adjacent[t][1]) and grid[adjacent[t][0]][adjacent[t][1]].visable is False:
            gray_tile +=1
    if gray_tile == grid[y_tile][x_tile].value:
        for t in range(8):
            if inbound(adjacent[t][0], adjacent[t][1]) and grid[adjacent[t][0]][adjacent[t][1]].visable is False:
                flag_em(adjacent[t][0], adjacent[t][1], grid)

#indint the TRUE VALUE: it subtract the number of adjacent flagged tile from the value
def find_true_value(y_tile, x_tile, grid):
    adjacent = make_adjacent(y_tile, x_tile)
    true_value = grid[y_tile][x_tile].value
    for t in range(8):
        if inbound(adjacent[t][0], adjacent[t][1]) and grid[adjacent[t][0]][adjacent[t][1]].flag is True:
            true_value -=1
    grid[y_tile][x_tile].tv = true_value
    open_corner(y_tile, x_tile, grid)


#if the true num is 0, it opens all the adjacent non flagged tiles
def open_corner(y_tile, x_tile, grid):
    if grid[y_tile][x_tile].tv == 0:
        adjacent = make_adjacent(y_tile, x_tile)
        for t in range(8):
            if inbound(adjacent[t][0], adjacent[t][1]) and grid[adjacent[t][0]][adjacent[t][1]].flag is False:
                open_a_tile(adjacent[t][0], adjacent[t][1], grid)

def seacch_1_1_pattern(y_tile, x_tile, grid):
    adj = make_adjacent(y_tile, x_tile)
    a_list = []
    b_list = []
    c_list = []

    for i in range(8):
        if (inbound(adj[i][0], adj[i][1]) and grid[adj[i][0]][adj[i][1]].flag is False and
                grid[adj[i][0]][adj[i][1]].visable is False):
            a_list.append([adj[i][0], adj[i][1]])
    for t in [1, 3, 4, 6]:
        if inbound(adj[t][0], adj[t][1]) and grid[adj[t][0]][adj[t][1]].tv == 1:
            make_gray_list(adj[t][0], adj[t][1], b_list, grid)
            #print('b', b_list)
            if 0 < len(a_list) < 3:
                for r in b_list:
                    if r not in a_list:
                        c_list.append(r)
                for l in a_list:
                    if l not in b_list:
                        return
                for t in range(len(c_list)):
                    open_a_tile(c_list[t][0], c_list[t][1], grid)
                    b_list.clear()
                    c_list.clear()
                    return True


def make_gray_list(y_tile, x_tile, b_list, grid):
    adj = make_adjacent(y_tile, x_tile)
    b_list.clear()
    for t in range(8):
        if (inbound(adj[t][0], adj[t][1]) and grid[adj[t][0]][adj[t][1]].flag is False and
                grid[adj[t][0]][adj[t][1]].visable is False):
            b_list.append([adj[t][0], adj[t][1]])
    return b_list
