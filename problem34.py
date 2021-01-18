





#슬라이싱 하고 factorial 에 넣어주면 되는데 함수를 어떻게 만둘지가 솬선
def f(a):
    fact={'0': 1, '1': 1, '2': 2, '3': 6, '4': 24, '5': 120, '6': 720, '7': 5040, '8': 40320, '9': 362880}
    b = list(str(a))
    sum1=0
    #d = factorial(int(b[0]))+factorial(int(b[1]))+factorial(int(b[2]))
    for i in range(len(b)):
        sum1+=fact[b[i]]
    return sum1
    

for x in range(145,10000000):
    aq=f(x)
    if f(x) == x:
        print(x)
    

#모든 수의 합 
a = {'0':0}
s =1
for i in range(1,10):
    s *= i
    a[str(i)] = s
    
    

for x in range(12,10000000):
     zz =fun(len(str(x)),str(x))
     
sum2=0
for x in range(144,10000000):
    n = list(str(x))
    sum1=0
    for n1 in range(len(n)):
        sum1 +=a[str(n[n1])]
        if len(str(sum1)) == len(n):
            if x == sum1 :
                print(x)
                sum2 += x
                if sum2 ==0 : break
            
