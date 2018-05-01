import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import leastsq
X= np.array([0,1,2,3,-1,-2,-3])
Y= np.array([-1.22,1.85,3.22,10.29,2.21,3.72,8.7])
plt.figure(figsize=(4,4))
def func(p,x):
    a,b,c=p
    return a*x**2+b*x+c
def wucha(p,x,y):
    return func(p,x)-y
p0=[4,2,9]
Para=leastsq(wucha,p0,args=(X,Y))
a,b,c=Para[0]
plt.scatter(X,Y,color="r")
x=np.linspace(-5,5,1000)
y=a*x**2+b*x+c
plt.plot(x,y,color="b")
plt.legend()
plt.show()
