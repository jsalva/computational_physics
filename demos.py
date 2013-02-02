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

def running_average(arr, window_radius):
     from numpy import NaN,array,hstack,squeeze,average

     arr = squeeze(array(arr))
     running_avg_arr = array([])
     for i in range(window_radius):
          running_avg_arr = hstack([running_avg_arr, NaN])
     for i in range(window_radius,len(arr)):
          running_avg = average(arr[i-window_radius:i+window_radius+1])
          running_avg_arr = hstack([running_avg_arr,running_avg])
     for i in range(window_radius):
          running_avg_arr[-(i+1)] = NaN
     return running_avg_arr


def sunspots():
     from pylab import show,plot
     from numpy import genfromtxt

     sun_spot_data = genfromtxt('sunspots.dat')
     month = sun_spot_data[:,0]
     num_spots = sun_spot_data[:,1]
     running_avg = running_average(num_spots,5) 
     plot(month,num_spots,'k.')
     plot(month,running_avg,'k--')
     show()

def stars():
     from pylab import scatter,xlabel,ylabel,xlim,ylim,show
     from numpy import loadtxt,log

     data = loadtxt("stars.dat",float)
     x = data[:,0]
     y = data[:,1]
     scatter(x,y)
     xlabel("Temperature")
     ylabel("Magnitude")
     xlim(0,13000)
     ylim(-5,20)
     show()

def circular_density():
     from pylab import imshow,show,gray,xlim,ylim
     from numpy import loadtxt,pi

     data = loadtxt("circular.dat",float)
     imshow(data,origin="lower",extent=[0,pi,0,pi])
     gray()
     show()

def wave_function(vec1,vec2,separation_cm):
     from math import sqrt,sin,pi
     from numpy import empty
     from pylab import imshow,gray,show

     amp1 = vec1[0]
     wavelength1 = vec1[1]
     k1 = 2*pi/wavelength1
     amp2 = vec2[0]
     wavelength2 = vec2[1]
     k2 = 2*pi/wavelength2
     side_cm = 100.0
     points = 500
     spacing = side_cm/points

     x1 = side_cm/2 - separation_cm/2
     y1 = side_cm/2
     x2 = side_cm/2 + separation_cm/2
     y2 = side_cm/2

     xi = empty([points,points],float)
     for i in range(points):
          y = spacing*i
          for j in range(points):
               x = spacing*j
               r1 = sqrt((x-x1)**2+(y-y1)**2)
               r2 = sqrt((x-x2)**2+(y-y2)**2)
               xi[i,j] = amp1*sin(k1*r1)+amp2*sin(k2*r2)
     
     imshow(xi,origin='lower',extent=[0,side_cm,0,side_cm])
     gray()
     show()
     
     
     

