#10n +i / (10i +d)
#n < i
ch,pa=[],[]
st=[]
for i in range(2,10):
    for n in range (1,i):
        for d in range(10):
            f = (10*n+i ) / (10*i +d)
            
            try:
                if f == n/d:
                    st.append(str(10*n+i) +'/'+str(10*i +d))
                    ch.append(10*n+i)
                    pa.append(10*i+d)
                
            except ZeroDivisionError:
                pass
print(st)

c,p=1,1
for i in range(len(ch)):
    c *= ch[i]
    p *= pa[i]
a = c/p
b = p/c
print(b)

            
