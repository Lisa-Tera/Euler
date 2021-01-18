#n자리 숫자이면서 n제곱수도 되는 양의 정수 7**5 =16807  -> 7**n 

#변수 2개 필요 a,b a**b  and str(a**b) ==b가 성립해야되고 개수는 sum으로 추가
s =0
for a in range(1,1000):
    for b in range(1,100):
        x =len(str(a**b))
        if x == b:
            s+=1
