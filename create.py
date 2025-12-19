# Creates an asset with given properties

def make_asset(asset, speed, shape, color, x, y):
    asset.speed(speed)
    asset.shape(shape)
    asset.color(color)
    asset.penup()
    asset.goto(x, y)
    asset.showturtle()