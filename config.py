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
width = 35
row = 22
col = 22
bomb_num = 80
msai_loop = 0
# initialization of systems
pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((width*row, width*col))
font1 = pygame.font.SysFont(None, 25)