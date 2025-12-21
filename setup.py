# A module for setting up the game screen and playfield

import turtle

import settings_vals

# Sets up the background
def setup_screen(wn, DIMS):
    wn.title("Python Python")
    wn.bgcolor("gray20")
    wn.setup(width=DIMS + 160, height=DIMS + 160)
    wn.tracer(0)

drawn = False

border = turtle.Turtle()
border.hideturtle()
border.speed(0)
border.penup()

# Draws the playing field
def draw_playfield(color, wn):
    border.clear()

    grid_max = settings_vals.grid_max
    grid_min = settings_vals.grid_min
    
    border.goto(grid_min, grid_min)
    border.pendown()
    border.color(color)
    border.begin_fill()

    size = grid_max - grid_min
    for _ in range(4):
        border.forward(size)
        border.left(90)

    border.end_fill()
    border.penup()