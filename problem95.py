#n의 자신을 제외한 약수를 반복해서 자기자신이 되는 것 = 친화고리
#1백만 이하의 수로만 이루어진 친화고리 중  가장 긴 고리의 가장 작은 수
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

prime = GetPrimes(1000000)

def sol(n):
    su,li =0,[]
    #for i in prime:
    for i in range(1,n):
        if n%i ==0:
            su +=i
            li.append(i)
    return (su,li)
            
dic,d ={},{}
for i in range(2,100):
    if i not in prime:
        a =sol(i)
        d[i] =a
        if a[0] not in prime:
            dic[i] = a[0]

di={}
for k in dic.keys():
    di[k] = []
    if dic[k] in dic.keys():
        di[k] += dic[k]
        
        
        
        

    