# 1~n까지 1,2,...,n의 숫자를 조합한 소수 중 가장 큰 수
'''
12 21                               2  2!
123 132 213 231 312 321             6  3! -2! ->4           
1234 1243 1324 1342 1423 1432 2134  24 4! - 3!*2 -> 12
12345                                  5! - 4!*2 -> 4!*3  1 3 5

최대가 9까지 9!인데 소수만 해당됨 ...-> 2의 배수 제거 해도됨

1. n을 정한다. -> 가장 큰 수 이므로 9부터 한다.
2. n!을 해서 숫자를 리스트에 넣는다.
3. 소수를 골라 낸다.

 '''
def isPrime(a):
  if(a<2):
    return False
  for i in range(2,a):
    if(a%i==0):
      return False
  return True


def penDigit(n):
    n = str(n)
    n_li = list(n) #3124
    dic = {}
    for i in range(1,len(n)+1):
        dic[i] = str(i)
        #li.append(str(i))# 1234
        
        
    for a in dic:
        try : 
            n_li.remove(dic[a])
        except KeyError : 
            
            return False
        except ValueError: 
            
            return False
    
    return True
        
        
    
    
'''dic[len(str(n))].remove
dic = {1:1}
for i in range(2,10):
    li=[]
    for j in range(1,i+1):
        li.append(j)   
    dic[i] = li 
'''

prime_list =[]
for num in range (7652400,7654321):
    if (isPrime(num)) and (penDigit(num)):
        print(num)
        break
        #prime_list.append(num)
        
        
'''
n_list=[]
for num in prime_list:
    for n in range(len(num)-1,-1,-1):
        p = int(num/(10**n))
        num -= p*(10**n)
        n_list.append(p)
    
        
'''



