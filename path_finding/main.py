import pygame as pg
import math
import sys
from queue import PriorityQueue
from .node import Node
from . import astar
from . import settings

class Game:
    def __init__(self):
        # Intialize game window, etc...
        self.running_program = True
        self.start = None
        self.end = None
        self.algo_started = False
        self.algo = astar
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((settings.WIDTH, settings.HEIGHT))
        pg.display.set_caption(settings.TITLE)
        self.clock = pg.time.Clock()

    def new(self):
        # Setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.grid = []
        for row in range(settings.ROWS):
            self.grid.append([])
            for col in range(settings.COLS):
                node = Node(row, col, self)
                self.grid[row].append(node)
        self.run()

    def draw_grid(self):
        for x in range(settings.COLS):
            pg.draw.line(self.screen, settings.GREY, (x * settings.NODE_SIZE, 0), (x  * settings.NODE_SIZE, settings.HEIGHT))

        for y in range(settings.ROWS):
            pg.draw.line(self.screen, settings.GREY, (0, y  * settings.NODE_SIZE), (settings.WIDTH, y  * settings.NODE_SIZE))

    def update(self):
        # Game Loop - update
        self.all_sprites.update()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(settings.FPS) / 1000.0
            self.events()
            self.update()
            self.draw()

    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_SPACE and not self.algo_started:
                    for row in range(settings.ROWS):
                        for col in range(settings.COLS):
                            node = self.grid[row][col]
                            node.set_neighbours()
                    self.algo.run()

            # If search has started make it impossible to change grid
            if self.algo_started:
                continue

            if pg.mouse.get_pressed()[0]: # CHeck for left button click
                node = self.get_clicked_node()
                if self.start is None and node != self.end:
                    self.start = node
                    node.make_start()
                elif self.end is None and node != self.start:
                    self.end = node
                    node.make_end()
                elif node != self.start and node != self.end:
                    node.make_wall()

            elif pg.mouse.get_pressed()[2]: # Check for right button click
                node = self.get_clicked_node()
                node.reset()
                if node == self.start:
                    self.start = None
                elif node == self.end:
                    self.end = None


    def get_clicked_node(self):
        pos = pg.mouse.get_pos()
        row, col = self.get_clicked_pos(pos)
        return self.grid[row][col]

    def get_clicked_pos(self, pos):
        row = pos[1] // settings.NODE_SIZE
        col = pos[0] // settings.NODE_SIZE
        return row, col

    def draw(self):
        # Game Loop - draw
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.screen.fill(settings.BGCOLOR)
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, sprite.pos)
        self.draw_grid()
        pg.display.flip()

    def launch_go_screen(self):
        # Game Over screen
        pass

    def launch_start_screen(self):
        # Start screen
        pass

    def quit(self):
        pg.quit()
        sys.exit()

g = Game()
g.launch_start_screen()

while g.running_program:
    g.new()
    g.launch_go_screen()

pg.quit()
sys.exit()
