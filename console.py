import assembler
from PIL import Image

CATAMARAN = 'Fonts/Catamaran-Black.ttf'
CINZEL = 'Fonts/Cinzel-Regular.ttf'
QUESTRIAL = 'Fonts/Questrial-Regular.ttf'
ZILLA = 'Fonts/ZillaSlab-Bold.ttf'
HEPTA = 'Fonts/HeptaSlab-Bold.ttf'

_file = 'alice-in-us.txt'

_des = 8

def do_it():
    global _des

    im = assembler.assemble(_file, 1024, 1024, HEPTA, desizing=_des, variance_factor=8, theme="SunsetWaters", condense=True, ignore=False)

    if(im == 'terminate'):
        print("Time taken too long, checking again with reduced sizes.")
        _des += 6
        do_it()

    if(im != None and im != 'terminate' and type(im) != 'str'):
        im.show()
        im.save("first.png")

do_it()