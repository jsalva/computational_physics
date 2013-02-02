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
    from numpy import loadtxt

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

def wave_function(wave_vector,steps):
    """this function creates interference patterns based on the   
    input wave vector. Wave vectors should be an array of values,
    one for each point in the format: [[amp,lambda,x,y],...]
    """
    
    from math import sqrt,sin,pi
    from numpy import empty
    from pylab import imshow,gray,show
    from imtools import simple_normalize
    from images2gif import writeGif

    side_cm = 100.
    points = 1000
    spacing = side_cm/points
    wave_vector = wave_vector.astype('float64')
    image_stack = []
    for step in range(steps):
        tmp_wave_vector = np.zeros(wavec.shape)
        for idx,item in enumerate(wave_vector):
            tmp_wave_vector[idx][0] = wave_vector[idx][0]
            tmp_wave_vector[idx][1] = 2.*np.pi/wave_vector[idx][1]
            tmp_wave_vector[idx][2] = (side_cm/2. + 
                step*wave_vector[idx][2])
            tmp_wave_vector[idx][3] = (side_cm/2. + 
                step*wave_vector[idx][3])

        xi = empty([points,points],float)
        for i in range(points):
            y = spacing*i
            for j in range(points):
                x = spacing*j
                xi[i,j] = 0
                for idx,item in enumerate(wave_vector):
                    r = sqrt((x-tmp_wave_vector[idx][2])**2 +
                        (y-tmp_wave_vector[idx][3])**2)
                    amp = tmp_wave_vector[idx][0]
                    k = tmp_wave_vector[idx][1]
                    xi[i,j] = xi[i,j] + amp*sin(k*r)
        image_stack.append(simple_normalize(xi))
    
    writeGif('interference.gif',image_stack,duration=0.1,dither=0)

def stm():
    from pylab import imshow,gray,show
    from numpy import loadtxt

    stm_data = loadtxt('stm.dat')
    imshow(stm_data)
    gray()
    show()

def sphere():

