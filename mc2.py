import numpy as np
import matplotlib.pyplot as pl

runs = 100000
sq = 0
c = 0

x = np.random.uniform(-6, 6, runs)
y = np.random.uniform(-3, 3, runs)

x_sq = []
y_sq = []
x_c = []
y_c = []

for i in range(runs):
    if ((x[i]>=-4 and x[i]<=-2) and (y[i]>=-1 and y[i]<=1)):
        sq+=1
        x_sq.append(x[i])
        y_sq.append(y[i])
    elif (((x[i]-3)**2+y[i]**2)<=4):
        c+=1
        x_c.append(x[i])
        y_c.append(y[i])
    
print(c/sq)

f = pl.figure(1)
pl.hist(x,edgecolor='black',bins=50,color='yellow')
f.show()

g = pl.figure(2)
pl.hist(y,edgecolor='black',bins=50,color='yellow')
g.show()

h = pl.figure(3)
pl.hist(x_sq)
h.show()

j = pl.figure(4)
pl.hist(y_sq)
j.show()

k = pl.figure(5)
pl.hist(x_c)
k.show()

p = pl.figure(6)
pl.hist(y_c)
p.show()


input()