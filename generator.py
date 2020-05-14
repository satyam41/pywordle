from PIL import Image, ImageDraw, ImageFont, ImageStat
import random
import spiral
import color
import time

def generate(l, xsize, ysize, font_location, fntsize, theme, condense):

    try:

        im = Image.new('L', (xsize, ysize), 0).convert('RGB')

        if(len(l) > 10):
            _drau = ImageDraw.Draw(im)
            fntu = ImageFont.truetype(font_location, size=round(l[0][1] * fntsize))
            _sizu = _drau.textsize(l[0][0], font=fntu)

            im = Image.new('L', (2*(xsize + _sizu[0]), 2*(ysize + _sizu[0])), 0).convert('RGB')

        m = 0
        n = len(l)
        n1 = 0
        terminate = False
        mazdoo = 60

        for i in l:
            k = [-1, 1]
            dir = k[random.randrange(0, 2)]

            _draw = ImageDraw.Draw(im)

            factor = 1
            d_fontar = round(i[1] * fntsize * factor)

            fnt = ImageFont.truetype(font_location, size=d_fontar)

            _size = _draw.textsize(i[0], font=fnt)
            
            if(_size[0] > im.size[0] or _size[1] > im.size[1]):

                if(len(l) < 1000):
                    fnt = ImageFont.truetype(font_location, size=round(100))
                    factor = 0.001
                    _size = _draw.textsize(i[0], font=fnt)
                else:
                    continue

            width, height = _size
            
            ranpos = (random.randrange(0, round(im.size[0]-width)), random.randrange(0, round(im.size[1]-height)))
            if(condense):
                try:
                    ranpos = (random.randrange(round(im.size[0]/4), round(((im.size[0]/4) * 3) - width)), random.randrange(round(im.size[1]/4), round(((im.size[1]/4) * 3) - height)))
                except:
                    ranpos = (random.randrange(0, round(im.size[0]-width)), random.randrange(0, round(im.size[1]-height)))

            xpos, ypos = ranpos
            point = spiral.Point(xpos, ypos)

            rancol = color.frompallete(theme)

            if(getbox(point, _size, im.convert('L'))):
                n1 += 1
                _draw.text(point.getcoor(), i[0], fill=rancol, font=fnt)
            else:
                t = time.time()
                while(True):
                    point.move_spiral(0.005 * dir, a=0.05*dir, b=0.05)
                    if(point.getcoor()[0] < 0 or point.getcoor()[0] > im.size[0] - width or point.getcoor()[1] < 0 or point.getcoor()[1] > im.size[1] - height):
                        newpoint = spiral.Point(random.randrange(0, round(im.size[0]-width)), random.randrange(0, round(im.size[1]-height)))
                        point = newpoint
                    free = getbox(point, _size, im.convert('L'))
                    if(free):
                        _draw.text(point.getcoor(), i[0], fill=rancol, font=fnt)
                        n1 += 1
                        break
                    if(time.time() - t >= mazdoo):
                        terminate = True
                        break
            
            if(terminate):
                mazdoo = 30
                perc_done = 0
                m = 0
                n1 = 0
                break

            perc_done = (n1/n) * 100
            round_perc = round(perc_done, 2)
            print(round_perc, '%', 'complete.')

            if(random.randrange(0, 2) == 0):
                im = im.rotate(90)
                m += 90

                if(m >= 180):
                    im = im.rotate(-180)
                    m = 0

        if(terminate):
            return 'terminate'

        return im
        
    except:
        print("Word sizes are too large, try decresing the desizing factor and tweaking variance factor.")
        return 'terminate'

def getbox (point, size, image):
    x, y = size
    box = (point.x, point.y, (point.x + x), (point.y + y))
    txtregion = image.crop(box)

    stats = ImageStat.Stat(txtregion)
    alpha = stats.extrema[0]

    if((point.x < 0) or (point.x > (4096 - x)) or (point.y < 0) or (point.y > (4096 - y))):
        return False

    if(alpha[1] == 0):
        return True
    
    return False