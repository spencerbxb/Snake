# Handles functions related to changing game sections

import settings_vals
import setup

# Functions that modify settings
def cycle_apples():
    if settings_vals.Apples == 10:
        settings_vals.Apples = 1
    else:
        settings_vals.Apples += 1

def cycle_dimensions(wn):
    if settings_vals.Dimensions == 30:
        settings_vals.Dimensions = 10
    else:
        settings_vals.Dimensions += 5
    settings_vals.update_bounds(wn)

def cycle_speedup():
    settings_vals.Speedup = not settings_vals.Speedup 

def cycle_color(_wn, var_name):
    current_index = getattr(settings_vals, var_name)
    current_index = (current_index + 1) % len(settings_vals.COLORS)
    setattr(settings_vals, var_name, current_index)

    color = settings_vals.COLORS[current_index]

    if var_name == "background":
        dims = settings_vals.Dimensions

        grid_max = settings_vals.grid_max
        grid_min = settings_vals.grid_min
        setup.draw_playfield(color, _wn)

    return color
