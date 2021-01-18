#삼각단어개수구하기
#일단 파일처리부터

f = open("C:\파이썬\words.txt",'r')
data = f.read()
data = data.replace('"','')
data = data.split(",")


f.close()
nlist = []
for n in range(1,30):
    nlist.append(n*(n+1)/2)
print(nlist)
thr=0
for i in range(len(data)):
    p = data[i]
    p = list(p)
    sum = 0
    for a in range(len(p)):
        sum +=ord(p[a])
    sum -=len(p)*64
    for n in range(len(nlist)):
        if sum == nlist[n] : thr +=1
        
    
    
print(thr)
