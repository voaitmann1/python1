from scipy.optimize import fmin_powell
import numpy as np
import copy

n=2#aso ne work, ma atal val ne not
FN=1

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

def fOrt(N):
    e=[]
    for i in range(1, N-1+1):
        e.append(0)
    e.append(1)
    for i in range(N+1, n+1):
        e.append(0)
    return e

def Subtract(X1, X2):
    X=[]
    for i in range(1, n+1):
        d=X1[i-1]-X2[i-1]
        X.append(d)
    return X

def whole_function(X):
    x1=X[1-1]
    x2=X[2-1]
    y=0
    if FN==1:
        y=(8-x1)**2 - (7-x2)**2 + 3*(x2**4) #task ab metoda
    elif FN==2:
        y=abs(eq1(X))+abs(eq2(X)) # uz sys alg eqs
    return y

#def calc_F1(X):  # komponent 1 gradient
#    x1=X[1-1]
#    x2=X[2-1]
#    y=2*x1 - 16 #task ab metoda
#    y=3*x1**2 + 6*x1 + x2 # uz sys alg eqs
#    return y
#
#def calc_F2(X):  # komponent 2 gradient
#    x1=X[1-1]
#    x2=X[2-1]
#    y= -2*x2 + 12*(x2**3) + 14 #task ab metoda
#    y=3*x2**2 + 2*x2 + x1 # uz sys alg eqs
#    return y

#def fXNew(alfa, X0):
#    x1_0=X0[1-1]
#    x2_0=X0[2-1]
#    CalcF1=0
#    CalcF2=0
#    if FN==1:
#        CalcF1=calc_F1(X0)
#        CalcF2=calc_F2(X0)
#    elif FN==2:
#        CalcF1=fOrt(1)
#        CalcF2=fOrt(2)
#    x1_1=x1_0-alfa*CalcF1
#    x2_1=x2_0-alfa*CalcF2
#    X1=[x1_1,x2_1]
#    print('fXNew: x1_0=',x1_0,' x2_0=',x2_0,' CalcF1=',CalcF1,' CalcF2=',CalcF2,' x1_1=',x1_1,' x2_1=',x2_1)
#    return X1

def fXNew(alfa, X0, d):
    x1_0=X0[1-1]
    x2_0=X0[2-1]
    CalcF=d
    CalcF1=CalcF[1-1]
    CalcF2=CalcF[2-1]
    x1_1=x1_0-alfa*CalcF1
    x2_1=x2_0-alfa*CalcF2
    X1=[x1_1,x2_1]
    print('fXNew: x1_0=',x1_0,' x2_0=',x2_0,' CalcF1=',CalcF1,' CalcF2=',CalcF2,' x1_1=',x1_1,' x2_1=',x2_1)
    return X1


    

def FindMin(alfa, X0, d):
    X1=fXNew(alfa, X0, d)
    print('FindMin: X0=',X0,' alfa=',alfa,' X=',X1, ' d=',d)
    return whole_function(X1)

#def FindMin(P):
#    print("FindMin starts working P=", P) 
#    alfa=P[1-1]
#    print("alfa=", alfa)
#    X0=P[2-1:]
#    print("X0=", X0)
#    X1=fXNew(alfa, X0)
#    print("FindMin finishes working P=", P)
#    return whole_function(X1)

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

def main():

    if FN==1:
        x1 = -3 #task ab metoda
        x2 = 5 #task ab metoda
    elif FN==2:
        x1 = 3#3#1.5#-3#1 #1.5 # uz sys alg eqs
        x2 = 4#4#3.5#5#2#3.5 # uz sys alg eqs
    eps1 = 0.000001#0.001
    eps2 = 0.000001
    #gradF1 = calc_F1(x1)
    #gradF2 = calc_F2(x2)
    #alfa = fmin_powell(calc_F1, 0.5)
    #
    IniGuess=np.array([x1, x2])
    #
    M_iter = 100
    K_iter = 0
    #
    #Xprev=np.array([x1,x2])
    Xprev=[x1,x2]
    u0=Xprev
    #Xprev=(x1,x2)
    contin=1
    while contin==1:
        K_iter+=1
        Xnext=Xprev
        d=[]
        for i in range(1, n+1):
            e=fOrt(i)
            d.append(e)
        alfa0=fmin_powell(FindMin, 0.5, (Xnext, d[n-1],))
        x0=fXNew(alfa0, u0, d[n-1])
        for i in range(1, n+1):
            if i==1:
                alfa=fmin_powell(FindMin, 0.5, (x0, d[i-1],))
                Xnext= fXNew(alfa, x0, d[i-1])
                x1=Xnext[1-1]
                x2=Xnext[2-1]
            else:
                alfa=fmin_powell(FindMin, 0.5, (Xnext, d[i-1],))
                Xnext= fXNew(alfa, Xnext, d[i-1])
                x1=Xnext[1-1]
                x2=Xnext[2-1]
        s=Subtract(Xnext, x0)
        for i in range(1, n-1+1):
            d[i-1]=copy.deepcopy(d[i+1-1])
        d[n-1]=copy.deepcopy(s)
        u0=Xnext
        print("{}), x1 = {}, x2 = {}, alfa = {}, func = {}".format(
        i, x1, x2, alfa, whole_function(Xnext)))
        #
        if abs(whole_function(Xnext))<eps1:
            whole_function_isSmallEnough=1
        else:
            whole_function_isSmallEnough=0
        if fCompareX(Xprev, Xnext, eps2)==1:
            CompareX_isSmallEnough=1
        else:
            CompareX_isSmallEnough=0
        if K_iter>=M_iter:
            CountIters_isBigEnough=1
        else:
            CountIters_isBigEnough=0
        #print("Iters:{}, x1 = {}, x2 = {}, alfa = {}, func = {} ; FValMic= {} dXMic= {}, QItersBig= {}".format(
        #K_iter, x1, x2, alfa, whole_function(Xnext), whole_function_isSmallEnough, CompareX_isSmallEnough, CountIters_isBigEnough))
        Xprev=Xnext
        xp1=Xprev[1-1]
        xp2=Xprev[2-1]
        print("Iters:{}, x1 = {}, x2 = {}, alfa = {}, func = {} ; FValMic= {} dXMic= {}, QItersBig= {}".format(
        K_iter, x1, x2, alfa, whole_function(Xnext), whole_function_isSmallEnough, CompareX_isSmallEnough, CountIters_isBigEnough))
        if whole_function_isSmallEnough==1 or CompareX_isSmallEnough==1 or CountIters_isBigEnough==1:
            break
        #Xprev=Xnext
        #
    print('\n\nChecking:\n')
    result=fmin_powell(whole_function, IniGuess)
    print result

if __name__ == '__main__':
    main()
        
        
