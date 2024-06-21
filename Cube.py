from functions import *
class Cube:
    def __init__(self):
        self.combx = False
        self.value = 0
        self.color = config.gray
        self.visable = False
        self.flag = False
        self.tv = self.value

    # giving the adjacent tiles of a bomb their number
    def im_a_bomb(self, boardY, boardX, grid):
        # self.color = red
        self.value = 0
        loop_adjacent_add_value(boardY, boardX, grid)

    def color_myself(self):
        if self.combx is False:
            self.color = config.white
        elif self.combx is True:
            self.color = config.red
        if self.flag is True:
            self.color = config.blue
