import copy
#1/x +1/y = 1/n
# 1/(n+a) +1/(n+b) = 1/n
# 2n+a+b :(n+a)(n+b) = 1:n
#n**2 = ab
# 약수 구하기 n -> 소인수 분해  x**m * y**n  => (m+1)*(n+1)
#n**2이므로 지수부분 ex)m,n **2 해줘야함
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
primes =GetPrimes(30)
#조건  x,y쌍이 1000개를 넘어야됨
s = 1
for p in primes:
    s *= p

limit = 1000000
d1,d2 ={},{}
for n in range(2,limit):#,2,-1):
    i = copy.deepcopy(n)
    dic={}
    s =1
    for p in primes:
        if i == 1: break
        while (i% p ==0):
            i = i //p                
            try: dic[p] += 1                            
            except: dic[p]=1
    for v in dic.values():
        if v == 1:
            s *=(v+2)
        elif v>1:
            s *= v*2+1
    d2[n] = (s+1)/2 # 공통인 부분이 생기므로 ex)n=4 |(1,4) (2,2) (4,1)|
    d1[n] = dic
    if d2[n] > 1000:
        print(n)
        break

         
                
                





