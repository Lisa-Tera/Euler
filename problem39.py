import operator
#39
#직각삼각형의 둘레 중 가장 많이 성립하는 것은? a+b >c
dic = {}
s =[]


for a in range(1,500):
    for b in range(1,500):
        if b <=a :
            c = (a**2+b**2)**0.5
            if type(c) == int:
               p = a+b+c            
               if p <= 1000:          
                   dic[p] =1

