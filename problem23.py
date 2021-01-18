'''초과수(약수의 합이 자기 자신을 초과한 수) 두 개의 합으로 나타낼 수 없는 모든 양의 정수의 합은 얼마입니까?'''

def sum_divisor(num):
    d_list =[1]
    s=0
    for i in range (1,num):
        if num % i ==0 :
            d_list.append(i)
            s +=i    
    if s > num : return True
    else : return False        



abun =[]
n=[]
for i in range (1,28123):
    li = sum_divisor(i)    
    if li == True : abun.append(i)
    
    n.append(i)    
n_sum = sum(n)

ab_sum=[]
for a in abun:
    for b in abun:
        if a+b <28123 : ab_sum.append(a+b)
            
abun_sum = sum(set(ab_sum))
print(n_sum - abun_sum)
    


        
            
        
            