'''
세제곱수인 41063625 (=345**3) -> 56623104 (=384**3) -> 66430125 (=405**3) 실제 41063625은, 자릿수로 만든 순열 중에서 3개가 세제곱수인 가장 작은 수입니다.
그러면 자릿수로 만든 순열 중에서 5개가 세제곱수인 가장 작은 숫자는 무엇입니까?
'''
#세제곱 한거 리스트에 넣기
dic={}
li=[]
for i in range(20000,0,-1):
    a = list(str(i**3))
    a.sort()
    a = ''.join(a)
    
    li.append(a)
    dic[i] =a


li.sort()

s=0
for i in range(1,len(li)):
    a=li[i]
    if li[i] ==li[i-1]: s+=1
    if li[i] !=li[i-1]: s=0
        
    if s ==4: break
    
    
    
for k in dic.keys(): 
    if dic[k] ==a :
        print(k,k**3)

