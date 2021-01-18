# a,b < 100 a**b의 자릿 수의 최대값 ex) 10**2 =100 -> 1+0+0  2**4 =16-> 1+6=7
max_s =0
for a in range(99,1,-1):
    for b in range(1,100):
        n = a**b
        s =list(str(n))
        sum =0
        for i in s:
            sum +=int(i)
        if max_s < sum :
            max_s =sum
        
            
        