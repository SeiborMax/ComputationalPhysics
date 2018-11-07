import pylab as pl
import math as ma
import numpy as np
def f1(n):
    x=[0]
    y=[0]
    z=[0]
    while(x[-1]<=60):
        z.append(z[-1]-(ma.sin(y[-1])+0.5*z[-1]-n*ma.sin(2/3*x[-1]))*0.01)
        y.append(y[-1]+z[-1]*0.01)
        while(y[-1]>=ma.pi):
            y[-1]=y[-1]-2*ma.pi
        while(y[-1]<=-ma.pi):
            y[-1]=y[-1]+2*ma.pi
        x.append(x[-1]+0.01)
    return x,y
r=1
while(r<=2):
    (x,y)=f1(r)
    r+=0.5
    pl.plot(x,y)
pl.show
