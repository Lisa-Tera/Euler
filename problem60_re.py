# 4개의 소수 5개의 소수
#앞,뒤 다 소수가 가능

f = open("prime.txt", 'r')
data = f.read()
f.close()

li = data.split(', ') #str 형태로 소수 가져오기
li2 = li[:30000]
li3 = li[:100000]
#변수 5 개 설정 

for a in range(100,len(li2)):
    for b in range(70,a):
        for c in range(30,b):
            for d in range(10,c):
                for f in range(d):
                    l =[]
                    f1,f2,f3,f4,f5= li2[a],li2[b],li2[c],li2[d],li2[f]
                    x1,x2,x3,x4,x5,x6 ,x7 = f1+f2, f1+f3, f1+f4, f1+f5, f2+f3, f2+f4, f3+f4
                    y1,y2,y3,y4,y5,y6 ,y7 = f2+f1, f3+f1, f4+f1, f5+f1, f3+f2, f4+f2, f4+f3
                    if x1 in li3 and y1 in li3:
                        if x2 in li3 and y2 in li3:
                            l.append(f1,f2,f3,f4,f5)
                            
                            
                            
                        
                            
                
                
                                
                    


