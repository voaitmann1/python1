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

ChosenMethodN=Cauchee_MethodN#FlatcherRivs_MethodN
vsh=1#1#Vals to Show or Hide


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
    #R=[d1X1, d1X2]
    R=np.array([d1X1, d1X2])
    return R

def fVectModule(vectExt):
    print()
    vect=copy.deepcopy(vectExt)
    vect=copy.deepcopy(vectExt)
    L=0
    #if isinstance(vect, list) :
    #    dims=len(vect)
    #    for i in range(1, dims+1):
    #        coord=vect[i-1]
    #        cur=coord*coord
    #        L=L+cur
    #    L=math.sqrt(L)
    #elif isinstance(vect, np.array):
    #    dims=len(vect)
    #    for i in range(1, dims+1):
    #        L=L+vect[i-1]*vect[i-1]
    #    L=math.sqrt(L)
    #else:
    #    L=vect
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
    #R=[line1, line2]
    #R=[col1, col2]
    #R=np.array(col1, col2)
    R=np.array([line1, line2])
    return R

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

def fXNewNewton(X, vsh=0):
    if vsh==1:
        print("fXNewNewton srarts working")
    Xprev=copy.deepcopy(X)
    Xnext=copy.deepcopy(Xprev)
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
        print("!!! det=0! Xnext=Xprev")
        for i in range(1, order+1):
            s.append(0)
        if len(neg)==2:
            print("L=2. -g=",neg)
            if neg[1-1]==0 and neg[2-1]==0:
                print("all components of gradient are equal to 0")
                pass# grad =0 ,function doesn't change
            #elif neg[1-1]!=0 and neg[2-1]==0:
            elif CheckIfNotZeroLine(H, 2)==0:
                s[1-1]=1.0*neg[1-1]/H[1-1][1-1]
            #elif neg[1-1]==0 and neg[2-1]!=0:
            elif CheckIfNotZeroLine(H, 1)==0:
                s[2-1]=1.0*neg[2-1]/H[2-1][2-1]
    else:
        s=np.linalg.solve(H, neg)
    Xnext=np.add(Xprev, s)
    if vsh==1:
        print("s=",s," Xnext=",Xnext)
        print("fXNewNewton finishes working")
    return Xnext

def fXNewNewtonMod(alfa, X, vsh=0):
    if vsh==1:
        print("fXNewNewton srarts working")
    Xprev=copy.deepcopy(X)
    Xnext=copy.deepcopy(Xprev)
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
        print("!!! det=0! Xnext=Xprev")
        for i in range(1, order+1):
            s.append(0)
        if len(neg)==2:
            print("L=2. -g=",neg)
            if neg[1-1]==0 and neg[2-1]==0:
                print("all components of gradient are equal to 0")
                pass# grad =0 ,function doesn't change
            #elif neg[1-1]!=0 and neg[2-1]==0:
            elif CheckIfNotZeroLine(H, 2)==0:
                s[1-1]=1.0*neg[1-1]/H[1-1][1-1]
            #elif neg[1-1]==0 and neg[2-1]!=0:
            elif CheckIfNotZeroLine(H, 1)==0:
                s[2-1]=1.0*neg[2-1]/H[2-1][2-1]
    else:
        s=np.linalg.solve(H, neg)
    s=s*alfa
    Xnext=np.add(Xprev, s)
    if vsh==1:
        print("s=",s," Xnext=",Xnext)
        print("fXNewNewton finishes working")
    return Xnext

def fXNewFlatcher(alfa, X, d, vsh=0):
    Xprev=copy.deepcopy(X)
    if vsh==1:
        print("fXNewFlatcherRivs srarts working")
        print("Xprev=",Xprev," d=",d, " vsh=",vsh)
    s=alfa*d
    Xnext=np.add(Xprev, s)
    if vsh==1:
        print("s=",s," Xnext=",Xnext)
        print("fXNewFlatcherRivs finishes working")
    return Xnext

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
        print("!!! det=0! Xnext=Xprev")
        for i in range(1, order+1):
            s.append(0)
        if len(neg)==2:
            print("L=2. -g=",neg)
            if neg[1-1]==0 and neg[2-1]==0:
                print("all components of gradient are equal to 0")
                pass# grad =0 ,function doesn't change
            #elif neg[1-1]!=0 and neg[2-1]==0:
            elif CheckIfNotZeroLine(H, 2)==0:
                s[1-1]=1.0*neg[1-1]/(H[1-1][1-1]+alfa)
            #elif neg[1-1]==0 and neg[2-1]!=0:
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
    if ChosenMethodN==Cauchee_MethodN:
        XNew=fXNew_Cauchee(alfa, X0)
    elif ChosenMethodN==Newton_MethodN:
        XNew=fXNew_Newton(X0)
    elif ChosenMethodN==NewtonMod_MethodN:
        XNew=fXNewNewtonMod(alfa, X0)
    elif ChosenMethodN==Marquardt_MethodN:
        XNew=fXNewMarquardt(alfa, X0)
    elif ChosenMethodN==FlatcherRivs_MethodN:
        XNew=fXNewFlatcher(alfa, X0, d, vsh)
    elif ChosenMethodN==DavidonFlatcherPowell_MethodN:
        XNew=fXNewFlatcher(alfa, X0, d, vsh)
    return XNew


