import numpy as np

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = np.sqrt((x*x) + (y*y))
        self.angle = np.arctan2(y, x)

    def move_spiral(self, theta, a=1, b=1):
        self.r += self.get_r(theta, a, b)
        self.angle += theta

        self.x = self.r*np.cos(self.angle)
        self.y = self.r*np.sin(self.angle)
        
    def get_r(self, theta, a, b):
        return a + (b * theta)

    def getcoor(self):
        coor = (self.x, self.y)
        return coor