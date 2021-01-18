li = open('triangle.txt', 'r').read().split('\n')
ali=[]

max_d={}
for i in range(len(li)):    
    li[i] = list(map(int,li[i].split(' ')))
    m = max(li[i])
    for j in range(len(li[i])):
        if li[i][j] == m:
            max_d[i] = [j,m]
        else 
        
    
   

for i in range(len(li)):
    dic={}
    for j in range(len(li[i])):
        dic[j] = li[i][j]
    
    ali.append(dic)        
'''
dd={}
def f(x):
    return od[x]
def f2(x):
    return od2[x]

for i in range(14,0,-1): # 14 번째 dic부터 시작
    for j in ali[i].keys():
        if j >0 and j <14 :
            od={j-1:ali[i-1][j-1] ,j:ali[i-1][j] ,j+1:ali[i-1][j+1] }
            mk = max(od.keys(),key=f)
            od2={mk-1:ali[i-2][mk-1] ,mk:ali[i-2][mk], mk+1:ali[i-2][mk+1]}
            mk2 = max(od2.keys(),key=f2)
            mv,mv2 = od[mk],od2[mk2]
            dd[str(j+mk+mk2)] = ali[i][j] + mv+mv2'''
            

            
        

        
        
    
 






           