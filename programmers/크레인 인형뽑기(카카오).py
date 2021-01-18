#1. 입력되는 값 board, moves  구하려는 값 :결과값

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

#result = 4

#맨 위에 오는 것 부터 구하면 됨  -> 각각 리스트를 설정하자
dic_n= {}
for j in range(len(board)):
    li =[]
    for i in board :        
        if i[j] != 0 : li.append(i[j])
    dic_n[j+1] = li
li2 =[]
result =0
for i in moves:
    if len(dic_n[i]) !=0 :
        a = dic_n[i][0]
        
        if len(li2) !=0 and li2[-1] == a : 
            result +=1                    
            del li2[-1]
        else :   
            li2.append(a)
        del dic_n[i][0]

#2. n*n