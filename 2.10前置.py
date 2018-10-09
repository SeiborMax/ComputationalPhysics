import pylab as pl
import math as ma
xt=21631
yt=0
g=9.8
dt=0.1
def lll(v0):
    x=0
    y=0
    ra=th*ma.pi/180
    vx =ma.cos(ra)*v0
    vy =ma.sin(ra)*v0
    while not(y<yt and d<0):
        v1=ma.sqrt(vx*vx+vy*vy)
        vx=vx-vx*v1*dt *0.00004
        x=x+vx*dt
        vy=vy-g*dt- vy*v1*dt*0.00004
        e=y
        y=y+vy*dt
        d=y-e
    return x
def hh(theta):
    global th
    th=theta
    v=200
    x=0
    y=0
    while not(abs(xt-x)<0.001*xt):
        v=v+1
        x=lll(v)
    return v
def show_re():
    v1=hh(30)
    v2=hh(40)
    v3=hh(50)
    v4=hh(60)
    vx1=ma.cos(30)*v1 
    vy1=ma.sin(30)*v1 
    svx1=[vx1] 
    svy1=[vy1] 
    sx1=[0] 
    sy1=[0]
    vx2=ma.cos(40)*v2 
    vy2=ma.sin(40)*v2 
    svx2=[vx2] 
    svy2=[vy2] 
    sx2=[0] 
    sy2=[0]
    vx3=ma.cos(50)*v3 
    vy3=ma.sin(50)*v3 
    svx3=[vx3] 
    svy3=[vy3] 
    sx3=[0] 
    sy3=[0]
    vx4=ma.cos(60)*v4 ;vy4=ma.sin(60)*v4 ;svx4=[vx4] ;svy4=[vy4] ;sx4=[0] ;sy4=[0]
    while not(sy1[-1] < yt and d1<0):
        v1=ma.sqrt(svx1[-1]*svx1[-1]+svy1[-1]*svy1[-1])
        svx1.append(svx1[-1]-svx1[-1]*v1*dt*0.00004)
        sx1.append(sx1[-1]+svx1[-1]*dt)
        svy1.append(svy1[-1]-g*dt-svy1[-1]*v1*dt*0.00004)
        sy1.append(sy1[-1]+svy1[-1]*dt)
        d1=sy1[-1]-sy1[-2]
    while not(sy2[-1] < yt and d2<0):
        v2=ma.sqrt(svx2[-1]*svx2[-1]+svy2[-1]*svy2[-1])
        svx2.append(svx2[-1]-svx2[-1]*v2*dt*0.00004)
        sx2.append(sx2[-1]+svx2[-1]*dt)
        svy2.append(svy2[-1]-g*dt-svy2[-1]*v2*dt*0.00004)
        sy2.append(sy2[-1]+svy2[-1]*dt)
        d2=sy2[-1]-sy2[-2]
    while not(sy3[-1] < yt and d3<0):
        v3=ma.sqrt(svx3[-1]*svx3[-1]+svy3[-1]*svy3[-1])
        svx3.append(svx3[-1]-svx3[-1]*v3*dt*0.00004)
        sx3.append(sx3[-1]+svx3[-1]*dt)
        svy3.append(svy3[-1]-g*dt-svy3[-1]*v3*dt*0.00004)
        sy3.append(sy3[-1]+svy3[-1]*dt)
        d3=sy3[-1]-sy3[-2]
    while not(sy4[-1] < yt and d4<0):
        v4=ma.sqrt(svx4[-1]*svx4[-1]+svy4[-1]*svy4[-1])
        svx4.append(svx4[-1]-svx4[-1]*v4*dt*0.00004)
        sx4.append(sx4[-1]+svx4[-1]*dt)
        svy4.append(svy4[-1]-g*dt-svy4[-1]*v4*dt*0.00004)
        sy4.append(sy4[-1]+svy4[-1]*dt)
        d4=sy4[-1]-sy4[-2]
    font = {'family': 'serif',
                'color':  'darkred',
                'weight': 'normal',
                'size': 16,
        }
    pl.plot(sx1,sy1,label='theta= %d'%(30))
    pl.plot(sx2,sy2,label='theta= %d'%(40))
    pl.plot(sx3,sy3,label='theta= %d'%(50))
    pl.plot(sx4,sy4,label='theta= %d'%(60))
    pl.title('Cannon with defferent theta', fontdict = font)
    pl.legend(loc=2)
    pl.xlabel('x ($m$)')
    pl.ylabel('y ($m$)')
    pl.show()
show_re()