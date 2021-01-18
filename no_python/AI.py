
from sklearn.linear_model import LinearRegression 


x = [[3],[6],[7],[9],[10],[12],[15],[17],[18],[21]]
y =[79, 82, 80, 85 ,84, 89, 93, 90 ,96,99]

model = LinearRegression()
model.fit(x,y)

a_li = list(str(model.coef_))
for i in range(len(a_li)):
    if a_li[i] =="." :
        a =int(a_li[i-1]+a_li[i+1]+a_li[i+2])/100


        

b_li=list(str(model.intercept_))
for j in range(len(b_li)):
    if b_li[j] == ".":
        b =int(b_li[j-1]+b_li[j+1]+b_li[j+2])/100

print("기울기 a =",a)
print("y 절편 b =",b)

print("y = ",a,"x+",b)
#예상 성적 예측 14시간
y_pred=model.predict([[14]])

#성적 예측값 출력
print(y_pred)