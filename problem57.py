'''
 √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213
 
 1000번째 까지 중 분자(c)의 자릿수가 분모(p)를 넘는 경우
 len(str(c))>len(str(p))
'''
a,b,s=5,2,0 #처음에 5분의 2 -> 0.4
li=[]
for i in range (1,1000):
    
    poin = a
    a = 2*a+b
    b=poin
    li.append([a+b,a]) #확인
    c = str(a+b)
    p = str(a)
    if len(c) > len(p): s+=1 #답 

print(s)
# 5/12   12/29   29/70 

