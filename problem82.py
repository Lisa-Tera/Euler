
import copy

def sol(x): 
    return {'a': '1', 'b': '2'}[x]

#데이터 리스트로 넣음
f = open('matrix.txt','r')
data = f.readlines()
f.close()

l3 = []
for i in range(len(data)):
    #a =i.split(',')
    #d.append(a)
    for j in range(80): l3.append(str(i)+'`'+str(j))
        
    a = list(map(int,data[i].split(',')))
    data[i] = a
li,li3 =[],[]
for i in range(0,80):
    s,j=data[i][j],0
    li2 =[]
    l = copy.deepcopy(l3)
    while True:
        #3개의 숫자
                    
        if j == 79 :
            li.append(s)
            break
        a1 = data[i][j+1]
        a3 = data[i-1][j]+data[i-1][j+1]
        
        if i<79:
            a2 = data[i+1][j] + data[i+1][j+1]
            m = min(a1,a2,a3)
        else :
            m = min(a1,a3)
        if m==a3 and i==0 :
            m = min(a1,a2)
        
        if m == a1 and str(i)+'`'+str(j+1) in l: 
            l.remove(str(i)+'`'+str(j+1))
            j+=1
            li2.append(str(i)+'`'+str(j))
            s+= a1
            
        elif m == a2 and str(i+1)+'`'+str(j) in l: 
            l.remove(str(i+1)+'`'+str(j))
            li2.append(str(i+1)+'`'+str(j))
            i+=1
            j+=1
            li2.append(str(i)+'`'+str(j))
            s+= a2
        elif m == a3 and i >0 and str(i-1)+'`'+str(j) in l: 
            l.remove(str(i-1)+'`'+str(j))
            li2.append(str(i-1)+'`'+str(j))
            i-=1
            j+=1
            li2.append(str(i)+'`'+str(j))
            s += a3
    
        a =[i,j,data[i][j]]
    li3.append(li2)
        

    
    
    

#0번부터 가자  작은 수를 찾는거 i=1 j =1 -> 2/1 > (0/1 + 0/2) or (2/1 + 2/2)

#어떻게 ..? 일단 비교해보고 3*3 더한 수 중에 가장 적은 수 로 저장해 보자
# 리스트로 3*3 중에 가장 작은 수를 더한 뒤 
#for i in range(80):
    
        
        
'''        
        
for i in range(1000000):
    n2 = copy.deepcopy(n)
    li=[]
    s,y=0,0 #부터 시작
    for x in range(79,-1,-1):
        if str(y+1)+'/'+str(x+1) in n2 :
            s += d2[y][x]
            li.append(str(y)+str(x))
            n2.remove(str(y+1)+'/'+str(x+1))
            r = random.choice([-1,0,1])
            if str(y+r+1)+'/'+str(x+1) in n2 :
                if y ==0 and r ==-1: pass
                y+= r
                s+=d2[y][x] 
                li.append(str(y)+str(x))        
                n2.remove(str(y+1)+'/'+str(x+1))
            
    d3.append([s,li])
    d4.append(s)

print(min(d4))
'''