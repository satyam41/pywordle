import generator
import numpy
from PIL import Image

def custom_sort(t):
    return t[1]

def check_variance(l):
    variance = numpy.var(l)
    return variance

def reduce_variance(l, factor):
    mean = sum(l)/len(l)
    for i in range(len(l)):
        l[i] = ((l[i] - mean)/factor) + mean
    return l

def assemble(datafile, w, h, font, desizing=9, variance_factor=8, min_freq=0, theme="White", condense=False, ignore=True):

    if(desizing < 8):
        desizing = 8
    
    if(variance_factor < 7):
        variance_factor = 7

    l = []
    datalist = []
    data = {}
    datacent = {}
    chars_to_ignore = ['.', ',', ';', ':', '[', ']', '(', ')', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    words_to_ignore = []
    if(ignore): words_to_ignore = ['The', 'the', 'of', 'and', 'to', 'for', 'of', 'For', 'Is', "is", 'it', 'or', 'Or', 'a', 'A', 'by', 'in', 'that', 'has', 'shall', 'an', 'as']
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

    if(len(l) == 0):
        l = ['Fuck']

    for i in l:
        k = list(data.keys())
        if(i in k):
            data[i] += 1
        else:
            data[i] = 1

    for i in data:
        if(data[i] > min_freq):
            datacent[i] = round((data[i]/len(data)), 5)

    keys = list(data.keys())
    values = list(data.values())
   
    values = reduce_variance(values, variance_factor)

    datalen = [len(x) for x in l]
    try:
        lsum = (w * w)/(sum(datalen) * desizing)

        for j in range(len(keys)):
            datalist.append((keys[j], values[j]))

        datalist.sort(key=custom_sort, reverse=True)

        im = generator.generate(datalist, w, h, font, lsum, theme, condense)

        print(len(l))

        return im
    
    except:
        print("no words bruh, type in some words to proceed.")
        return None