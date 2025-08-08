import copy
import math
import numpy as np

M1=[[11,12,13,14,15],
    [21,22,23,24,25],
    [31,32,33,34,35],
    [41,42,43,44,45],
    [51,52,53,54,55]
   ]

M3=[[11, 12, 13, 14, 15, 16],
    [21, 22, 23, 24, 25, 26],
    [22, 24, 26, 28, 30, 32],# 11-22
    [00, 00, 00, 00, 00, 00],
    [42, 44, 46, 48, 50, 52],#42 - 21
    [63, 66, 69, 72, 75, 78] #63 - 21
   ]

M2=[[61,12,13,14,15],
    [21,62,23,24,25],
    [31,32,63,34,35],
    [41,42,43,64,45],
    [51,52,53,54,65]
   ]

V1=[105, 195, 285, 375, 465]
V2=[305, 315, 345, 395, 455]
V3=[0, 0, 0, 0, 0]
V4=[0, 0, 0, 0, 1]

def VectorOfZeros(n):
    X=[]
    for i in range(n):
        X.append(0)
    return X

def VectorOfOnes(n):
    X=[]
    for i in range(n):
        X.append(1)
    return X


def VectorsEuclidesNorm(x):
    Q=len(x)
    y=0
    for i in range (1, Q+1):
        y+=x[i-1]*x[i-1]
    y=math.sqrt(y)
    return y

def sign(x, ZeroAllowed=0):
    if(x>0):
        y=1
    elif(x<0):
        y=-1
    else:
        if ZeroAllowed==0:
            y=1
        else:
            y=0
    return y

def fE(n):
    Y=[]
    for i in range(1, n+1):
        R=[]
        for j in range(1, n+1):
            if i==j:
                R.append(1)
            else:
                R.append(0)
        Y.append(R)
    return Y
        

def Householder1(A, vsh=0):#VectorFor
    if vsh==1:
        print("Householder starts working")
        print("A="+str(A))
    F=copy.deepcopy(A)
    QC=len(F)
    QL=len(F[1-1])
    F=copy.deepcopy(A)
    R=copy.deepcopy(F)
    Q=fE(QL)
    E=fE(QL)
    for k in range (1, QL+1):
        if vsh==1:
            print("k="+str(k))
        #a HouseHolder Vector
        if vsh==1:
            print("Calculate Householder vector")    
        x=[]
        Rk=VectorOfMatrixColumn(R, k)
        Rkk=R[k-1][k-1]
        #xnorm=VectorsEuclidesNorm(Rk)
        Vn=[]
        for j in range (k+1, QL+1):
            Vn.append(R[j-1][k-1])
        xnorm=VectorsEuclidesNorm(Vn)
        xk=Rkk+sign(Rkk)*xnorm
        for i in range(1, k-1+1):
            x.append(0)
        x.append(xk)
        for i in range(k+1, QL+1):
            x.append(0)
        if vsh==1:
            print(" Rkk="+str(Rkk)+" Rk="+str(Rk)+" norm(Rk)="+str(xnorm)+" xk="+str(xk))
            print("Householder vector["+str(k)+"]="+str(x))
        #b HouseHolder Reflection
        if vsh==1:
            print("Calculate Householder Reflection")
        #x=transpose(x)#
        multDenomR=multiply(transpose(x), x)
        multDenom=multDenomR[1-1][1-1]
        multNumerat=multiply(x, transpose(x))
        toSubtract=multiply(2, multiply(multNumerat, 1/multDenom))
        H_k=Subtract(E, toSubtract)
        if vsh==1:
            print(" multDenom="+str(multDenom)+" multNumerat="+str(multNumerat)+" vectToSubtr="+str(toSubtract))
            print("E="+str(E))
            print(" Matrix of Householder reflection: "+str(H_k))
        #Cotrrection of Q, R
        if vsh==1:
            print("Matrices modification for more precision:")
            print("Trying to multiply Q x H_k")
            print("Q="+str(Q))
            print("H_k="+str(H_k))
        Q=multiply(Q, H_k)
        if vsh==1:
            print("Now Q="+str(Q))
            print("Trying to multiply R x H_k")
            print("R="+str(R))
            print("H_k="+str(H_k))
        R=multiply(H_k, R)
        if vsh==1:
            print("Now R="+str(R))
    if vsh==1:
        print("Answer:")
        print("Q="+str(Q))
        print("R="+str(R))
        print("Checking: A="+str(A)+" Q*R="+str(multiply(Q, R))+" Q*QT="+str(multiply(Q,transpose(Q))))
        print("HouseHolder finishes working") 
    return (Q, R)

#def Householder(A, vsh=0):
        


