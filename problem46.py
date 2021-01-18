def prime_num(n):
    for i in range(2,n):
        if n % i == 0 :
            return 0
    return 1

prime = []
odd_comp =[]
for i in range(2,10000):
    if prime_num(i):
        prime.append(i)
    else :
        if i % 2 ==1:    odd_comp.append(i)
li ={}

for x in range(len(odd_comp)):
    for j in range(len(prime)):
        for n in range(1,100):
            if odd_comp[x] == prime[j]+2*(n**2):
                li[odd_comp[x]] = (str(prime[j])+'+2*'+str(n**2))
                continue
                
    if li[odd_comp[x]] == None:
        print(odd_comp[x])
        break


for n in range(30,1000):
    if pp(n) and pp(n+1) and pp(n+2):
        print(n,n+1,n+2)
        break
        