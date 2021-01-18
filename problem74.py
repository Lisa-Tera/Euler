#1/6/9 → 3/6/3/6/0/1 → 1/4/5/4 → 1/6/9


dic ={'0':1}
for i in range(1,10):
    dic[str(i)] = dic[str(i-1)]*i

        
def sol(n):
    total=0
    li2 = [n]
    while True:
        li = list(str(n))
        s=0
        for i in li:
            s+= dic[i]
        if s == n : return total
        total+=1    
        if s in li2:return total
        li2.append(s)
        n =s
    
    
    

s = 0
num = 1000000
while num >1000:
    num-=1
    a = sol(num)
    if a == 60:
        s+=1
        

    