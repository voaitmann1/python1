from scipy.optimize import fmin_powell
import numpy as np
import copy

Cauchee_MethodN=1
Newton_MethodN=2

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

def fXNew_Cauchee(alfa, X0, func):
    x1_0=X0[1-1]
    x2_0=X0[2-1]
    CalcF1=0
    CalcF2=0
    if func==functionToTest:
        CalcF1=deriv1_byX1(X0)
        CalcF2=deriv1_byX2(X0)
    x1_1=x1_0-alfa*CalcF1
    x2_1=x2_0-alfa*CalcF2
    X1=[x1_1,x2_1]
    #print('fXNew_Cauchee: x1_0=',x1_0,' x2_0=',x2_0,' CalcF1=',CalcF1,' CalcF2=',CalcF2,' x1_1=',x1_1,' x2_1=',x2_1)
    return X1

def fXNew_Newton(alfa, XIni, func):
    x1_0=XIni[1-1]
    x2_0=XIni[2-1]
    CalcF1=0
    CalcF2=0
    if func==functionToTest:
        CalcF1=deriv1_byX1(XIni)
        CalcF2=deriv1_byX2(XIni)
        g=np.array(CalcF1,CalcF2)
        fg=np.array(-CalcF1, -CalcF2)
        H=fHesse(XIni)
        alfa=fmin_powell(fAlfaToOptimize, 0.5, (Xprev, func, MethodN))
        d=np.solve(H, fg)
        
    x1_1=x1_0-alfa*CalcF1
    x2_1=x2_0-alfa*CalcF2
    X1=[x1_1,x2_1]
    #print('fXNew_Cauchee: x1_0=',x1_0,' x2_0=',x2_0,' CalcF1=',CalcF1,' CalcF2=',CalcF2,' x1_1=',x1_1,' x2_1=',x2_1)
    return X1

def fXNew(alfa, X0, func, MethodN):
    y=0
    if MethodN==Cauchee_MethodN:
        y=fXNew_Cauchee(alfa, X0, func)
    if MethodN==Newton_MethodN:
        y=fXNew_Newton(alfa, X0, func)
    return y

def fAlfaToOptimize(alfa, X0, func, methodN):
    X1=fXNew(alfa, X0, func, methodN)
    #print('fAlfaToOptimize: X0=',X0,' alfa=',alfa,' X=',X1)
    
    return functionToTest(X1)

def fXNew_NewtonSub(alfa, X0, d):
    X1=[]
    QDims=2
    for i in range(1, +1):
        x=X0[i-1]+alfa*d[i-1]
        X1.append(x)
    return X1


def fCompareX(X0, X1, eps):
    b=0
    for i in range(1, len(X0)+1):
        if abs(X1[i-1]-X0[i-1])>eps:
            b=1
    if b==0:
        v=1
    else:
        v=0
    return v

def MyOptimCauchee(func, X_ini_guess, cfg, vsh=0):
    Xprev=copy.deepcopy(X_ini_guess)
    if(func==functionToTest):
        print("Variant 2")
    itersCount=0
    contin=1
    MethodN=Cauchee_MethodN
    precY=cfg[1-1]
    precX=cfg[2-1]
    QItersMax=cfg[3-1]
    while contin==1:
        itersCount+=1
        print("Iter: "+str(itersCount))
        alfa=fmin_powell(fAlfaToOptimize, 0.5, (Xprev, func, MethodN))
        Xnext= fXNew(alfa, Xprev, func, MethodN)
        #
        y=func(Xnext)
        if abs(y)<precY:
            function_isSmallEnough=1
        else:
            function_isSmallEnough=0
        if fCompareX(Xprev, Xnext, precX)==1:
            CompareX_isSmallEnough=1
        else:
            CompareX_isSmallEnough=0
        if itersCount>=QItersMax:
            CountIters_isBigEnough=1
        else:
            CountIters_isBigEnough=0
        if function_isSmallEnough==1 or CompareX_isSmallEnough==1 or CountIters_isBigEnough==1:
            contin=0
        print("Iter "+str(itersCount)+") Xprev= "+str(Xprev)+"; Xnext= "+str(Xnext)+"; alfa="+str(alfa)+"; f = "+str(y)+"; f->0: "+str(function_isSmallEnough)+"; sdX->0: "+str(CompareX_isSmallEnough)+"; QIters->inf: "+str(CountIters_isBigEnough))
        Xprev=Xnext
    R=[Xnext,y]
    return R

def MyOptimNewton(func, X_ini_guess, cfg, vsh=0):
    Xprev=copy.deepcopy(X_ini_guess)
    if(func==functionToTest):
        print("Variant 2")
    itersCount=0
    contin=1
    MethodN=Newton_MethodN
    precY=cfg[1-1]
    precX=cfg[2-1]
    QItersMax=cfg[3-1]
    while contin==1:
        itersCount+=1
        print("Iter: "+str(itersCount))
        alfa=fmin_powell(fAlfaToOptimize, 0.5, (Xprev, func, MethodN))
        Xnext= fXNew(alfa, Xprev, func, MethodN)
        #
        y=func(Xnext)
        if abs(y)<precY:
            function_isSmallEnough=1
        else:
            function_isSmallEnough=0
        if fCompareX(Xprev, Xnext, precX)==1:
            CompareX_isSmallEnough=1
        else:
            CompareX_isSmallEnough=0
        if itersCount>=QItersMax:
            CountIters_isBigEnough=1
        else:
            CountIters_isBigEnough=0
        if function_isSmallEnough==1 or CompareX_isSmallEnough==1 or CountIters_isBigEnough==1:
            contin=0
        print("Iter "+str(itersCount)+") Xprev= "+str(Xprev)+"; Xnext= "+str(Xnext)+"; alfa="+str(alfa)+"; f = "+str(y)+"; f->0: "+str(function_isSmallEnough)+"; sdX->0: "+str(CompareX_isSmallEnough)+"; QIters->inf: "+str(CountIters_isBigEnough))
        Xprev=Xnext
    R=[Xnext,y]
    return R

def main():
    X_ini_guess=[3, 2]
    precY=0.001
    precX=0.001
    QItersMax=50
    config=[precY, precX, QItersMax]
    MethodN=Cauchee_MethodN
    if MethodN==Cauchee_MethodN:
        print("Cauchee MethodN")
        my_result=MyOptimCauchee(functionToTest, X_ini_guess, config)
    print("Answer: f("+str(my_result[1-1])+")="+str(my_result[2-1]))
    #
    print('\n\nChecking:\n')
    their_result=fmin_powell(functionToTest, np.array(X_ini_guess))
    print their_result
    #
    print('Done successfully')

if __name__ == '__main__':
    main()
        
        
