'''
 나선형 ㅁ 1 9 25 49  -> 1 3 5 7 9
 대각선을 구해야 됨
 3 - 3 5 7 9
 5 - 13 17 21 25
 7 - 31 37 43 49

'''

def prime(n):
    if n != 1:                 
        for f in range(2, n):  
            if n % f == 0:     
                return False
            
    else: return False  
            
    return True       
    
'''   
n=[[3,9],[5,25],[7,49]]
num = 7

#for i in range(2,49):
for j in n:
    for i in range(0,4):    
        a = j[1] - i*(j[0]-1)
        ali.append(a)
        if (prime(a)):
            pli.append(a)  
if int(len(pli)/len(ali))*100 <10 :
    print(num)
        
else : 
    num +=2
    for i in range(0,4):
        a = num**2 - i*(num-1)
        ali.append(a) 
        if (prime(a)):
            pli.append(a)  
'''
def sol(n):
    n2= n**2
    prime(n2)
    
    s=0
    for i in range(0,4):
        a= n2 - i*(n-1)
        if a% 2 !=0:
            if (prime(a)):s+=1
    return s
n = 1
tli=1
s=0
while True :
    n+=2
    s += sol(n)
    tli+=4        
    
    if (s/tli) <0.1 :
        print(n)
        break
            
            