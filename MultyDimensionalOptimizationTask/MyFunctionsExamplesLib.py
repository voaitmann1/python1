def signum(x, z=0):
    if x==0:
        y=z
    else:
        y=x/abs(x)
    return 

def eq1(X):
    x1=X[1-1]
    x2=X[2-1]
    y=x1**3 - 3*x1*x2 + x2**2 -(-1)
    return y

def eq2(X):
    x1=X[1-1]
    x2=X[2-1]
    y=3*x1**2 + 4*x1*x2 + x2**3 - 63 
    return y

def fIniX(N):
    if N==2:
        X=[0, 0]
    elif N==5:
        X=[-1, 0]
    elif N==7:
        X=[-3, 5]
    elif N==10:
        X=[0, 0]
    elif N==13:
        X=[-12, 17]
    elif N==18:
        X=[0, 0]
    elif N==19:
        X=[-1, 0]
    elif N==24:
        X=[-1, 2]
    elif N==30:#Rosenbrock?
        X=[0, 0]#
    elif N==40:#MySys
        X=[3, 5]#

def functionToOptimize(X, N):
    x1=X[1-1]
    x2=X[2-1]
    if N==2:
        y = (5-2*x1)**8 + (6-3*x2)**4
    elif N==5:
        y = (1-x1)**2 + (2-x2)**2 + 0.01*x1*x2
    elif N==7:
        y = (81-x1)**2 - (7-x2)**2 + 3*x2**4
    elif N==10:
        y = 2*x1**2 + 4*x1*x2**3 - 10*x1*x2 + x2**3
    elif N==13:
        y = 22*(abs(x1))**7 + 24*(x1**3)*x2**6 - x1*x2 + x2**3
    elif N==18:
        y = 3 - 3.3*x1 - 1.1*x1**2 + 3*x1**2 + 4*x2**2
    elif N==19:
        y = (1-x1)*2 + (2-x2)**2 - (x1**(-1))*x2**2
    elif N==24:
        y = 6*x1**(-2) + 2*x2**8 - 6*x1*x2 + 8*x2**4
    elif N==30:#Rosenbrock?
        y = (1-x1)**2 + 100*(x2-x1**2)**2
    elif N==40:#MySys
        y = abs(eq1(X))+abs(eq2(X))
    return y

def fDeriv1ByX1(X, N):
    x1=X[1-1]
    x2=X[2-1]
    if N==2:
        y = 16*(2*x1-5)**7
    elif N==5:
        y = 2*x1+0.001*x2-2
    elif N==7:
        y = 2*x1-162
    elif N==10:
        y = 4*x2**3 - 10*x2 + 4*x1
    elif N==13:
        #y = 7*signum(x1)*(abs(x1))**6 - x2 + 72*(x1**2)*(x2**6)
        y = 7*(x1**6) - x2 + 72*(x1**2)*(x2**6)
    elif N==18:
        y = 6*x1-3.3
    elif N==19:
        y = 2*x1 + x2**2/(x1**2) - 2
    elif N==24:
        y = -6*x2 - 12/x1**3
    elif N==30:#Rosenbrock?
        y=2*x1-400*(x2 - x1**2)
    elif N==40:#MySys
        y=3*x1**2 + 2*x1 + x2
    return y

def fDeriv1ByX2(X, N):
    x1=X[1-1]
    x2=X[2-1]
    if N==2:
        y = 12*(3*x2-6)**3
    elif N==5:
        y = 2*x2+0.01*x1-4
    elif N==7:
        y = 12*x2**3 - 2*x2 + 14
    elif N==10:
        y = 12*x1*x2**2 - 10*x1 + 3*x2**2
    elif N==13:
        y = 144*(x1**3)*(x2**5) - x1 + 3*x2**2
    elif N==18:
        y = 8*x2-1.1
    elif N==19:
        y = 2*x2 - 2*x2/x1 - 4
    elif N==24:
        y = 16*x2**7+32*x2**3-6*x1
    elif N==30:#Rosenbrock?
        y=200*x2-200*x1**2
    elif N==40:#MySys
        y=(3*x2**2 + 2*x2 + x1
    return y

def fDeriv2ByX1Twice(X, N):
    x1=X[1-1]
    x2=X[2-1]
    if N==2:
        y = 224*(2*x1-5)**6
    elif N==5:
        y = 2
    elif N==7:
        y = 2
    elif N==10:
        y = 4
    elif N==13:# abs ignored
        y = 42*x1**5+144*x1*x2**6
    elif N==18:
        y = 6
    elif N==19:
        y = 2-2*x2**2/(x1**3)
    elif N==24:
        y = 36/x1**4
    elif N==30:#Rosenbrock?
        y=1200*x1**2 - 400*x2 + 2
    elif N==40:#MySys
        y=6*x1+2
    return y

def fDeriv2ByX2Twice(X, N):
    x1=X[1-1]
    x2=X[2-1]
    if N==2:
        y = 108*(3*x2-6)**2
    elif N==5:
        y = 2
    elif N==7:
        y = 36*x2**2 - 2
    elif N==10:
        y = 6*x2 + 24*x1*x2
    elif N==13:# abs ignored
        y = 720*(x1**3)*(x2**4)  + 6*x2
    elif N==18:
        y = 8
    elif N==19:
        y = 2 - 2/x1
    elif N==24:
        y = 112*x2**6+96*x2**2
    elif N==30:#Rosenbrock?
        y=200
    elif N==40:#MySys
        y=6*x2 + 2
    return y
