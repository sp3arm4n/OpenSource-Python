import math

def pathlength(x,y):
    L = 0
    for k in range(len(x) - 1):
        L += math.sqrt((x[k + 1] - x[k])**2 + (y[k + 1] - y[k])**2)
    return L

if __name__ == "__main__":
    x = [1,2,1,1,]; y=[1,1,2,1]
    print(pathlength(x,y))