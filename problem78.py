def num(n):
    li = []
    for n in range(1,n+1):
        li.append(n)
    return li

def f(x): 
	coins= num(x)
	dp=[0 for i in range(x+1)]
	dp[0]=1
	for coin in coins:
		for cost in range(1,x+1):
			if cost-coin>=0:
				dp[cost]+=dp[cost-coin]
	return dp[-1]
n =10
while True:
    
    if f(n) %1000000 ==0:
        print(f(n),n) 
        break
    n +=1


    