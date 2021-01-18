def prime_num(n):
    for i in range(2,n):
        if n % i == 0 :
            return 0
    return 1

prime = []
for i in range(2,1000):
    if prime_num(i): 
        prime.append(i)
prime.sort()

def pp(n):
    for x in range(len(prime)):
        
        if n % prime[x] ==0 : 
            n_x = n / prime[x]
            for a in range(15):
               if n_x / prime[x] ==int(n_x / prime[x]):n_x =n_x / prime[x] 
               else:break
            if n_x==1:break
        
            for y in range(x+1,len(prime)):
                if n_x % prime[y] ==0 : 
                    n_y = n_x / prime[y]
                    for a in range(15):
                        if n_y / prime[y] ==int(n_y / prime[y]):n_y =n_y / prime[y] 
                        
                        else:break
                    if n_y==1:break
                    for v in range(y+1,len(prime)):
                
                        if n_y % prime[v] ==0 : 
                            n_v = n_y / prime[v]
                            for a in range(15):
                                if n_v / prime[v] ==int(n_v / prime[v]):n_v =n_v / prime[v] 
                        
                                else:break
                            if n_v==1:break
        
                
            
                            for z in range(v+1,len(prime)):
                                n_z = n_v / prime[z]
                                if n_z == 1:return 1
                            
s = 2*3*7*5                
for n in range(s,150000):
    if pp(n) and pp(n+1) and pp(n+2) and pp(n+3):
        print(n,n+1,n+2,n+3)
        break