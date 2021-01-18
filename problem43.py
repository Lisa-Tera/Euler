#소수로 나누어 지는게 가능해야함
import numpy as np

def penDigit(n):
    st_li= list(map(int, str(n)))
    st_li.sort()
    li=[0,1,2,3,4,5,6,7,8,9]
    return np.array_equal(st_li,li)

def pen2(n):
    st_li= list(map(int, str(n)))
    st_li.sort()
    li=[0,1,2,3,4,5,6,7,8,9]
    for i in st_li:   
        li.remove(i)
    return li
def pen(n):
    s_n = list(set(list(str(n))))
    if len(s_n) == len(str(n))  : return True
    return False
        
'''
inum =1406357289

prime_Li=[2,3,5,7,11,13,17]

sum,sli=0,[]
d6_10=[952867,357289]
d1_4 =[0134, 0146]
while inum < 9876543211:
    st = str(inum)
    d4,d6 = int(st[3]),int(st[5])
    if d4 % 2 ==0 and d6 == 5:
        if penDigit(inum):
            for x in range (len(prime_Li)):           
                s = int(st[x+1:x+4]) 
                if s % prime_Li[x] !=0 :   break
                if x == 6: 
                    sum+= inum
                    sli.append(inum)
    inum+=1
'''
'''
d4에 0,2,4,6,8   d6은 5 
d6이 0이면 d678 성립X 011,022.. d6 ==5여야함  
6789
5 065 x ,5 17 x ,5 286 o ,5 390 o, 5 611 x, 5 728 o ,5 832 o ,5 94 x
867 901 28 323x
'''
n11,n13,n17 = [],[],[] # 13*i< 100  %11 성립
for i in range(8):
    n =506 +11*i
    if pen(n):
        n13.append(n-500)
        n11.append(n)

d9,d10=[],[]

for j in n13:
    for i in range(10):
        a = j*10+i
        b = int(j%10)*10+i
        if a %13 ==0 and pen(a+5000):
            d9.append(5000+a)
            n17.append(b)
left=[]            
for j in range(len(n17)):
    for i in range(10):
        a = n17[j]*10+i
        b = d9[j]*10+i
        if a %17 ==0 and pen(b):
            d10.append(b)
            left.append(pen2(b))

            
        
            
            



'''
sum =0
li =[]
d4=['30952867','60357289','06357289']

d3 =[14,41]
for i in d4:
    for j in d3:
        a=int(str(j)+i)
        sum+= a
        li.append(a)
        '''
