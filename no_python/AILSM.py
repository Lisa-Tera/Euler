import numpy as np
import math

# x & y 값
x = [3,6,7,9,10,12,15,17,18,21]
y =[79, 82, 80, 85 ,84, 89, 93, 90 ,96,99]

mx = np.mean(x)
my = np.mean(y)

div = sum([(mx-i)**2 for i in x])
dividend = 0
for i in range(len(x)):
    dividend += (x[i]- mx)*(y[i] - my)
'''
def top(x,mx,y,my):
    d = 0
    for i in range(len(x)):
        d += (x[i]- mx)*(y[i] - my)
    return d
divide = top(x,mx,y,my)
'''
a = round(dividend/div,2)
b = round(my - (mx*a),2)
print("y =",a,"x+",b)