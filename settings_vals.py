# Stores values & arrays related to the settings module

# Gameplay:
Apples = 0
Dimensions = 0
Speedup = True

# Customization values:
p1h = 9
p1t = 10

p2h = 5
p2t = 4

background = 11

COLORS = [
    "black",        # 0
    "gray",         # 1
    "white",        # 2
    "yellow",       # 3
    "orange",       # 4
    "red",          # 5
    "pink",         # 6
    "magenta",      # 7
    "purple",       # 8
    "blue",         # 9
    "cyan",         # 10
    "light green",  # 11
    "green",        # 12
    "brown"         # 13
]

# Function to get the colors:
def fetch_color(var_name):
    return COLORS[globals()[var_name]]

# Relating to bounds, don't change these:

grid_max = 0
grid_min = 0
CELL_SIZE = 0

total_tiles = 0  # Total number of tiles on the grid

import setup
import loop

def update_bounds(wn):
    global grid_max
    global grid_min
    global total_tiles

    grid_cells = Dimensions // 2
    grid_max = grid_cells * CELL_SIZE
    grid_min = -grid_max

    loop.grid_max = grid_max
    loop.grid_min = grid_min
    loop.grid_cells = grid_cells

    total_tiles = (2 * grid_cells + 1) ** 2  # Total tiles = (positions per axis)^2

    color = fetch_color("background")

    setup.draw_playfield(color, wn)
    