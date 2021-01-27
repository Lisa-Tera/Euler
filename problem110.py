import copy
#문제점 수가 너무 커서 오래 걸림



primes =[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
# 13개 일 때 부터 limit 넘어감  2 3 5 .... primes13 번째 3**13 > limit
a =41 # 13번째 prime
   
'''
total = 3**13 > limit

n_last**2 =1681
어떻게 계산해야될까?
일단 계산되는 수가 41보단 작아야됨
11 1번 쓰이므로 (n+2) 임 --> 1+2 에서 9에 가까운 수를 만들어야됨 n*2+1
3< n*2+1 <=9  1<n<=4  --> n= 2,3,4   5/7/9 --> 2일때 limit보다 작으므로 
                            n =3,4 -->숫자가 n_last**2넘음

--> 지수는 2,3,5,7 중에 커져야 성립 
'''


p_2=[2,3,5,7]  #     +2**4까지는 성립  #2 3 5 7  제곱은 안 됨  

d1,d2 ={},{}
for n in range(2,a**2): #a**2보다 크면 의미가 없기 때문에 
    i = copy.deepcopy(n)
    dic={}
    s =1
    for p in p_2:
        if i == 1: break
    
        while (i% p ==0):
            i = i //p                
            try: dic[p] += 1                            
            except: dic[p]=2
            
    for v in dic.values(): s *= v*2+1
    
    d2[n] = (s+1)//2 # 공통인 부분이 생기므로 ex)n=4 |(1,4) (2,2) (4,1)|
    d1[n] = dic

limit = 4000000   
total = 3**8     
num=1

for x in primes: num *= x  
  
for k in d2.keys():
    if total*d2[k] > limit:
        print(limit,'의 조건을 충족하는 수',num*k)
        break
    

    

    