def VectorOfMatrixLine(M, N):
    R=[]
    if isinstance(M, list):
        if not isinstance(A[1-1], list):
            M=Make2DOf1D(M)
        if(N>=1 and N<=len(M)):
            R=M[N-1]
    return R

def VectorOfMatrixColumn(M, N):
    R=[]
    if isinstance(M, list):
        if not  isinstance(M[1-1], list):
            M=Make2DOf1D(M)
        QL=len(M)
        QC=len(M[1-1])
        if N >= 1 and N <= QC:
            for i in range(1, QL+1):
                R.append(M[i-1][N-1])
    return R

def transpose(A):
    if isinstance(A, list) and not isinstance(A[1-1], list):
        A=Make2DOf1D(A)
    QL_old_QC_new=len(A)
    QC_old_QL_new=len(A[1-1])
    Y=[]
    for i in range(1, QC_old_QL_new+1):
        R=[]
        for j in range(1, QL_old_QC_new+1):
            R.append(A[j-1][i-1])
        Y.append(R)
    return Y

def Make2DOf1D(v):
    n=len(v)
    Y=[]
    for i in range(1, n+1):
        R=[]
        R.append(v[i-1])
        Y.append(R)
    return Y

def SetCol(M, V, N):
    R=copy.deepcopy(M)
    if isinstance(M, list) and isinstance(M[1-1], list) and isinstance(V, list):
        QL=len(M)
        QC=len(M[1-1])
        L=len(V)
        if(QL==L and N>=1 and N<=QC):
            for i in range(1, QL+1):
                R[i-1][N-1]=V[i-1]
    return R
            
def AddCol(M, V):
    Y=copy.deepcopy(M)
    if isinstance(Y, list):
        if not isinstance(Y[1-1],list):
            Y=Make2DOf1D(Y)
        QL=len(Y)
        QC=len(Y[1-1])
        for i in range(1, QL+1):
            Y[i-1].append(V[i-1])
    return Y

def Add(A1, A2):
    Y=[]
    if isinstance(A1, list) and isinstance(A2, list):
        if not isinstance(A1[1-1],list):
            A1=Make2DOf1D(A1)
        if not isinstance(A2[1-1],list):
            A2=Make2DOf1D(A2)
        QL1=len(A1)
        QC1=len(A1[1-1])    
        QL2=len(A2)
        QC2=len(A2[1-1])
        if QL1==QL2 and QC1==QC2 and QL1>=1 and QC1>=1:
            QL=QL1
            QC=QC1
            for i in range (1, QL+1):
                R=[]
                for j in range (1, QC+1):
                    x=A1[i-1][j-1]+A2[i-1][j-1]
                    R.append(x)
                Y.append(R)
    return Y

def Subtract(A1, A2):
    Y=[]
    if isinstance(A1, list) and isinstance(A2, list):
        if not isinstance(A1[1-1],list):
            A1=Make2DOf1D(A1)
        if not isinstance(A2[1-1],list):
            A2=Make2DOf1D(A2)
        QL1=len(A1)
        QC1=len(A1[1-1])    
        QL2=len(A2)
        QC2=len(A2[1-1])
        if QL1==QL2 and QC1==QC2 and QL1>=1 and QC1>=1:
            QL=QL1
            QC=QC1
            for i in range (1, QL+1):
                R=[]
                for j in range (1, QC+1):
                    x=A1[i-1][j-1]-A2[i-1][j-1]
                    R.append(x)
                Y.append(R)
    return Y

def multiply(A1, A2):
    if isinstance(A1, list) and not  isinstance(A1[1-1], list):
        A1=Make2DOf1D(A1)
    if isinstance(A2, list) and not  isinstance(A2[1-1], list):
        A2=Make2DOf1D(A2)
    if isinstance(A1, list) and isinstance(A2, list):
        QL1=len(A1)
        QC1=len(A1[1-1])
        QL2=len(A2)
        QC2=len(A2[1-1])
        QL=QL1
        QC=QC2# zb vector
        QIdem=QC1#=QL2
        if QL2!=QIdem:
            print("Error! You are trying to multiply incompatible matrices!")
        Y=[]
        for i in range(1, QL+1):
            R=[]
            for j in range(1, QC+1):
                s=0
                for k in range(1, QIdem+1):
                    x=A1[i-1][k-1]*A2[k-1][j-1]
                    s+=x
                R.append(s)
            Y.append(R)
    elif isinstance(A1, list) and  not isinstance(A2, list):
        QL1=len(A1)
        QC1=len(A1[1-1])
        Y=[]
        for i in range(1, QL1+1):
            R=[]
            for j in range(1, QC1+1):
                x=A1[i-1][j-1]*A2
                R.append(x)
            Y.append(R)
    elif not isinstance(A1, list) and isinstance(A2, list):
        QL2=len(A2)
        QC2=len(A2[1-1])
        Y=[]
        for i in range(1, QL2+1):
            R=[]
            for j in range(1, QC2+1):
                x=A2[i-1][j-1]*A1
                R.append(x)
            Y.append(R)
    elif not isinstance(A1, list) and not isinstance(A2, list):
        Y=A1*A2
    return Y
    

