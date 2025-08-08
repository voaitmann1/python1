from scipy.optimize import fmin_powell
import numpy as np
import copy

CaucheeN=1

MethodN=CaucheeN

def functionToTest(X):
    x1=X[1-1]
    x2=X[2-1]
    y=abs((5-2*x1)**8 - (6-3*x2)**4)
    #y=(5-2*x1)**8 - (6-3*x2)**4
    #print("f("+str(x1)+", "+str(x2)+")="+str(y)) 
    return y

def deriv1ByX1(X):  
    x1=X[1-1]
    x2=X[2-1]
    return 16*(2*x1-5)**7

def deriv1ByX2(X):  
    x1=X[1-1]
    x2=X[2-1]
    return 12*(3*x2-6)**3

def fXNew_Cauchee(alfa, X0):
    x1_0=X0[1-1]
    x2_0=X0[2-1]
    CalcF1=deriv1ByX1(X0)
    CalcF2=deriv1ByX2(X0)
    x1_1=x1_0-alfa*CalcF1
    x2_1=x2_0-alfa*CalcF2
    X1=[x1_1,x2_1]
    #print('fXNew_Cauchee: x1_0=',x1_0,' x2_0=',x2_0,' CalcF1=',CalcF1,' CalcF2=',CalcF2,' x1_1=',x1_1,' x2_1=',x2_1)
    return X1

def fXNew(alfa, X0):
    y=0
    global MethodN
    if MethodN==CaucheeN:
        y=fXNew_Cauchee(alfa, X0)
    return y

def fAlfaToOptimize(alfa, X0):
    X1=fXNew(alfa, X0)
    #print('fAlfaToOptimize: X0=',X0,' alfa=',alfa,' X=',X1)
    return functionToTest(X1)

#def fAlfaToOptimize(P):
#    print("fAlfaToOptimize starts working P=", P) 
#    alfa=P[1-1]
#    print("alfa=", alfa)
#    X0=P[2-1:]
#    print("X0=", X0)
#    X1=fXNew(alfa, X0)
#    print("fAlfaToOptimize finishes working P=", P)
#    return functionToTest(X1)

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

class MyItersPrecisionConfig:
    def __init__(self):
        self.precX=0.001
        self.precY=0.001
        self.QIters=100
    #
    def __str__(self):
        return "Stop iterations when reached: precX="+str(self.precX)+" precX="+str(self.precX)+" QIters="+str(self.QIters)
    #    
    def setPrecX(self, precX):
        self.precX=precX
    def setPrecY(self, precY):
        self.precY=precY
    def setQIters(self, QIters):
        self.QIters=QIters
    #
    def getPrecX(self):
        return self.precX
    def getPrecY(self):
        return self.precY
    def getQIters(self):
        return self.QIters
            

def MyOptimCauchee(func, X_ini_guess, cfg, vsh=0):
    Xprev=copy.deepcopy(X_ini_guess)
    itersCount=0
    contin=1
    while contin==1:
        itersCount+=1
        alfa=fmin_powell(fAlfaToOptimize, 0.5, (Xprev,))
        Xnext= fXNew(alfa, Xprev)
        x1=Xnext[1-1]
        x2=Xnext[2-1]
        print("Iterations:{}, x1 = {}, x2 = {}, alfa = {}, func = {}".format(
        itersCount, x1, x2, alfa, functionToTest(Xnext)))
        if abs(functionToTest(Xnext))<cfg.getPrecY() or fCompareX(Xprev, Xnext, cfg.getPrecX())==1 or itersCount>=cfg.getQIters():
            contin=0
        Xprev=Xnext

def main():
    X_ini_guess=[3, 2]
    config=MyItersPrecisionConfig()
    y=MyOptimCauchee(functionToTest, X_ini_guess, config)
    #
    print('\n\nChecking:\n')
    #result=fmin_powell(functionToTest, (np.array(X_ini_guess),))
    #result=fmin_powell(functionToTest, X_ini_guess)
    result=fmin_powell(functionToTest, np.array(X_ini_guess))
    print result
    #
    print('Done successfully')

if __name__ == '__main__':
    main()
        
        
