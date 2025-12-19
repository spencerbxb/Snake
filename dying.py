# Death function

import time

import writing
import game_starter
import game_engine

gamemode = 0    # updated by main

def death(head, controller, GRID_MAX, segments, wn):

    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"

    controller.reset()

    player = controller.player_id

    writing.update_score(True, player, wn=None)            # End the game + declare other player winner if multiplayer

    # Hide the segments
    for segment in segments:
        segment.goto(GRID_MAX * 2, GRID_MAX * 2)  # Move off-screen

    # Clear the segments list
    segments.clear()

    if gamemode == 2:   # force restart for multiplayer
        game_engine.Playing = False
        wn.ontimer(lambda: game_starter.end_game(), 2500)