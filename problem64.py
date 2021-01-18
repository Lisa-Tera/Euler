
li=[]
n=23
r2 = n**0.5
a0 = int(n**0.5) =4

분모 = n - int(n**0.5)**2 = 7
분자 = int(n**0.5) + a0 =r23 + 4 

a1= int((int(n**0.5) + a0)/분모)  = 1

a1+ (분자 - a1*분모)/분모

분모 / (분자 - a1*분모) 



a1 = int(n**0.5)

p= r2+int(r2) # r3 +1
a = n-int(r2) # n=3이면 2임  무조건 정수임
b= int(p/a) # 1
li.append(b)
p =r2+ int(r2)- b*a


s= 0
def sol(n):
    
for n in range(3,4):#10000):
    r2 = n**0.5
    ir2 = int(r2)
    if (n-ir2**2) ==1:
        s+=1
    else: # 1이 아닐 때
        p= r2+int(r2) # r3 +1
        a = n-int(r2) # n=3이면 2임  무조건 정수임
        b= int(p/a) # 1
        p = p- b*a
        
        
        
    



#a0 = a -int(a) = 1/(a+int(a))  = > int(a+int(a))/((a -int(a))*(a +int(a))) 
#pp,pm=int(p),int(p*m)
#a0= int(p/pm)

















































'''
a = 23**0.5 
a0= 1/(a-int(a))
a1= 1/(a0-int(a0))
a2 =1/(a1-int(a1))
'''








'''
n_li=[]
for i in range(2,10001):
    if i**0.5 != int(i**0.5):
        n_li.append(i)


def sol(li):
    dic={}
    for i in li:
        dic[i]=0
    for i in li:
        dic[i]+=1
    vmax = max(dic.values())
    if vmax >1 : return len(dic)
    return 0
  
      
        
        
    
    #for i in li:
s=0
dic={}
for i in n_li:
    n = i**0.5
    an,bn,cn = n,-n,1
    
    li=[]
    for j in range(10):    
        cn = (n-bn**2)/cn
        an = (n-bn)/cn
        bn = -bn -an*cn
        li.append(round(an,1))
        
    dic[i] = li
    if dic[i] %2 != 0:s+=1
            
        #afx = int(a) +(a-int(a))
        x = (a+int(a))
        y = (a-int(a))
        axy = 1/y
        #a = 1/(a - int(a))
        if axy == (inta+axy):
            li.append(inta)
            break
        a = a - inta
        sl.add(inta)
        if j ==4 and len(sl)==2:
            break
        if j ==0: 
            li.append(inta)
        else:
            if li[j-1] == inta:
                break
            if li[j-1] != inta:
                li.append(inta)
                
    dic[i] = sol(li)
    if sol(li) %2 !=0:
        s+=1
    #dic[i] = sol(n)


#원래 a = 1/(a - int(a)) 로  했는데 오류
        x = (a+int(a))
        y = (a-int(a))
        a = x/(x*y)
        ai = int(a)
        a = a-int(a) 
        
        a = int(a) +(a-int(a))
        a = 1/(a-int(a)) 
        a = (a+int(a)) / ((a-int(a))*(a+int(a)))
        x = (a+int(a))
        y = (a-int(a))
        fx = 1/y =  x/(x*y)
        a1 = int(fx)
        a= a/(x*y) -a1*(x*y) = (a- a1*(x*y))/ (x*y)
        
        a2 = 1/a
        a = 1/(a-int(a)) //x = (a+int(a))  y = (a-int(a))
        a = 1/y =  x/(x*y)
'''
        
    
    
    
        
