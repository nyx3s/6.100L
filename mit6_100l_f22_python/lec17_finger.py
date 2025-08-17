import math


class Circle():
    def __init__(self, radius):
        """ Initializes self with radius """
        # your code here
        self.radius = radius

    def get_radius(self):
        """ Returns the radius of self """
        # your code here
        return self.radius

    def set_radius(self, radius):
        """ radius is a number
        Changes the radius of self to radius """
        # your code here
        self.radius = radius

    def get_area(self):
        """ Returns the area of self using pi = 3.14 """
        # your code here
        return math.pi * (self.radius)**2

    def equal(self, c):
        """ c is a Circle object
        Returns True if self and c have the same radius value """
        # your code here
        return self.radius == c.radius

    def bigger(self, c):
        """ c is a Circle object
        Returns self or c, the Circle object with the bigger radius """
        # your code here

        if self.radius > c.radius:
            return self
        else:
            return c
    def __str__(self):
        return "Circle: "+str(self.get_radius())

c1 = Circle(5)
c2 = Circle(20)

print(c1.get_area())
print(c1.equal(c2))
print(c1.bigger(c2))
print(c1)
