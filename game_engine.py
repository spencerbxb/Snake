import turtle
import controls
import create
import loop
import writing

STEP = 20

# Key mappings
WASD_KEYS = {
    "w": lambda c: c.go_up(),
    "s": lambda c: c.go_down(),
    "a": lambda c: c.go_left(),
    "d": lambda c: c.go_right(),
}

ARROW_KEYS = {
    "Up": lambda c: c.go_up(),
    "Down": lambda c: c.go_down(),
    "Left": lambda c: c.go_left(),
    "Right": lambda c: c.go_right(),
}


SINGLE_KEYS = WASD_KEYS | ARROW_KEYS

def start_game(mode, wn, GRID_MIN, GRID_MAX, DELAY):
    writing.mode(mode)

    food = turtle.Turtle()
    create.make_asset(food, 0, "circle", "red", 0, 100)

    segments = []

    if mode == 1:  # Single Player
        head = turtle.Turtle()
        create.make_asset(head, 0, "square", "black", 0, 0)
        head.direction = "stop"

        wn.update()

        controller = controls.MovementController(head, SINGLE_KEYS)
        controller.player_id = 0  # Single-player
        controller.bind_keys(wn)

        players = [
            {
                "id": 0,
                "head": head,
                "segments": segments,
                "controller": controller,
            }
        ]

        def game_tick():
            loop.main_loop(wn, players, food, GRID_MIN, GRID_MAX)
            wn.ontimer(game_tick, int(DELAY * 1000))

        game_tick()

    elif mode == 2:  # Two Player
        # Player 0
        head0 = turtle.Turtle()
        create.make_asset(head0, 0, "square", "black", -40, 0)
        head0.direction = "stop"
        controller0 = controls.MovementController(head0, WASD_KEYS)
        controller0.player_id = 0
        controller0.bind_keys(wn)

        # Player 1
        head1 = turtle.Turtle()
        create.make_asset(head1, 0, "square", "blue", 40, 0)
        head1.direction = "stop"
        controller1 = controls.MovementController(head1, ARROW_KEYS)
        controller1.player_id = 1
        controller1.bind_keys(wn)

        wn.update()

        players = [
            {
                "id": 0,
                "head": head0,
                "segments": segments,
                "controller": controller0,
            }, 
            {
                "id": 1,
                "head": head1,
                "segments": segments,
                "controller": controller1,
            }
        ]

        def game_tick():
            loop.main_loop(wn, players, food, GRID_MIN, GRID_MAX)
            wn.ontimer(game_tick, int(DELAY * 1000))

        game_tick()  