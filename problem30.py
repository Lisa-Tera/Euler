#39
#직각삼각형의 둘레 중 가장 많이 성립하는 것은? a+b >c
dic = {}
s =[]
for a in range(20):
    for b in range(20):
        for c in range(20):
            if a+b >c:
                z = a**2+b**2
                if z == c**2:
                    s.append(a+b+c)
                    dic[a+b+c] = 1
                    

#같은 수가 나오면 +1씩 해줘야 하는디 처음에 0으로 안정해져 있어서....
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        dic[s[i]] +=1
    
