import math

def sphere_volume(r):
    v = (4.0 / 3.0) * math.pi * (r ** 3)
    return v

def sphere_surface(r):
    s = 4.0 * math.pi * (r ** 2)
    return s

def cylinder_volume(r, h):
    v = math.pi * (r ** 2) * h
    return v

def cylinder_surface(r, h):
    s = 2.0 * math.pi * r * (r + h)
    return s

def cone_volume(r, h):
    v = (1.0 / 3.0) * math.pi * (r ** 2) * h
    return v

def cone_surface(r, h):
    s = math.pi * r * (r + math.sqrt((r ** 2) + (h ** 2)))
    return s

if __name__ == '__main__':
    print('Sphere Volume', sphere_volume(2))
    print('Sphere Surface', sphere_surface(2))
    print('Cylinder Volume', cylinder_volume(2, 3))
    print('Cylinder Surface', cylinder_surface(2, 3))
    print('Cone Volume', cone_volume(2, 3))
    print('Cone Surface', cone_surface(2, 3))