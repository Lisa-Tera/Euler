def prime_num(n): #소수 만드는 함수
    for i in range(2,n):
        if n % i == 0 :
            return 0
    return 1
'''
prime = [] #소수 2,3,5

for i in range(2,100):
    if prime_num(i): 
        prime.append(i)
s1,s2,s3 ={},{},{}#s1 =  2,2+3,2+3+5....   
a=0        
for j in range(len(prime)):  
    a +=prime[j]
    s1[prime[j]] = a
    if j < 9:s2[prime[j+1]] = 0 - a
'''
s1,s2,s3 ={},{},{}
prime={}
qq=0
for i in range(2,4000):
    if prime_num(i):
        qq+=1
        prime[i] =qq
        s3[qq] =0


a=0        
for j in prime.keys():  
    a += j
    s1[j] = a
    s2[j] = j- a

pp=[]
#print(s1[11] +s2[3],3+5+7+11,s1[17]+s2[5],5+7+11+13+17)
for key1 in s1.keys():
    for key2 in s2.keys():
        if key1 == 2: continue
        if key1 > key2: 
            if prime_num(s1[key1]+s2[key2]) and s1[key1]+s2[key2] <1000000 and 100000<s1[key1]+s2[key2]:
                s3[prime[key1]-prime[key2]] = s1[key1]+s2[key2]
                pp.append((prime[key1]-prime[key2], s1[key1]+s2[key2]))
                
                #aaa.append(prime[key1]-prime[key2])
pp.sort()
print(pp[-1])