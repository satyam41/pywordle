import assembler
from PIL import Image

CATAMARAN = 'D:/UnityProjects/Version/Fonts/Fonts/12 After The Date/Catamaran/Catamaran-Black.ttf'
CINZEL = 'D:/UnityProjects/Version/Fonts/Fonts/12 After The Date/Cinzel/Cinzel-Regular.ttf'
QUESTRIAL = 'D:/UnityProjects/Version/Fonts/Fonts/Questrial/Questrial-Regular.ttf'
ZILLA = 'D:/UnityProjects/Version/Fonts/Fonts/Hepta_Slab,Zilla_Slab/Zilla_Slab/ZillaSlab-Bold.ttf'
HEPTA = 'D:/UnityProjects/Version/Fonts/Fonts/Hepta_Slab,Zilla_Slab/Hepta_Slab/static/HeptaSlab-Bold.ttf'

_file = 'declaration.txt'
im = assembler.assemble(_file, 1024, 1024, QUESTRIAL, min_freq=0)

im.show()
im.save("first.png")