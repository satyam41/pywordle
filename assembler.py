import generator
from PIL import Image

def custom_sort(t):
    return t[1]

def assemble(datafile, w, h, font, s, min_freq=1):
    l = []
    datalist = []
    data = {}
    datacent = {}
    chars_to_ignore = ['.', ',', ';', ':', '[', ']', '(', ')', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    words_to_ignore = ['the', 'of', 'and', 'to', 'for', 'of', 'For', 'Is', "is", 'it', 'or', 'Or', 'a', 'A', 'by', 'in', 'that', 'has', 'shall', 'an', 'as']
    #'the', 'of', 'and', 'to', 'for', 'of', 'For', 'Is', "is", 'it', 'or', 'Or', 'a', 'A', 'by', 'in', 'that', 'has', 'shall', 'an', 'as'
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

    for i in data:
        if(data[i] > min_freq):
            datacent[i] = round(((data[i]/len(data)) + (1/data[i])/400), 5)

    keys = list(datacent.keys())

    for j in keys:
        datalist.append((j, datacent[j]))

    datalist.sort(key=custom_sort, reverse=True)

    im = generator.generate(datalist, w, h, font, s)

    return im