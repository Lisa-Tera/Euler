#피보나치 1,1,2,3,5,8 
#F541 자릿수 113 마지막 자리수 9개 팬디지털 
#F2749 자릿수 575 처음 9개 자리수 팬디지털 
#F??? 첫 9 끝 9 자리 팬디지털

#일단 피보나치를 리스트로 만들고 생각해보자

def F(n):
    f1 = 1
    f2 = 1
    li =[str(f1),str(f2)]
    for i in range(n):
        f = f1+f2
        li.append(str(f))
        f1 = f2
        f2 = f
    return li

li = F(1000000)
#str 형태로 자르자

for i in range(len(li),541,-1):
    
    a =li[i]
    #f,d =list(li[i][:9]),list(li[i][-9:])
    f,d =set(li[i][:9]),set(li[i][-9:])
    
    f,d = list(f),list(d)
    
        
    if len(f)==9 and len(d)==9:
        if '0' in f or '0' in d: pass
        else:
            print(i+1)
            break
            
    
    
    
    
    
    
    
        