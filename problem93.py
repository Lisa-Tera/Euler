import random

solli=[]
for i in range(4,10):
    for i2 in range(3,i):
        for i3 in range(2,i2):
            for i4 in range(1,i3):
                solli.append([i4,i3,i2,i])
                '''a = [i4,i3,i2,i] 중복 확인용
                if a not in li: li.append(a) '''
solli.sort()
del (i4,i3,i2,i)


def switch(n,a1,a2):
    if n == 0: return a1 + a2
    elif n==1 : return a1 / a2
    elif n==2 : return a1 * a2
    elif n ==3 : return (a1 - a2)

dic,maxli ={},[]

for aa in solli:
    se,li2 = set(),[]
    
    for i in range(50):
        sample = random.sample(aa, 4)
        if sample not in li2: li2.append(sample)
   
    
    for a in li2:
        s = 0
        li = []
        
        for j in range(4):
            s = switch(j,a[0],a[1]) #a[0]과 a[1]의 사칙연산  
            li.append(s)
            
            for j2 in range(4):
                s1,s11 = switch(j2,s,a[2]),switch(j2,a[2],a[3])
                li.append(s1)
                
                for j3 in range(4):
                    s2,s22 = switch(j3,s1,a[3]),switch(j3,s,s11)
                    li.append(s2)
                    
                    if s2 == int(s2) and s2 >0: se.add(int(s2))
                    if s22 == int(s22) and s22 >0: se.add(int(s22))
  
    li = list(se)
    for i2 in range(len(li)):
        if li[i2] != (i2+1):break
    maxli.append(i2)
    dic[str(aa)] = [i2,li]
m =max(maxli)
for k in dic.keys():
    if dic[k][0] == m :
        print(k)

'''
1234의 경우
import random

se = set()
li =[1,2,3,4]#,[1,2,4,3],[1,3,4,2],[1,3,2,4], ...]
#for a in range(24):
li2=[]

for i in range(100):
    sample = random.sample(li, 4)
    if sample not in li2:
        li2.append(sample)
li2.sort()       
        
def switch(n,a1,a2):
    if n == 0: return a1 + a2
    elif n==1 : return a1 / a2
    elif n==2 : return a1 * a2
    elif n ==3 : return (a1 - a2)
      

dic ={}
for a in li2:
    s = 0
    li = []
    for j in range(4):
        s = switch(j,a[0],a[1]) #a[0]과 a[1]의 사칙연산  
        li.append(s)
        for j2 in range(4):
            s1 = switch(j2,s,a[2])# s a[2]
            li.append(s1)
            for j3 in range(4):
                s2 = switch(j3,s1,a[3])#s a[3]
                li.append(s2)
                if s2 == int(s2) and s2 >0: se.add(int(s2))
            
    
                
    
li = list(se)


일단 1~4까지 일 때 4! = 24 
 + - * / 는 총 3번 쓸 수 있음 4*4*4 =64가지의 경우
24*27

순서는 상관 ㄴㄴ
숫자조합이 이어지는거로 가장 긴거 찾기 인데
4의 경우는 1~28까지임
1 = (4+1-3)/2
2 = 4/(1+3)*2
a < b < c < d 인 숫자 네 개로 위와 같이 했을 때
순서를 어떻게 해야될까...?
모르겠다ㅏㅏㅏㅏ passssss

'''

    
        
    