#def VVT(v):
#    A=[]
#    n=len(v)
#    for i in range(1, n+1):
#        R=[]
#        for j in range(1, n+1):
#            R.append(v[i-1]*v[j-1])
#        A.append(R)
#    return A
#
#def VTV(v):
#    y=0
#    n=len(v)
#    for i in range(1, +1):
#        y+=v[i-1]*v[i-1]
#    return A


def EqualApprox_intR(x1, x2, eps=1E-6):
    R=0
    if(abs(x1-x2)<=eps):
        R=1
    return R

def EqualApprox_bool(x1, x2, eps=1E-6):
    return (abs(x1-x2)<=eps)

def NotEqualApprox_intR(x1, x2, eps=1E-6):
    R=1
    if(abs(x1-x2)<=eps):
        R=0
    return R

def NotEqualApprox_bool(x1, x2, eps=1E-6):
    return (abs(x1-x2)>eps)

def GreaterApprox_intR(x1, x2, eps=1E-6):
    R=0
    if((x1-x2)>eps):
        R=1
    return R

def GreaterApprox_bool(x1, x2, eps=1E-6):
    return((x1-x2)>eps)

def LessApprox_intR(x1, x2, eps=1E-6):
    R=0
    if((x2-x1)>eps):
        R=1
    return R

def LessApprox_bool(x1, x2, eps=1E-6):
    return((x2-x1)>eps)

def GreaterOrEqualApprox_intR(x1, x2, eps=1E-6):
    R=1
    if((x2-x1)>eps):
        R=0
    return R

def GreaterOrEqualsApprox_bool(x1, x2, eps=1E-6):
    return(not(x2-x1)>eps)

def LessOrEqualApprox_intR(x1, x2, eps=1E-6):
    R=1
    if((x1-x2)>eps):
        R=0
    return R

def LessOrEqualsApprox_bool(x1, x2, eps=1E-6):
    return(not(x1-x2)>eps)



def GaussTriangularTransform(Me):
    M=copy.deepcopy(Me)
    QL=len(M)
    QC=len(M[1-1])
    for i in range(1, QL+1):
        ci=-M[i-1][i-1]*1.0
        for j in range(i+1, QL+1):
            cj=M[j-1][i-1]*1.0
            for k in range(1, QC+1):
                M[j-1][k-1]=M[j-1][k-1]*ci*1.0+M[i-1][k-1]*cj*1.0
            if ci!=0:
                for k in range(1, QC+1):
                    M[j-1][k-1]/=ci*1.0
    return M

def AddCol(Q, V):
    L=len(Q)
    M=copy.deepcopy(Q)
    for i in range(1, L+1):
        M[i-1].append(V[i-1])
        
    return M



def ValIsInVectorUnderFirstN(Vec, val):
    N=0
    L=len(Vec)
    for i in range(1, L+1):
        if(Vec[i-1]==val and N==0):
            N=i;
            break;
    return N

def FirstNValsOfVectorAreZeros(V, N, eps=10e-6):
    R=0
    count=0
    for i in range(1, N+1):
        if V[i-1]==0:
            count+=1
    if count==N:
        R=1
    return R

def VectorConsistsOfZerosOnly(V, eps=10e-6):
    R=0
    L=len(V)
    count0=0
    for i in range(1, L+1):
        if EqualApprox_bool(V[i-1], 0, eps):
            count0+=1
    if count0==L:
        R=1
    return R

def VectorConsistsOfZerosOnlyExceptLast(V, eps=10e-6):
    R=0
    L=len(V)
    count0=0
    for i in range(1, L-1+1):
        if EqualApprox_bool(V[i-1], 0, eps):
            count0+=1
    if count0==L-1:
        R=1
    return R

def GaussSolutionTransform(Me):
    QL=len(Me)
    QC=len(Me[1-1])
    M=GaussTriangularTransform(Me)
    X=[]
    for i in range(1, QL+1):
        X.append(0)
    for i in range(1, QL+1):
        N=QL-i+1
        X[N-1]=M[N-1][QC-1]/M[N-1][N-1]*1.0
        for j in range (1, N-1+1):
            M[j-1][QC-1]-=M[j-1][N-1]*X[N-1]*1.0
            M[j-1][N-1]=0
    return M

