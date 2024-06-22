# Minesweeper Game README

## Overview

This is a Python implementation of the classic Minesweeper game using the Pygame library, in order to practice OOP.
The game includes functionalities for creating the game grid, placing bombs, revealing tiles, and flagging suspected bombs. Additionally, there is an Solver component that attempts to solve the grid.

## demo:


https://github.com/IdoSefi/MineSweeperSolver/assets/172110264/7a90543a-7f8a-49d2-b711-04643afc642f

https://github.com/IdoSefi/MineSweeperSolver/assets/172110264/d6b8937d-8587-4127-b51b-52bd36d0d4fe

## loosing demo:


https://github.com/IdoSefi/MineSweeperSolver/assets/172110264/38a7ff61-340b-4408-b1bb-560b323af6bf




## Requirements

- Python 3.x
- Pygame
- Pynput

To install the required libraries, use the following commands:

```bash
pip install pygame
pip install pynput
```

## Code Structure

### Variables

- `white`, `red`, `blue`, `green`, `black`, `gray`: RGB color definitions for the game.
- `width`: Width of each tile in the grid.
- `row`, `col`: Number of rows and columns in the grid.
- `bomb_num`: Number of bombs to be placed in the grid.
- `msai_loop`: Counter for AI loops.

### Initialization

- Pygame is initialized and the game screen is set up with a defined size.
- A clock is initialized to control the frame rate.

### Classes

#### Cube

This class represents each tile in the Minesweeper grid. It includes methods for:
- Initializing the tile.
- Marking the tile as a bomb and updating adjacent tiles.
- Coloring the tile based on its state (unrevealed, revealed, flagged).

### Functions

#### Grid and Bomb Placement

- `loop_adjacent(y_tile, x_tile)`: Prints adjacent tiles.
- `loop_adjacent_visable(y_tile, x_tile)`: Makes adjacent tiles visible.
- `loop_adjacent_add_value(y_tile, x_tile)`: Adds values to adjacent tiles indicating the number of bombs nearby.
- `inbound(y, x)`: Checks if a tile is within the grid bounds.
- Bomb placement logic iterates to randomly place bombs on the grid.

#### Drawing and Interaction

- `draw_grid(grid)`: Draws the current state of the grid to the screen.
- `clicked_tile_left(mx, my)`: Handles left mouse clicks to reveal tiles.
- `clicked_tile_right(mx, my)`: Handles right mouse clicks to flag tiles.
- `open_a_tile(boardY, boardX)`: Reveals a tile and potentially adjacent tiles.
- `flag_em(y_tile, x_tile)`: Flags a tile as containing a bomb.
- `you_loose()`: Reveals all bombs and indicates a loss.

#### AI Functions

- `msai()`, `msai2()`: AI loops that attempt to solve the Minesweeper grid.
- `corner(y_tile, x_tile)`: Flags adjacent tiles if the number of hidden tiles matches the tile's value.
- `find_true_value(y_tile, x_tile)`: Updates the tile's true value considering flagged tiles.
- `open_corner(y_tile, x_tile)`: Opens all adjacent non-flagged tiles if the true value is 0.
- `seacch_1_1_pattern(y_tile, x_tile)`: AI pattern search for solving the grid.
- `make_gray_list(y_tile, x_tile, b_list)`: Creates a list of adjacent hidden tiles.

### Main Game Loop

- Handles user input for quitting, left and right mouse clicks.
- Calls AI functions at intervals.
- Draws the grid and updates the display at each iteration.

## Running the Game

To run the game, simply execute the script. The game window will open, and you can start playing Minesweeper. Use the left mouse button to reveal tiles and the right mouse button to flag suspected bombs.

```bash
python minesweeper.py
```

after the board is open. click on an empty tile and the Solver will do the rest. it will click on safe tiles and mark in blue the flagged mine tiles

## Future Improvements

- Make the board and mines prettier
- seperating the Solver and the Board files
- making the Solver more capeable

Enjoy playing Minesweeper!
