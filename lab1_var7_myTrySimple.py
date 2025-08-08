from scipy.optimize import fmin_powell
import numpy as np

def f(x):
    return x*x

def whole_function(x1, x2):
    #return (8-x1)**2 - (7-x2)**2 + 3*(x2**2)
    return (8-x1)**2 - (7-x2)**2 + 3*(x2**4)

def f2(X):
    #return (8-x1)**2 - (7-x2)**2 + 3*(x2**2)
    x1=X[1-1]
    x2=X[2-1]
    y=(8-x1)**2 - (7-x2)**2 + 3*x2**4
    return y




#def main():

x1 = -3
x2 = 5
#eps = 0.001

InitialGuess=np.array([x1,x2])

#result=fmin_powell(f, -1)#so works
#result=fmin_powell(whole_function, InitialGuess)
#result=fmin_powell(whole_function, [x1, x2])
result=fmin_powell(f2, InitialGuess)


print result
