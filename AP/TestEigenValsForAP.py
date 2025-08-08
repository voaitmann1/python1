from MyPolynomeEqsLib import *
from MyLinAlgLibEn import *
from MyMathLib import *
from MyLib import *
from scipy.optimize import fmin_powell

A_side=[[-1.5, -1.5, 1, -0.5], [0.563, -1, -2.047, 0], [0.125, -1.25, -1.375, 0], [0, 1, -0.017, 0]]


A_lngt=[[  -1.5, -0.438,      0.25,     0.25, -0.125],
        [-3.798, -0.017, -4.135E-3, -1.599E-3,     0],
        [ -5.84, -0.036, -8.693E-3, -3.361E-3,     0],
        [-6.084, -0.004, -9.518E-3, -3.680E-3,     0],
        [     0,      0,         1,         0,     0]]



print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
print("A_side:")
printMatrix(A_side)
print("\nA_side, Krylov:")
CharEq=fKrylovCharEq(A_side, eps=1e-6, MaxQIters=10, vsh=1)
print(str(CharEq))
print("\nCharacteristic equation:")
#printListAsPolynome(CharEq, 0)
print(PolynomeToString(CharEq)+" =0")
print("\nAlg eq solution:")
AlgRoots=polynomeEqOfPower4(CharEq[4], CharEq[3], CharEq[2], CharEq[1], CharEq[0], 1)
print("roots:")
realParts=AlgRoots[0]
cmpxParts=AlgRoots[1]
countComplex=0
for val in cmpxParts:
    if val!=0:
        countComplex+=1
if countComplex==0:
    Roots=realParts
else:
    Roots=[]
    L1=len(realParts)
    for i in range(L1):
        Roots.append(Complex(realParts[i], cmpxParts[i]).get())
print("Alg eq answer (first):")
print(AlgRoots)
print("\nAlg eq answer (final):")
print(Roots)
errs=CalcEigenValError(A_side, Roots)
print("\nError value(s): "+str(errs))
#print("\nAuto:")
#v,w=li
print("\n--------------------------------------Try calc eigenvectors:")
print("\nEigenvectors:")
EigVecs=[]
for i in range(4):
    print(str(i+1)+") eigenvalue="+str(Roots[i]))
    b=EigenVecByEigenValIterMethod(A_side, Roots[i], eps=1e-6, maxQIters=10, RelayMethodNo0Yes1=0, vsh=1)
    EigVecs.append(b)
    R=multiply(MatrixScalarSubtractDiagonal(A_side, Roots[i], vsh=0), b)
    print("\nEigenvector"+str(i+1)+": "+str(R))
    print("\nChecking:")
    printMatrix(R)
#
print("\nEigenvectors:")
for i in range(4):
    print(str(i+1)+") eigenvalue="+str(Roots[i]))
    print(str(EigVecs[i]))
#------------------------------------------------
print("\nEigenvectors:")
EigVecs=[]
for i in range(4):
    #b=[]
    print(str(i+1)+") eigenvalue="+str(Roots[i]))
    eigVec=EigenVecByEigenValIterMethod(A_side, Roots[i], eps=1e-6, maxQIters=10, RelayMethodNo0Yes1=0, vsh=1)
    EigVecs.append(eigVec)
    R=EigenVectorErr(A_side, Roots[i], eigVec)
    #R1=np.dot(np.subtract(np.array(A_lngt), np.dot(np.eye(5), RootsOf5thPowerEq[i])), np.array(b))
    R1= EigenVectorErr_by_np(A_side, Roots[i], eigVec)
    #(np.array(A_lngt))
    print("\nChecking1 Eigenvector"+str(i+1)+": "+str(R))
    print("\nChecking2 Eigenvector"+str(i+1)+": "+str(R1))
    print("\nChecking:")
    printMatrix(R)
    print("\nChecking:")
    printMatrix(R1)
