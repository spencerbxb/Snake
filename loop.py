# loop.py

import random
import turtle
import time

import create
import dying
import writing

GRID_CELLS = 0      # To be set by main.py

Delay = 0.1         # Default delay; can be modified by writing.py

GRID_MAX = 0
GRID_MIN = 0        # Initialized by main.py

all_moving = False

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

PLAYER_COLORS = {
    0: "yellow",
    1: "purple",
}

# Manage food within the play space
def check_food(players, food):
    for player in players:
        player["new_segments_this_tick"] = []

        head = player["head"]
        segments = player["segments"]

        if head.distance(food) < 20:
            writing.update_score(False, player["id"], wn=None)

            # move food
            x = random.randint(-GRID_CELLS, GRID_CELLS) * 20
            y = random.randint(-GRID_CELLS, GRID_CELLS) * 20
            food.goto(x, y)

            # choose tail color by player id
            color = PLAYER_COLORS.get(player["id"], "grey")

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
            head.xcor() > GRID_MAX or head.xcor() < GRID_MIN or
            head.ycor() > GRID_MAX or head.ycor() < GRID_MIN
        ):
            dying.death(head, controller, GRID_MAX, segments, wn)

        # self collision
        for seg in segments[1:]:
            if head.distance(seg) < 20:
                dying.death(head, controller, GRID_MAX, segments, wn)

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
                    dying.death(head, controller, GRID_MAX, segments, wn)

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
