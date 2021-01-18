import math
fli = open('base_exp.txt','r').read().split()
dic,li={},[]
for i in range(len(fli)):
    i1 = fli[i]
    i1 = i1.split(',')
    a,a1=int(i1[0]),int(i1[1])
    fli[i] = [a,a1]
    y = a1*math.log10(a)
    li.append(y)
    dic[y] = (i+1)
m = max(li)
m1 = dic[m]