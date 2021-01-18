# (x**2+x)(y**2+y) /4 ==사각형 개수 x**4보다 큼
dic={}
a = 2000000
b = 1000
ra = int((a*4)**0.25)
li = []
for x in range(ra*2,int(ra/3),-1):
    for y in range(x,0,-1):
        fx=(x**2+x)*(y**2+y) /4 

        if fx< (a+b) and (a-b) < fx:
            dic[(x,y)] = [a-fx,fx]
            li.append([x,y,x*y])
            


        
    
        