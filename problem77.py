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

def f(x): 
	coins= GetPrimes(x)
	dp=[0 for i in range(x+1)]
	dp[0]=1
	for coin in coins:
		for cost in range(1,x+1):
			if cost-coin>=0:
				dp[cost]+=dp[cost-coin]
	return dp[-1]
n =10
while True:
    
    if f(n) >5000:
        print(f(n),n) 
        break
    n +=1


    