import pygame as pg
import math
import sys
import os

from .node import Node
from . import astar
from . import dijkstras
from . import settings

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (settings.WINDOW_X_POS, settings.WINDOW_Y_POS)

class Game:
    def __init__(self):
        '''
        Method to initialize pygame, game window, sound, font and clock
        '''
        # Intialize game window, etc...
        self.running_program = True
        self.algo = dijkstras
        self.algo_name = 'dijkstras'
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((settings.WIDTH, settings.HEIGHT))
        pg.display.set_caption(settings.TITLE)
        self.clock = pg.time.Clock()
        self.font_name = pg.font.match_font(settings.FONT_NAME)

    def new(self):
        '''
        Method to reset a new game / run of algorithm
        '''
        self.all_sprites = pg.sprite.Group()
        self.grid = []
        self.start = None
        self.end = None
        self.algo_results = False, None
        # Initialize the nodes
        for row in range(settings.ROWS):
            self.grid.append([])
            for col in range(settings.COLS):
                node = Node(row, col, settings.NODE_WEIGHT, self)
                self.grid[row].append(node)
        self.run()

    def update(self):
        '''
        Updates all sprites
        '''
        self.all_sprites.update()

    def run(self):
        '''
        Main game loop where everything is run
        '''
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(settings.FPS) / 1000.0
            self.events()
            self.update()
            self.draw()

    def events(self):
        '''
        Event loop where checking for user input.
        '''
        for event in pg.event.get():
            # Check if user want to quit ('x' in top right or 'ESC' is pressed)
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

                # Set A* algorithm
                if event.key == pg.K_a:
                    self.algo = astar
                    self.algo_name = 'astar'

                # Set Dijkstra algorithm
                if event.key == pg.K_d:
                    self.algo = dijkstras
                    self.algo_name = 'dijkstras'

                # Check if algorithm shall start
                if event.key == pg.K_SPACE and self.start and self.end:
                    # Set neighbours according to current grid status
                    for row in range(settings.ROWS):
                        for col in range(settings.COLS):
                            node = self.grid[row][col]
                            node.set_neighbours()
                    # Run path-finding algorithm and get results
                    self.algo_results = self.algo.run(lambda: self.draw(), self, self.start, self.end)

                    # Exit game loop
                    self.playing = False

            # Get user mouse input
            if pg.mouse.get_pressed()[0]: # Check for left button click
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
        '''
        Method that returns the node at which the user clicked
        RETURN: Node
        '''
        pos = pg.mouse.get_pos()
        row, col = self.get_clicked_pos(pos)
        return self.grid[row][col]

    def get_clicked_pos(self, pos):
        '''
        Method that returns the row and column at which the user clicked
        RETURN: int, int
        '''
        row = pos[1] // settings.NODE_SIZE
        col = pos[0] // settings.NODE_SIZE
        return row, col

    def reconstruct_path(self, previous_node):
        '''
        Method to reconstruct and display the path found from start to finish
        '''
        current = self.end

        # Loop over the path starting from the end
        while current in previous_node:
            current = previous_node[current]
            current.make_path()

        # Set start and end nodes as intended
        self.start.make_start()
        self.end.make_end()
        self.draw()

    def draw(self):
        '''
        Method to draw all sprites to screen
        '''
        #pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.screen.fill(settings.BGCOLOR)
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, sprite.pos)
        self.draw_grid()
        self.draw_text(settings.ALGORITM_NAME[self.algo_name], settings.MEDIUM_TEXT_SIZE, settings.BLUE, settings.WIDTH - 100, 10)
        pg.display.flip()

    def draw_grid(self):
        '''
        Draws the grid for visualization purpose
        '''

        # Vertical lines
        for x in range(settings.COLS):
            pg.draw.line(self.screen, settings.GREY, (x * settings.NODE_SIZE, 0), (x  * settings.NODE_SIZE, settings.HEIGHT))

        # Horizontal lines
        for y in range(settings.ROWS):
            pg.draw.line(self.screen, settings.GREY, (0, y  * settings.NODE_SIZE), (settings.WIDTH, y  * settings.NODE_SIZE))

    def draw_text(self, text, size, color, x, y):
        '''
        Method for displaying text on the game screen
        '''
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def launch_go_screen(self):
        '''
        Method that runs at the end of the game / algorithm
        '''
        if self.algo_results[0]: # If path was found
            self.reconstruct_path(self.algo_results[1])
            self.draw_text(settings.PATH_FOUND, settings.LARGE_TEXT_SIZE, settings.BLUE, settings.WIDTH / 2, settings.HEIGHT / 2)
        else: # If path was not found
            self.draw_text(settings.NO_PATH_FOUND, settings.LARGE_TEXT_SIZE, settings.BLUE, settings.WIDTH / 2, settings.HEIGHT / 2)

        self.draw_text(settings.GOSCREEN_PRESS_ANY, settings.LARGE_TEXT_SIZE, settings.RED, settings.WIDTH / 2, settings.HEIGHT * 3 / 4)

        pg.display.flip()
        self.wait_for_key()

    # Waiting for any key input
    def wait_for_key(self):
        '''
        Method that waits for any key input from user before exiting.
        User can still quit using 'x' at top left or pressing 'ESC'
        '''

        waiting = True
        key_down = False

        while waiting: # Waiting for suer input
            self.clock.tick(settings.FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.quit()
                if event.type == pg.KEYDOWN:
                    key_down = True
                if event.type == pg.KEYUP and key_down:
                    waiting = False

    def launch_start_screen(self):
        '''
        Method that runs at the start to display information
        '''

        self.screen.fill(settings.BGCOLOR)
        self.draw_grid()

        self.draw_text(settings.STARTSCREEN_MOUSE_INSTRUCTION_1, settings.LARGE_TEXT_SIZE, settings.WHITE, settings.WIDTH / 2, settings.HEIGHT * 4 / 48)
        self.draw_text(settings.STARTSCREEN_MOUSE_INSTRUCTION_2, settings.LARGE_TEXT_SIZE, settings.WHITE, settings.WIDTH / 2, settings.HEIGHT * 8 / 48)
        self.draw_text(settings.STARTSCREEN_MOUSE_INSTRUCTION_3, settings.LARGE_TEXT_SIZE, settings.WHITE, settings.WIDTH / 2, settings.HEIGHT * 12 / 48)

        self.draw_text(settings.STARTSCREEN_START_ALGORITHM, settings.LARGE_TEXT_SIZE, settings.GREEN, settings.WIDTH / 2, settings.HEIGHT * 20 / 48)
        self.draw_text(settings.STARTSCREEN_START_CHOOSE_ALGORITHM_1, settings.LARGE_TEXT_SIZE, settings.GREEN, settings.WIDTH / 2, settings.HEIGHT * 24 / 48)
        self.draw_text(settings.STARTSCREEN_START_CHOOSE_ALGORITHM_2, settings.LARGE_TEXT_SIZE, settings.GREEN, settings.WIDTH / 2, settings.HEIGHT * 28 / 48)

        self.draw_text(settings.STARTSCREEN_PRESS_ANY, settings.LARGE_TEXT_SIZE, settings.RED, settings.WIDTH / 2, settings.HEIGHT * 36 / 48)

        pg.display.flip()
        self.wait_for_key()

    def quit(self):
        '''
        Method that quits pygame and exits the program.
        '''
        pg.quit()
        sys.exit()

g = Game()
g.launch_start_screen()

while g.running_program:
    g.new()
    g.launch_go_screen()

pg.quit()
sys.exit()
