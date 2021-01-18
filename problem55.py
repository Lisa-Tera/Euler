def re(n):#2,3,4자리수 
    li,f_li=[],[]
    
    for i in range(1,50):
        li= list(map(int, str(n)))
        a = int(len(li)/2)
        
        if len(li) %2 ==0 :
            a1,a2= li[:a] ,li[a:]
            a2.reverse()
            if a1 ==a2 and i >1:  return False #i가 1이면 [4994, 8778, 9999] 같은 수는 제외되기 때문에 조건 추가 ★
            
        else :
            a1,a2= li[:a] ,li[a+1:]
            a2.reverse()
            if a1 ==a2 and i > 1 : return False
        
        li.reverse()
        
        st =''
        for i in li: st +=str(i)
        f_li.append(n)
        n+= int(st)
    return True

s_li=[]
s=0
for i in range (1,10000):
    if re(i):
        s_li.append(i)
        s+=1
    

''' //다른 사람거
def reverse_n(n):
    return int(str(n)[::-1])
 
ans = 0
li=[]
for tmp_n in range(1, 10000):
    n = tmp_n + reverse_n(tmp_n)
 
    for i in range(1, 50):
        if n == reverse_n(n):
              break
        n += reverse_n(n)
     
    else:
        li.append(tmp_n)
        ans += 1
'''