import assembler
from PIL import Image

CATAMARAN = 'Fonts/Catamaran-Black.ttf'
CINZEL = 'Fonts/Cinzel-Regular.ttf'
QUESTRIAL = 'Fonts/Questrial-Regular.ttf'
ZILLA = 'Fonts/ZillaSlab-Bold.ttf'
HEPTA = 'Fonts/HeptaSlab-Bold.ttf'

_file = 'declaration.txt'
im = assembler.assemble(_file, 2048, 2048, CINZEL, 2.6, min_freq=0)

im.show()
im.save("first.png")