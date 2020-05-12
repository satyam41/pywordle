import random
import json

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def hextorgb(hex):
    _hex = hex.lstrip('#')
    rgb = tuple(int(_hex[i:i+2], 16) for i in (0, 2, 4))
    return rgb

def getrandom():
    rancol = (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))
    return rancol

def getpalletes():
    return 'palettes.json'

def frompallete(pallete):
    with open(getpalletes()) as f:
        _json = json.load(f)
        pal = _json[pallete]
        _col = pal[random.randrange(0, len(pal))]
        return hextorgb(_col)
