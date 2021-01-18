'''
 나선형 ㅁ 1 9 25 49  -> 1 3 5 7 9
 대각선을 구해야 됨
 3 - 3 5 7 9
 5 - 13 17 21 25
 7 - 31 37 43 49

'''
def Gets(n):
    Seeds = []
    if n<11:
        Seeds=[2,3,5,7]
    else:
        Seeds=Gets(int(n**0.5)+1)

    s=[1 for _ in range(n)]
    for i in Seeds:
        for j in range(2, int(n/i)+1):
            s[i*j-1]=0
    
    result=[]
    for i in range(2, n+1):
        if s[i-1]==1:
            result.append(i)
    return result

def Prime():      
    dic={}
    for i in range(3,25000,2):
        a = Gets(i**2)
        for j in (Gets((i-2)**2)):
            a.remove(j)
        dic[i**2] = a
    return dic

a = Prime()

fo={}
to={}
t=1
for i in range(3,25000,2):
    n = i**2
    li=[]
    for j in range(1,4):
        li.append(n - j*(i-1))
    fo[n] =li
    t+=4
    to[n] = t

s =0
for i in a.keys():
    for aa in a[i]:
        for bb in fo[i]:
            if aa == bb:
                s+=1
    v = s/(to[i])
    if v <0.1:
        print(i)
        break

        
        

'''
prime = Gets(25000)

di =Prime()


'''

'''
def prime(n):
    
    

def sol(n,s):
    n2= n**2
    for i in range(1,4):
        a = n2 - i*(n-1)
        if a %2 !=0 and (prime(a)):s+=1
    return s

s,t=0,1
for i in range(3,25000,2):
    s = sol(i,s)
    t+=4        
    b = round(s/t,3)
    if b <0.1 :
        print(i)
        break
'''          
            