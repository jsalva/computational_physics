from PIL import Image
from pylab import *

def imresize(img,size):
    """ Resize an image array using PIL. """
    pil_im = Image.fromarray(uint8(img))

    return array(pil_im.resize(size))

def histeq(img,num_bins=256):
    """ Histogram equalization of a grayscale image. """

    # get image histogram
    imghist,bins = histogram(img.flatten(),num_bins,normed=True)
    cdf = imghist.cumsum() # cumulative distribution function
    cdf = 225 * cdf / cdf[-1] # normalize

    # use linear interpolation of cdf to find new pixel values
    img2 = interp(img.flatten(),bins[:-1],cdf)

    return img2.reshape(img.shape),cdf

def compute_average(imlist):
    """ Compute the average of a list of images. """

    #open first image and make into array of type float
    averageim = array(Image.open(imlist[0]), 'f')

    for imname in imlist[1:]:
        try:
            averageim += array(Image.open(imname))
        except:
            print imname + '...skipped'
    avarageim /= len(imlist)

    # return average as uint8
    return array(averageim, 'uint8')

def simple_normalize(array):
    array = array.astype('float64')
    print [array.max(),array.min()]
    array_range = array.max() - array.min()
    array = (array - array.min())/array_range
    print [array.max(),array.min()]
    return array
    
    

