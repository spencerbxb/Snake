import turtle

import setup
import writing
import game_engine
import loop

##############################
# Game Confiugurations:
##############################

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

# Functions to start game modes
def start_mode_1():
    global started
    if not started:
        started = True
        game_engine.start_game(1, wn, GRID_MIN, GRID_MAX, START_DELAY)
        writing.write_score()
        writing.write_controls()
    

def start_mode_2():
    global started
    if not started:
        started = True
        game_engine.start_game(2, wn, GRID_MIN, GRID_MAX, START_DELAY)
        writing.write_multiplayer_score()
        writing.write_controls_multiplayer()

writing.GRID_MAX = GRID_MAX
writing.TEXT_SIZE = GRID_MAX // 10  # Text size scales with grid size
writing.Delay = START_DELAY
writing.SPEEDUP = SPEEDUP
loop.GRID_CELLS = GRID_CELLS

wn.listen()

wn.onkeypress(start_mode_1, "1")
wn.onkeypress(start_mode_2, "2")
    
wn.mainloop()