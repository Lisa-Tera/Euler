#16 or 17 인데 오각형에 있으면 17, 끝에 있으면 16이므로
#16중 가장 큰 수를 구하여라

#시계방향으로 가장 낮은 수부터 시작
#숫자가 같아야 되는데 그런 경우 6 + 3+5 / 7 + 2+5 / 8 + 2+4 / 9+ 1+4 / 10 + 1+3

#그냥 계산으로도 되지만  경우를 추측하는 코드를 완성해보자

a = [6,7,8,9,10]
b = [1,2,3,4,5]
b2 = b*2
num =[[1, 2], [1, 3], [2, 3], [1, 4], [2, 4], [3, 4], [1, 5], [2, 5], [3, 5], [4, 5]]

dic ={}
for i in num:
    s = i[0]+i[1]
    try : dic[s]  =[dic[s] ,i]
    except: dic[s] = i


li,li2 =[],[]
for k in dic:
    if k+4 in dic.keys():
        li.append([10+k,[6,dic[k+4]],[10,dic[k]]] )
        if type(dic[k][0]) == list:
            li2.append([10+k,dic[k+4]+dic[k][0]])
            li2.append([10+k,dic[k+4]+dic[k][1]])
        elif type(dic[k+4][0]) == list:
            li2.append([10+k,dic[k+4][0]+dic[k]])
            li2.append([10+k,dic[k+4][1]+dic[k]])
        else:            
            li2.append([10+k,dic[k+4]+dic[k]])
        
        #li2.append(dic[k+4]+dic[k][0])
        
        
for i in li2:
    b2 = b*2
    for i2 in i[1]:
        if i2 in b2: b2.remove(i2)#지우고 
    for q in range(3): #7,8,9일 때
        if type(dic[i[0]-a[q+1]][0]) == list:
            for q2 in dic[i[0]-a[q+1]]:
            if q2[0] in b2 :
                b2.remove(q2[0])  
            if q2[1] in b2:       
                b2.remove(q2[1])
            if len(b2) == 0 :
                break


                       
            
        
    
    




'''    
# 6 10더했을 때
m =a[-1]-a[0]
while True:
    b6 = random(4)
    s = a[0]+5+b6
    

    i = random.sample(b2,4)
    a1,a2 =i[0]+i[1],i[2]+i[3]
    if a1 == a2+m :
        li=[[a[0],i[0],i[1]],[a[-1],i[2],i[3]]]
        sub_b = [x for x in b2 if x not in i] 
        sub_b += b
        
        for j in range(1,4):
            while True:
                i = random.sample(sub_b,2)
                a3=i[0]+i[1]
                if a3 == a2 +m-j :
                    if i in num :
                        li.append([a[j],i[0],i[1]])
                        sub_b.remove(i[0])
                        sub_b.remove(i[1])
        if len(li) == 5:break
                        
                    
                
        #li.append([a1,[6,i[0][0],i[0][1]],[10,i[1][0],i[1][1]]])
    
        
   '''     
