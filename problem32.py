def factorial(n):
    if n == 1:
        return 1
    return n *factorial(n-1)

def get_next_permutation(string):
    i=len(string)-2
    while i >= 0:
        if string[i] < string[i+1]:
            target = sorted(string[i:])
            new_num = target.pop(target.index(string[i])+1)
            last_nums = ''.join(target)
            return string[:i] + new_num + last_nums
        i-=1
 



t = '123456789'
tt = (factorial(len(t)))
'''
1*1000 =1000
10*100 = 1000 4자리 이상
99*999  =  98901 5자리 이하 2 *3 =4
100*100 = 10000 5자리 이상 불가 
'''
sum={}
vv = []
for i in range(1,tt):    
    t = get_next_permutation(t)
    a1,b1,c1 = int(t[:2]),int(t[2:5]),int(t[5:])
    if a1*b1 ==c1:vv.append(c1)
    
    a2,b2,c2 = int(t[:3]),int(t[3:5]),int(t[5:])
    if a2*b2 ==c2 :vv.append(c2)#sum[str(t[:3]+' '+t[3:5] )] = c2 확인용
    
    a1,b1,c1,a2,b2,c2 = int(t[:1]),int(t[1:5]),int(t[5:]),int(t[:4]),int(t[4:5]),int(t[5:])
    if a1*b1 ==c1 or a2*b2 ==c2 :
        vv.append(c1)
        vv.append(c2)
    
        

vv = list(set(vv))
s=0
for j in range(len(vv)):
    s+=vv[j]

#for v in sum.values():
    
    
    





'''
test = "123456789"
m=len(test)
total = []
while not test == None:
    for i in range(1,m):
        str1=test[0:i]
        for j in range(i+1,m):
            str2=test[i:j]
            str3=test[j:m]
            if int(str1)*int(str2)==int(str3):
                print(str1,str2,str3)
                total.append(int(str3))
    test = get_next_permutation(test)
print(total)
'''