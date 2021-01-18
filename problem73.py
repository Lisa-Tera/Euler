#d ≤ 12,000일 때 1/3과 1/2 사이의 기약 진분수
from fractions import Fraction

o1 = 1/3
o2 = 1/2
chd= 12

s=0
dic={}
for d in range(3,12001):
    d1,d2 =int(d/3)+1,int(d/2)+1
    for n in range(d1,d2):
        if d%n !=0:
            x =str(Fraction(n,d))
            x1 =str(n)+'/'+str(d)
            if x == x1:
                s+=1
                dic[n/d] = x
                
