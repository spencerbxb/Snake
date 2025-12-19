# loop.py

import random
import turtle
import time

import create
import dying
import writing

GRID_CELLS = 0  # To be set by main.py

Delay = 0.1  # Default delay; can be modified by writing.py

def main_loop(wn, players, food, GRID_MIN, GRID_MAX):

    # --- FOOD ---
    for player in players:
        head = player["head"]
        segments = player["segments"]

        if head.distance(food) < 20:
            writing.update_score(False, player["id"], wn)

            cell_min = -GRID_CELLS
            cell_max = GRID_CELLS

            x = random.randint(cell_min, cell_max) * 20
            y = random.randint(cell_min, cell_max) * 20
            food.goto(x, y)

            seg = turtle.Turtle()
            create.make_asset(seg, 0, "square", "grey", 0, 0)
            segments.append(seg)

    # --- MOVE SEGMENTS ---
    for player in players:
        head = player["head"]
        segments = player["segments"]

        for i in range(len(segments) - 1, 0, -1):
            segments[i].goto(segments[i - 1].pos())

        if segments:
            segments[0].goto(head.pos())

    # --- MOVE HEADS ---
    for player in players:
        player["controller"].apply()

    # --- COLLISIONS ---
    for player in players:
        head = player["head"]
        segments = player["segments"]
        controller = player["controller"]

        # border
        if (
            head.xcor() > GRID_MAX or head.xcor() < GRID_MIN or
            head.ycor() > GRID_MAX or head.ycor() < GRID_MIN
        ):
            dying.death(head, controller, GRID_MAX, segments)

        # self
        for seg in segments[1:]:
            if head.distance(seg) < 20:
                dying.death(head, controller, GRID_MAX, segments)

        # others
        for other in players:
            if other is player:
                continue
            for seg in other["segments"]:
                if head.distance(seg) < 20:
                    print("COLLIDED WITH OTHER PLAYER, DYING PLAYER IS:", player["id"])
                    dying.death(head, controller, GRID_MAX, segments)

    wn.update()
    time.sleep(Delay)