def GaussSolution(Me):
    M1=copy.deepcopy(Me)
    M2=GaussTriangularTransform(M1)
    M3=GaussSolutionTransform(M2)
    QL=len(Me)
    QC=len(Me[1-1])
    X=[]
    for i in range(1, QL+1):
        X.append(M3[i-1][QC-1]/M3[i-1][i-1])
    return X

def CoefsOfVectors(V1, V2, eps=1e-6, vsh=0):
    if(vsh==1):
        print("CoefsOfVectors starts working")
        print("V1["+str(len(V1))+"]="+str(V1))
        print("V2["+str(len(V2))+"]="+str(V2))
    L=len(V1)
    count=0
    c=[]
    i=L-1
    if((V1[L-1-1]==0) or (V2[L-1-1]==0)):
        c1=0
        if(vsh==1):
            if V1[L-1-1]==0 and V2[L-1-1]!=0:
                print("c1=0 because V1["+str(L-1)+"="+str(V1[L-1-1]))
            elif V1[L-1-1]!=0 and V2[L-1-1]==0:
                print("c1=0 because V2["+str(L-1)+"="+str(V2[L-1-1]))
            elif V1[L-1-1]==0 and V2[L-1-1]==0:
                print("c1=0 because V1["+str(L-1)+"]="+str(V1[L-1-1])+" and V2["+str(L-1)+"]="+str(V2[L-1-1]))
    else:
        c1=1.0*V1[L-1-1]/V2[L-1-1]
        if(vsh==1):
            print("c1= V1["+str(L-1-1)+"]/V2["+str(L-1-1)+"]="+str(c1))
    for i in range(1, L+1):
        if i!=L-1:
            if((V1[i-1]==0) or (V2[i-1]==0)):
                c=0
                if(vsh==1):
                    if V1[i-1]==0 and V2[i-1]!=0:
                        print("c=0 because V1["+str(i)+"="+str(V1[i-1]))
                    elif V1[i-1]!=0 and V2[i-1]==0:
                        print("c=0 because V2["+str(i)+"="+str(V2[L-1-1]))
                    elif V1[i-1]==0 and V2[i-1]==0:
                        print("c=0 because V1["+str(L-1)+"]="+str(V1[-1])+" and V2["+str()+"]="+str(V2[-1]))
            else:
                c=1.0*V1[i-1]/V2[i-1]
                if(vsh==1):
                    print(str(i)+") c= V1["+str(i-1)+"]/V2["+str(i-1)+"]="+str(V1[i-1])+"/"+str(V2[i-1])+"]="+str(c))
            if(NotEqualApprox_bool(c1, c)==1):
                count+=1
                if(vsh==1):
                    print("count="+str(count))
    R=[c1, count]
    if(vsh==1):
        print("Answer: "+str(R))
        print("CoefsOfVectors finishes working")
    return [c1, count]
        
        
def LinearLines(M, eps=1e-6, vsh=1):
    if(vsh==1):
        print("LinearLines starts working")
        print("M="+str(M))
    QL=len(M)
    QC=len(M[1-1])
    R=[]
    R1=[]
    LinDepLinesNs=[]
    countAll=0
    for i in range(1, QL+1):
        if FirstNValsOfVectorAreZeros(M[i-1], QL)==1:
            LinDepLinesNs.append(i)
            countAll+=1
            if(vsh==1):
                print("Line "+str(i)+"consists of zeros: "+str(M[i-1])+" - "+str(countAll)+" linearly dependent line")
    for i in range(1, QL+1):
        if(vsh==1):
            print("Line "+str(i)+": "+str(M[i-1]))
        r1=[]
        r1.append(i)
        if FirstNValsOfVectorAreZeros(M[i-1], QL)==1:
            r1.append(QL-1)
            if(vsh==1):
                print("Line of zeros")
        elif ValIsInVectorUnderFirstN(LinDepLinesNs, i)>0:
            r1.append(QL-1)
            if(vsh==1):
                print("Line is already detected as linearly dependent")
        elif ValIsInVectorUnderFirstN(LinDepLinesNs, i)==0:
            countSingle=0
            for j in range(i+1, QL+1):
                if(vsh==1):
                    if(i==j):
                        print(str(i)+"="+str(j)+" - not considered")
                    if(ValIsInVectorUnderFirstN(LinDepLinesNs,j)>0):
                        print(str(j)+"th line is already noted as linearly dependent")
                if(i!=j and ValIsInVectorUnderFirstN(LinDepLinesNs,j)==0):
                    if(vsh==1):
                        print("  comparing to Line "+str(j)+": "+str(M[j-1]))
                    r2=[]
                    r2=CoefsOfVectors(M[i-1], M[j-1], eps, vsh)
                    if r2[2-1]==0:
                        countSingle+=1
                        countAll+=1
                        LinDepLinesNs.append(j)#
                    if(vsh==1):
                        if r2[2-1]!=0:
                            print("these are linearly independent lines")
                        else:
                            print("this is "+str(countAll)+" linearly dependent lin with k="+str(r2[1-1]))
                    
            r1.append(countSingle)
            if(vsh==1):
                print(" Line has "+str(countSingle)+" linearly dependent lines")
        if(vsh==1):
                print(" Matrix has "+str(countAll)+" linearly dependent lines")
        R.append(r1)
    R1.append(countAll)
    R1.append(R)
    R1.append(LinDepLinesNs)
    #R.append(CoefsOfVectors(V1, V2, eps))
    if(vsh==1):
        print("LinearLines finishes working")
    return R1


