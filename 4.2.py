import pylab as pl
import math as ma

g=9.8
l=9.8
q=0.5
od=2/3
dt=0.1
fd=1
w=[0.]
t=[0.]

def f1(th):
    the=[th]
    while(t[-1]<=20):
        w.append(w[-1]-((g/l)*ma.sin(the[-1])-q*w[-1]+fd*ma.sin(od*t[-1]))*dt)
        the.append(the[-1]+w[-1]*dt)
        while the[-1]>=ma.pi:
            the[-1]=the[-1]-2*ma.pi
        while the[-1]<=-ma.pi:
            the[-1]=the[-1]+2*ma.pi
        t.append(t[-1]+dt)
    return t,the
(t,the)=f1(0.2)
pl.plot(t,the,label='theta= %.2f'%(0.2))
pl.legend(loc=2)
pl.xlabel('time ($s$)')
pl.ylabel('theta ')
pl.show()