def fAlfaToOptimize(alfa, X0, d=[], vsh=0):
    X1=fXNew(alfa, X0, d, vsh)
    if vsh==1:
        print('fAlfaToOptimize: X0=',X0,' alfa=',alfa,' X=',X1,' d=',d," vsh=", vsh)
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
    return Xnext

def MyOptimNewton(func, X_ini_guess, cfg, vsh=0):
    Xprev=copy.deepcopy(X_ini_guess)
    itersCount=0
    contin=1
    while contin==1:
        itersCount+=1
        Xnext=fXNewNewton(Xprev, vsh)
        #
        if abs(func(Xnext))<cfg.getPrecY() or fCompareX(Xprev, Xnext, cfg.getPrecX())==1 or itersCount>=cfg.getQIters():
            contin=0
        Xprev=Xnext
    return Xnext

def MyOptimNewtonMod(func, X_ini_guess, cfg, vsh=0):
    Xprev=copy.deepcopy(X_ini_guess)
    if vsh==1:
        print("MyOptimNewtonMod starts working")
        print("X_ini_guess=",Xprev)
    itersCount=0
    contin=1
    while contin==1:
        itersCount+=1
        if(vsh==1):
            print("Iteration: "+str(itersCount)+" X= ",Xprev," Starting calculating alfa")
        alfa=fmin_powell(fAlfaToOptimize, 0.5, (Xprev,))
        if(vsh==1):
            print("alfa="+str(alfa))
        Xnext= fXNew(alfa, Xprev)
        if(vsh==1):
            print("X=",Xnext)
        #
        if abs(func(Xnext))<cfg.getPrecY() or fCompareX(Xprev, Xnext, cfg.getPrecX())==1 or itersCount>=cfg.getQIters():
            contin=0
        Xprev=Xnext
        if vsh==1:
            print("Xprev=",Xprev)
    if vsh==1:
        print("answer: X=",Xnext)
        print("MyOptimNewtonMod finishes working")
    return Xnext

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
        if(vsh==1):
            #print("Iteration: "+str(itersCount)+" X= ",Xprev," Starting calculating alfa")
            print("Iteration: "+str(itersCount)+" X= ",Xprev)
        continSingleIteration=1
        subIterCount=0
        while continSingleIteration==1:
            #if itersCount==1:
            #    alfa=1000
            #else:
            #    alfa=fmin_powell(fAlfaToOptimize, 0.5, (Xprev,))
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
                print("too big QSteps at current iteration: "+str(subIterCount)+". Interrupting iteration")
        #
        cond_gradient=(abs(fVectModule(fGradient(Xnext)))<cfg.getPrecY())
        cond_X_small1=(abs(fVectModule(np.subtract(Xprev, Xnext))<cfg.getPrecY()))
        cond_X_small2=(fCompareX(Xprev, Xnext, cfg.getPrecX())==1)
        cond_iters=(itersCount>=cfg.getQIters())
        print("cond_gradient="+str(cond_gradient)+"cond_X_small1="+str(cond_X_small1)+"cond_iters="+str(cond_iters))
        cond_stop=cond_gradient or cond_X_small1 or cond_iters
        print("cond_stop="+str(cond_stop))
        if cond_gradient or cond_X_small1 or cond_iters:
            continIterationsSuccession=0
        Xprev=Xnext
        if vsh==1:
            print("now Xprev=",Xprev)
    #if vsh==1:
    print("answer: X=",Xnext, " Iterations: ", itersCount)
    print("MyOptimMarquardt finishes working")
    return Xnext