def LinearlyDependenLinesN(M, eps=1e-6, vsh=0):
    anRes=LinearLines(M, eps, vsh)
    LinDepLinNs=anRes[3-1]
    return LinDepLinNs

def LinearlyIndependenLinesN(M, eps=1e-6, vsh=0):
    LinDepLinNs=LinearlyDependenLinesN(M, eps, vsh)
    QL=len(M)
    LinIndepLinNs=[]
    for i in range(1, QL+1):
        if ValIsInVectorUnderFirstN(LinDepLinNs, i)==0:
            LinIndepLinNs.append(i)
    return LinIndepLinNs

def MatrixQLinDepLins(M, eps=1e-6, vsh=0):
    LinDepLinNs=LinearlyDependenLinesN(M, eps, vsh)
    return len(LinDepLinNs)

def getMatrixRank(M, eps=1e-6, vsh=0):
    return len(M)-MatrixQLinDepLins(M)
    
def VectorReverse(X):
    buf=0
    Y=copy.deepcopy(X)
    L=len(Y)
    if L%2==0:
        N=L/2
    else:
        N=(L-1)/2
    for N1 in range(1, N+1):
        N2=L-N1+1
        buf=Y[N1-1]
        Y[N1-1]=Y[N2-1]
        Y[N2-1]=buf
    return Y

def fPolynomeIni_coefsOrderNEqualToPower(C, x):
    L=len(C)
    y=C[0]
    xp=1
    for p in range(1, L-1+1):
        xp*=x
        y=y+C[p]*xp
    return y

def fPolynomeIni_coefsOrderPowerDecrease(C, x):
    L=len(C)
    y=0#C[L-1]
    for i in range(0, L-1+1):
        p=L-i-1
        y=y+C[i]*x**p
    return y

def fGorner_forGeneral_coefsOrderPowerDecrease(ap, cr):
    ord1=len(ap)
    ord2=ord1-1
    bp=[]
    bp.append(ap[1-1])
    for k in range(2, ord1+1):
        bp.append(ap[k-1]+cr*bp[k-1-1])
    return bp

def fGorner_forRoot_coefsOrderPowerDecrease(ap, cp):
    ord1=len(ap)
    ord2=ord1-1
    fp=[]
    bp=fGorner_forGeneral_coefsOrderPowerDecrease(ap, cp)
    for k in range(1, ord2+1):
        fp.append(bp[k-1])
    return fp

def fGorner_forRoot_coefsOrderNEqualToPower(ape, cp):
    ap=VectorReverse(ape)
    bp=fGorner_forRoot_coefsOrderPowerDecrease(ap, cp)
    yr=VectorReverse(bp)
    return yr

def fGorner_forGeneral_coefsOrderNEqualToPower(ape, cr, vsh=1):
    if(vsh==1):
        print("fGorner_forGeneral_coefsOrderNEqualToPower starts working")
        print("given: "+str(ape))
    ap=VectorReverse(ape)
    if(vsh==1):
        print("reversed: "+str(ap))
    bp=fGorner_forGeneral_coefsOrderPowerDecrease(ap, cr)
    if(vsh==1):
        print("fGorner_forGeneral_coefsOrderPowerDecrease="+str(bp))
    fp=fGorner_forRoot_coefsOrderNEqualToPower(apw, cp)
    if(vsh==1):
        print("fGorner_forRoot_coefsOrderNEqualToPower="+str(fp))
    yr=copy.deepcopy(fp)
    yr.append(bp[len(bp)-1])
    if(vsh==1):
        print("Answer="+str(yr))
    return yr


def fPolynomeGorner_coefsOrderPowerDecrease(Cp, x, c):
    ord1=len(Cp)
    bp=fGorner_forRoot(Cp, c)
    PolLesOrd=fPolynomeIni_coefsOrderPowerDecrease(bp, x)
    y=PolLesOrd*(x-c)
    return y

