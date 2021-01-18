#34
'''
def f(n): 
    if n == 1: return 1
    if n == 0 : return 0
    return n*f(n-1)

sum =0 

i=100
while True:
    a = list(str(i))
    fun=0
    for x in range(len(a)):
        fun += f(int(a[x]))
        if fun == i :
            sum += i
            print(i)
            

            
    i = i+1
    if i >10000000:stop
            

#36

sum = 0 
def pal(n):
  s = str(n)
  return s == s[::-1]

for i in range (1,1000000):
    a = bin(i)[2:]
    if pal(i) == True and pal(a) == True:
        sum += i

#39
peri = 12
a,b,c
a+b+c=12
a+b >c 
a**2+b**2==c**
for i in range(peri):
    print(i)
    peri=+1


#40 yes
b= '1'
for i in range(2,1000000):
    b = b +str(i)

a = list(b)
#print(a[0],a[9],a[99],a[999],a[9999],a[99999],a[999999])
int(a[0])*int(a[9])*int(a[99])*int(a[999])*int(a[9999])*int(a[99999])*int(a[999999])




#44
p=[]
i=2000
a =[]
while True:
    five = i*(3*i-1)/2
    i+=1
    p.append(five)
    if i>4000 : break

for i in range(500):
    #for j in range(len(p)):
    for y in range(500):
        for x in range(1000):
            if p[x]+p[x+y] == p[x+y+i] :
                #print(p[x],p[x+y])
                a.append(p[x+y]-p[x])
a.sort()
for i in range(len(a)):
    for j in range(len(p)):
        if a[i] == p[j]: print(a[i])
         
        
    '''

#
prime =[]
so =2
so_1=[]
for num in range(2,10000):
    check =True
    for i in range(2,num):
        if num % i ==0:
            check=False
            break
    if check:
        prime.append(num)

for i in range(len(prime)):
    for j in range(len(prime)):
        if int(str(prime[i])+str(prime[j]))%so == 0 or int(str(prime[j])+str(prime[i]))%so ==0:
            print(so)
            if num == so : print(so,prime[i],prime[j])
            
        else : so +=1

        '''
num =2
so = 2

while True:
    
    if num %so ==0 : # ex) 4이면 다시 위로 올라와서 이 if문을 통과하므로 소인수로 분해됨
        num = num/ so
        print(so)
        
        
    else :
        so += 1
        
    if num == 1 : break #여기서 끝나게 되므로 변수를 하나 더 만듦
    f = num
    '''













