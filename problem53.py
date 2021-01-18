def factorial(n):
    
    if n==1 : return 1
    return factorial(n-1)*n

def ncr(n,r):
    c = factorial(n)/(factorial(r)*factorial(n-r))
    return c
a=[]    
for i in range(1,101):
    for j in range(1,i+1):
        if i>j :
            if ncr(i,j) > 1000000:            
                a.append([i,j, ncr(i,j)])
print(len(a))            