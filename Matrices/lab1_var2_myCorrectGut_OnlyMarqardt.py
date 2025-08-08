from scipy.optimize import fmin_powell
import numpy as np
import copy
import math

Cauchee_MethodN=1
Newton_MethodN=2
NewtonMod_MethodN=3
Marquardt_MethodN=4
FlatcherRivs_MethodN=5
DavidonFlatcherPowell_MethodN=6

ChosenMethodN=Marquardt_MethodN#FlatcherRivs_MethodN
vsh=0#1#Vals to Show or Hide


def CheckIfNotZeroLine(X, N):
    IsNotZero=0
    L=0
    if(N>=1 and N <=len(X)):
        line=X[N-1]
        L=len(line)
        for i in range(1, L+1):
            x=line[N-1]
            if(x!=0):
                IsNotZero=1
    return IsNotZero

def GetIdentityMatrix(order):
    row=[]
    M=[]
    for i in range(1, order+1):
        row=[]
        for j in range(1, order+1):
            if i==j:
                val=1
            else:
                val=0
            row.append(val)
        M.append(row)
    return np.array(M)

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

def deriv2ByX1(X):  
    x1=X[1-1]
    x2=X[2-1]
    return 224*(2*x1-5)**6

def deriv2ByX2(X):  
    x1=X[1-1]
    x2=X[2-1]
    return 108*(3*x2-6)**2

def deriv2ByX2X1(X):  
    x1=X[1-1]
    x2=X[2-1]
    return 0

def deriv2ByX1X2(X):  
    x1=X[1-1]
    x2=X[2-1]
    return 0

def fGradient(X):
    R=[]
    x1=X[1-1]
    x2=X[2-1]
    d1X1=deriv1ByX1(X)
    d1X2=deriv1ByX2(X)
    R=np.array([d1X1, d1X2])
    return R

def fVectModule(vectExt):
    print()
    vect=copy.deepcopy(vectExt)
    vect=copy.deepcopy(vectExt)
    L=0
    dims=len(vect)
    for i in range(1, dims+1):
        L=L+vect[i-1]*vect[i-1]
    L=math.sqrt(L)
    return L
        

def Hessian(X):
    R=[]
    x1=X[1-1]
    x2=X[2-1]
    d2X1=deriv2ByX1(X)
    d2X2=deriv2ByX2(X)
    d2X1X2=deriv2ByX1X2(X)
    d2X2X1=deriv2ByX2X1(X)
    line1=[d2X1, d2X1X2]
    line2=[d2X2X1, d2X2]
    col1=[d2X1, d2X2X1]
    col2=[d2X1X2, d2X2]
    R=np.array([line1, line2])
    return R

def fXNewMarquardt(alfa, X, vsh=0):
    if vsh==1:
        print("fXNewMarquardt srarts working")
    Xprev=copy.deepcopy(X)
    Xnext=copy.deepcopy(Xprev)
    I=GetIdentityMatrix(len(Xprev))
    s=[]
    order=len(X)
    g=fGradient(Xprev)
    neg=g*(-1)
    H=Hessian(Xprev)
    detH=np.linalg.det(H)
    if vsh==1:
        print("Xprev=",Xprev)
        print("gradient=",g,"; -gradient=",neg)
        print("H=",H)
        print("detH=",detH)
    if(detH==0):
        if vsh==1:
            print("!!! det=0! Xnext=Xprev")
        for i in range(1, order+1):
            s.append(0)
        if len(neg)==2:
            if vsh==1:
                print("L=2. -g=",neg)
            if neg[1-1]==0 and neg[2-1]==0:
                if vsh==1:
                    print("all components of gradient are equal to 0")
                pass# grad =0 ,function doesn't change
            elif CheckIfNotZeroLine(H, 2)==0:
                s[1-1]=1.0*neg[1-1]/(H[1-1][1-1]+alfa)
            elif CheckIfNotZeroLine(H, 1)==0:
                s[2-1]=1.0*neg[2-1]/(H[2-1][2-1]+alfa)
    else:
        A=H+I*alfa
        s=np.linalg.solve(A, neg)
    #s=s*alfa
    Xnext=np.add(Xprev, s)
    if vsh==1:
        print("s=",s," Xnext=",Xnext)
        print("fXNewMarquardt finishes working")
    return Xnext

