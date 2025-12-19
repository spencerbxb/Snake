# Writes the score & game mode menu

import turtle
import time

import loop

Delay = 0.1
SPEEDUP = True

# Global constants (defined by main.py)

GRID_MAX = 0    # To be changed by main.py
TEXT_SIZE = 0   # To be changed by main.py

# Global mutables for score tracking
score0 = 0      # score for single player or player 0 in multiplayer
score1 = 0      # high score for single player or score for player 1 in multiplayer

pen = turtle.Turtle()

gamemode = 1    # 1 for single player, 2 for multiplayer

# Initializes the pen turtle for writing
def pen_init():
    pen.hideturtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.goto(0, 260)

pen_init()

# Writes the controls at the bottom
def write_controls():
    pen.goto(0, -GRID_MAX + 20)
    pen.write(
        "W/A/S/D | Arrow Keys",
        align="center",
        font=("Courier", int(TEXT_SIZE * 0.75), "normal")
    )

def write_controls_multiplayer():
    # Write W/A/S/D controls
    pen.goto(-GRID_MAX + 50, -GRID_MAX + 20)
    pen.write(
                "Player 1 - W/A/S/D",
                align = "left",
                font=("Courier", int(TEXT_SIZE * 0.75), "normal")
    )
    # Write arrow key controls
    pen.goto(GRID_MAX - 50, -GRID_MAX + 20)
    pen.write(
                "Player 2 - Arrow Keys",
                align = "right",
                font=("Courier", int(TEXT_SIZE * 0.75), "normal")
    )

# Writes the current score and high score
def write_score():
    pen.goto(0, GRID_MAX + 30)      # Position above the playfield
    pen.clear()
    pen.write(
        f"Score: {score0}, High Score: {score1}",
        align="center",
        font=("Courier", TEXT_SIZE, "normal")
    )

# Clears the score display for a given player
def clear_score():
    pen.clear()

# flashes the score without blocking the main loop
def flash_score(wn, write_func, iterations=3, wait=100):
    if wn is None or write_func is None:
        return  # silently do nothing
    count = {"i": 0}

    def step():
        if count["i"] >= iterations * 2:
            return
        if count["i"] % 2 == 0:
            pen.clear()
        else:
            write_func()
        count["i"] += 1
        wn.update()
        wn.ontimer(step, wait)

    step()

# Writes the current scores for both players in multiplayers
def write_multiplayer_score():
    pen.goto(0, GRID_MAX + 30)
    pen.clear()
    pen.write(
        f"Player 1: {score0}, Player 2: {score1}",
        align="center",
        font=("Courier", TEXT_SIZE, "normal")
    )

# Writes the winner of the multiplayer game
def write_winner(winner):
    pen.clear()
    pen.goto(0, 0)
    pen.write(
        f"Player {winner} Wins!",
        align="center",
        font=("Courier", TEXT_SIZE, "normal")
    )

# Updates the score & high score; if ending is True, resets score to 0
def update_score(ending, player, wn=None):
    global score0, score1

    if gamemode == 1:
        if not ending: score0 += 10
        if score0 > score1: score1 = score0
        if ending: score0 = 0

        if score0 % 100 == 0 and score0 != 0 and wn:
            global Delay
            flash_score(wn, write_score)
            if SPEEDUP:
                Delay = max(0.03, Delay - 0.01)  # Decrease delay, min 0.03

            loop.Delay = Delay  # Update delay in loop module
        else:
            write_score()

    elif gamemode == 2:
        if not ending:
            if player == 0: score0 += 10
            elif player == 1: score1 += 10

        if wn and (score0 % 100 == 0 and score0 != 0 or score1 % 100 == 0 and score1 != 0):
            flash_score(wn, write_multiplayer_score)
        elif ending:
            if player == 0: write_winner(1)
            elif player == 1: write_winner(0)
            score0 = 0
            score1 = 0

def mode(mode):
    global gamemode
    gamemode = mode

# Writes the game mode selection menu
def write_menu():
    pen.clear()
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(0)
    pen.write(
        "Select game mode:\n\n1. Single Player\n2. Two Player",
        align="center",
        font=("Courier", 24, "normal")
    )
