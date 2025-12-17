import turtle
import time
import random

import setup
import movement
import loop
import create
import dying
import score

##############################
# Global constants
##############################

DELAY = 0.15
DIMS = 600

PADDING = 20
GRID_MAX = DIMS // 2 - PADDING
GRID_MIN = -GRID_MAX

# Setting up the screen
wn = turtle.Screen()

setup.setup_screen(wn, DIMS)   
setup.draw_playfield(GRID_MIN - 10, GRID_MAX + 10)

score.write_score() # Initialize score display to 0, 0

##############################
# Setting up assets:
##############################

# Make the snake's head
head = turtle.Turtle()
create.make_asset(head, 0, "square", "black", 0, 0)
head.direction = "stop"
pending_direction = "stop"

# Make the snake's body segments
segments = []

# Snake food
food = turtle.Turtle()
create.make_asset(food, 0, "circle", "red", 0, 100)

# Movement
controller = movement.MovementController(head)
controller.bind_keys(wn)

##############################
# Main game loop:
##############################

while True:
    wn.update()
    loop.main_loop(wn, head, food, segments, controller, GRID_MIN, GRID_MAX, DELAY)