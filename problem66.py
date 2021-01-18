#x**2 – D* y**2 = 1
#d는 제곱수면 불가함
import math 
li,li2=[],[]
q = 0

for y in range(1000,10000000000):
    for x in range(y,1000000000):
        for d in range(10,1000):
            d1 = math.sqrt(d)
            if d1 != int(d1):
                s = (x+d1*y)*(x-d1*y)
                if s >0.99999999999  and s <=1.0000000000001:
                    if x >q :
                        q=x
                    li.append([x,d,y])
'''
for d in range(1000,100):
    a =math.sqrt(d)
    if  a != int(a):
        #문제는 y를 대략 구해야 x룰 구할 수 있는데
        
            x**2 = d*y**2+1
            s1 = math.sqrt(s)
            if s1 == int(s1):
                li.append([s1,d])        
        
'''