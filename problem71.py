
# GCD(n,d) = 1 -> 2/4 no  so, d%n !=0
# d<= 1000000

from fractions import Fraction

a = 3/7 #0.42857142857142855
a1 = str(a)[:8]
dic = {3/7:'3/7'}
li =[3/7]

for d in range (1000000,999950,-1):
#for d in range(10,2,-1):
    for n in range(int(d/2),int(d/3),-1):
        x =str(Fraction(n,d))  
        x1 =str(n)+'/'+str(d) # x == x1 이 성립하면 약분 불가
        dd = round(n/d,10) # e로 나와서 바꿔야함
        xst = str(dd)[:8] #위에 a1하고 맞춰야함
        
        if a1 == xst and x==x1 :
            dic[n/d] = x
            li.append(n/d)
        if dd <a: break
        
li.sort()
for i in range(len(li)):
    if li[i] == a:
        print(dic[li[i-1]])
        
       


