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
def pow234(primes,two,three,four): 
    a,s,dic =0 ,0,{}
    
    for x in range(two):
        for y in range(three):
            for z in range(four):
                a = primes[x]**2 +primes[y]**3 +primes[z]**4
                if a < n : 
                    s += 1
                    dic[a] = (str(primes[x])+"**2 +"+str(primes[y])+"**3 +"+str(primes[z])+"**4")
    return len(dic)
        
        
# n = x**2  +y**3 +z**4
n = 50000000                
tt,t,f = int(n ** (1/2)),len(GetPrimes(int(n ** (1/3)))), len(GetPrimes(int(n ** (1/4))))
prime = GetPrimes(tt)
q = pow234(prime,len(prime),t,f)                