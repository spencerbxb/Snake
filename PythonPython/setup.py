# A module for setting up the game screen and playfield

import turtle

# Sets up the background
def setup_screen(wn, dims):
    wn.title("Python Python")
    wn.bgcolor("gray20")
    wn.setup(width=dims, height=dims)
    wn.tracer(0)

# Draws the playing field
def draw_playfield(GRID_MIN, GRID_MAX, color="lightgreen"):
    border = turtle.Turtle()
    border.hideturtle()
    border.speed(0)
    border.penup()
    border.goto(GRID_MIN, GRID_MIN)
    border.pendown()
    border.color(color)
    border.begin_fill()

    size = GRID_MAX - GRID_MIN
    for _ in range(4):
        border.forward(size)
        border.left(90)

    border.end_fill()
