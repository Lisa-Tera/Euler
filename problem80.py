
two = [1,4,9,16,25,36,49,64,81,100]

def sqrt(n,count):
    for i in range(len(two)-1):
        if two[i] <  n  < two[i+1]:
            b = (n - int(n**0.5)**2)*100
            s = int(n**0.5)
            a = s*2
            
            break
        if two[i] ==n:
            return n
     
    if n != s**2 :
        for x in range(count-1):
            for c in range(9,-1,-1):
                if (a*10+c)*c <= b:
                    b = b - (a*10+c)*c
                    a = a*10 + 2*c
                    s +=c
                    break
                
            
            b = b*100
            
    return s
f=0
for x in range(1,100):
    for y in range(10):
        if x == two[y]: 
            break
        if x < two[y]: 
            f += sqrt(x,100)
            print(f,sqrt(x,100),x) #확인
            break
print(f)


'''
보고 가져온거
def sqrt(n, count=20):
  #100미만의 정수 N의 제곱근을 숫자 count개까지 구한다.
  result = []
  a, b, c = 0, n, 0
  while c < count and b > 0:
   #일의 자리가 될 숫자 i 찾기
    for i in range(1, 11):
      if (a * 10 + i) * i <= b:
        continue
      break
    # i 가 허용치를 넘었을 때 루프가 끝나므로
    i = i - 1
    result.append(i)
    b = (b - (a * 10 + i) * i) * 100
    a = (a * 10 + i) + i
    c += 1
  return result

sum()

xs = [sqrt(x, 100) for x in range(1, 100)]
print(sum(sum(x) for x in xs if len(x) == 100))
'''