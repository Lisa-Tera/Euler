
def sum_divisor(num):
    s=0
    for i in range(1,num+1):
        if num %i ==0:
            s += i
    s -= num
    return s
            
ss=[]
s=0
for i in range(10000):
    a = sum_divisor(i) # i = 20 a =22 i =220 a = 284
    b = sum_divisor(a)# b = 1+2+11 =  a=284 b = 220
    if  i == b and a !=b and a<b:
        s= s+a+b
        ss.append((a,b,s))
        
        
        
        
        
        
'''
import math

def get_divisor(num):
    divisors=[]
    length = int(math.sqrt(num))+1
    
    for i in range(1,length):
        if num %i ==0:
            divisors.append(i)
            divisors.append(num//i)
    divisors.sort()
    del divisors[-1]
    return divisors
'''