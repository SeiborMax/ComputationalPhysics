import pylab as pl
import math as ma
class cannon:
    def __init__(self,g=9.8, time_step=0.1,v0=700,x0=0,y0=0,theta=45):
        ra=theta*ma.pi/180
        self.g=g
        self.vx =ma.cos(ra)*v0
        self.vy =[ma.sin(ra)*v0]
        self.x = [x0]
        self.y = [y0]
        self.dt = time_step  
        print("theta -> ", theta)
        print("initial_velocity -> ", v0)
    def run(self):
        while(self.y[-1] >= 0):
            self.x.append(self.x[-1]+self.vx*self.dt)
            self.vy.append(self.vy[-1]-self.g*self.dt)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt)
    def show_results(self):
        font = {'family': 'serif',
                'color':  'darkred',
                'weight': 'normal',
                'size': 16,
        }
        pl.plot(self.x, self.y)
        pl.title('Cannon without air drag', fontdict = font)
        pl.xlabel('x ($m$)')
        pl.ylabel('y ($m$)')
        pl.show()
a = cannon()
a.run()
a.show_results()