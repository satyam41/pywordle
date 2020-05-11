import generator
from PIL import Image

def custom_sort(t):
    return t[1]

def assemble(datafile, w, h, font, min_freq=1):
    l = []
    datalist = []
    data = {}
    datacent = {}
    chars_to_ignore = ['.', ',', ';', ':']
    words_to_ignore = ['the', 'of', 'and', 'to', 'for', 'of', 'For']
    #'the', 'of', 'and', 'to', 'for', 'of', 'For'
    with open(datafile, 'r') as f:
        checkNone = False
        while(True):
            word = ''
            while(True):
                a = f.read(1)
                if(a in chars_to_ignore):
                    continue
                if(a == ' ' or a == '\n'):
                    break
                if(a == ''):
                    checkNone = True
                    break
                word += a
            if(word not in words_to_ignore):
                l.append(word)
            if(checkNone):
                break  

    for i in l:
        k = list(data.keys())
        if(i in k):
            data[i] += 1
        else:
            data[i] = 1

    n = len(l)

    for i in data:
        if(data[i] > min_freq):
            datacent[i] = round(((data[i]/n) + (1/data[i])/350), 5)

    keys = list(datacent.keys())

    for j in keys:
        datalist.append((j, datacent[j]))

    datalist.sort(key=custom_sort, reverse=True)

    im = generator.generate(datalist, w, h, font)

    return im