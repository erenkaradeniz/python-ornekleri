# -*- coding: utf-8 -*-
#!/usr/bin/Python

"""
@author : Eren Karadeniz
"""

# operator overloading
# operator : +, *, /, **, -, >, ==, ...

class Nokta:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x,self.y)

    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Nokta(x,y)

nokta1 = Nokta(1,9)
nokta2 = Nokta(-5,6)

print(nokta1 + nokta2)


"""
__add__(self,other) +
__mul__(self, other) *
__sub__(self, other) -
__mod__(self, other) %
__truediv__(self, other)
__lt__(self, other) # less than
__pow__(self, other) *

https://docs.python.org/3/library/operator.html
"""