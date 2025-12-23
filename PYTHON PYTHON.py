##################################################################
###                                                            ###
###   # # #   #   #   # # # #   #     #     # #     #      #   ###
###   #   #   #   #      #      #     #    #   #    # #    #   ###
###   #   #   #   #      #      #     #   #     #   #  #   #   ###
###   # # #    ###       #      # # # #   #     #   #   #  #   ###
###   #         #        #      #     #   #     #   #    # #   ###
###   #         #        #      #     #    #   #    #     ##   ###
###   #         #        #      #     #     # #     #      #   ###
###                                                            ###
###   # # #   #   #   # # # #   #     #     # #     #      #   ###
###   #   #   #   #      #      #     #    #   #    # #    #   ###
###   #   #   #   #      #      #     #   #     #   #  #   #   ###
###   # # #    ###       #      # # # #   #     #   #   #  #   ###
###   #         #        #      #     #   #     #   #    # #   ###
###   #         #        #      #     #    #   #    #     ##   ###
###   #         #        #      #     #     # #     #      #   ###
###                                                            ###
##################################################################
#
# spencerbxb        https://github.com/spencerbxb
#

############################################################################################
# Game Defaults, these can be modified, they are also modifiable in settings
############################################################################################

DEFAULT_FOOD_AMOUNT = 1         # Number of food items on the screen at once
DEFAULT_FOOD_MULTIPLIER = 1     # Increase food amount by this factor for every additional player
DEFAULT_START_DELAY = 0.1       # Delay between screen updates (in seconds), diminishes -0.01 for every +10 length
DEFAULT_DIMENSIONS = 10         # Width and height of the screen (in pixels)
DEFAULT_SPEEDUP = True          # Whether to speed up the game as the snake grows

# Colors for body parts, see settings_vals.py for table
DEFAULT_P1H = 9
DEFAULT_P1T = 10

DEFAULT_P2H = 5
DEFAULT_P2T = 4

DEFAULT_BACKGROUND = 11












############################################################
# DO NOT CHANGE THE FOLLOWING VALUES
############################################################

CELL_SIZE = 25               # Size of each cell in the grid (in pixels)  
DIMS = DEFAULT_DIMENSIONS * CELL_SIZE + CELL_SIZE

GRID_CELLS = DEFAULT_DIMENSIONS // 2
GRID_MAX =  GRID_CELLS * CELL_SIZE
GRID_MIN = -GRID_MAX

##############################

import turtle

import setup
import writing
import game_engine
import loop
import settings_vals
import key_binds

started = False

# Functions to end the game modes:

# Set constants in writing module
def writing_constants():
    writing.GRID_MAX = GRID_MAX
    writing.GRID_MIN = GRID_MIN
    writing.TEXT_SIZE = GRID_MAX // 10
    writing.Delay = DEFAULT_START_DELAY
    writing.SPEEDUP = DEFAULT_SPEEDUP
    loop.GRID_CELLS = GRID_CELLS

# Set constants in game_engine module
def game_engine_constants():
    game_engine.START_DELAY = DEFAULT_START_DELAY

def loop_constants():
    loop.grid_max = GRID_MAX
    loop.grid_min = GRID_MIN
    loop.grid_cells = GRID_CELLS

    loop.Delay = DEFAULT_START_DELAY
    loop.DEFAULT_DELAY = DEFAULT_START_DELAY

# Set settings constants
def settings_vals_init():
    settings_vals.Apples = DEFAULT_FOOD_AMOUNT
    settings_vals.Dimensions = DEFAULT_DIMENSIONS
    settings_vals.Speedup = DEFAULT_SPEEDUP

    settings_vals.grid_max = GRID_MAX
    settings_vals.grid_min = GRID_MIN
    settings_vals.CELL_SIZE = CELL_SIZE

    # Colors
    settings_vals.p1h = DEFAULT_P1H
    settings_vals.p1t = DEFAULT_P1T
    settings_vals.p2h = DEFAULT_P2H
    settings_vals.p2t = DEFAULT_P2T
    settings_vals.background = DEFAULT_BACKGROUND

    settings_vals.total_tiles = (2 * GRID_CELLS + 1) ** 2

writing_constants()
game_engine_constants()
loop_constants()
settings_vals_init()

# Setting up the screen
wn = turtle.Screen()

setup.setup_screen(wn, DIMS)   
setup.draw_playfield("light green", wn)

wn.update()

writing.write_menu()  # Display the game mode selection menu

wn.listen()

# Initialize keybinds
key_binds.init(wn)

wn.mainloop()