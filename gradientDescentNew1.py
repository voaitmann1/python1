import copy
import math

def orth(N, Q):
    Y=[]
    for i in range(Q):
        Y.append(0)
    Y[N]=1
return Y

def f(X):
    return X

class GradientDescentConfig:
    def __init__(self, epsY, epsX, gamma0, alfa=0, maxQIters=50):
        self.epsX=epsX
        self.epsY=epsY
        self.gamma0=gamma0
        self.gamma=gamma0
        self.alfa=alfa
        self.maxQIters=maxQIters

def Gradient(func, X, cfg):
    return X

def GradientDescentStep(func, X0, cfg):
    countIters=0
    grad=Gradient(func, X0, cfg)
    Y0=func(X0)
    X1=X0-gamma*grad*X0-alfa*X0#matrix
    Y1=func(X1)
    if math.fabs(grad)<cfg.epsY:
        pass
    else:
        while Y1>Y0:
            gamma/=5
            X1=X0-gamma*grad*X0-alfa*X0#matrix
            Y1=func(X1)
    return Y1, gamma

def GradientDescent(func, X0, cfg):
    QDims=len(X0)
    countIters=0
    contin=1
    while contin==1:
        X1, gamma=GradientDescentStep(func, X0, cfg)
        cfg.gamma=gamma
        X0=X1
        Y0=func(X0)
        X3=X0
        countIters+=1
        for i in range(QDims):
            X2=X1+0.25/100/epsX*cfg.gamma0*orth(i, QDims)#matrix
            Y2=func(X2)
            if Y2<Y0:
                X0=X2
            X2=X1+0.5/100/epsX*cfg.gamma0*orth(i, QDims)#matrix
            Y2=func(X2)
            if Y2<Y0:
                X0=X2
            X2=X1+0.75/100/epsX*cfg.gamma0*orth(i, QDims)#matrix
            Y2=func(X2)
            if Y2<Y0:
                X0=X2
            X2=X1+1/100/epsX*cfg.gamma0*orth(i, QDims)#matrix
            Y2=func(X2)
            if Y2<Y0:
                X0=X2
            #
            X2=X1-0.25/100/epsX*cfg.gamma0*orth(i, QDims)#matrix
            Y2=func(X2)
            if Y2<Y0:
                X0=X2
            X2=X1-0.5/100/epsX*cfg.gamma0*orth(i, QDims)#matrix
            Y2=func(X2)
            if Y2<Y0:
                X0=X2
            X2=X1+0.75/100/epsX*cfg.gamma0*orth(i, QDims)#matrix
            Y2=func(X2)
            if Y2<Y0:
                X0=X2
            X2=X1+1/100/epsX*cfg.gamma0*orth(i, QDims)#matrix
            Y2=func(X2)
            if Y2<Y0:
                X0=X2
        X2=X1
        for i in range(QDims):
            X2=X2+0.5/100/epsX*cfg.gamma0*orth(i, QDims)#matrix
            Y2=func(X2)
            if Y2<Y0:
                X0=X2
        X2=X1
        for i in range(QDims):
            X2=X2-0.5/100/epsX*cfg.gamma0*orth(i, QDims)#matrix
            Y2=func(X2)
            if Y2<Y0:
                X0=X2
        #    
        if countIters>=cfg.maxQIters or math.fabs(Y2-Y0)<cfg.epsY:
            contin=0
    return X3
            
