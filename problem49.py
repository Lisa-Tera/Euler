

def GetPrimes(n):
    primeSeeds = []
    if n<11:
        primeSeeds=[2,3,5,7]
    else:
        primeSeeds=GetPrimes(int(n**0.5)+1)

    primes=[1 for _ in range(n)]
    for i in primeSeeds:
        for j in range(2, int(n/i)+1):
            primes[i*j-1]=0
    result=[]
    for i in range(2, n+1):
        if primes[i-1]==1:
            result.append(i)
    return result

limit=9999
primes=GetPrimes(limit)
primes[:168] = []
prime=[]

ss,ss2=[],[]
a ={}
for i in range(len(primes)):
    s = list(str(primes[i]))
    for four in range(4):
        s[four] = int(s[four])
    s.sort()
    ss.append(s) 
    #ss.sort() #ss에 3개 이상 있어야됨
 
for j in range(len(primes)):
    if ss.count(ss[j]) >=3 : 
        a[primes[j]] = ss.count(ss[j])
        ss2.append(ss[j]) 
        prime.append(primes[j])
 
s_xy,s_yz=[],[]
for x in range(len(ss2)):
    for y in range(x+1,len(ss2)):
        for z in range(y+1,len(ss2)):
            if ss2[x] == ss2[y] and ss2[z] == ss2[y]:
                s=(prime[y] - prime[x])
                if prime[y]+s ==prime[z]:
                    print(prime[x],prime[y],prime[z])
            

'''    
ss2=[]
di = {}
for j in range(len(primes)-2):
    a,b,c = ss[j],ss[j+1],ss[j+2]
    if a==b and b==c:
        ss2.append(ss[j])
 
ss3 = list(set(map(tuple,ss2)))
ss3.sort()
#등차만 하면 됨...
for aa in range(len(ss3)):
    f=ss3[aa]
    ff = ss2.count(f)

'''