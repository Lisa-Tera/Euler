'''
a = [4,6,8,9]
li=[]
li2=[]
for i in a:
    for j in range(2,i):
        if i%j !=0:
            li.append([j,i, j/i])

n =1000000
s=0
primeSeeds =[2,3,5,7]

primes=[1 for _ in range(n)]
for i in primeSeeds:
    for j in range(2, int(n/i)+1):
        primes[i*j-1]=0
result=[]
for i in range(2, n+1):
    if primes[i-1]!=1:
        result.append(i)
        s+=(i-1)
'''
result = []
li =[]
dic ={}
primeSeeds =[2,3,5,7]
n =32
primes=[1 for _ in range(n)]
for i in primeSeeds:
    for j in range(2, int(n/i)+1):
        ii =i*j
        primes[ii-1]=0
        
        if primes[i-1] ==1 and primes[j-1]==1 and j>=i:
            dic[ii]= 0
            li.append(ii)
            if i != j and j>i:
                result.append([ii,i,j])
                dic[ii] = [i,j]
                
            else : 
                result.append([ii,i])
                dic[ii]=[i]
     
        else:
            if i in dic.keys():
                s = list(set(dic[i]+[j]))
            if j in dic.keys():
                s = list(set([i]+dic[j]))
            dic[ii] =s
               
        
li = list(set(li))
'''
        else:
            if j in li:
                for oj in result:
                    if j ==oj[0] :
                        se = list(set(oj[1:]+[i,ii]))
                        se.sort(reverse = True)   
                        result.append(se)
                    
                    

                
       


'''
          
'''  
            
li=[]
for d in result:
    s = 1
    for i in range(1,len(d)+1): # [4,2] i = 4 , 2   [6,3,2] i = 6 ,3 ,2
        s *=i
        li.append(s)
'''         