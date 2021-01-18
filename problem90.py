# 100 미만의 제곱수를 모두 나타낼 수 있는 숫자의 조합은?
#첫번째 주사위와 두번째 주사위의 순서는 상관없음
#숫자의 경우는 0~8 (7을 제외하고 ) 8가지의 경우 8!
import random
def fac(n):
    if n ==1 : 
        return n
    return fac(n-1)*n
a = fac(6)**2 *2
li=[]
dic = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '8':0}#{0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 8:0}
for i in range(1,10):
    i = i**2
    if i < 10:
        if i ==9 : i =6
        
        li.append([str(0),str(i)])
        #dic[i] +=1
        #dic[0] +=1
        dic['0'] +=1
        dic[str(i)] +=1
    else:
        l = str(i)
        i1,i2= l[0],l[1]
        if i2 == '9' : i2 = '6'
        dic[i1]+=1
        dic[i2]+=1
        #dic[int(i1)] +=1
        #dic[int(i2)] +=1
        
        li.append([i1,i2])

#주사위는 6면체이므로 숫자는 12개 가능
i1,i2 = [],[]
l =set()
for i in range(200):
    a1 = random.sample(dic.keys(),6)
    if '5' not in a1:
        a1.sort()
        if a1 not in i1:
            i1.append(a1)


for i in i1:
    i3=[]
    for k in dic.keys():
        if k in i :
            if dic[k] !=1:
                i3.append(k)
            
        else : i3.append(k)
    i2.append(i3)