import copy
li = []
dic ={}
for n in range(1,10):
    Un =1+ n**2 + n**4+ n**6 + n**8 + n**10
    Un -= n+n**3+n**5+n**7+n**9
    
    li.append(Un)
    dic[n] = copy.deepcopy(li)