# 빗변 -1 = 이등변 and 삼각형의 넓이 = 정수 and 둘레 = 10억
# 높이/ 밑변 = r3에 가까움 1< r3<2 
#if a가 작은수 일 때 6 6 5 인 경우 3a+2 36 25/4 36*4 = 119/4 h 5보다 큼 
li=[]
'''
for i in range(2,100):
    li.append(i**2)
'''
limit = 1000000000
tris=0

s = 0
for a in range(3, 136500430):
    
    b = a+1
    if s < limit:
        if b %2 ==0:
            h = (a**2 -(b/2)**2)**0.5
            q = h*(b/2)
            if int(h) == h and int(q) == q:
                
                
                if a**2 == (h**2 +(b/2)**2):
                    li.append([q,a,b,h,2*a+b])
                    s+= 2*a+b
                    
        else :
            h = (b**2 - (a/2)**2)**0.5
            q = h*(a/2)
            if int(h) == h and int(q) == q:
                li.append([b,a,h,2*b +a])
                s +=  2*b +a
       
'''                
        #1 
        b= a+1
        x = (3*a-1)/2
        # 3*(h**2) =x**2- 1 
        h2 = (x**2-1)/3 # a**2 = (b/2)**2 +h2
        #hh2=a**2 -(b/2)**2
        h = h2**0.5
        if int(h) == h:
            q1=h2 +(b/2)**2
            if a**2 ==q1:
        #if h2 ==hh2 and int(h2) ==h2:
                tris += (3*a+1)
                li.append([a,b,h,tris,3*a+1])
                #print(a,b,h,(3*a+1),tris)
            
        
        #2 
        b =a-1
        x = (3*a+1)/2 
        h2 = (x**2-1)/3
        h = h2**0.5
        if int(h) == h:
            q1 = h2 + (b/2)**2
            if a**2 ==q1:
                tris += (3*a-1)
                li.append([a,b,h,tris,3*a-1])
            #print(a,b,h,(3*a-1),tris)

    else: break'''
'''
li =[
[5,6,4.0,16],
[17,16,15.0,50],
[65,66,56.0,196],
[241,240,209.0,772],
[901,902,780.0,2704],
[3361,3360,2911.0,10082],
[12545,12546,10864.0,37636],
[46817,46816,40545.0,140450],
[174725,174726,151316.0,524176],
[652081,652080,564719.0,1956242],
[2433601,2433602,2107560.0,7300804],
[9082321,9082320,7865521.0,27246962],
[33895685,33895686,29354524.0,101687056],
#[84739212,84739213,73386310.0,254217637],
#[92604733,92604734,80198051.0,277814200],
[126500417,126500416,379501250]]
16002355501173888
lis=0
for i in  li:
    s = i[1]*i[2]/2
    if s == int(s):
        if i[1]<i[0]:
            
            a1=(i[1]/2)**2
            a2=i[0]**2
            a3= i[2]**2
            if i[1]**2 ==(i[0]/2)**2+i[2]**2:
                lis+=i[3]
        else :
            a1=(i[1]/2)**2
            a2=i[0]**2
            a3= i[2]**2
            if  i[0]**2== (i[1]/2)**2+i[2]**2:
                lis+=i[3]
        
a =[84739212,84739213,73386310.0,254217637]

if a[1]**2 ==a[0]**2+a[3]**2:
    print(a)
'''




