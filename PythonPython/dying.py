# Death function

import time
import score
import movement

def death(head, controller, GRID_MAX, segments):
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"

    controller.reset()

    score.update_score(True)

    # Hide the segments
    for segment in segments:
        segment.goto(GRID_MAX * 2, GRID_MAX * 2)  # Move off-screen

    # Clear the segments list
    segments.clear()