import pylab as pl
import math as ma
xt=21631
yt=0
g=9.8
def f1(v0): 
    dt=0.05
    x=0
    y=0
    ra=th*ma.pi/180
    a=ma.cos(ra)
    b=ma.sin(ra)
    vx =a*v0
    vy =b*v0
    while not(y<yt and d<0):
        v1=ma.sqrt(vx*vx+vy*vy)
        vx=vx-vx*v1*dt *0.00004
        x=x+vx*dt
        vy=vy-g*dt- vy*v1*dt*0.00004
        e=y
        y=y+vy*dt
        d=y-e
    return x
def f2(theta):
    global th
    th=theta
    v=600
    x=0
    y=0
    while not(abs(xt-x)<0.001*xt):
        v=v+1
        x=f1(v)
    return v
i=30
tt=50
th1=[i]
vm=[f2(i)]
while not(i>=tt):
    i=i+0.5
    th1.append(i)
    vm.append(f2(i))
print('v_min=',min(vm))
print('theta=',th1[vm.index(min(vm))])
pl.scatter(th1,vm,s=5)
pl.xlabel('theta ($°$)')
pl.ylabel('v ($m/s$)')
pl.show()