# -*- coding: cp932 -*-

class Line:
    def __init(self,slp,x0,y0):
        self.slp = float(slp)
        self.x0 = x0
        self.yo = y0

# the y on the left or the right edge crossing with the turtle's locus

    def get_y(self,x):
        return self.slp*(x-self.x0)+self.yo

# the x on the uppert or the bottom edge crossing with the turtle's locus
    def get_x(self,y):
        return self.x0+(y-self.y0)/self.slp

    
