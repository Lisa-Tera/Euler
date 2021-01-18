import time
start = time.time() 
'''
3개 일 때
for i in P3:
    a,a1 = i[:2],i[2:]
    for j in P4: 
        b,b1 = j[:2],j[2:]
        
        if a == b1 or a1 ==b:
            for l in P5:
                c,c1 = l[:2],l[2:]
                if(c== a1 or c==b1) and(c1 ==a or c1 ==b):                    
                    print(i,j,l)
'''

# 다각수가 이어지는 것 순서 X
P3,P4,P5,P6,P7,P8=[],[],[],[],[],[]


for n in range(19,151):
    P3.append(str(int(n*(n+1)/2)))   #1035 ~9870
    P4.append(str(n**2))             #1024~9801
    P5.append(str(int(n*(3*n-1)/2))) #1001~9801 
    P6.append(str(n*(2*n-1)))        #1035~9730
    P7.append(str(int(n*(5*n-3)/2))) #1071 9828
    P8.append(str(n*(3*n-2)))        #1045 ~9976

def sol(Pn):
    for i in range(len(Pn)):
        if len(Pn[i]) == 4:
            break
    for j in range(len(Pn)):
        if len(Pn[j]) == 5:
            break
    Pn = Pn[i:j]
    return Pn


P3,P4,P5,P6,P7,P8 = sol(P3),sol(P4),sol(P5),sol(P6),sol(P7),sol(P8)
li =[('3',P3)]+[('4',P4)]+[('5',P5)]+[('6',P6)]+[('7',P7)]+[('8',P8)]
del P3,P4,P5,P6,P7,P8


def pro(P0,P1):
    li=[]
    for i in P0:
        a,a1 = i[:2],i[2:]
        for j in P1: 
            b,b1 = j[:2],j[2:]
            if a == b1 :
                li.append([i,j,a,a1,b])
            if a1 ==b:
                li.append([j,i,a1,b1,a])
                        
    return li

dic={}
for i in range(len(li)):
    for j in range(i):
        
        dic[li[j][0]+li[i][0]] = pro(li[i][1],li[j][1])

#st = ['3','4','5','6','7','8'] 
st=[]           
li =set()

for i in dic.keys():
    for j in dic.keys():
        for l in dic.keys():
            if i!=j and j!=l and l!=i:
                for a in range(2):
                    li.add(i[a])
                    li.add(j[a])
                    li.add(l[a])
           
            if len(li) == 6:
                
                for a in dic[i]:
                    for b in dic[j]:
                        for c in dic[l]:
                            if (a[3] == b[4]) :
                                if (a[4] == c[3]) and (b[3] ==c[4]):
                                    pp= [a[0],a[1],b[0],b[1],c[0],c[1]]
                                    pp.sort()                                
                                    break
            li.clear()

list_a = map(int, pp)
s = sum(list_a)
                                
                            
                                    


'''            
['1024', '2415', '24', '10', '15'] a[3] ==c [4]
['1536', '3628', '24', '15', '28'] a[4] == b[3]
['2841', '4110', '41', '28', '10'] b[4] = c[3]
'''


