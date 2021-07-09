from p12 import *
import math

x = []
y = []

for k in range(2, 11):
    N = 2 * k
    for i in range(N + 1):
        x.append(1/2 * math.cos(2 * math.pi * i/N))
        y.append(1/2 * math.sin(2 * math.pi * i/N))
    print("N: %d|Pathlength: %d "%(N,pathlength(x,y)))
    x.clear()
    y.clear()