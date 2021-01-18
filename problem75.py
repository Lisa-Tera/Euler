'''
(m**2 - n**2)**2 + (2*m*n)**2 = (m**2 + n**2)**2
a = m**2 + n**2 
b = 2*m*n mn 20
c = m**2 - n**2 
m>n>0

da = d*a
db= d*b
dc = d*c
d = a,b,c의 최대 공약수
ex)12 cm: (3,4,5) -> d=1
   24 cm: (6,8,10) -> d=2

a+b+c = s = 2*m(m+n)*d
-> m < (s/2)**0.5

m <k <2m
m <k <s/2m
k = 홀수
'''

limit = 1500000
#limit= 120

li=set()
dic = {}
a =int(limit**0.5)
sums=0
for m in range(2,a):
    for n in range(1,m):
        if ((n+m)%2) ==1:
            a = m**2 + n**2
            b = 2*m*n
            c = m**2 - n**2
            s = a+b+c
        #if s == 120 : break
            if s == int(s) and s<1500000 and s%60 !=0:
                dic[s] = [a,b,c]

'''

limit = 80000
#limit= 120

dic={}
for b in range(2,600):
    for c in range(1,b):
        a2 = b**2+c**2
        a = a2**0.5
        s = a+b+c
        if a == int(a) and s <limit:
            
            if s in dic.keys():
                dic[int(s)]+= [a,b,c]
            else: dic[int(s)] = [a,b,c]
            
s=0
da={}

li=[]
for a in dic.keys():
    if len(dic[a]) !=3:
        if a%36 ==0:
            print(a)
        da[int(a)] = dic[a]
        li.append(a)


li2=set()
for i in li :
    for j in range(1,100):
        
        if i*j <1500000:
            li2.add(i*j)
li2 = list(li2)

       
        


            
            
            
            
            