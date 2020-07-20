import pygame as pg
from . import settings
from .settings import vec

class Node(pg.sprite.Sprite):
    '''
    Node class which is a grid square
    '''
    def __init__(self, row, col, game):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.row = row
        self.col = col
        self.color = settings.WHITE
        self.neighbours = set()
        self.width = settings.NODE_SIZE
        self.height = settings.NODE_SIZE
        self.pos = vec(self.col * settings.NODE_SIZE, self.row * settings.NODE_SIZE)
        self.draw()

    def get_pos(self):
        return self.row, self.col

    def is_visited(self):
        return self.color == settings.RED

    def is_open(self):
        return self.color == settings.ORANGE

    def is_wall(self):
        return self.color == settings.BLACK

    def is_start(self):
        return self.color == settings.GREEN

    def is_end(self):
        return self.color == settings.PURPLE

    def reset(self):
        self.color = settings.WHITE
        self.draw()

    def make_visited(self):
        self.color = settings.RED
        self.draw()

    def make_open(self):
        self.color = settings.ORANGE
        self.draw()

    def make_wall(self):
        self.color = settings.BLACK
        self.draw()

    def make_start(self):
        self.color = settings.GREEN
        self.draw()

    def make_end(self):
        self.color = settings.PURPLE
        self.draw()

    def make_path(self):
        self.color = settings.YELLOW
        self.draw()

    def draw(self):
        self.image = pg.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def set_neighbours(self):
        # CLear current set of neighbours
        self.neighbours = set()
        directions = {(1, 0), (-1, 0), (0, 1), (0, -1)}

        # Loop over all possible neighbours and check if valid neighbour
        for dir in directions:
            neighbour_row = self.row + dir[0]
            neighbour_col = self.col + dir[1]

            if self.is_inside(neighbour_row, neighbour_col):
                node = self.game.grid[neighbour_row][neighbour_col]
                if not node.is_wall():
                    self.neighbours.add(node)

    def is_inside(self, row, col):
        return 0 <= row < settings.ROWS and 0 <= col < settings.COLS

    def __lt__(self, other):
        return False
