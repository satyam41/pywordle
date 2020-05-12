import assembler
from PIL import Image

CATAMARAN = 'Fonts/Catamaran-Black.ttf'
CINZEL = 'Fonts/Cinzel-Regular.ttf'
QUESTRIAL = 'Fonts/Questrial-Regular.ttf'
ZILLA = 'Fonts/ZillaSlab-Bold.ttf'
HEPTA = 'Fonts/HeptaSlab-Bold.ttf'

_file = 'alice-in-us.txt'
im = assembler.assemble(_file, 1024, 1024, HEPTA, theme="ToweringOver")

im.show()
im.save("first.png")