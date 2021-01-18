li=[]
for x in range(51):
    for y in range(51):
        li.append([x,y])
del li[0]

tri=[]
for p in li:
    for q in li:
        if p!= q and p[0]<=q[0] and q[1]<=p[1]: 
            
            o1 = p[0]**2 + p[1]**2
            o2 = q[0]**2 + q[1]**2
            o3 = (p[0]-q[0])**2+ (p[1]-q[1])**2
           
            a = [o1,o2,o3]
            a.sort()
            if a[-1] == a[0]+a[1]:
                tri.append([a,p,q])
        
        
        
        
        
        