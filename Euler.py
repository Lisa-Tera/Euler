



    
#1
'''
a = 3
sum = 0
for a in range(999):
    a += 1
    if a % 3 == 0 or a % 5 == 0 :
        sum += a

print(sum)                   '''

#2 파보나치
'''
a = 1 #파보나치 수
b =1
even =0
for i in range(1000):
    a += b
    b += a
    if a <= 4000000 and a % 2 == 0:
        even += a
    if b <= 4000000 and b % 2 == 0:

        even += b                    '''


#3 소인수
'''
num =997
so = 2
d = 0

while True:
    if num %so ==0 : # ex) 4이면 다시 위로 올라와서 이 if문을 통과하므로 소인수로 분해됨
        num = num/ so
        
    else :
        so += 1
        
    if num == 1 : break #여기서 끝나게 되므로 변수를 하나 더 만듦
    f = num
print(f)     '''             

#4 대칭수  x*y = abccba  에러ㅓㅓㅓㅓㅓ

'''
for x in range (100,1000):
    for y in range (100,1000):
        num = x*y
        a =9
        b=9
        c=9
        f= 0 
        for i in range(1,10):
            if (num - a*100000) < 100000 and (num - a) %10 ==0 :
                num -= a*100000 + a
                f +=a*100000 + a
                if (num - b*10000) < 10000 and (num - b*10) %100 ==0 :
                     num -= b*10000+ b*10
                     f +=b*10000+ b*10
                     if (num - c*1000) < 1000 and (num - c*100) %1000 ==0 :
                         num -= c*1000+ c*100
                         f+= c*1000+ c*100
                     else : c = c - 1
                else:b = b -1
            else : a = a - 1
                            
                    
                


        
        

        for a in range(1,10):
            
            if (num - a*100000) < 100000 and (num - a) %10 ==0 :
                num -= a*100000 + a
                f += a*100000 + a
                for b in range(1,10):
                    if (num - b*10000) < 10000 and (num - b*10) %100 ==0 :
                        num -= b*10000+ b*10
                        f += b*10000+ b*10
                        for c in range(1,10):
                            if (num - c*1000) < 1000 and (num - c*100) %1000 ==0 :
                                num -= c*1000+ c*100
                                f += c*1000+ c*100'''


            
            
#25
'''
a = 1 #파보나치 수 1
b =1 #2
i=2
while True:
    a = a+b
    i +=1
    b = a+b
    i+=1
    if len(str(b)) >=1000 or len(str(a)) >=1000:
        print(i)
        break'''

#26 순환마디가 가장 긴 것은?  2,3,5의 배수는 제외 --------모르겠
'''
for i in range(2,30) :
    
    else:
        if flt = 1 / i 
        print(i, flt)
'''
#27
# n**2 +n+41 39까지 소수 40도 소수인데 41로 나눠지기도함
# n**2 -79n +1601 79까지 다 소수
'''
n=0
a = -999
b = = -999
#while을 쓰던 for 을 쓰던 써야되
while True:
    n**2 + a*n + b
    if a <1000 : a += 1
    else:break
    if b <1000 : b += 1
    else:break
    
        
    n +=1
'''
#28 1001
'''
a =1
x= 2
sum=1
while x <1001:
    for i in range(4):
        a = a +x
        sum +=a        
    x += 2
print(sum) '''

#29
'''
s =[]
for a in range(2,101):
    for b in range(2,101):
        s.append(a**b)

s1 = set(s)  
print(len(s1))      '''

#30
'''
i =2
sum=0
#while True:

for i in range(10000):
    if i <10 :pass
    if i < 100 and i >=10 :
        b = int(i /10)
        a = i - b*10
        #print(a,b,i)
        if i == b**4+a**4: print(i)
    
    if i < 1000 and i >=100:
        c = int(i /100)
        b = int((i-c*100)/10)
        a = i - (c*100+b*10)
        #print(c,b,a,i)
        if i == c**4+b**4+a**4: print(i)
    
        
    if i < 10000 and i >=1000:
        d = int(i/1000)
        c = int((i-d*1000) /100)
        b = int((i-(d*1000+c*100))/10)
        a = i - (d*1000+c*100+b*10)
        #print(d,c,b,a,i)
        if i == d**4+c**4+b**4+a**4:
            print(i)
            sum +=i                 '''
'''

for i in range(1000000):
    if i <10 :pass
    if i < 100 and i >=10 :
        b = int(i /10)
        a = i - b*10
        #print(a,b,i)
        if i == b**5+a**5: print(i)
    
    if i < 1000 and i >=100:
        c = int(i /100)
        b = int((i-c*100)/10)
        a = i - (c*100+b*10)
        #print(c,b,a,i)
        if i == c**5+b**5+a**5: print(i)
    
        
    if i < 10000 and i >=1000:
        d = int(i/1000)
        c = int((i-d*1000) /100)
        b = int((i-(d*1000+c*100))/10)
        a = i - (d*1000+c*100+b*10)
        #print(d,c,b,a,i)
        if i == d**5+c**5+b**5+a**5:
            print(i)
            sum +=i
    if i < 100000 and i >=10000:
        e = int(i/10000)
        d = int((i-e*10000)/1000)
        c = int((i-(e*10000+d*1000)) /100)
        b = int((i-(e*10000+d*1000+c*100))/10)
        a = i - (e*10000+d*1000+c*100+b*10)
        #print(d,c,b,a,i)
        if i == e**5+d**5+c**5+b**5+a**5:
            print(i)
            sum +=i
    if i < 1000000 and i >=100000:
        f = int(i/100000)
        e = int((i-f*100000)/10000)
        d = int((i-(f*100000+e*10000))/1000)
        c = int((i-(f*100000+e*10000+d*1000)) /100)
        b = int((i-(f*100000+e*10000+d*1000+c*100))/10)
        a = i - (f*100000+e*10000+d*1000+c*100+b*10)
        #print(d,c,b,a,i)
        if i == f**5+e**5+d**5+c**5+b**5+a**5:
            print(i)
            sum +=i
      
    



          
            
            
    else: i+=1

    '''
    

            
            
