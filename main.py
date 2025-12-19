import turtle

import setup
import writing
import game_engine
import loop
import game_starter
import loop

##############################
# Game Confiugurations:
##############################

FOOD_AMOUNT = 1         # Number of food items on the screen at once
FOOD_MULTIPLIER = 1     # Increase food amount by this factor for every additional player
START_DELAY = 0.1       # Delay between screen updates (in seconds), diminishes -0.01 for every +10 length
SQUARES = 20            # Width and height of the screen (in pixels)
SPEEDUP = True          # Whether to speed up the game as the snake grows

##############################

CELL_SIZE = 20               # Size of each cell in the grid (in pixels)  
DIMS = SQUARES * CELL_SIZE

GRID_CELLS = SQUARES // 2
GRID_MIN = -GRID_CELLS * CELL_SIZE
GRID_MAX =  GRID_CELLS * CELL_SIZE

##############################

started = False

# Setting up the screen
wn = turtle.Screen()

setup.setup_screen(wn, DIMS)   
setup.draw_playfield(GRID_MIN - 10, GRID_MAX + 10)

wn.update()

writing.write_menu()  # Display the game mode selection menu
# writing.write_score() # Initialize score display to 0, 0

# Functions to end the game modes:

# Set constants in writing module
def writing_constants():
    writing.GRID_MAX = GRID_MAX
    writing.GRID_MIN = GRID_MIN
    writing.TEXT_SIZE = GRID_MAX // 10
    writing.Delay = START_DELAY
    writing.SPEEDUP = SPEEDUP
    loop.GRID_CELLS = GRID_CELLS

# Set constants in game_engine module
def game_engine_constants():
    game_engine.GRID_MAX = GRID_MAX
    game_engine.GRID_MIN = GRID_MIN
    game_engine.START_DELAY = START_DELAY

def loop_constants():
    loop.GRID_MAX = GRID_MAX
    loop.GRID_MIN = GRID_MIN

writing_constants()
game_engine_constants()
loop_constants()

wn.listen()

wn.onkeypress(lambda: game_starter.start_mode_1(wn), "1")
wn.onkeypress(lambda: game_starter.start_mode_2(wn), "2")
wn.onkeypress(game_starter.end_game, "space")
    
wn.mainloop()