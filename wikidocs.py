'''1~10
print("Hello World")    #1

print("Mary's cosmetics")   #2

print('신씨가 소리 질렀다. "도둑이야"') #3

print("C:\Windows") #4

print("안녕하세요.\n만나서\t\t반갑습니다.") #5 \n은 줄바꿈 \t는 탭

print("오늘은","일요일") #6 예상: ,로 인해 한 칸 띄우기

+   ,를 쓰면 띄어쓰기가 되어 출력되는데 sep을 사용하면 띄어쓰기 대신 다른 문자를 넣을 수 있음
ex)print("010","1234","5678", sep="-") #출력: 010-1234-5678

print("naver;kakao;sk;samsung") #7 
print('naver','kakao','sk','samsung',sep=';')

print('naver','kakao','sk','samsung',sep= '/')

 end='' or ""는 앞에 있는 것으 출력 후 마지막에 무엇을 쓸지 정해줌 
 원래 end='\n'이 되있어서 한 줄 띄우기 됨
print("first",end='/');print("second") #9

print(5/3) #10

 #11~20

#11
삼성전자 = 50000
총평가금액 = 삼성전자*10
print(총평가금액)

바인딩(Binding) 이란 프로그램의 어떤 기본 단위가 가질 수 있는 구성요소의 구체적인 값, 성격을 확정하는 것
 C에서는 int n =12 ->정적 바인딩 이름, 자료형, 자료값에 각각 num, int, 123 이라는 구체적인 값을 할당하는 각각의 과정
 파이썬처럼 n = 12 ->동적 바인딩 되는 변수를 동적 변수

#12
시가총액 = 2980000
현재가=50000
PER=15.79
print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))

#13
s = "hello"
t = "python"
print(s,t,sep="! ") #print(s+"!", t)

#15
a = "132"
print(type(a))

#16
num_str = "720"
num_int = int(num_str)

#17
num= 100
str_n = str(num)

#18
str_n= "15.79"
flo_n = float(str_n)

#19
year= "2020"
year= int(year)
print(year-2,year-1,year)

#20
money_m = 48584
no_in= 36
total = money_m*no_in

21~30
letters = 'python'
print(letters[0],letters[2])

license_plate = "24가 2210"
print(license_plate[-4:])

string ="홀짝홀짝홀짝"
for i in range(0,len(string),2):
    print(string[i],end='')
or print(string[::2])    

뒤집기 ★
string = "PYTHON"
print(string[::-1])

phone_number = "010-1111-2222"
print(phone_number.replace('-',' '))

url = "http://sharebook.kr"
domain = url.split('.')
print(domain[-1])

★문자열은 수정할 수 없습니다.
lang = 'python'
lang[0] = 'P'
print(lang)

string = 'abcdfe2a354a32a'
print(string.replace('a',"A"))

string = 'abcd'
print(string.replace('b','B'))

#35 ★★ formatting
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print("이름:",name1,"나이:",age1)
print("이름: %s 나이: %s"%(name2,age2))
print(f"이름: {name1} 나이: {age2}")
print("이름: {} 나이 : {}".format(name2,age1))

y,m,d = 2019,8,4
str1 = "오늘은 %d년 %d월 %d일" % (int(y), int(m), int(d))
str2 = "오늘은 %s년 %s월 %s일" % (y,m,d)
str3 = "오늘은 {0}년 {1}월 {2}일".format(y,m,d)
str4 = "오늘은 {year}년 {month}월 {day}일".format(year=y,month=m,day=d)Z
str5 = f"오늘은 {y}년 {m}월 {d}일"

상장주식수 = "5,969,782,550"
상장=int(상장주식수.replace(",",''))

분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

#40
data = "   삼성전자    "
print(data.strip())

'''

https://wikidocs.net/78558







