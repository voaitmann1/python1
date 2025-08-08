from scipy.optimize import fmin_powell
import numpy as np


FN=2 #1-task ab metoda, 2 - uz alg eqs sys
#gamma=0.0002#0.002 gut ma#0.000002
alfa=0.5
n=2



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

def whole_function(X):
    x1=X[1-1]
    x2=X[2-1]
    y=0
    if FN==1:
        y=(8-x1)**2 - (7-x2)**2 + 3*(x2**4) #task ab metoda
    elif FN==2:
        y=abs(eq1(X))+abs(eq2(X)) # uz sys alg eqs
        #y=(eq1(X))+(eq2(X)) # uz sys alg eqs
    elif FN==3:
        y=(1-x1)**2 + 100*(x2-x1**2)**2 # uz sys alg eqs
    return y

def calc_F1(X):  # komponent 1 gradient
    x1=X[1-1]
    x2=X[2-1]
    if FN==1:
        y=2*x1 - 16 #task ab metoda
    elif FN==2:
        y=abs(3*x1**2 + 6*x1 + x2)# uz sys alg eqs
        y=(3*x1**2 + 6*x1 + x2)# uz sys alg eqs
    elif FN==3:
        y=2*x1-2+100*(-4*x2*x1 + 4*x1**3)
    return y

def calc_F2(X):  # komponent 2 gradient
    x1=X[1-1]
    x2=X[2-1]
    y=0
    if FN==1:
        y= -2*x2 + 12*(x2**3) + 14 #task ab metoda
    elif FN==2:
        y=abs(3*x2**2 + 2*x2 + x1) # uz sys alg eqs
        y=(3*x2**2 + 2*x2 + x1) # uz sys alg eqs
    elif FN==3:
        y=100*(2*x2-2*x1**2)
    return y

def Grad(X):
    Y=[]
    Y.append(calc_F1(X))
    Y.append(calc_F2(X))
    return Y

#def fXNew(gamma, alfa, X0, Xprev):
#    x1_0=X0[1-1]
#    x2_0=X0[2-1]
#    x1_p=Xprev[1-1]
#    x2_p=Xprev[2-1]
#    CalcF1=calc_F1(X0)
#    CalcF2=calc_F2(X0)
#    #y=whole_function(X0)
#    #y1=Y[1-1]
#    #y2-Y[2-1]
#    x1_1=x1_0-gamma*CalcF1+alfa*(x1_0-x1_p)
#    x2_1=x2_0-gamma*CalcF2+alfa*(x2_0-x2_p)
#    X1=[x1_1,x2_1]
#    ss="fXNew: gamma="+str(gamma)+" alfa="+str(alfa)
#    ss=ss+" X1=("
#    for i in range (1, n):
#        ss=ss+str(X1[i-1])+", "
#    ss=ss+str(X1[n-1])+") "
#    ss=ss+" X0=("
#    for i in range (1, n):
#        ss=ss+str(X0[i-1])+", "
#    ss=ss+str(X0[n-1])+") "
#    ss=ss+" Xp=("
#    for i in range (1, n):
#        ss=ss+str(Xprev[i-1])+", "
#    ss=ss+str(Xprev[n-1])+") "
#    for i in range (1, n):
#        ss=ss+str(Xprev[i-1])+", "
#    ss=ss+str(Xprev[n-1])+") "
#    #print(ss)#'fXNew: x1_0=',x1_0,' x2_0=',x2_0,' CalcF1=',CalcF1,' CalcF2=',CalcF2,' x1_p=',x1_p,' x2_p=',x2_p,'. x1_1=',x1_1,' x2_1=',x2_1)
#    return X1
    

#def FindMin(alfa, X0):
#    X1=fXNew(alfa, X0)
#    print('FindMin: X0=',X0,' alfa=',alfa,' X=',X1)
#    return whole_function(X1)

##def FindMin(P):
##    print("FindMin starts working P=", P) 
##    alfa=P[1-1]
##    print("alfa=", alfa)
##    X0=P[2-1:]
##    print("X0=", X0)
##    X1=fXNew(alfa, X0)
##    print("FindMin finishes working P=", P)
##    return whole_function(X1)

def subtractX(X0, X1):
    dX=[]
    for i in range(1, len(X0)+1):
        dX.append(X1[i-1]-X0[i-1])
    return dX

