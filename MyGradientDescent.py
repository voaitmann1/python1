from scipy.optimize import fmin_powell
import numpy as np
import copy



def functionToTest(X):
    x1=X[1-1]
    x2=X[2-1]
    y=abs((5-2*x1)**8 - (6-3*x2)**4)
    #y=(5-2*x1)**8 - (6-3*x2)**4
    #print("f("+str(x1)+", "+str(x2)+")="+str(y)) 
    return y

def deriv1_byX1(X):#, func):  
    x1=X[1-1]
    x2=X[2-1]
    y=16*(2*x1-5)**7
    #if func==functionToTest:
    #    y=16*(2*x1-5)**7
    return y

def deriv1_byX2(X):#, func):  
    x1=X[1-1]
    x2=X[2-1]
    y=12*(3*x2-6)**3
    #if func==functionToTest:
    #    y=12*(3*x2-6)**3
    return y

def deriv2_byX1_2x(X):#, func):  
    x1=X[1-1]
    x2=X[2-1]
    y=224*(2*x1-5)**6
    #if func==functionToTest:
    #    y=16*(2*x1-5)**7
    return y

def deriv2_byX2_2x(X):#, func):  
    x1=X[1-1]
    x2=X[2-1]
    y=0
    #if func==functionToTest:
    #    y=12*(3*x2-6)**3
    return y

def deriv2_byX1X2(X):#, func):  
    x1=X[1-1]
    x2=X[2-1]
    y=0
    #if func==functionToTest:
    #    y=16*(2*x1-5)**7
    return y

def deriv2_byX2X1(X):#, func):  
    x1=X[1-1]
    x2=X[2-1]
    y=12*(3*x2-6)**3
    #if func==functionToTest:
    #    y=12*(3*x2-6)**3
    return y

def fHesse(X):
    d2_x1_2x=deriv2_byX1_2x(X)
    d2_x2_2x=deriv2_byX2_2x(X)
    d2_x1x2=deriv2_byX1X2(X)
    d2_x2x12=deriv2_byX2X1(X)
    M=np.array([d2_x1_2x, d2_x2x1], [d2_x1x2, d2_x2_2x])
    return M

def fXNew_gradDesc(X, gamma, alfa):
    Xnext=[]
    for i in range (1, n+1):
        #x_cd=Xprev[i-1]
        #gradcd=grad[i-1]
        contin_change_step=1
        xnew_cd=Xprev[i-1]-gamma*grad[i-1]+alfa*(Xprev[i-1]-Xprev1[i-1])
        Xnext.append(xnew_cd)
    return Xnext
    

def GradientDescent(func, X_ini_guess, params):
    gamma=params.gamma
    alfa=params.alfa
    epsX=params.epsX
    Xprev=copy.deepcopy(X_ini_guess)
    while continIter==1:
        Xnext=[]
        grad=Grad(Xprev)
        Xnext=[]
        grad=Grad(Xprev)
        fXnext=fXNew_gradDesc(X, gamma, alfa)
        if func(Xnext)>=func(Xprev) and grad > epsX:
            contin_change_step==1:
            while contin_change_step==1:
                gamma/=5
                fXnext=fXNew_gradDesc(X, gamma, alfa)
                if func(Xnext)>=func(Xprev) and grad > epsX:
                    contin_change_step=0
                
            
            
            
    
    
