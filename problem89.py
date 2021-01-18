'''
뺄셈을 ㄱ
뺄셈을 구성하는 부분은 I, X, C로만 시작할 수 있다.
I는 V, X 앞에만 올 수 있다. 1--5 or 1--10 = 4 or 9만가능
X는 L, C 앞에만 올 수 있다.
C는 D, M 앞에만 올 수 있다
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
MMMMDCLXXII
MMDCCCLXXXIII
MMMDLXVIIII
MMMMDXCV
DCCCLXXII
MMCCCVI
MMMCDLXXXVII
'''
lf = open('roman.txt', 'r').read().split('\n')
s= 0
for i in lf:
    s +=len(i)
