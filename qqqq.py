# week3.py
y = input("오늘의 연도:") # y=2019
m = input("오늘의 월:") # m = 9
d = input("오늘의 일:") # d = 17
str1 ="오늘은 %d년 %d월 %d일" % ( int(y) , int(m) , int(d))
str2 ="오늘은 %s년 %s월 %s일" % (y, m, d)
str3 = "오늘은 {0}년 {1}월 {2}일".format(y, m, d)
str4 = "오늘은 {year}년 {month}월 {day}일".format(year=y,month=m,day=d)
str5 = f"오늘은 {y}년 {m}월 {d}일"

print(str1)
print(str2)
print(str3)
print(str4)
print(str5)





