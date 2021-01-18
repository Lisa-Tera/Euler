#번호가 n,n+x,n+x+y 순이다
f = open("banknumber.txt", 'r')
lines = f.readlines()
f.close()
line0,line1,line2 =[],[],[]
#dic_line0,dic_line1,dic_line2 ={1:0, 2:0, 3:0, 6:0, 7:0, 8:0},{1:0, 2:0, 3:0, 6:0, 8:0, 9:0},{0:0, 1:0, 2:0, 6:0, 8:0, 9:0}
for i in range(len(lines)):
    line0.append(lines[i][0])
    line1.append(lines[i][1])
    line2.append(lines[i][2])
    
    lines[i] = int(lines[i])



line0,line1,line2 = set(line0),set(line1),set(line2)
#print(line0,line1,line2)

'''
6*5*4 / 3*2
5*4*3 / 3*2
4*3*2 / 3*2

최소  n *n-1*n-2 >300 ---> 8자리이상
                            01236789
                            
                            
                            '''

print('1.',line0&line1,line1-line0,line0-line1,
      '\n2.',line0&line2,line2-line0,line0-line2,
      '\n3.',line1&line2,line2-line1,line1-line2)