def fPolynomeGorner_coefsOrderNEqualToPower(Cp, x, c):
    ord1=len(Cp)
    bp=fGorner_forRoot(Cp, c)
    PolLesOrd=fPolynomeIni_coefsOrderPowerDecrease(bp, x)
    y=PolLesOrd*(x-c)
    return y

def fScalarProduct(v1, v2):
    L=len(v1)
    p=0
    for i in range(1, L+1):
        p+=v1[i-1]*v2[i-1]
    return p

def fVectorNormalized(v):
    r=[]
    Q=len(v)
    L=0
    for i in range(1, Q+1):
        L+=v[i-1]*v[i-1]
    for i in range(1, Q+1):
        r.append(v[i-1]/L)
    return r

def fVectorMultiplyToCoef(v, k):
    r=[]
    L=len(v)
    for i in range (1, L+1):
        r.append(v[i-1]*k)
    return r
    
def GrahamSchmidtProcess_vViki(A):
    B=[]
    Q=len(A)
    L=len(A[1-1])
    for i in range (1, Q+1):
        ai=A[i-1]
        bi=ai
        if i==1:
            #NOp
            pass
        else:
            for j in range(1, i-1+1):
                bj=B[j-1]
                proj_on_bj_of_ai=bj*fScalarProduct(ai, bj)/fScalarProduct(bj, bj)
                for k in range(1, L+1):
                    bi[k-1]-=ai[k-1]*proj_on_bj_of_ai[k-1]
        B.append(fVectorNormalized(bi))
    return B

def fVectorNorm2(v):
    y=0
    Q=len(v)
    for i in range (1, Q+1):
        y+=math.abs(v[i-1])*math.abs(v[i-1])
    y=math.sqrt(s)
    return(y)

def MatrixScalarSubtractDiagonal(M, x):
    Y=[]
    QL=len(M)
    QC=QL
    for i in range(QL):
        R=[]
        for j in range(QC):
            if i==j:
                R.append(M[i][j]-x)
            else:
                R.append(M[i][j])
        Y.append(R)
    return Y
    
   
    
def GrahamSchmidtProcess_vBook(A):
    #ColN first, line N - second,
    # quadratic matrices A, Q and R should be tranasposed, their lines are vectors
    n=len(A)
    n=len(A[1-1])#must be same
    Q=[]
    R=[]
    linRows=[]
    for j in range(1, n+1):
        aj=A[j-1]
        qj=aj
        rj=[]
        for i in range (1, j-1+1):
            qi=Q[i-1]
            rij=fScalarProduct(qi, aj)
            rj.append(rij)
            qj-=fVectorMultiplyToCoef(qi, rij)
        Q.append(qj)
        #
        rjj=fVectorNorm2(qj)
        rj.append(rjj)
        for i in range(j+1, n+1):
            rj.append(0)
        R.append(rj)
    return[Q, R]


def ExtremValsOfMatrix(M):
    QL=len(M)
    QC=len(M[1-1])
    mn=0
    mx=0
    mna=0
    mxa=0
    if factic0abs1==0:
        for i in range (QL):
            for j in range (QC):
                if i==0 and j==0:
                    mn=M[i][j]
                    mx=M[i][j]
                    mna=math.abs(M[i][j])
                    mxa=math.abs(M[i][j]) 
                else:
                    if M[i][j]<mn:
                        mn=M[i][j]
                    if M[i][j]>mx:
                        mx=M[i][j]
                    if math.abs(M[i][j])<mna:
                        mna=math.abs(M[i][j])
                    if math.abs(M[i][j])>mxa:
                        mxa=math.abs(M[i][j])
    return [mn, mx, mna, mxa]

def Seidel(M, V, X0, eps=1e-6, maxQIters=20, howAnywaySeidel0NurIfDetET01AnywayMatrix2=0):
    n=len(M)
    countIters=0
    contin=1
    deltaSumQ=0
    det=np.linalg.det(np.array(M))
    if EqualApprox_bool(det, 0, eps) and howAnywaySeidel0NurIfDetET01AnywayMatrix2!=2:
        X=[]
        while contin==1:
            countIters+=1
            X=[]
            for i in range(1, n+1):
                if i==1:
                    #Sbefi=0
                    Safti=0
                    for j in range (i+1, n+1):
                        Safti+=M[i-1][j-1]*X0[j-1]
                    x=1/M[i-1][i-1]*(V[i-1]-0-Safti)
                    X.append(x)
                elif i==n:
                    Sbefi=0
                    #Safti=0
                    for j in range (1, i-1+1):
                        Sbefi+=M[i-1][j-1]*X[j-1]
                    x=1/M[i-1][i-1]*(V[i-1]-Sbefi-0)
                    X.append(x)
                else:
                    Sbefi=0
                    Safti=0
                    for j in range (1, i-1+1):
                        Sbefi+=M[i-1][j-1]*X[j-1]
                    for j in range (i+1, n+1):
                        Safti+=M[i-1][j-1]*X0[j-1]
                    x=1/M[i-1][i-1]*(V[i-1]-Sbefi-Safti)
                    X.append(x)
                deltaSumQ=(X[i-1]-X0[i-1])*(X[i-1]-X0[i-1])
                X0[i-1]=X[i-1]
            delta=math.sqrt(deltaSumQ)
            if countIters>=maxQIters:
                cond_QIters= 1
            else:
                cond_QIters= 0
            if delta<eps:
                cond_delta = 1
            else:
                cond_delta = 0       
            if cond_QIters==1 and cond_delta == 1:
                contin = 1
            else:
                contin = 0
            cond_det_ET_0=1
        
    else:
        X=np.linalg.solve(M, V)
    return X

