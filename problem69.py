#소인수 일 경우 p가 가장 크고 아닌 경우 p가 작으므로 소인수가 아닐경우일 수록 커짐


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

prime=GetPrimes(100)        
p=1
li=[]
for i in prime:
    p *=i
    if p<1000000:
        li.append(p)

print(max(li))
    


        
        
'''
def get_divisor(num):
    divisors = []
    
    for i in range(2,num+1):
        
        if num % i == 0:
            divisors.append(i)
            
        else:
            d2.append(i)
    divisors.remove(1)
    for i in divisors:
        for j in range(2,int(num/2)):
            if i*j < num:
                divisors.append(i*j)
                #d2.remove(i*j)
            
    
    
    p = num/(num-len(set(divisors)))
    return p 
    
dic={}
for i in range(2,1000000):
    a=get_divisor(i)
    if a>2:dic[i]= a
for k in dic.keys():
    if dic[k] ==max(dic.values):
        print(k)

'''
