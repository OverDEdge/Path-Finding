import pygame as pg

# Set vector
vec = pg.math.Vector2

WIDTH = 1200
HEIGHT = 720
TITLE_AREA = 50
WINDOW_X_POS = 50
WINDOW_Y_POS = 50
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
MEDIUM_TEXT_SIZE = 25
SMALL_TEXT_SIZE = 15
NO_PATH_FOUND = "No valid path found!"
PATH_FOUND = "Path found! See colored path!"
GOSCREEN_PRESS_ANY = "Press any KEY to clear screen and restart"
ALGORITM_NAME = {'dijkstras': "Dijkstra's Algorithm", 'astar': "A* Algorithm"}
STARTSCREEN_MOUSE_INSTRUCTION_1 = "Use Left Mouse-click to place out Start, End and Walls"
STARTSCREEN_MOUSE_INSTRUCTION_2 = "First click places Start, second places End, and following places Walls"
STARTSCREEN_MOUSE_INSTRUCTION_3 = "To clear a node use Right Mouse-click on node position"
STARTSCREEN_START_ALGORITHM = "Press 'Space' to start the chose path-finding algorithm"
STARTSCREEN_START_CHOOSE_ALGORITHM_1 = "Press 'A' for A* Algorithm"
STARTSCREEN_START_CHOOSE_ALGORITHM_2 = "Press 'D' for Dijkstra's Algorithm"
STARTSCREEN_PRESS_ANY = "Press any KEY to continue to path-finding game"
