# loop.py

import random
import turtle
import time

import create
import dying
import writing
import settings_vals

grid_cells = 0      # To be set by main.py

Delay = 0.1         # Default delay; can be modified by writing.py

grid_max = 0
grid_min = 0        # Subject to change by settings_vals

# Manage movement of players around the map
def move_players(players):
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

# Manage food within the play space
def check_food(players, food):
    for player in players:
        player["new_segments_this_tick"] = []

        head = player["head"]
        segments = player["segments"]

        if head.distance(food) < 20:
            writing.update_score(False, player["id"], wn=None)

            # move food
            x = random.randint(-grid_cells, grid_cells) * 20
            y = random.randint(-grid_cells, grid_cells) * 20
            food.goto(x, y)

            # choose tail color by player id
            if player["id"] == 0:
                color = settings_vals.fetch_color("p1t")
            else:
                color = settings_vals.fetch_color("p2t")

            # create new tail segment
            seg = turtle.Turtle()
            create.make_asset(seg, 0, "square", color, 0, 0)
            segments.append(seg)

            player["new_segments_this_tick"] = [seg]

def check_collisions(players, wn):
    # --- COLLISIONS ---
    for player in players:
        head = player["head"]
        segments = player["segments"]
        controller = player["controller"]

       # border collision)
        if (
            head.xcor() > grid_max or head.xcor() < grid_min or
            head.ycor() > grid_max or head.ycor() < grid_min
        ):
            dying.death(head, controller, grid_max, segments, wn)

        # self collision
        for seg in segments[1:]:
            if head.distance(seg) < 20:
                dying.death(head, controller, grid_max, segments, wn)

       # other players collision
        for other in players:
            if other is player:
                continue
            # skip only segments that were just spawned this tick
            newly_spawned = getattr(other, "new_segments_this_tick", [])
            for seg in other["segments"]:
                if seg in newly_spawned:
                    continue
                if head.distance(seg) < 20:
                    dying.death(head, controller, grid_max, segments, wn)


all_moving = False

def main_loop(wn, players, food):

    global all_moving

    if not all_moving:
        one_moving = False
        # determine if a player is moving
        for player in players:
            head = player["head"]
            if head.direction != "stop":
                one_moving = True
                break

        if one_moving:
            for player in players:
                head = player["head"]
                if head.direction == "stop":  # hasn’t moved yet
                    head.direction = "up"    # default move
            
            all_moving = True

    check_food(players, food)
    move_players(players)
    check_collisions(players, wn)

    wn.update()
    time.sleep(Delay)