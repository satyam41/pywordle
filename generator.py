from PIL import Image, ImageDraw, ImageFont, ImageStat
import random
import spiral
import color

def generate(l, xsize, ysize, font_location, fntsize, theme):

    try:
        im = Image.new('L', (xsize, ysize), 0).convert('RGB')
        m = 0
        n = len(l)
        n1 = 0

        for i in l:
            k = [-1, 1]
            dir = k[random.randrange(0, 2)]

            _draw = ImageDraw.Draw(im)
            fnt = ImageFont.truetype(font_location, size=round((i[1] * (xsize/2) * fntsize)))
            _size = _draw.textsize(i[0], font=fnt)
            
            width, height = _size

            ranpos = (random.randrange((xsize/4), ((xsize/4) * 3) - width), random.randrange(ysize/4, ((ysize/4) * 3) - height))
            xpos, ypos = ranpos
            point = spiral.Point(xpos, ypos)

            rancol = color.frompallete(theme)

            if(getbox(point, _size, im.convert('L'))):
                n1 += 1
                _draw.text(point.getcoor(), i[0], fill=rancol, font=fnt)
            else:
                while(True):
                    point.move_spiral(0.005 * dir, a=0.05*dir, b=0.05)
                    if(point.getcoor()[0] < 0 or point.getcoor()[0] > xsize - width or point.getcoor()[1] < 0 or point.getcoor()[1] > ysize - height):
                        newpoint = spiral.Point(random.randrange((xsize/4), ((xsize/4) * 3) - width), random.randrange(ysize/4, ((ysize/4) * 3) - height))
                        point = newpoint
                    free = getbox(point, _size, im.convert('L'))
                    if(free):
                        _draw.text(point.getcoor(), i[0], fill=rancol, font=fnt)
                        n1 += 1
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

        return im
    
    except:
        print("Word sizes are too large, try reducing the size factor when calling assemble.")

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