def solution(s):
    answer = ''
    li = list(s)
    for i in range(len(li)):
        if i % 2 ==0:
            li[i] = li[i].upper()
        else :
            li[i] = li[i].lower()
    answer =''.join(li)
    return answer

s = "hi im al"
a =solution(s)