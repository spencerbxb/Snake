# A module for handling controls & player movement

STEP = 20

class MovementController:
    def __init__(self, head):
        self.head = head
        self.pending_direction = "stop"

    def reset(self):
        self.pending_direction = "stop"
        self.head.direction = "stop"
        self.enabled = False

    def go_up(self):
        if self.head.direction != "down":
            self.pending_direction = "up"

    def go_down(self):
        if self.head.direction != "up":
            self.pending_direction = "down"

    def go_right(self):
        if self.head.direction != "left":
            self.pending_direction = "right"

    def go_left(self):
        if self.head.direction != "right":
            self.pending_direction = "left"

    def apply(self):
        if self.pending_direction != "stop":
            self.head.direction = self.pending_direction

        if self.head.direction == "up":
            self.head.sety(self.head.ycor() + STEP)
        elif self.head.direction == "down":
            self.head.sety(self.head.ycor() - STEP)
        elif self.head.direction == "right":
            self.head.setx(self.head.xcor() + STEP)
        elif self.head.direction == "left":
            self.head.setx(self.head.xcor() - STEP)

    def bind_keys(self, wn):
        wn.listen()
        bindings = [
            ("Up", self.go_up), ("w", self.go_up),
            ("Down", self.go_down), ("s", self.go_down),
            ("Right", self.go_right), ("d", self.go_right),
            ("Left", self.go_left), ("a", self.go_left),
        ]
        for key, func in bindings:
            wn.onkeypress(func, key)