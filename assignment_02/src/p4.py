import math

class Sphere():
    def __init__(self, r):
        self.r = r
        self.v = 0
        self.s = 0

    def volume(self):
        self.v = (4.0 / 3.0) * math.pi * (self.r ** 3)
        return self.s

    def surface(self):
        self.s = 4.0 * math.pi * (self.r ** 2)
        return self.s

class Cylinder():
    def __init__(self, r, h):
        self.r = r
        self.h = h
        self.v = 0
        self.s = 0

    def volume(self):
        self.v = math.pi * (self.r ** 2) * self.h
        return self.v

    def surface(self):
        self.s = 2.0 * math.pi * self.r * (self.r + self.h)
        return self.s

class Cone():
    def __init__(self, r, h):
        self.r = r
        self.h = h
        self.v = 0
        self.s = 0

    def volume(self):
        self.v = (1.0 / 3.0) * math.pi * (self.r ** 2) * self.h
        return self.v

    def surface(self):
        self.s = math.pi * self.r * (self.r + math.sqrt((self.r ** 2) + (self.h ** 2)))
        return self.s

if __name__ == '__main__':
    sphere = Sphere(2)
    cylinder = Cylinder(2, 3)
    cone = Cone(2, 3)
    print('Sphere Volume', sphere.volume())
    print('Sphere Surface', sphere.surface())
    print('Cylinder Volume', cylinder.volume())
    print('Cylinder Surface', cylinder.surface())
    print('Cone Volume', cone.volume())
    print('Cone Surface', cone.surface())