def MyOptimFlatcherRivs(func, X_ini_guess, cfg, vsh=0):
    Xprev=copy.deepcopy(X_ini_guess)
    alfa=10000
    #if vsh==1:
    print("MyOptimFlatcherRivs starts working")
    print("X_ini_guess = ",Xprev)
    g=fGradient(Xprev)
    gt=np.transpose(g)
    q=np.dot(gt ,g)
    d=(-1)*g
    itersCount=0
    continIterationsSuccession=1
    while continIterationsSuccession==1:
        itersCount+=1
        #if(vsh==1):
            #print("Iteration: "+str(itersCount)+" X= ",Xprev," Starting calculating alfa")
        print("Iteration: "+str(itersCount)+" X= ",Xprev)
        #g=fGradient(Xprev)
        #gt=np.transpose(g)
        #q=np.dot(gt ,g)
        #d=(-1)*g
        if vsh==1:
            print(" g=",g," gt=",gt," q=",q," -g=d=",d)
        alfa=fmin_powell(fAlfaToOptimize, 0.5, (Xprev, d, vsh,))
        if(vsh==1):
            print("alfa="+str(alfa))
        Xnext= fXNew(alfa, Xprev, d, vsh)
        s=np.subtract(Xnext, Xprev)#not rational, but...
        print("Xnext=",Xnext," s=",s)
        g=fGradient(Xnext)
        gt=np.transpose(g)
        p=np.dot(gt ,g)
        beta=p/q
        neg=(-1)*g
        bd=beta*d
        d=np.add(neg, bd)
        q=p
        if(vsh==1):
            print(" g=",g," gt=",gt," p=",p," beta=",beta," bd=",bd," d=",d)
        if(fVectModule(s)<=cfg.precX):
            continIterationsSuccession=0
            if(vsh==1):
                print("|s|<eps, stopping iterations")
        Xprev=Xnext
    #if vsh==1:
    print("answer: X=",Xnext," Iterations: ",itersCount)
    print("MyOptimFlatcherRivs finishes working")
    return Xnext

def MyOptimDavidonFlatcherPowell(func, X_ini_guess, cfg, vsh=0):
    Xprev=copy.deepcopy(X_ini_guess)
    alfa=10000
    #if vsh==1:
    print("MyOptimDavidonFlatcherPowell starts working")
    print("X_ini_guess = ",Xprev)
    g=fGradient(Xprev)
    d=(-1)*g
    G=GetIdentityMatrix(len(X_ini_guess))
    gprev=g
    itersCount=0
    continIterationsSuccession=1
    while continIterationsSuccession==1:
        itersCount+=1
        #if(vsh==1):
            #print("Iteration: "+str(itersCount)+" X= ",Xprev," Starting calculating alfa")
        print("Iteration: "+str(itersCount)+" X= ",Xprev)
        #g=fGradient(Xprev)
        #gt=np.transpose(g)
        #q=np.dot(gt ,g)
        #d=(-1)*g
        if vsh==1:
            print(" g=",g," d=",d," G=",G)
        alfa=fmin_powell(fAlfaToOptimize, 0.5, (Xprev, d, vsh,))
        if(vsh==1):
            print("alfa="+str(alfa))
        Xnext= fXNew(alfa, Xprev, d, vsh)
        s=np.subtract(Xnext, Xprev)#not rational, but...
        print("Xnext=",Xnext," s=",s)
        if(fVectModule(s)<=cfg.precX):
            continIterationsSuccession=0
            if(vsh==1):
                print("|s|<eps, stopping iterations")
        else:
            g=fGradient(Xnext)
            p=np.subtract(g ,gprev)
            v=np.dot(G, p)
            st=np.transpose(s)
            sst=np.dot(s, st)
            stp=np.dot(st, p)
            vt=np.transpose(v)
            vvt=np.dot(v,vt)
            vtp=np.dot(vt,p)
            if(vsh==1):
                print(" g=",g," p=",p," st=",st," sst=",sst," stp=",stp," vt=",vt," vvt=",vvt," vtp=",vtp)
            GA=np.divide(sst, stp)
            GS=np.divide(vvt, vtp)
            G=np.add(G, GA)
            G=np.subtract(G, GS)
            mG=(-1)*G
            if(vsh==1):
                print(" GA=",GA," GS=",GS," G=",G," mG=",mG)
            d=np.dot(mG, g)
            if(vsh==1):
                print(" d=",d)
        Xprev=Xnext
        gprev=g
    #if vsh==1:
    print("answer: X=",Xnext," Iterations: ",itersCount)
    print("MyOptimDavidonFlatcherPowell finishes working")
    return Xnext
            

def main():
    X_ini_guess=[3, 2]
    #X_ini_guess=[3, 3]
    config=MyItersPrecisionConfig()
    if ChosenMethodN==Cauchee_MethodN:
        X=MyOptimCauchee(functionToTest, X_ini_guess, config)
    elif ChosenMethodN==Newton_MethodN:
        X=MyOptimNewton(functionToTest, X_ini_guess, config, vsh)
    elif ChosenMethodN==NewtonMod_MethodN:
        X=MyOptimNewtonMod(functionToTest, X_ini_guess, config, vsh)
    elif ChosenMethodN==Marquardt_MethodN:
        X=MyOptimMarquardt(functionToTest, X_ini_guess, config, vsh)
    elif ChosenMethodN==FlatcherRivs_MethodN:
        X=MyOptimFlatcherRivs(functionToTest, X_ini_guess, config, vsh)
    elif ChosenMethodN==DavidonFlatcherPowell_MethodN:
        X=MyOptimDavidonFlatcherPowell(functionToTest, X_ini_guess, config, vsh)
    else:#test
        print(GetIdentityMatrix(3))
        print( fXNewFlatcher(0.5, X_ini_guess, 1))
    #
    print("ANSWER: f="+str(functionToTest(X))+" at X="+str(X))
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
        
        
