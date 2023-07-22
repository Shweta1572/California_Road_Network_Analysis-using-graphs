import matplotlib.pyplot as plt
from pandas import *
data=read_csv("clustering_coeff.csv")
x=data['clustering_coefficient'].tolist()
y=data['time_taken'].tolist()


plt.scatter(x,y,c="blue")
plt.xlabel=("Clustering Coefficient")
plt.ylabel=("Time Takein in sec")
plt.show()
