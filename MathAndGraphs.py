import math
import copy

import MyLib#.py

import numpy as Math1
import scipy as Math2
import matplotlib as Math3
# from mpmath import * # says no module named so

#from matplotlib.pylab import *

from Math3 import * #No module named Math3.pylab
plot([1,-2,4,8,7,-3,5,3],linewidth=3); 
show()    # следующее окно слева 


f=lambda x: sin(x)/x 
#Math3.pylab.plot(f, [-24, 24])
#matplotlib.pylab.plot(f, [-24, 24])
plot(f, [-24, 24])
