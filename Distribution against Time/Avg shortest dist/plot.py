import matplotlib.pyplot as plt
x=[1,0,2.14,3.17,1.67,1.43,2.6,2.9,4.2,1.2,1.96,3.58]
y=[5,3,8,9,6,5,8,7,15,5,7,12]
for i in range(1,89):
    x.append(int(0))
for j in range(1,45):
    y.append(int(3))
for j in range(45,54):
    y.append(int(2))
for j in range(54,89):
    y.append(int(4))

plt.scatter(x,y,c="blue")
plt.xlabel=("Average Distance")
plt.ylabel=("Time in sec")
plt.show()
