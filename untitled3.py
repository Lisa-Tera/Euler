b = [[30,40,53,10,51],[42,52,50,20,8]]


a = {0:[0,1,3] , 1 :[1,2,3]}
li = [[0, 0], [0, 1], [1, 1], [1, 2],[1, 3], [0, 3]]

li2 = []
s = 0
for i in range(5):
    s+=b[0][i]
    li2.append(s)
sa = 0
li3 = []
for i in li:
    i1,i2 =i[0] , i[1]
    sa+=b[i1][i2]
    li3.append(sa)
    
    
if li2[3] < sa:
    del a[1]