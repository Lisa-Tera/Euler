def isPrime(a):
  if(a<2):
    return False
  for i in range(2,a):
    if(a%i==0):
      return False
  return True


tot_dict ={}
for a in range(-999,1000):
    for b in range (-999,1000):
        n =0
        while True :        
            fx = n**2 + a*n + b        
            if (isPrime(fx)) ==False: break
            n+=1
        tot_dict[n] = [a,b]
        
m =max(tot_dict.keys())        
print(tot_dict[m][0]*tot_dict[m][1])
        
            