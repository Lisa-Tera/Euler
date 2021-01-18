tlist,plist,hlist=[],[],[]
d={}
num=20000
for n in range(num+1):
    #t = n*(n+1)/2    p = n*(3*n-1)/2   h = n*(2*n-1)
    tlist.append(n*(n+1)/2)
    plist.append(n*(3*n-1)/2)
    hlist.append(n*(2*n-1))

tt = tlist[19999]
pp = plist[19999] 
del tlist[:3976]
del plist[:2296]
del hlist[:1988]
'''
for i in range(20000-2296):
    if tt < plist[i]: 
        del plist[i:num]
        break
    
for t in range(19999):
    for p in range(i):
        if tlist[t] == plist[p]:
            d[tlist[t]] = (t,p)


'''
'''
for t in range(num-285):
    for p in range(i):
        if tlist[t] == plist[p]: a = plist[p]
        else : del tlist[t]
        for h in range(j):
            if hlist[h] == plist[p]: b = plist[p]
            else: del hlist[h]



        
        
del tlist[:19]
del plist[:11]
#del hlist[:143]        

'''
