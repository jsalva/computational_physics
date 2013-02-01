#! /bin/python

def example_plot():
     from pylab import plot,show
     x = [ 0.5, 1.0, 2.0, 4.0, 7.0, 10.0 ]
     y = [ 1.0, 2.4, 1.7, 0.3, 0.6, 1.8 ]
     plot(x,y)
     show()

def trig_plot():
     from pylab import plot,ylim,xlabel,ylabel,show
     from numpy import linspace,sin,cos,sqrt
     x = linspace(0,10,100)
     y1 = sin(x)
     y2 = cos(x)
     plot(x,y1,"k-")
     plot(x,y2,"k--")
     ylim(-1.1,1.1)
     xlabel("x axis")
     ylabel("y = sin x or y = cos x")
     show()

def iterative_sin_plot():
     from pylab import plot,show
     from math import sin
     from numpy import linspace
     xpoints = []
     ypoints = []
     for x in linspace(0,10,100):
          xpoints.append(x)
          ypoints.append(sin(x))
     plot(xpoints,ypoints)
     show()


