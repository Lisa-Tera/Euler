li = open('t18.txt', 'r').read().split('\n')
ali=[]


for i in range(len(li)):    
    li[i] = list(map(int,li[i].split(' ')))
   
dic={}
for i in range(len(li)-1,0,-1):
    for j in range(len(li[i])):
        a = max(li[i])
        if li[i][j] ==a :
            m =li[i][j]
            ali.append([i,j,m])
            dic[i]= [j,m]
            

#for i in range(14,0,-1):
    
        
    
        

    
'''
    for j in range(len(li[i])):
        m = max(li[i]) 
        if li[i][j] ==m :
            if i >0 and 
            ali[i]=([i,j,m])
            
'''       
        
    
    
    
    
