import pygame as pg
from queue import PriorityQueue

def run(draw, game, start, end):
    '''
    Method for running the A* algorithm.
    The "cost" for each node is calculated based on:
    F = G + H

    G: Minimum distance from start to current node
    H: Manhattan distance from current node to end
    F: Sum of G and H to get a "guess" of total distance.

    F-value is used to choose which node to consider next. The node with the
    lowest "guess" is chosen from a PriorityQueue

    RETURNS: bool, dictionary
    '''
    count_ = 0
    open_set = PriorityQueue()

    # Add start node to queue
    open_set.put((0, count_, start)) # Count is used to separate nodes with same cost value

    # Keep track of where we came from
    previous_node = {}

    # Initialize cost functions g and f
    g_score = {node: float("inf") for row in game.grid for node in row}
    g_score[start] = 0
    f_score = {node: float("inf") for row in game.grid for node in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    # Need this since can't check in PriorityQueue if an item exists in it but easy with a hash set
    open_hash_set = {start}

    # Run the Astar algorithm until the set is empty (no more nodes to visit) or end is found
    while not open_set.empty():

        # Need to have quit condition during this loop, in case suer wants to quit.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

        # Get the node with lowest cost from open_set
        current = open_set.get()[2]
        open_hash_set.remove(current)

        # Check if it is end node
        if current == end:
            # Return True for path found and the dictionary to reconstruct path
            return True, previous_node

        # Loop over neghbours
        for neighbour in current.neighbours:
            # Calculate G value for neighbour
            temp_g_score = g_score[current] + neighbour.weight
            # Check if calculated score for position is less than already found
            if temp_g_score < g_score[neighbour]:
                # Calculate H and F for the neighbour
                g_score[neighbour] = temp_g_score
                f_score[neighbour] = temp_g_score + h(neighbour.get_pos(), end.get_pos())
                previous_node[neighbour] = current

                if neighbour not in open_hash_set:
                    # Increase count variable to break ties.
                    count_ += 1

                    # Add neighbour to PrioriyQueue and hash set
                    open_set.put((f_score[neighbour], count_, neighbour))
                    open_hash_set.add(neighbour)

                    # Set neighbour as being in open set (waiting to be considered)
                    neighbour.make_open()

        # Call draw function for game to update grid with current status of the nodes
        game.draw()

        # Set current node to visited since all neighbours have been calculated
        if current != start:
            current.make_visited()

    # Return False if no path was found
    return False, {}


def h(pos1, pos2):
    '''
    Method to calculate Manhattan distance between two positions
    RETURNS: int
    '''
    return abs(pos1.x - pos2.x) + abs(pos1.y - pos2.y)
