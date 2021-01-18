# n의 수를 제곱해서 더하고 반복하면 1 or 89가 나온다 천
#천만 이하의 자연수 중 89에 도달하는 숫자의 개수를 구하라
dic={'0':0}
for i in range(1,10):
    dic[str(i)] =  i*i

def sol(n):
    li = list(str(n))
    s =0
    for i in li:
        s+=dic[i]
    if s == 1 :
        return False
    if s == 89:
        return True
    else : 
        return sol(s)
s =0    
for i in range(1,10000000):
    
    if sol(i) == True:
        s+=1
