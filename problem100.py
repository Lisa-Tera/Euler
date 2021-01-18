# 1. 21개의 공 중 2개를 뽑을 때 모두 파란색이 나오는 공의 비율
#2. 120개의 공

#문제는 10의 12제곱 중에

#total = 21 #total = b+r
for total in range(150,1000000):
    for b in range(1,total+1):
        r = b*(b-1)/(total*(total-1))
        if r == 0.5 :
            break
