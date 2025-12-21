# Writes the score & game mode menu

import turtle

import loop
import dying
import settings_vals

DEFAULT_DELAY = 0.1
Delay = 0.1
Speedup = True  # Mutable by settings.py

# Global constants (defined by main.py)

GRID_MAX = 0    # To be changed by main.py
GRID_MIN = 0    # To be changed by main.py
TEXT_SIZE = 0   # To be changed by main.py

# Global mutables for score tracking
score0 = 0      # score for single player or player 0 in multiplayer
score1 = 0      # score for player 1 in multiplayer

high_single = 0    # high score for singleplayer

pen = turtle.Turtle()

gamemode = 0    # 1 for single player, 2 for multiplayer

# Initializes the pen turtle for writing
def pen_init():
    pen.hideturtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("black")
    pen.penup()
    pen.goto(0, 260)

pen_init()

# Writes the controls at the bottom
def write_controls():
    pen.goto(0, GRID_MIN + 20)
    pen.color(settings_vals.fetch_color("p1h"))
    pen.write(
        "W/A/S/D | Arrow Keys",
        align="center",
        font=("Courier", TEXT_SIZE // 2, "normal")
    )
    pen.color("white")

def write_controls_multiplayer():
    # Write W/A/S/D controls
    pen.goto(GRID_MIN + 20, GRID_MIN + 20)
    pen.color(settings_vals.fetch_color("p1h"))
    pen.write(
                "Player 1 - W/A/S/D",
                align = "left",
                font=("Courier", TEXT_SIZE // 2, "normal")
    )
    # Write arrow key controls
    pen.goto(GRID_MAX - 20, GRID_MIN + 20)
    pen.color(settings_vals.fetch_color("p2h"))
    pen.write(
                "Player 2 - Arrow Keys",
                align = "right",
                font=("Courier", TEXT_SIZE // 2, "normal")
    )
    pen.color("white")

# Write return to menu message
def write_return_to_menu():
    pen.goto(0, GRID_MIN - 50)
    pen.write(
        "SPACE: Return to Menu",
        align="center",
        font=("Courier", TEXT_SIZE, "normal")
    )

# Writes the current score and high score
def write_score():
    pen.goto(0, GRID_MAX + 30)      # Position above the playfield
    pen.clear()
    pen.color("white")
    if gamemode == 1:
        pen.write(
        f"Score: {score0}, High Score: {high_single}",
        align="center",
        font=("Courier", TEXT_SIZE, "normal")
    )
    elif gamemode == 2:
        pen.goto(0, GRID_MAX + 30)
        pen.clear()
        pen.write(
            f"Player 1: {score0}, Player 2: {score1}",
            align="center",
            font=("Courier", TEXT_SIZE, "normal")
        )


# flashes the score without blocking the main loop
def flash_score(wn, iterations=3, wait=100):
    if not wn or gamemode not in (1, 2): return

    i = 0

    def step():
        nonlocal i

        if i >= iterations * 2: return
        if i % 2 == 0:
            pen.clear()
        else:
            write_score()
        i += 1
        wn.update()
        wn.ontimer(step, wait)

    step()
    write_return_to_menu()      # Re-write return to menu message (will be cleared by score updates)

# Writes the winner of the multiplayer game
def write_winner(winner):
    color = "white"
    if winner == 1:
        color = settings_vals.fetch_color("p1h")
    elif winner == 2:
        color = settings_vals.fetch_color("p2h")
    pen.clear()
    pen.goto(0, 0)
    pen.color(color)
    pen.write(
        f"Player {winner} Wins!",
        align="center",
        font=("Courier", TEXT_SIZE, "normal")
    )

# Updates the score & high score; if ending is True, resets score to 0
def update_score(ending, player, wn=None):
    global score0, score1, high_single, Delay

    if gamemode == 1:
        if not ending: score0 += 10
        else: Delay = DEFAULT_DELAY
        if score0 > high_single: high_single = score0
        if ending: score0 = 0

        if score0 % 100 == 0 and score0 != 0 and wn:
            flash_score(wn)
            if Speedup:
                Delay = max(0.03, Delay - 0.01)  # Decrease delay, min 0.03

            loop.Delay = Delay  # Update delay in loop module
        else:
            write_score()
    
        write_return_to_menu()

    elif gamemode == 2:
        if not ending:
            if player == 0: score0 += 10
            elif player == 1: score1 += 10

        if wn and (score0 % 100 == 0 and score0 != 0 or score1 % 100 == 0 and score1 != 0):
            flash_score(wn)
            write_return_to_menu()
        elif not ending:
            write_score()
            write_return_to_menu()
        else:
            if player == 0: write_winner(2)
            elif player == 1: write_winner(1)
            score0 = 0
            score1 = 0
            Delay = DEFAULT_DELAY

# Wipe scores for game mode change, maintains high score though
def wipe_scores():
    global score0, score1
    score0, score1 = 0, 0

# Change game mode
def mode(mode):
    global gamemode
    if gamemode != mode:
        wipe_scores()
        gamemode = mode
        dying.gamemode = mode

# Writes the game mode selection menu
def write_menu():
    pen.clear()
    pen.penup()
    pen.goto(0, GRID_MAX - 80)
    pen.seth(0)

    pen.color("dark green")

    pen.write(
        "🐍PYTHON PYTHON🐍",
        align = "center",
        font=("Courier", int(TEXT_SIZE * 1.5), "bold")
    )

    pen.goto(0, GRID_MIN)

    pen.color("black")
    pen.write(
        "Select game mode:\n\n"
        "1. Single Player\n"
        "2. Two Player"
        "\n\n\n\n"
        "Esc: Open Settings",
        align="center",
        font=("Courier", TEXT_SIZE, "normal")
    )

# Writes the settings menu
def write_bottom():
    font_size = int(TEXT_SIZE / 1.5)

    pen.penup()
    pen.goto(0, GRID_MIN + 10)
    pen.write(
        "Esc: Main Menu",
        align="center",
        font=("Courier", int(font_size * 1.25), "bold")
    )

def write_settings():
    pen.clear()
    pen.penup()

    font_size = int(TEXT_SIZE / 1.5)
    line_height = font_size
    num_lines = 13

    start_y = -(line_height * num_lines) * 0.75

    pen.color("white")

    pen.goto(GRID_MIN + 20, GRID_MAX + 20)

    pen.write(
        "SETTINGS",
        align="left",
        font=("Courier", int(font_size * 1.25), "bold")
    )

    pen.goto(GRID_MIN + 5, start_y - 10)
    pen.seth(0)

    pen.color("black")

    # Write the left side
    pen.write(
        "1. Apples:\n\n"
        "2. Dimensions:\n\n"
        "3. Speedup:\n\n"
        "4. Player 1 head:\n\n"
        "5. Player 1 tail:\n\n"
        "6. Player 2 head:\n\n"
        "7. Player 2 tail:\n\n"
        "8. Background:",
        align="left",
        font=("Courier", font_size, "normal")
    )

    pen.goto(GRID_MAX - 5, start_y - 10)
    pen.seth(180)

    p1h_color = settings_vals.fetch_color("p1h")
    p1t_color = settings_vals.fetch_color("p1t")
    p2h_color = settings_vals.fetch_color("p2h")
    p2t_color = settings_vals.fetch_color("p2t")
    background_color = settings_vals.fetch_color("background")

    # Write the right side
    pen.write(
        f"{settings_vals.Apples}\n\n"
        f"{settings_vals.Dimensions}\n\n"
        f"{settings_vals.Speedup}\n\n"
        f"{p1h_color}\n\n"
        f"{p1t_color}\n\n"
        f"{p2h_color}\n\n"
        f"{p2t_color}\n\n"
        f"{background_color}",
        align="right",
        font=("Courier", font_size, "normal")
    )

    write_bottom()
