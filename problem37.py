def isPrime(a):
  if(a<2):
    return False
  for i in range(2,a):
    if(a%i==0):
      return False
  return True

def strCh(num):
    c = str(num)
    s=0
    for x in range(1,len(c)):
        if isPrime(int(c[x:])): #왼쪽
            if isPrime(int(c[:-x])): #오른쪽 
                s +=1
    if s ==(len(c)-1): return True
    return False
sum = 8920

i = 739397
if (isPrime(i)):
    if (strCh(i)):
        sum+=i
'''
i=11
li=[]
sum =0
while True:
    if len(li) == 11:
        break
    if (isPrime(i)):
        if (strCh(i)):
            li.append(i)
            sum+=i
    i+=2
print(sum)
      '''          
        
    