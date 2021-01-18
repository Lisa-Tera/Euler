# 제곱수를 나타내는 애너그램 쌍 찾기 
dic,dic2={},{}
fli = open('words.txt','r').read().split('","')
fli = fli[1:-1]
nli,nli2,li,li2=[],[],[],[] 
n=12
for i in fli:
    n1 = list(str(n**2))
    n2 = set(n1)
    n1.sort()
    # n1의 요소중에 3개 이상 반복 되면 리스트 추가 X
    if len(n1)- len(n2) >1:
        pass
    else: 
        nli.append(n1)   
        dic2[n**2] = n1
    n+=1
    i1 = list(i)
    i1.sort()
    li.append(i1)
    dic[i] = i1
    
    '''알파벳 개수 맞는지 확인
    for j in list(i):
        if j not in li2:
            li2.append(j)'''

li.sort()
nli.sort()
for i in range(0,len(li)-1):
    if li[i] == li[i+1]:
        li2.append(li[i])
    if i < len(nli)-1:
        if nli[i] == nli[i+1]:
            nli2.append(nli[i])


# li2의 최대 개수는 9 -> 제곱 시 8 자리수가 최대인데 아닐거 같음


