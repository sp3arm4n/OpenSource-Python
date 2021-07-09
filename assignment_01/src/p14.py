def C2F(degree):
    return degree * 1.8 + 32.0

def F2C(degree):
    return (degree - 32.0) / 1.8

def C2K(degree):
    return degree + 273.15

def K2C(degree):
    return degree - 273.15

def F2K(degree):
    return C2K(F2C(degree))

def K2F(degree):
    return C2F(K2C(degree))