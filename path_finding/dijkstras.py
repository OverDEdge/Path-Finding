import pygame as pg
from queue import PriorityQueue

def run(draw, game, start, end):
    '''
    Method for running the Dijkstras algorithm.

    The min distance to every node from start is calculated.
    Every direction is checked and added to a PriorityQueue (if not already checked)

    Function returns True if path to end is found along with a dictionary for retracing the path. If no path is found False and empty dictionary is returned-

    RETURNS: bool, dictionary
    '''

    count_ = 0
    open_set = PriorityQueue()

    # Add start node to queue
    open_set.put((0, count_, start)) # Count is used to separate nodes with same cost value

    # Keep track of where we came from
    previous_node = {}

    # Initialize distances
    distances = {node: float("inf") for row in game.grid for node in row}
    distances[start] = 0

    # Need this since can't check in PriorityQueue if an item exists in it but easy with a hash set
    open_hash_set = {start}

    # Run Dijkstras algorithm until the set is empty (no more nodes to visit) or end is found
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
            # Calculate distance for neighbour from start
            distance = distances[current] + neighbour.weight

            # Check if calculated distance for node is less than already found
            if distance < distances[neighbour]:
                # Set distance as new minimum
                distances[neighbour] = distance
                previous_node[neighbour] = current

                if neighbour not in open_hash_set:
                    # Increase count variable to break ties.
                    count_ += 1

                    # Add neighbour to PrioriyQueue and hash set
                    open_set.put((distance, count_, neighbour))
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
