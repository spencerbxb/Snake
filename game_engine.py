import turtle

import controls
import create
import loop
import writing
import endgame

import settings_vals

STEP = 20

Playing = False

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

# Constants passed from main:
START_DELAY = 0

def start_game(mode, wn):
    loop.all_moving = False         # Initialize to False for all new game starts

    writing.mode(mode)

    food = turtle.Turtle()
    create.make_asset(food, 0, "circle", "red", 0, 100)

    segments = []

    if mode == 1:  # Single Player
        head0 = turtle.Turtle()
        create.make_asset(head0, 0, "square", settings_vals.fetch_color("p1h"), 0, 0)
        head0.direction = "stop"

        controller = controls.MovementController(head0, SINGLE_KEYS)
        controller.player_id = 0  # Single-player
        controller.bind_keys(wn)

        players = [
            {
                "id": 0,
                "head": head0,
                "segments": segments,
                "controller": controller,
            }
        ]

        def game_tick():
            if not Playing:
                endgame.destroy_game(wn, players, food)
                return

            loop.main_loop(wn, players, food)
            wn.ontimer(game_tick, int(START_DELAY * 1000))

        game_tick()

    elif mode == 2:  # Two Player
        # Player 0
        head0 = turtle.Turtle()
        create.make_asset(head0, 0, "square", settings_vals.fetch_color("p1h"), -40, 0)
        head0.direction = "stop"
        segments0 = []  # <- separate list
        controller0 = controls.MovementController(head0, WASD_KEYS)
        controller0.player_id = 0
        controller0.bind_keys(wn)

        # Player 1
        head1 = turtle.Turtle()
        create.make_asset(head1, 0, "square", settings_vals.fetch_color("p2h"), 40, 0)
        head1.direction = "stop"
        segments1 = []  # <- separate list
        controller1 = controls.MovementController(head1, ARROW_KEYS)
        controller1.player_id = 1
        controller1.bind_keys(wn)

        players = [
            {
                "id": 0,
                "head": head0,
                "segments": segments0,   # <- assign individual list
                "controller": controller0,
            },
            {
               "id": 1,
                "head": head1,
                "segments": segments1,   # <- assign individual list
                "controller": controller1,
            }
        ]

        def game_tick():
            if not Playing:
                endgame.destroy_game(wn, players, food)
                return

            loop.main_loop(wn, players, food)
            wn.ontimer(game_tick, int(START_DELAY * 1000))

        game_tick()
