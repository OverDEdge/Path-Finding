import pygame as pg

# Set vector
vec = pg.math.Vector2

WIDTH = 1200
HEIGHT = 720
FPS = 60
NODE_SIZE = 20

ROWS = HEIGHT // NODE_SIZE
COLS = WIDTH // NODE_SIZE

# Some defined colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
DARKGREY = (40, 40, 40)
GREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (106, 55, 5)
ORANGE = (255, 165, 0)
TURQUOISE = (64, 224, 208)
PURPLE = (128, 0, 128)

BGCOLOR = BLACK

TITLE = 'Path-Finding Visualization'
NODE_WEIGHT = 1

# Text Prompts
FONT_NAME = 'arial'
LARGE_TEXT_SIZE = 40
NO_PATH_FOUND = "No valid path found. Press any KEY to clear screen and restart"
PATH_FOUND = "Path found. Press any KEY to clear screen and restart"
