
'''
k는 + or * 앞,뒤에 붙는 숫자의 개수 and n :최솟값 
k = 2 : 4 =  2*2  =  2+2
k = 3 : 6 = 1*2*3 = 1+2+3
중복을 제외한 2<= k <= 12000 범위에 대한 합곱수의 합은?
'''
dic ={} # dic[k] = 계산한 값 or li
n = 4

# 3인 경우 3**3 = 27 3+3+3 = 9
maxi = n*n # 더하기 최대  
mini = n #더하기 최소 곱하기 최소 =1
li=[]
for i in range(n):
    li.append(1)

for i in range(n):
    for j in range(n):
        