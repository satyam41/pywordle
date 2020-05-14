import time

t = time.time()

while (True):
    if(time.time() - t >= 10):
        print(time.time() - t)
        break
