from p14 import *
import sys

s = sys.argv[1]
n = len(s)
num = float(s[0:n - 1])

if(s[-1] == 'C'):
    print("%fF, %fK"%(C2F(num), C2K(num)))

elif(s[-1] == 'F'):
    print("%fC, %fK"%(F2C(num), F2K(num)))

elif(s[-1] == 'F'):
    print("%fC, %fF"%(K2C(num), K2F(num)))

else:
    print("please C, F, K")