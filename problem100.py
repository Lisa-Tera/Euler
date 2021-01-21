'''
 1. 21개의 공 중 2개를 뽑을 때 모두 파란색이 나오는 공의 비율
 2. b*(b-1)    1
    ------- = ---
    n*(n-1)    2
Dario Alpern’s Generic two integer variable equation solver.
Recursive solutions:
xn+1이 xn보다 클 때
xn+1 = 3 ⁢xn + 2 ⁢yn - 2
yn+1 = 4 ⁢xn + 3 ⁢yn - 3

and also:
xn+1이 xn보다 작을 때
xn+1 = 3 ⁢xn - 2 ⁢yn
yn+1 = - 4 ⁢xn + 3 ⁢yn + 1

'''
total = 10**12
#공이 total보다 커야되면서 최소인 경우 파란 공의 개수는?
bn = 15 #파란공
tn = 21 #총 공의 개
while True:
    b = bn*3+ tn*2 -2
    t = bn*4+ tn*3 -3
    if t >total:
        print("파란공의 개수 :",b)
        break
    bn = b
    tn= t
     