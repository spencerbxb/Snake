# loop.py

import random
import turtle
import time

import create
import dying
import writing
import settings_vals
import game_starter

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
def spawn_food(foods, players):
    # Calculate available space
    total_length = 0
    for p in players:
        if p["id"] == 0:
            total_length += 1 + (writing.score0 // 10)
        else:
            total_length += 1 + (writing.score1 // 10)
    total_cells = settings_vals.total_tiles
    available_space = total_cells - total_length
    
    if len(foods) >= available_space:
        return  # No space for more food
    
    x = random.randint(-grid_cells, grid_cells) * 20
    y = random.randint(-grid_cells, grid_cells) * 20
    for _ in range(settings_vals.total_tiles // 2):  # limit attempts to avoid infinite loope loop
        valid = True
        for p in players:
            if p["head"].distance((x, y)) < 20:
                valid = False
                break
            for seg in p["segments"]:
                if seg.distance((x, y)) < 20:
                    valid = False
                    break
        if valid:
            for f in foods:
                if f.distance((x, y)) < 20:
                    valid = False
                    break
        if valid:
            food = turtle.Turtle()
            create.make_asset(food, 0, "circle", "red", x, y)
            foods.append(food)
            return
        x = random.randint(-grid_cells, grid_cells) * 20
        y = random.randint(-grid_cells, grid_cells) * 20
    
    # Failsafe: Scan from top-left to bottom-right for first available tile
    for x_grid in range(-grid_cells, grid_cells + 1):
        for y_grid in range(grid_cells, -grid_cells - 1, -1):
            x = x_grid * 20
            y = y_grid * 20
            valid = True
            for p in players:
                if p["head"].distance((x, y)) < 20:
                    valid = False
                    break
                for seg in p["segments"]:
                    if seg.distance((x, y)) < 20:
                        valid = False
                        break
            if valid:
                for f in foods:
                    if f.distance((x, y)) < 20:
                        valid = False
                        break
            if valid:
                food = turtle.Turtle()
                create.make_asset(food, 0, "circle", "red", x, y)
                foods.append(food)
                return
    # If still no spot (shouldn't happen with available_space check), do nothing

def check_food(players, foods):
    eaten_foods = set()
    for player in players:
        player["new_segments_this_tick"] = []
        head = player["head"]
        for food in list(foods):  # iterate over copy to avoid issues
            if head.distance(food) < 20 and food not in eaten_foods:
                eaten_foods.add(food)
                writing.update_score(False, player["id"], wn=None)

                # choose tail color by player id
                if player["id"] == 0:
                    color = settings_vals.fetch_color("p1t")
                else:
                    color = settings_vals.fetch_color("p2t")

                # create new tail segment
                seg = turtle.Turtle()
                create.make_asset(seg, 0, "square", color, 0, 0)
                player["segments"].append(seg)
                player["new_segments_this_tick"].append(seg)

    # Remove eaten foods and spawn new ones
    for food in eaten_foods:
        foods.remove(food)
        food.hideturtle()
    for _ in eaten_foods:
        spawn_food(foods, players)

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

def main_loop(wn, players, foods):

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

    check_food(players, foods)
    move_players(players)
    check_collisions(players, wn)

    if len(players) == 1 and len(players[0]["segments"]) + 1 >= settings_vals.total_tiles:
        # If player length is MAXXED, win
        writing.write_single_win()

        time.sleep(Delay * 2)

        wn.ontimer(lambda: game_starter.end_game(), 2500)

    wn.update()
    time.sleep(Delay)