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

def moving_average(arr, window):
     from numpy import NaN,array,hstack
     moving_avg = array([])
     for i = range(window):
          moving_avg = hstack([moving_average, NaN])
     for i = range(window,len(arr)):
          


def sunspots():
     from pylab import show,plot
     from numpy import genfromtxt
     sun_spot_data = genfromtxt('sunspots.dat')
     month = sun_spot_data[:,0]
     num_spots = sun_spot_data[:,1]
     
     plot(month,num_spots,'ko')
     plot(month,running_average,'k--')
     show()
