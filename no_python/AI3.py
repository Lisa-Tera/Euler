
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = [[2, 0], [4, 0], [6, 0], [8, 1], [10, 1], [12, 1], [14, 1]]

x_data = [x_row[0] for x_row in data]
y_data = [y_row[1] for y_row in data]
a,b,lr =0, 0, 0.05

def sigmoid(x):
    return 1/(1+np.e**(-x))
        
for i in range(2001):
    for x_data, y_data in data:
        a_diff = x_data * (sigmoid(a*x_data + b) - y_data)
        b_diff =sigmoid(a*x_data + b) - y_data
        a = a - lr * a_diff
        b = b - lr * b_diff
        if i % 1000 == 0:   
          print("epoch=%.f, 기울기=%.04f, 절편=%.04f" % (i, a, b))
plt.scatter(x_data, y_data) # 앞서 구한 기울기와 절편을 이용해 그래프18.19.
plt.xlim(0, 15)
plt.ylim(-.1, 1.1)
x_range = (np.arange(0, 15, 0.1)) #그래프로 나타낼 x값의 범위를 정합니다.
plt.plot(np.arange (0, 15, 0.1), np.array([sigmoid(a*x + b) for x in x_range]))
plt.show()
'''    
x = [i[0] for i in data]
y = [i[1] for i in data]
x_1=statm.add_constant(x)
results=statm.OLS(y,x_1).fit()
hour_class=pd.DataFrame(x, columns=['study_hours','private_class'])
hour_class['Score']=pd.Series(y)
model = statfa.ols(formula='Score ~ study_hours + private_class', data=hour_class)
results_formula = model.fit()
a, b = np.meshgrid(np.linspace(hour_class.study_hours.min(),hour_class.study_hours.max(),100),
       np.linspace(hour_class.private_class.min(),hour_class.private_class.max(),100))
x_ax = pd.DataFrame({'study_hours': a.ravel(), 'private_class': b.ravel()})
fittedY=results_formula.predict(exog=x_ax)
fig = plt.figure()
graph = fig.add_subplot(111, projection='3d')
graph.scatter(hour_class['study_hours'],hour_class['private_class'],hour_class['Score'],c='blue',marker='o', alpha=1)
graph.plot_surface(a,b,fittedY.values.reshape(a.shape),rstride=1, cstride=1, color='none', alpha=0.4)
graph.set_xlabel('study hours')
graph.set_ylabel('private class')
graph.set_zlabel('Score')
graph.dist = 11
plt.show()
'''