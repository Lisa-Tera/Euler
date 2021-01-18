li,l2=[],[]
l=set()
n=7830457
m = 28433
a = 2
#for i in range(1,1000):
while True:
    if len(li) == n:
        break
    
    if len(str(a)) >=10:
        sa = str(a)[-10:]
        li.append(sa)
        a = int(sa)*2
    else:
        a *=2
        li.append(a)

y = m*int(sa)+1
y = str(y)[-10:]