def fKrylov(A, eps=1e-6, MaxQIters=10):
    c=[]
    P=[]
    c.append(1)
    L=len(A)
    for i in range(2, L+1):
        c.append(0)
    contin=1
    c1=c
    P=AddColumn(P, multiply(-1, c1))
    for i in range(1, L-1+1):
        c1=multiply(A, c1)
        P=AddColumn(P, multiply(-1, c1))
    F=multiply(A, c1)
    p=Seidel(P, F, c, eps, MaxQIters, 0, 1)
    return p

def householder_qr(A):
    m, n = A.shape
    R = np.copy(A)
    Q = np.eye(m)

    for k in range(n):
        x = R[k:, k]
        e = np.zeros_like(x)
        e[0] = np.sign(x[0])

        u = x + e * np.linalg.norm(x)
        u /= np.linalg.norm(u)

        R[k:, k:] -= 2.0 * np.outer(u, np.dot(u, R[k:, k:]))
        Q[k:] -= 2.0 * np.outer(u, np.dot(u, Q[k:]))

    return Q, R


def qr_eigenvalues(A, num_iterations=10):
    n = A.shape[0]
    eigenvalues = np.zeros(n)

    for i in range(num_iterations):
        Q, R = householder_qr(A)
        A = np.dot(R, Q)

    for i in range(n):
        eigenvalues[i] = A[i, i]

    return eigenvalues

#print("\n\nHouseHolderQR:")


          
    
    
    
M05=[[11, 21, 31, 41, 51],
     [12, 22, 32, 42, 52],
     [13, 23, 33, 43, 53],
     [14, 24, 43, 44, 54],
     [15, 25, 35, 45, 55]
    ]

