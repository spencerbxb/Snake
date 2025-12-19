# Holds Functions to start game modes

import game_engine
import writing

started = False

# Starts singleplayer
def start_mode_1(wn):
    global started
    if not started:
        started = True
        game_engine.Playing = True
        game_engine.start_game(1, wn)
        writing.gamemode = 1
        writing.write_score()
        writing.write_controls()

# Starts multiplayer
def start_mode_2(wn):
    global started
    if not started:
        started = True
        game_engine.Playing = True
        game_engine.start_game(2, wn)
        writing.gamemode = 2
        writing.write_score()
        writing.write_controls_multiplayer()

# Ends the current game mode
def end_game():
    global started
    started = False
    game_engine.Playing = False
    writing.write_menu()