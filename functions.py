
import config

def make_adjacent(y_tile, x_tile):
    adjacent = ([y_tile - 1, x_tile - 1], [y_tile - 1, x_tile], [y_tile - 1, x_tile + 1], [y_tile, x_tile - 1],
                [y_tile, x_tile + 1], [y_tile + 1, x_tile - 1], [y_tile + 1, x_tile], [y_tile + 1, x_tile + 1])
    return adjacent


# looping through adjacent
def loop_adjacent(y_tile, x_tile):
    adjacent = make_adjacent(y_tile, x_tile)
    for t in range(8):
        if inbound(adjacent[t][0], adjacent[t][1]):
            print(adjacent[t])
    print("----------------------------------")


# looping through adjacent and making them visible (spreading of 1 click)
def loop_adjacent_visable(y_tile, x_tile, grid):
    adjacent = make_adjacent(y_tile, x_tile)
    for t in range(8):
        if inbound(adjacent[t][0], adjacent[t][1]) and grid[adjacent[t][0]][adjacent[t][1]].combx is False and \
                grid[adjacent[t][0]][adjacent[t][1]].visable is False:
            grid[adjacent[t][0]][adjacent[t][1]].visable = True
            if grid[adjacent[t][0]][adjacent[t][1]].value == 0:
                loop_adjacent_visable(adjacent[t][0], adjacent[t][1], grid)


# looping through adjacent of a bomb and adding a value to each tile
def loop_adjacent_add_value(y_tile, x_tile, grid):
    adjacent = make_adjacent(y_tile, x_tile)
    for t in range(8):
        if inbound(adjacent[t][0], adjacent[t][1]) and grid[adjacent[t][0]][adjacent[t][1]].combx is False:
            grid[adjacent[t][0]][adjacent[t][1]].value += 1





# checking inbound

def inbound(y, x):
    if 0 <= x < config.row and 0 <= y < config.col:
        return True
    else:
        return False


# this draws the grid to the screen
def draw_grid(grid, row, col, screen, width):
    for y in range(row):
        for x in range(col):
            if grid[y][x].visable is True:
                grid[y][x].color_myself()
                grid[y][x].flag = False
            config.pygame.draw.rect(screen, grid[y][x].color, [x * width, y * width, width - 3, width - 3])
            if grid[y][x].value != 0 and grid[y][x].visable is True:
                value_to_screen = config.font1.render(str(grid[y][x].value), True, config.black)
                screen.blit(value_to_screen, [x * width + width // 3, y * width + width // 4])


# finding the clicked tile
def clicked_tile_left(mx, my, width, grid):
    x_tile = mx // width
    y_tile = my // width
    if grid[y_tile][x_tile].flag is False:
        open_a_tile(y_tile, x_tile, grid)


def clicked_tile_right(mx, my,width, grid):
    x_tile = mx // width
    y_tile = my // width
    flag_em_human(y_tile, x_tile, grid)
    #if grid[y_tile][x_tile].tv == 1:
        #seacch_1_1_pattern(y_tile, x_tile)
        #flag_em(y_tile, x_tile, grid)


def open_a_tile(boardY, boardX, grid):
    grid[boardY][boardX].visable = True
    if grid[boardY][boardX].value == 0 and grid[boardY][boardX].combx is False:
        loop_adjacent_visable(boardY, boardX, grid)
    elif grid[boardY][boardX].combx is True:
        you_loose(grid)

# flagging a tile
def flag_em_human(y_tile, x_tile, grid):
    if grid[y_tile][x_tile].flag == False:
        grid[y_tile][x_tile].flag = True
        grid[y_tile][x_tile].color_myself()
    else:
        grid[y_tile][x_tile].flag = False
        grid[y_tile][x_tile].color = config.gray

def flag_em(y_tile, x_tile, grid):
    grid[y_tile][x_tile].flag = True
    grid[y_tile][x_tile].color_myself()

def you_loose(grid):
    draw_grid(grid, config.row, config.col, config.screen, config.width)
    print('------------------------------------------------------')
    #time.sleep(15)
    for y in range(config.row):
        for x in range(config.col):
            if grid[y][x].combx is True:
                grid[y][x].visable = True