# Writes the score

import turtle

score = 0
high_score = 0

pen = turtle.Turtle()

def pen_init():
    pen.hideturtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.goto(0, 260)

pen_init()

def write_score():
    pen.clear()
    pen.write(
        f"Score: {score}, High Score: {high_score}",
        align="center",
        font=("Courier", 24, "normal")
    )

def update_score(ending):
    global score
    global high_score

    if not ending: score += 10

    if score > high_score:
            high_score = score

    if ending: score = 0

    write_score()