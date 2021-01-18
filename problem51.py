# 6개의 소수   7개의 소수   8개의 소수는? 교차도 성립하고 틀도 성립해야됨 (00~99 이상으로 바꿔도 성립해야됨) 
#    *3         56**3        
#일단 리스트를 자릿 수 대로 쪼개자 
import copy

#value로 키 찾기
def find_key(dict, val):
    return next(key for key, value in dict.items() if value == val)

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

limit=1000000

p =GetPrimes(limit) #소수인 리스트 생성
p = p[9592:]


#일단 7개인 경우를 구해보자

# 2개의 숫자를 제거 하고 틀이 맞는지 확인해보자 
#깊은 복사 b = copy.deepcopy(a)


for i in range(2,6):        
    for j in range(1,i):            
        for z in range(j):
            l1,c=[],{}
            for s in p:
                b = copy.deepcopy(str(s))
                if  b[i] ==b[j]:
                    b = list(b)
                    q = b[i]
                    del b[i]
                    del b[j]
                    if q== b[z] : del b[z]
                    
                    b = str(b)
                    #l1.append(b)                        
                    try: c[b] += 1                         
                    except: c[b]=1
                    if c[b] == 8 :                            
                        print(s,b)
                        break
                        
            
    
            
'''
for i in p:
    a = str(i) # 1:3 2:4 3:
    #if b[0]+b[2]+b[4] in li : l1.append(b[1]+b[3]+b[5])
    b = copy.deepcopy(a)
    al = b[1]+b[5]
    if b[0]+b[2] in li : l1.append(b[1]+b[3]+b[4]+b[5])
    if b[2]+b[4] in li : l2.append(b[0]+b[1]+b[3]+b[5])
    if b[0]+b[4] in li : l3.append(b[1]+b[2]+b[3]+b[5])
    if b[3]+b[5] in li : l4.append(b[0]+b[1]+b[2]+b[4])
    
    if b[1:3] in li : l1.append(int(b[0]+b[3:] ))
    if b[2:4] in li : l2.append(int(b[:2]+b[4:6]))
    if b[3:5] in li : l3.append(int(b[:3]+b[5]))
    if b[4:] in li : l4.append(int(b[:4]))
    
c1,c2,c3,c4 = {},{},{},{}   
for i in l1:
    try: c1[i] += 1
    except: c1[i]=1    
for i in l2:
    try: c2[i] += 1
    except: c2[i]=1
for i in l3:
    try: c3[i] += 1
    except: c3[i]=1
for i in l4:
    try: c4[i] += 1
    except: c4[i]=1

print(find_key(c1, 8))
print(find_key(c2, 8))
print(find_key(c3, 8))
print(find_key(c4, 8))
'''