# Death function

import time
import writing
import controls

def death(head, controller, GRID_MAX, segments):
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