def fCompareXmin(X0, X1):
    dX=subtractX(X0, X1)
    minimum=0
    maximum=0
    for i in range(1, len(X0)+1):
        if i==1 or (i>1 and dX[i-1]<minimum):
            minimum=dX[i-1]
        if i==1 or (i>1 and dX[i-1]>maximum):
            maximum=dX[i-1]
    return maximum

def fCompareXeps(X0, X1, eps):
    v=0
    if abs(fCompareXmin(X0, X1))<=eps:
        v=1
    return v

def main():
    #global gamma
    if FN==1:
        x1 = -3 #task ab metoda
        x2 = 5 #task ab metoda
        gamma=0.002#0.002  #0.000002 loc min -3.5, 1.328, 115 #4 - zu big, calcs nan #0.4, 0.1, 0.04 zu big, ecri tic err
        alfa=0
    elif FN==2:
        x1 = -3#1#3#1.5#-3#1#3#! #1.5 #-3#1 #1.5 # uz sys alg eqs
        x2 = 5#2#4#3.5#5#2#4#! #3.5 #5#2#3.5 # uz sys alg eqs
        gamma=0.000002#0.0002
        alfa=0
    elif FN==3:
        x1 = 1#-3#0.1#0#1.5 #-3#1 #1.5 # uz sys alg eqs  
        x2 = 2#5#0.1#0#3.5 #5#2#3.5 # uz sys alg eqs
        gamma=0.002
        alfa=0
    eps1 = 0.000000001#0.001
    eps2 = 0.000000001
    #gradF1 = calc_F1(x1)
    #gradF2 = calc_F2(x2)
    #alfa = fmin_powell(calc_F1, 0.5)
    #
    IniGuess=np.array([x1, x2])
    #
    M_iter = 500000#100#5000000
    K_iter = 0
    #
    #Xprev=np.array([x1,x2])
    Xprev=[x1,x2]
    Xprev1=[x1,x2]
    Xprev2=[x1,x2]
    Xprev3=[x1,x2]
    Xprev4=[x1,x2]
    Yprev=whole_function(Xprev)
    Yprev1=whole_function(Xprev1)
    Yprev2=whole_function(Xprev2)
    Yprev3=whole_function(Xprev3)
    Yprev4=whole_function(Xprev4)
    gamma_ini=gamma
    gamma_min=gamma
    gamma_max=gamma
    #Xprev=(x1,x2)
    contin=1
    while contin==1:
        K_iter+=1
        grad=Grad(Xprev)
        #Xnext=Xprev
        continIter=1
        print(K_iter)
        localMin_reached=0
        if localMin_reached==0:
            countSubIter=0
            while continIter==1:
                Xnext=[]
                grad=Grad(Xprev)
                for i in range (1, n+1):
                    #x_cd=Xprev[i-1]
                    #gradcd=grad[i-1]
                    xnew_cd=Xprev[i-1]-gamma*grad[i-1]+alfa*(Xprev[i-1]-Xprev1[i-1])
                    #print("it."+str(K_iter)+" dim "+str(i)+" xcd="+str(xcd)+" g="+str(gradcd)+" xp="+str(xpcd))
                    Xnext.append(xnew_cd)
                Ynext=whole_function(Xnext)
                countSubIter+=1                     
                if Ynext>Yprev:#K_iter>3 and
                    gamma=gamma/2
                else:
                    continIter=0
                if gamma<eps1 or countSubIter>100:
                    continIter=0
                    contin=0
                    localMin_reached=1
                    print("can't find fn value > => min reached")
                print("      "+str(countSubIter)+" gamma="+str(gamma)+" X="+str(Xnext)+" Yprev="+str(Yprev)+" Ynext="+str(Ynext))
                X_LocMin=Xnext
        if localMin_reached==1:
            continIter=1
            countSubIter=0
            gamma=gamma_ini
            while continIter==1:
                Xnext=[]
                grad=Grad(Xprev)
                for i in range (1, n+1):
                    #x_cd=Xprev[i-1]
                    #gradcd=grad[i-1]
                    xnew_cd=Xprev[i-1]-gamma*grad[i-1]+alfa*(Xprev[i-1]-Xprev1[i-1])
                    #print("it."+str(K_iter)+" dim "+str(i)+" xcd="+str(xcd)+" g="+str(gradcd)+" xp="+str(xpcd))
                    Xnext.append(xnew_cd)
                Ynext=whole_function(Xnext)
                countSubIter+=1                     
                if  Ynext>Yprev:#K_iter>3 and
                    gamma=gamma*2.5
                else:
                    continIter=0
                if gamma>gamma_ini/eps1 or countSubIter>100:
                    continIter=0
                    contin=0
                    Xnext=X_LocMin
                    print("can't find value far arounfd local min => let it be min reached: X="+str(Xnext))
                print("      "+str(countSubIter)+" gamma="+str(gamma)+" X="+str(Xnext)+" Yprev="+str(Yprev)+" Ynext="+str(Ynext))
            #end while
        #if localMin_reached==1 et greater gamma found Xnext then it'll be used
        #Xnext=X
        x1=Xnext[1-1]
        x2=Xnext[2-1]
        #print("Iterations:{}, x1 = {}, x2 = {}, alfa = {}, func = {} ".format(
        #K_iter, x1, x2, alfa, whole_function(Xnext)))
        #whole_function_isSmallEnough
        #
        #if fCompareXeps(Xprev, Xnext, eps2)==1:
        #    gamma=gamma/2
        #
        if abs(whole_function(Xnext))<eps1:
            whole_function_isSmallEnough=1
        else:
            whole_function_isSmallEnough=0
        if fCompareXeps(Xprev, Xnext, eps2)==1:
            CompareX_isSmallEnough=1
        else:
            CompareX_isSmallEnough=0
        if K_iter>=M_iter:
            CountIters_isBigEnough=1
        else:
            CountIters_isBigEnough=0
        #print("Iters:{}, x1 = {}, x2 = {}, alfa = {}, func = {} ; FValMic= {} dXMic= {}, QItersBig= {}".format(
        #K_iter, x1, x2, alfa, whole_function(Xnext), whole_function_isSmallEnough, CompareX_isSmallEnough, CountIters_isBigEnough))
        SNIter=str(K_iter)
        while(len(SNIter)<8):
            SNIter="0"+SNIter
        ss="Iter "+SNIter+" gamma="+str(gamma)+" alfa="+str(alfa)
        ss=ss+" X=("
        for j in range (1, n):
            ss=ss+str(Xnext[j-1])+", "
        ss=ss+str(Xnext[n-1])+") "
        ss=ss+" grad=("
        for j in range (1, n):
            ss=ss+str(grad[j-1])+", "
        ss=ss+str(grad[n-1])+") "
        ss=ss+" Xprev=("
        for j in range (1, n):
            ss=ss+str(Xprev[j-1])+", "
        ss=ss+str(Xprev[n-1])+") "
        ss=ss+" Xprev1=("
        for j in range (1, n):
            ss=ss+str(Xprev1[j-1])+", "
        ss=ss+str(Xprev1[n-1])+") "
        ss=ss+" f="+str(whole_function(Xnext))
        ss=ss+" FnMic:="+str(whole_function_isSmallEnough)+" QItersbig: "+str(CountIters_isBigEnough)+ " dXMic: "+str(CompareX_isSmallEnough)
        #if K_iter %100==0 or K_iter<10:
        #    print(ss)
        print(ss)
        #
        if CompareX_isSmallEnough==1 and K_iter>20:
            gamma=0.75*gamma
            print("Xnext="+str(Xnext)+" - Xprev="+str(Xprev)+" dX = "+str(subtractX(Xnext, Xprev))+" => gamma now = "+str(gamma))
        #
        if K_iter>4:
            Xprev4=Xprev3
            Xprev4=Xprev3
        if K_iter>3:
            Xprev3=Xprev2
            Yprev3=Yprev2
        if K_iter>2:
            Xprev2=Xprev1
            Yprev2=Yprev1
        if K_iter>1:
            Xprev1=Xprev
            Yprev1=Yprev
        Xprev=Xnext
        Yprev=whole_function(Xprev)

        #if fCompareXeps(Xprev3, Xprev4, eps2*100)==1 and K_iter>10:# and K_iter>8: # fn = 43->28
        #    gamma=gamma*0.75
        #    print("Xprev4="+str(Xprev4)-" Xprev3="+str(Xprev3)+" = "+str(subtractX(X4, X3)))
        
        if whole_function_isSmallEnough==1 or CountIters_isBigEnough==1 or (CompareX_isSmallEnough==1 and K_iter>20):
            #break
            contin=0
            print("\n"+ss+"\n")
        #Xprev=Xnext
        
        #
    print('\n\nChecking:\n')
    result=fmin_powell(whole_function, IniGuess)
    print result

if __name__ == '__main__':
    main()
        
        
