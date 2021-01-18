def pen(n):
    s_n = list(set(list(str(n))))
    if len(s_n) == len(str(n))  : return True
    return False

def pen2(n):
    st_li= list(map(int, str(n)))
    st_li.sort()
    return st_li
    
def multi(n):
    li = []
    for i in range(2,7):
        if pen2(n*i) == pen2(n): li.append(i)
            
    if len(li) == 5:
        print(li)
        return True
    return False

a=125874
while True:
    if pen(a):
        if multi(a):
            print(a)

            break
    a +=1
