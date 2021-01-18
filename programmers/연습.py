from itertools import combinations

def solution(d, budget): #d :부서마다 신청 금액 리스트  budget :금액 
    answer = 0
    sum=0
    #일단... d를 다 더했을 때 예산보다 > = < 나누고
    #1
    for i in d:
        sum += i
    
    if sum == budget:
        answer = len(d)
         
    
    return answer # 몇 개의 부서를 지원해 줄 수 있는지
d = [1,3,2,5,4]
budget =9
answer = 0
sum=0
#일단... d를 다 더했을 때 예산보다 > = < 나누고
#1
for i in d:
    sum += i

if sum == budget:
    answer = len(d)
else :
    d.sort()
    s =0
    for i in d:
        if budget <= (s+i):
            break
        s+=i
    a=3
    
    li=[]
    li += combinations(d,a)
    for i in li:
        s1 =0
        for j in range(a):
            s1 += i[j]
        if s1 == budget:
            break
        
        #123 124 125 134 135 145
    