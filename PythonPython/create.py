# Creates an asset with given properties

def make_asset(asset, speed, shape, color, x, y):
    asset.speed(speed)
    asset.shape(shape)
    asset.color(color)
    asset.penup()            # no drawing
    asset.goto(x, y) 