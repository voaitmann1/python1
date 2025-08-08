from scipy.optimize import fmin_powell
import numpy as np
import copy

CaucheeN=1

MethodN=CaucheeN

def writeln(vsh, data):
    if(vsh==1):
        print(str(data)+"\n")

def functionToTest(X):
    x1=X[1-1]
    x2=X[2-1]
    #y=abs((5-2*x1)**8 - (6-3*x2)**4)#tic
    #y=(5-2*x1)**8 - (6-3*x2)**4
    #print("f("+str(x1)+", "+str(x2)+")="+str(y))
    y=-x1*x1+6*x1-2*x2*x2+4*x2
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

def Gradient_and_Hesse(X, fx, delta=0.000001, vsh=0):
    writeln(vsh, "Gradient_and_Hesse starts working")
    n=len(X)
    Y=copy.deepcopy(X)
    Z=copy.deepcopy(X)
    a=1/(2*delta)
    b=1/(delta*delta)
    i=1
    g=[]
    H=[]
    F=[]
    for i in range(1, n+1):
        #H.append(g)
        g.append(0)
        row=[]
        for j in range(1, n+1):
            row.append(0)
        H.append(row)
    writeln(vsh, "Hessian initialized with 0s: ")
    writeln(vsh, H) 
    for i in range(1, n+1):
        Y[i-1]=X[i-1]+delta
        Z[i-1]=X[i-1]-delta
        fy=functionToTest(Y)
        fz=functionToTest(Z)
        #
        if vsh==1:
            print("X=",X," Y+ ",Y," Z= ",Z," fx= ",fx," fy= ",fy," fz= ",fz,"\n")
        #
        g[i-1]=a*(fy-fz)
        H[i-1][i-1]=b*(fy-2*fx+fz)
        #
        Y[i-1]=X[i-1]
        Z[i-1]=X[i-1]
        F.append(fy)
    for i in range(1, n-1+1):
        Y[i-1]=X[i-1]+delta
        for j in range(i+1, n+1):#i=1..n-1 et j=i+1..n ob s'calc'd triangle left above
            Y[j-1]=X[j-1]+delta
            #
            #for k in range(1, n+1):
            #    if k==i or k==j:
            #        Y[k-1]=X[k-1]+delta
            #    else:
            #        Y[k-1]=X[k-1]
            #
            fy=functionToTest(Y)
            H[i-1][j-1]=b*(fy-F[i-1]-F[j-1]+fx)
            H[j-1][i-1]=H[i-1][j-1]
            Y[j-1]=X[j-1]
        Y[i-1]=X[i-1]
    writeln(vsh, "Gradient_and_Hesse finishes working")
    #
    return [g, H]
    #R=[g, H]
    #return R

def main():
    X=[1, 2]
    fx=functionToTest(X)
    delta=0.000001
    vsh=1
    print("__Ini data:__ X=", X," fx= ",fx," delta= ",delta,"\n")
    H=Gradient_and_Hesse(X, fx, delta, vsh)
    print("__Answer:__")
    print(H)
    #
    #X_ini_guess=[3, 2]
    #config=MyItersPrecisionConfig()
    #y=MyOptimCauchee(functionToTest, X_ini_guess, config)
    #
    #print('\n\nChecking:\n')
    ##result=fmin_powell(functionToTest, (np.array(X_ini_guess),))
    ##result=fmin_powell(functionToTest, X_ini_guess)
    #result=fmin_powell(functionToTest, np.array(X_ini_guess))
    #print result
    #
    print('Done successfully')

if __name__ == '__main__':
    main()
        
        
