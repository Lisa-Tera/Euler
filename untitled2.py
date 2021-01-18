#맨 왼쪽의 아무열에서 출발하여 맨 오른쪽 위에 열까지 숫자의 합이 가장 작은 경우는? 위/아래/오른쪽 [0][1]/[0][-1]/[1][0]
#시작점은 a[0][0],a[1][0],a[2][0],a[3][0],a[4][0] 중에 하나임
''' ex  
a[0][0] -> a[0][1] or a[1][0] 
a[1][0] -> a[1][1] or a[2][0] or a[0][0]
a[2][0] -> a[2][1] or a[3][0] or a[1][0]
a[3][0] -> a[3][1] or a[4][0] or a[2][0]
a[4][0] -> a[4][1] or a[3][0] 



a= [131,673,234,103,18,
    201,96 ,342,965,150,
    630,803,746,422,111,
    537,699,497,121,956,
    805,732,524,37,331]'''

    
    
    
n =80#5
    
lf = open('t.txt', 'r').read().split('\n')
b =[]

for i in range(len(lf)):
    
    a =lf[i].split(',')
    a= list(map(int, a))
    b.append(a)
    '''
    dic2={}
    for j in range(n):
        dic2[a[j]] =((i,j))
    dic[i] = dic2'''
    

a.clear()
dic2.clear()

i,j,s =0,0,0
li=[]
solli =[]

while True:
    if i ==0 and j ==(n-1):#79
    
        solli.append(s)
        li =[]
        i +=len(solli)
        j,s=0,0
        li.append([i,j])
        solli.append((li,s))
    if len(solli) == n:#5:
        mimi = min(solli)
        break    
        
    li.append([i,j])
    s +=b[i][j]
    if i ==0 :
        if j ==(n-1) : break #4
        sol = min(b[i+1][j],b[i][j+1]) # 0,0 ->0,1 
        
    elif i ==(n-1) :
        sol = min(b[i-1][j],b[i][j+1])
    else:
        sol = min(b[i+1][j],b[i-1][j],b[i][j+1])
        if j ==(n-1) and i !=0: #j==4
            for x in range(i+1,n):
                b[i][j] +=b[x][n-1]#4
                
    if sol == b[i][j+1]:
        j +=1
    else :            
        if sol == b[i+1][j]: 
            i+=1
            if [i,j] in li:
                i-=1
                if b[i-1][j] < b[i][j+1]:
                    i -=1
                else :j+=1
        else :
            i-=1
            if [i,j] in li:
                i+=1 
                
                if b[i+1][j] < b[i][j+1] and i >1:
                    i+=1
                else: j+=1
            '''
            li.append([i,j])
            s +=b[i][j]
            sol = min(b[i-1][j],b[i][j+1]) # i값이 바뀜 ->
            if sol == b[i][j+1]:j+=1
            else: i-=1'''

            
            
            
        #i,j=dic[i][sol][0],dic[i][sol][1] 
        
'''        
error why? 위/아래로 가는거 아래로 내려갔다가 다시 위로 올라옴 nono  막아놔야 됨      
  00  ->  10 11 12 > 01 이거 막아놔야됨    
  dic에다가 넣으면 a = [0: j0,j1 1:j2,j3]    if 0: j0~3 <a : dic[0] = j0,j1,j2,j3 and dic[1]
  
'''
  
  
  
  
  
  
  
  
  
  
      