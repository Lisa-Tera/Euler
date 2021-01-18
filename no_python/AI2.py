import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data= [[38,6,12], [65,27,48],[87,45,41], [92, 87,63],[89,62,54],[78,98,72]]

x1=[i[0] for i in data]
x2=[i[1] for i in data]
y=[i[2] for i in data]

x1_data = np.array(x1)
x2_data = np.array(x2)
y_data = np.array(y)
a1=0
a2=0
b=0
#print(x1_data,x2_data,y_data)

lr =0.05
epochs =2001
for i in range(epochs):
  y_pred = a1*x1_data + a2*x2_data +b
  error = y_data - y_pred
  a1_diff =  -(1/len(x1_data))*sum(x1_data*(error))
  a2_diff =  -(1/len(x2_data))*sum(x2_data*(error))
  b_new =  -(1/len(y_data))*sum(y_data- y_pred)

  a1 = a1 - lr*a1_diff
  a2 = a2 - lr*a2_diff
  b = b -lr *b_new
  
  if i %100 ==0:
    print("epoch = %.f,기울기 1 = %5.4f,기울기 2 = %5.4f,절편 = %5.4f" %(i,a1,a2,b))


