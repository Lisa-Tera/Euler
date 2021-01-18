number = 150
      
list = [1,2,5,10,20,50,100,200]





#50 904
#100 8222
'''
for y in range(150//list[4]+1):
    for z in range(150//list[3]+1):
        for c in range(150//list[2]+1):
            for b in range(150//list[1]+1):
                for a in range(150+1):
                    n = list[0]*a +list[1]*b +list[2]*c +list[3]*z +list[4]*y 
                    if n == number : total+=1
                    '''
               
values = [1, 2, 5, 10, 20, 50, 100, 200]
def ww(total, max_value):
    if total == 0:
        return 1
    temp = 0
    for v in values:
        if v <= max_value and total >= v:
            print(total-v,v,'qqqqqqq')
            temp += ww(total - v, v)
    return temp
print(ww(5, 5))


'''
list = [1,2,5,10,20,50,100,200]
def fun(total,max_value):
    if total == 0:
        return 1
    temp = 0
    for i in list:
        if i <= max_value and total >=i:
            '''
