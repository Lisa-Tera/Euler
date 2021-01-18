# 오각수 중에서 합and차 모두 오각수이면서 차가 가장 작은 경우
'''
nlist = []
for n in range(1000,2200):nlist.append(n*(3*n-1)/2)
mm=[]
final =[]
for x in range(len(nlist)):
    for y in range(x):            
        p = nlist[x]+nlist[y] 
        m = nlist[x]-nlist[y] 
        if p -m == 2*nlist[y]: mm.append(m)
for i in range(len(nlist)):
    for j in range(len(mm)):
        if nlist[i] ==mm[j]:
            final.append(mm[j])
            

            '''

            
       
i=1          
while True:
    i+=1
    n = i*(3*i-1)/2
    for j in range(i-1,0,-1):
        m= j*(3*j-1)/2
        a = ((24*(n-m)+1)**0.5+1)/6
        b = ((24*(n+m)+1)**0.5+1)/6
        if a ==int(a) and b == int(b):
            result = n-m
            break
            
print(result)   