M03=AddCol(M2, V2)
print("SLAE as single matrix: "+str(M03))
print("Triangular transformation by Gauss")
X=GaussTriangularTransform(M03)
print(X)
print("Solution by Gauss Transform:")
M4=GaussSolutionTransform(M03)
print(str(M4))
X=GaussSolution(M03)
print(X)
print("")
print("Linearly dependent lines and rank analysis:")
cl=LinearLines(M3)
print(cl)
print("Matrix: "+str(M3))
print("Linearly Dependent lines Ns: "+str(LinearlyDependenLinesN(M3)))
print("Linearly Independent lines Ns: "+str(LinearlyIndependenLinesN(M3)))
print("Q linearly Dependent lines Ns: "+str(MatrixQLinDepLins(M3)))
print("rang= "+str(getMatrixRank(M3)))
print("")
print("Matrix: "+str(M2))
print("Linearly Dependent lines Ns: "+str(LinearlyDependenLinesN(M2)))
print("Linearly Independent lines Ns: "+str(LinearlyIndependenLinesN(M2)))
print("Q linearly Dependent lines Ns: "+str(MatrixQLinDepLins(M2)))
print("rang= "+str(getMatrixRank(M2)))
print("")
print(str(V3)+" zeros only? "+str(VectorConsistsOfZerosOnly(V3)))
print(str(V4)+" zeros only? "+str(VectorConsistsOfZerosOnly(V4)))
print(str(V4)+" alm all zeros? "+str(VectorConsistsOfZerosOnlyExceptLast(V4)))
print("")
print("Gorner Algorythm:")
ap=[1, -6, 11, -6]
xp=7
cp=2
print("reverse"+str([1, -6, 11, -6])+"="+str(VectorReverse([1, -6, 11, -6])))      
apw=VectorReverse(ap)
print("Polynome (order - power decrease) by C="+str(ap )+", x="+str(xp)+" = "+str(fPolynomeIni_coefsOrderNEqualToPower(apw, xp)))
print("Polynome (power order - N = power) by C="+str(apw)+", x="+str(fPolynomeIni_coefsOrderNEqualToPower(apw, xp)))
print("Polynome (order - power decrease) by C="+str([1, -4, 3])+", x="+str(xp)+" = "+str(fPolynomeIni_coefsOrderPowerDecrease([1, -4, 3], xp)))
print("Check simple order")
gcfs=fGorner_forGeneral_coefsOrderPowerDecrease(ap, cp)
gcrs=fGorner_forRoot_coefsOrderPowerDecrease(ap, cp) 
print("Coefs by Gorner schem (for general) by cr="+str(cp)+" = "+str(gcfs))
print("Coefs by Gorner schem (for root) by cr="+str(cp)+" = "+str(gcrs)) 
print("Check: (x-c)= "+str(xp-cp)+" polynome(C="+str(gcrs)+", x="+str(xp)+") = "+str(fPolynomeIni_coefsOrderPowerDecrease(gcrs, xp)))
print("Check: (x-c)*G(x)= "+str((xp-cp)*fPolynomeIni_coefsOrderPowerDecrease(gcrs, xp)))
print("Check order as power")
gcfp=fGorner_forGeneral_coefsOrderNEqualToPower(apw, cp)
gcrp=fGorner_forRoot_coefsOrderNEqualToPower(apw, cp)
print("Coefs by Gorner schem (for general) by cr="+str(cp)+" = "+str(gcfp))
print("Coefs by Gorner schem (for root) by cr="+str(cp)+" = "+str(gcrp)) 
print("Check: (x-c)= "+str(xp-cp)+" polynome(C="+str(gcrp)+", x="+str(xp)+") = "+str(fPolynomeIni_coefsOrderNEqualToPower(gcrp, xp)))
print("Check: (x-c)*G(x)= "+str((xp-cp)*fPolynomeIni_coefsOrderNEqualToPower(gcrp, xp)))      
#vvt=VVT([1,2,3])
#print("VVT(1,2,3)="+str(vvt))
print("AT="+str(len([[11,12,13],[21,22,23],[31,32,33]])))
A1=[[1,2,3],[4,5,6],[7,8,9]]
A2=[[9,2,5],[4,8,1],[3,7,6]]
print("A1="+str(A1)+" A2="+str(A2))
print("A1*A2="+str(multiply(A1,A2)))
A1=[[1,2,3],[4,5,6],[7,8,9]]
A2=[1,2,3]
print("A1="+str(A1)+" A2="+str(A2))
print("A1*A2="+str(multiply(A1,A2)))
A1=[[1,2,3],[4,5,6],[7,8,9]]
A2=10
print("A1="+str(A1)+" A2="+str(A2))
print("A1*A2="+str(multiply(A1,A2)))
A1=10
A2=[[1,2,3],[4,5,6],[7,8,9]]
print("A1="+str(A1)+" A2="+str(A2))
print("A1*A2="+str(multiply(A1,A2)))
A1=[1,2,3]
print("A1="+str(A1))
print("A1*A1T="+str(multiply(A1,transpose(A1))))
print("A1*A1T="+str(multiply(transpose(A1), A1)))
A1=10
A2=[1,2,3]
print("A1="+str(A1)+" A2="+str(A2))
print("A1*A2="+str(multiply(A1,A2)))
print("\n\n")
print("M05="+str(M05))
vsh=1
#Householder(M05, vsh)
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]], dtype=complex)

#Q, R = householder_qr(A)
#eigenvalues = qr_eigenvalues(A)
#
v,w=np.linalg.eig(A)##no: np.linalg.eigenvals, np.linalg.eigenvalues, np.linalg.eigen, np.eigenvalues, np.eigenvals, np.eigen
#
#print("Матрица Q:")
#print(Q)
#print("Матрица R:")
#print(R)
print("A:")
print(A)
print("Собственные числа:")#it writes it  - in russian coding!
#print(eigenvalues)
print(v)
print("Собственные векторы")
print(w)    
Mde=MatrixScalarSubtractDiagonal(A,w[0])
print("A-x[0]="+str(Mde))
print("\nSeidel\n")
A=[[1.179, 0.887, 1.033, 2.2], [0.887, 0.668, 0.778, 1.656], [1.033, 0.778, 0.906, 1.928], [2.2, 1.656, 1.928, 4.105]]
An=np.array(A)
det=np.linalg.det(A)
B=[1.775, -1.336, -1.555, -3.312]
Bn=np.array(B)
print("A (det="+str(det)+")=\n",A,"\nB=\n",B)
X=Seidel(A, B, VectorOfZeros(len(A)) )
print("Seidel(A, B, 0)=",X)
X=Seidel(A, B, VectorOfOnes(len(A)) )
print("Seidel(A, B, 1)=",X)
Xn=np.linalg.solve(An, Bn)
print("Xn=",Xn)
