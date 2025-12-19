STEP = 20

class MovementController:
    def __init__(self, head, keymap):
        self.head = head
        self.pending_direction = "stop"
        self.keymap = keymap
        self.player_id = 0  # Default, can be overridden

    def go_up(self):
        if self.head.direction != "down":
            self.pending_direction = "up"

    def go_down(self):
        if self.head.direction != "up":
            self.pending_direction = "down"

    def go_left(self):
        if self.head.direction != "right":
            self.pending_direction = "left"

    def go_right(self):
        if self.head.direction != "left":
            self.pending_direction = "right"

    def apply(self):
        if self.pending_direction != "stop":
            self.head.direction = self.pending_direction
        if self.head.direction == "up":
            self.head.sety(self.head.ycor() + STEP)
        elif self.head.direction == "down":
            self.head.sety(self.head.ycor() - STEP)
        elif self.head.direction == "left":
            self.head.setx(self.head.xcor() - STEP)
        elif self.head.direction == "right":
            self.head.setx(self.head.xcor() + STEP)

    def bind_keys(self, wn):
        wn.listen()
        for key, action in self.keymap.items():
            wn.onkeypress(lambda a=action: a(self), key)

    def reset(self):
        self.pending_direction = "stop"
        self.head.direction = "stop"