from datetime import date

dayOfTheWeek = {0:"월", 1:"화", 2:"수", 3:"목", 4:"금", 5:"토", 6:"일"}

D = 1    

D_sum =0
for y in range(1901,2001):   
    for m in range (1,13):
        DayName = date(y,m,D).weekday()
        if DayName ==6 :
            D_sum+=1

print(D_sum)

