import random
import turtle
import time

import create
import dying
import score

# Main game loop
def main_loop(wn, head, food, segments, controller, GRID_MIN, GRID_MAX, DELAY):

    # Check for collision with border
    if (head.xcor() > GRID_MAX or head.xcor() < GRID_MIN or
        head.ycor() > GRID_MAX or head.ycor() < GRID_MIN):
        dying.death(head, controller, GRID_MAX, segments)

    # Check for collision with food
    if head.distance(food) < 20:    # Snake head has touched the food
        # Update the score
        score.update_score(False)

        # Move the food to a random spot
        x = random.randint(GRID_MIN // 20, GRID_MAX // 20) * 20
        y = random.randint(GRID_MIN // 20, GRID_MAX // 20) * 20
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        create.make_asset(new_segment, 0, "square", "grey", 0, 0)
        segments.append(new_segment)

    # Move the end segments first in reverse order
    
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Update segment 0
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    # Check for head collision with body segments
    for segment in segments[1:]:
        if segment.distance(head) < 20:
            dying.death(head, controller, GRID_MAX, segments)

    controller.apply()
    time.sleep(DELAY)