#
eigVals=Roots
M=A_side
QVals=len(eigVals)
#
print("\nEigenvectors:")
for i in range(QVals):
    eigVal=eigVals[i]
    print(str(i+1)+")")
    print("eigenvalue="+str(eigVal))
    print("eigenValue Error="+str(np.linalg.det(np.subtract(M, np.dot(np.eye(QVals), eigVal)))))
    eigVec=EigVecs[i]
    print(str(EigVecs[i]))
    print("eigenVector Error:")
    R1= EigenVectorErr_by_np(M, eigVal, eigVec)
    printMatrix(R1)
#
print("\nAuto:")
v,w=np.linalg.eig(M)
#print("eigenvals: "+str(v))
#print("eigenvecs:")
#printMatrix(w)
for i in range(QVals):
    #print(str(i+1))
    #print(str(v[i]))
    #print(str(w[i]))
    #
    eigVal=v[i]
    print(str(i+1)+")")
    print("eigenvalue="+str(eigVal))
    print("eigenValue Error="+str(np.linalg.det(np.subtract(M, np.dot(np.eye(QVals), eigVal)))))
    eigVec=w[i]
    print(str(EigVecs[i]))
    print("eigenVector Error:")
    R1= EigenVectorErr_by_np(M, eigVal, eigVec)
    printMatrix(R1)
print("\n--------------------------------------Chk eq 3rd power:")
AlgRoots=polynomeEqOfPower3(2, 2.533, -1.33, -2.004, 1)
print("Alg eq answer:")
print(AlgRoots)
print("test power")
q=-0.571
Q=0.017
print("q=-0.571="+str(-0.571)+"="+str(q))
print("Q=0.017="+str(0.017)+"="+str(Q))
print("-1.0*q/2="+str(-1.0*q/2))
print("math.sqrt(Q)="+str(math.sqrt(Q)))
print("-1.0*q/2+math.sqrt(Q)="+str(-1.0*q/2+math.sqrt(Q)))
print("math.pow((-1.0*q/2+math.sqrt(Q)),1/3)="+str(math.pow((-1.0*q/2+math.sqrt(Q)),1/3)))
print("math.pow((-1.0*q/2+math.sqrt(Q)),1.0/3)="+str(math.pow((-1.0*q/2+math.sqrt(Q)),1.0/3)))
print("math.pow((-1.0*q/2+math.sqrt(Q)),0.3333)="+str(math.pow((-1.0*q/2+math.sqrt(Q)),0.3333)))
print("(-1.0*q/2+math.sqrt(Q))**(1/3)="+str((-1.0*q/2+math.sqrt(Q))**(1/3)))
print("(-1.0*q/2+math.sqrt(Q))**(1.0/3)="+str((-1.0*q/2+math.sqrt(Q))**(1.0/3)))
print("(-1.0*q/2+math.sqrt(Q))**(0.3333)="+str((-1.0*q/2+math.sqrt(Q))**(0.3333)))
#print("math.pow((-1.0*q/2+math.sqrt(Q)),0.3333)="+str(math.pow((-1.0*q/2+math.sqrt(Q)),0.3333)))
GershgorinCircles=fGershgorinCircles(A_side, 0)
print("GershgorinCircles of A_side...:")
printMatrix(GershgorinCircles)
print("They mean ranges:")
QCircles=len(A_side)

def Fn(x, coefs):
    L=len(coefs)
    maxPow=L-1
    xp=1
    y=coefs[0]
    for i in range(maxPow+1):
        xp*=x
        y+=coefs[i]*xp
    return y
        


for i in range (1, QCircles+1):
   circle= GershgorinCircles[i-1]
   x=circle[0]
   r=circle[1]
   LB=x-r
   HB=x+r
   dichotomyParams=DichotomyParams(LB, HB, 20)
   #X=Dichotomy( (CharEq[4]*x**4+CharEq[3]*x**3+CharEq[2]*x**2+CharEq[1]*x+CharEq[0]), dichotomyParams, [], 1)
   #X=Dichotomy( Fn, dichotomyParams, CharEq, 1)
   X=Dichotomy(fPolynome_coefsOrderNEqualToPower, dichotomyParams, CharEq, 1)
   print(str(i)+" x=" +str(x)+" r="+str(r)+" ("+str(x-r)+"..."+str(x+r)+")")
   print("X="+str(X))
