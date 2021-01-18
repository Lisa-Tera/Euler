'''
sum =0
for i in range(1,1001):
    sum +=i**i
s = str(sum)
print(s[-10:])
'''
       
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



limit=1000
primes=GetPrimes(limit)
dicNums={}
'''
for i in range(len(primes)):
    a=0
    print(i)
    for j in range(i, len(primes)-1):
         if a in primes:dicNums[a]=j-i+1

max=0
for key,val in dicNums.items():
    if max<val:print((str(key)+', '+str(val)))'''