def fXNew(alfa, X0, d=[], vsh=0):#
    XNew=0
    global ChosenMethodN
    if ChosenMethodN==Marquardt_MethodN:
        XNew=fXNewMarquardt(alfa, X0)
    return XNew


def fAlfaToOptimize(alfa, X0, d=[], vsh=0):
    X1=fXNew(alfa, X0, d, vsh)
    print('fAlfaToOptimize: X0=',X0,' alfa=',alfa,' X=',X1,' d=',d," vsh=", vsh)
    return functionToTest(X1)

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
        self.precX=0.001# self.precX=0.001 #2.69 2.607 2.58 2.55
        self.precY=0.00000001# self.precY=0.001 #2.69 2.64 2.607 2.58 2.56 2.55
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
            


def MyOptimMarquardt(func, X_ini_guess, cfg, vsh=0):
    Xprev=copy.deepcopy(X_ini_guess)
    alfa=10000
    #if vsh==1:
    print("MyOptimMarquardt starts working")
    print("X_ini_guess = ",Xprev)
    itersCount=0
    continIterationsSuccession=1
    while continIterationsSuccession==1:
        itersCount+=1
        #if(vsh==1):
        print("Iteration: "+str(itersCount)+" Xhrev= ",Xprev)
        continSingleIteration=1
        subIterCount=0
        while continSingleIteration==1:
            subIterCount+=1
            Xnext= fXNew(alfa, Xprev)
            fprev=func(Xprev)
            fnext=func(Xnext)
            if(vsh==1):
                print("alfa="+str(alfa)," Xprev=",Xprev," Xnext=",Xnext," fprev=",fprev," fnext=",fnext)
            if fnext<fprev:
                continSingleIteration=0
                alfa*=0.5
                if(vsh==1):
                    print("fnext<fprev. Now alfa="+str(alfa)+" coming to next iteration")
            else:
                alfa*=2
                if(vsh==1):
                    print("fnext is NOT < fprev. Now alfa="+str(alfa)+" continuing current iteration")
            if subIterCount>cfg.getQIters():
                continSingleIteration=0
                if(vsh==1):
                    print("too big QSteps at current iteration: "+str(subIterCount)+". Interrupting iteration")
        #
        cond_gradient=(abs(fVectModule(fGradient(Xnext)))<cfg.getPrecY())
        cond_X_small1=(abs(fVectModule(np.subtract(Xprev, Xnext))<cfg.getPrecY()))
        cond_X_small2=(fCompareX(Xprev, Xnext, cfg.getPrecX())==1)
        cond_iters=(itersCount>=cfg.getQIters())
        if vsh==1:
            print("cond_gradient="+str(cond_gradient)+"cond_X_small1="+str(cond_X_small1)+"cond_iters="+str(cond_iters))
        cond_stop=cond_gradient or cond_X_small1 or cond_iters
        if vsh==1:
            print("cond_stop="+str(cond_stop))
        if cond_gradient or cond_X_small1 or cond_iters:
            continIterationsSuccession=0
        Xprev=Xnext
        if vsh==1:
            print("now Xprev=",Xprev)
    print("answer: X=",Xnext," Iterations: ",itersCount)
    print("MyOptimMarquardt finishes working")
    return Xnext


            

def main():
    X_ini_guess=[3, 2]
    config=MyItersPrecisionConfig()
    if ChosenMethodN==Marquardt_MethodN:
        X=MyOptimMarquardt(functionToTest, X_ini_guess, config, vsh)
    print("ANSWER: ",X)
    #
    print('\n\nChecking:\n')
    result=fmin_powell(functionToTest, np.array(X_ini_guess))
    print result
    #
    print('Done successfully')

if __name__ == '__main__':
    main()
        
        
