# Visualization of Path-Finding Algorithms
This program uses Pygame to visualize path-finding algorithms on a grid.
Necessary packages:

- Pygame

## Application Instructions
### Placement of Start, End and Walls
Placement of Start, End and Wall Nodes are done by Left-Click (using mouse/touchpad) anywhere on the visible grid.

- The first press sets the Start Node (Coloured in Green)
- The second press sets the End Node (Coloured in Purple)
- The remaining clicks (or by holding the mouse button down) will place Wall Nodes (Coloured in Black)

At any time you can 'reset' a Node by Right-Click on it. If erase Start or End Node then these will be place down first when doing Left-Click again (Start is always first if not placed).

It is possible to switch between two Path-Finding algorithms (currently):

- Press 'a' on keyboard: A* Algorithm
- Press 'd' on keyboard: Dijkstra's Algorithm

The currently chosen algorithm is displayed in the top right corner in blue text.

## How to start the application
Download a copy of the repository into a folder. Navigate and enter folder. In Command Prompt type:

- python -m path-finding

This will start the game and game will launch in a separate window. 'ESC' or pressing the 'x' at top right can be used to exit the application at any time.

## Inspiration
The inspiration for this application is based on:
- The game skeleton, presented by: [KidsCanCode.org](https://www.youtube.com/channel/UCNaPQ5uLX5iIEHUCLmfAgKg9 Youtube channel.
- Visualization of A* algorithm by [TechWithTim](https://www.youtube.com/channel/UC4JX40jDee_tINbkjycV4Sg) Youtube channel.
- Project structure based on instructions in the book: [Python The Hard Way](https://learncodethehardway.org/python/)
