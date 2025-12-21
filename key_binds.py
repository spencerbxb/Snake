# Handles functions related to game settings

import settings
import key_actions

_wn = None
in_settings = False

def init(screen):
    global _wn
    _wn = screen

    # Calls to functions:
    _wn.onkeypress(lambda: key_actions.bind_1(_wn), "1")
    _wn.onkeypress(lambda: key_actions.bind_2(_wn), "2")
    _wn.onkeypress(lambda: key_actions.bind_3(_wn), "3")
    _wn.onkeypress(lambda: key_actions.bind_4(_wn), "4")
    _wn.onkeypress(lambda: key_actions.bind_5(_wn), "5")
    _wn.onkeypress(lambda: key_actions.bind_6(_wn), "6")
    _wn.onkeypress(lambda: key_actions.bind_7(_wn), "7")
    _wn.onkeypress(lambda: key_actions.bind_8(_wn), "8")

    _wn.onkeypress(lambda: key_actions.bind_space(_wn), "space")
    _wn.onkeypress(lambda: key_actions.bind_space(_wn), "Escape")