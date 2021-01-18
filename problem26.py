
rc = rc_1 = 0
for i in range(2,1000):
    r=1
    rlist=[]
    while r!=0:
        while r < i:
            r = r*10
        r %= i
        if r not in rlist:
            rlist.append(r)
        else:break
    if len(rlist) > rc and 0 not in rlist:
        rc=len(rlist)
        rc_1 = i
print(rc_1)
       

       
