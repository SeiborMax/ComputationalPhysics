import pylab as pl
import math as ma
class beita:
    def __init__(self,ba=2.05,gms=1,vx0=0,x0=-0.5,y0=0,dt=0.01,tt=20):
        self.vx=[vx0]
        self.vy=[(0.55/gms)**(0.5-0.5*ba)]
        self.x=[x0]
        self.y=[y0]
        self.ba=ba
        self.t=0
        self.tt=tt
        self.dt=dt
        self.r=0.5
        self.the=ma.pi
        self.f=0
        self.gg=gms
        self.s=0
        self.c=0
    def run(self):
        while(self.t <self.tt):
            self.s=self.y[-1]/self.r
            self.c=self.x[-1]/self.r
            self.f=-self.gg*self.r**(-self.ba)
            self.vx.append(self.vx[-1]+self.f*self.c*self.dt)
            self.x.append(self.x[-1]+self.vx[-1]*self.dt)
            self.vy.append(self.vy[-1]+self.f*self.s*self.dt)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt)
            self.r=ma.sqrt(self.x[-1]*self.x[-1]+self.y[-1]*self.y[-1])
            self.t+=self.dt
    def show_results(self):
        pl.plot(self.x, self.y)
        pl.xlabel('x ')
        pl.ylabel('y ')
        pl.title('b=2.05')
        pl.show()
a = beita()
a.run()
a.show_results()