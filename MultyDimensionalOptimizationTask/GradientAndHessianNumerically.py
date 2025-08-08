from scipy.optimize import fmin_powell
import numpy as np
import copy



def writeln(vsh, data):
    if(vsh==1):
        print(str(data)+"\n")


def FnToTestGradientAndHessian(X):
    x1=X[1-1]
    x2=X[2-1]
    y=-x1*x1+6*x1-2*x2*x2+4*x2
    # f(1,2)=5, g(1,2)=[4, -4], H(1,2)=[[-2, 0],[0, -4]]
    return y

def functionToTest(X):
    x1=X[1-1]
    x2=X[2-1]
    #y=abs((5-2*x1)**8 - (6-3*x2)**4)#tic
    #y=(5-2*x1)**8 - (6-3*x2)**4
    #print("f("+str(x1)+", "+str(x2)+")="+str(y))
    y=-x1*x1+6*x1-2*x2*x2+4*x2
    # f(1,2)=5, g(1,2)=[4, -4], H(1,2)=[[-2, 0],[0, -4]]
    return y

 


def Gradient_and_Hesse(X, funclink, delta=0.000001, vsh=0):
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
    fx=funclink(X)
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
        fy=funclink(Y)
        fz=funclink(Z)
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
    #
    X=[1, 2]
    fx=functionToTest(X)
    delta=0.000001
    vsh=1
    print("__Ini data:__ X=", X," fx= ",fx," delta= ",delta,"\n")
    R=Gradient_and_Hesse(X, functionToTest, delta, vsh)
    print("__Answer:__")
    print(R)
    #
    #print('\n\nChecking:\n')
    #
    #X_ini_guess=[3, 2]
    #config=MyItersPrecisionConfig()
    #y=MyOptimCauchee(functionToTest, X_ini_guess, config)
    #
    #print('\n\nChecking:\n')
    #result=fmin_powell(functionToTest, (np.array(X_ini_guess),))
    #result=fmin_powell(functionToTest, X_ini_guess)
    #result=fmin_powell(functionToTest, np.array(X_ini_guess))
    #print result
    #
    print('Done successfully')

if __name__ == '__main__':
    main()
        
        
