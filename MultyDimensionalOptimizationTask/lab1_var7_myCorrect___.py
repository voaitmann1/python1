from scipy.optimize import fmin_powell
import numpy as np

def whole_function(X):
    x1=X[1-1]
    x2=X[2-1]
    y=(8-x1)**2 - (7-x2)**2 + 3*(x2**4)
    return y

def calc_F1(X):  # komponent 1 gradient
    x1=X[1-1]
    x2=X[2-1]
    return 2*x1 - 16

def calc_F2(X):  # komponent 2 gradient
    x1=X[1-1]
    x2=X[2-1]
    return - 2*x2 + 12*(x2**3) + 14

def fXNew(alfa, X0):
    x1_0=X0[1-1]
    x2_0=X0[2-1]
    CalcF1=calc_F1(X0)
    CalcF2=calc_F2(X0)
    x1_1=x1_0-alfa*CalcF1
    x2_1=x2_0-alfa*CalcF2
    X1=[x1_1,x2_1]
    #print('fXNew: x1_0=',x1_0,' x2_0=',x2_0,' CalcF1=',CalcF1,' CalcF2=',CalcF2,' x1_1=',x1_1,' x2_1=',x2_1)
    return X1
    

def FindMin(alfa, X0):
    X1=fXNew(alfa, X0)
    print('FindMin: X0=',X0,' alfa=',alfa,' X=',X1)
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

    x1 = -3
    x2 = 5
    eps1 = 0.001
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
    #Xprev=(x1,x2)
    contin=1
    while contin==1:
        K_iter+=1
        alfa=fmin_powell(FindMin, 0.5, (Xprev,))
        Xnext= fXNew(alfa, Xprev)
        x1=Xnext[1-1]
        x2=Xnext[2-1]
        print("Iterations:{}, x1 = {}, x2 = {}, alfa = {}, func = {}".format(
        K_iter, x1, x2, alfa, whole_function(Xnext)))
        #whole_function_isSmallEnough
        if abs(whole_function(Xnext))<eps1 or fCompareX(Xprev, Xnext, eps2)==1 or K_iter>=M_iter:
            break
        Xprev=Xnext
        #
        print('\n\nChecking:\n')
        result=fmin_powell(whole_function, IniGuess)
        print result
        #
        print('Done successfully')

if __name__ == '__main__':
    main()
        
        