#print("Alg eq answer:")
#print(AlgRoots)
#dichotomyParams=DichotomyParams()
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
#
print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
print("A_lngt:")
printMatrix(A_lngt)
print("\nA_lngt, Krylov:")
CharEq=fKrylovCharEq(A_lngt, eps=1e-6, MaxQIters=10, vsh=1)
print(str(CharEq))
print("\nCharacteristic equation:")
#printListAsPolynome(CharEq, 0)#also works
print(PolynomeToString(CharEq)+" = 0")
print("")
GershgorinCircles=fGershgorinCircles(A_lngt, 1)
print("GershgorinCircles")
printMatrix(GershgorinCircles)
QCircles=len(GershgorinCircles)
BestCircleN=0
GershgorinCirclesNonComplex=[]
#for circle in range GershgorinCircles:
for i in range (1, QCircles+1):
    circle=GershgorinCircles[i-1]
    x=circle[0]
    r=circle[1]
    if complex(x).imag==0 and complex(r).imag==0:
        BestCircleN=i
        GershgorinCirclesNonComplex.append(circle)
firstRealRoot=0
if BestCircleN==0:
    BestCircleN=QCircles
    print("error! All values are complex!")
else:
    print("analyzing circles")
    QCircles=len(GershgorinCirclesNonComplex)
    print("\nLocalizing roots:")
    for i in range(5):
        circle=GershgorinCirclesNonComplex[i-1]
        x=circle[0]
        r=circle[1]
        LB=x-r
        HB=x+r
        print(str(i+1)+") x="+str(x)+" r="+str(r)+" LB="+str(LB)+" HB="+str(HB))
    CircleN=0
    SeekingRoot=1
    FirstRealRootFound=0
    while SeekingRoot==1:
        X=[]
        CircleN+=1
        circle=GershgorinCirclesNonComplex[CircleN-1]
        x=circle[0]
        r=circle[1]
        print("\nCircle "+str(CircleN)+" x="+str(x)+" r="+str(r)+" - searching for roots")
        LB=x-r
        HB=x+r
        X=Dichotomy(fPolynome_coefsOrderNEqualToPower, DichotomyParams(LB, HB, 5), CharEq, 1)
        if X==[]:
            print("Circle "+str(CircleN)+" - roots not found")
        elif isinstance(X, list) and len(X)>0:
            print("First real root found!")
            SeekingRoot=0
            FirstRealRootFound=1
            firstRealRoot=X[0]
            y1=fPolynome_coefsOrderNEqualToPower(firstRealRoot, CharEq)
            print( PolynomeToString(CharEq)+" (by x="+str(firstRealRoot)+") = "+str(y1))
        if CircleN>=QCircles:
            print("all circles are investigated")
            SeekingRoot=0
    if FirstRealRootFound==1:
        print("\nFirst real root: "+str(firstRealRoot))
        print("Applying Gorner algorythm of order decreasing")
        cr=firstRealRoot
        cDecr=fGorner_forRoot_coefsOrderNEqualToPower(CharEq, cr)
        x=5
        y1=fPolynome_coefsOrderNEqualToPower(x, CharEq)
        y2=(x-cr)*fPolynome_coefsOrderNEqualToPower(x, cDecr)
        #y3=fPolynomeGorner_coefsOrderNEqualToPower(arr, x, cr)
        #print("**4**")
        print(PolynomeToString(CharEq)+" (by x="+str(x)+") = "+str(y1))
        print(PolynomeToString(CharEq)+" = (x-"+str(cr)+")*("+PolynomeToString(cDecr)+")"+" (by x="+str(x)+") = "+str(y2))#+" = "+str(y3))
        print("\nSo 4th power order-decreased eq:")
        print(PolynomeToString(cDecr)+" =0")
        print("\nSearching for next 4 roots:")
        #
        #AlgRoots=polynomeEqOfPower4(CharEq[4], CharEq[3], CharEq[2], CharEq[1], CharEq[0], 1)
        AlgRoots=polynomeEqOfPower4(cDecr[4], cDecr[3], cDecr[2], cDecr[1], cDecr[0], 1)
        print("roots:")
        realParts=AlgRoots[0]
        cmpxParts=AlgRoots[1]
        countComplex=0
        for val in cmpxParts:
            if val!=0:
                countComplex+=1
        if countComplex==0:
            Roots=realParts
        else:
            Roots=[]
            L1=len(realParts)
            for i in range(L1):
                Roots.append(Complex(realParts[i], cmpxParts[i]).get())
        print("Alg eq (of decreaded order - 4th power) answer (lists form):")
        print(AlgRoots)
        print("Alg eq (of decreaded order - 4th power)answer :")
        print(Roots)
        #print("Nu sha "+len(RootsOf5thPowerEq)+" roots")
        RootsOf5thPowerEq=[]
        RootsOf5thPowerEq.append(firstRealRoot)
        for i in range(4):
            RootsOf5thPowerEq.append(Roots[i])
        #print("Nu sha "+len(RootsOf5thPowerEq)+" roots")
        print("\nRoots of 5th power eq:")
        for i in range(5):
            x=RootsOf5thPowerEq[i]
            y=fPolynome_coefsOrderNEqualToPower(x, CharEq)
            print(str(i+1)+") "+str(x)+" "+PolynomeToString(CharEq)+" = (by x="+str(x)+") = "+str(y))
        #
        print("\nError value(s):")
        errs=CalcEigenValError(A_lngt, RootsOf5thPowerEq)
        #print("\nError value(s): "+str(errs))
        for i in range(5):
            print(str(errs[i]))
        #print(str(errs))
        EigVecs=[]
        print("\nEigenvectors:")
        for i in range(5):
            print(str(i+1)+") eigenvalue="+str(RootsOf5thPowerEq[i]))
            eigVec=EigenVecByEigenValIterMethod(A_lngt, RootsOf5thPowerEq[i], eps=1e-6, maxQIters=10, RelayMethodNo0Yes1=0, vsh=1)
            EigVecs.append(eigVec)
            R=EigenVectorErr(A_lngt, RootsOf5thPowerEq[i], eigVec)
            #R1=np.dot(np.subtract(np.array(A_lngt), np.dot(np.eye(5), RootsOf5thPowerEq[i])), np.array(b))
            R1= EigenVectorErr_by_np(A_lngt, RootsOf5thPowerEq[i], eigVec)
            #(np.array(A_lngt))
            print("\nChecking1 Eigenvector"+str(i+1)+": "+str(R))
            print("\nChecking2 Eigenvector"+str(i+1)+": "+str(R1))
            print("\nChecking:")
            printMatrix(R)
            print("\nChecking:")
            printMatrix(R1)
        #
        eigVals=RootsOf5thPowerEq
        M=A_lngt
        QVals=len(eigVals)
        #
        print("\nEigenvectors:")
        for i in range(QVals):
            eigVal=eigVals[i]
            print(str(i+1)+")")
            print("eigenvalue="+str(eigVal))
            print("eigenValue Error="+str(np.linalg.det(np.subtract(M, np.dot(np.eye(QVals), eigVal)))))
            #eigVec=EigVecs[i]
            print("eigenVector:")
            print(str(EigVecs[i]))
            print("eigenVector Error:")
            R1= EigenVectorErr_by_np(M, eigVal, eigVec, vsh=0)
            printMatrix(R1)
        #
        print("\nAuto:")
        v,w=np.linalg.eig(M)
        for i in range(QVals):
            #
            eigVal=v[i]
            print(str(i+1)+")")
            print("eigenvalue="+str(eigVal))
            print("eigenValue Error="+str(np.linalg.det(np.subtract(M, np.dot(np.eye(QVals), eigVal)))))
            eigVec=w[i]
            print("eigenVector:")
            print(str(EigVecs[i]))
            print("eigenVector Error:")
            R1= EigenVectorErr_by_np(M, eigVal, eigVec)
            printMatrix(R1)
    else:
        print("error - real roots not found")

X=fmin_powell(fPolynome_coefsOrderNEqualToPower, np.array([x]), (CharEq,))
print(str(X))
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

