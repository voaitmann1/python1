import copy
import math
import numpy as np
import sys
from MyMathLib import *

#reload(sys)
#sys.setdefaultencoding('ascii')
#
#print('Hi!')

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







#def AddCol(Q, V):
#    L=len(Q)
#    M=copy.deepcopy(Q)
#    for i in range(1, L+1):
#        M[i-1].append(V[i-1])
#        
#    return M

            


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
            if isinstance(Y, list) and isinstance(Y[1-1], list) and len(Y[1-1])==1:
                R=[]
                for i in range(QL1):
                    R.append(Y[i-1][1-1])
                Y=copy.deepcopy(R)
    return Y

def Subtract(A1, A2):
    Y=[]
    if(isinstance(A1, np.ndarray)):
       print("A1 is np.array. Its shape:"+str(A1.shape))
       print(A1)
       A1new=[]
       #for
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
            if isinstance(Y, list) and isinstance(Y[1-1], list) and len(Y[1-1])==1:
                R=[]
                for i in range(QL1):
                    R.append(Y[i-1][1-1])
                Y=copy.deepcopy(R)
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
        #print(""+str(A1)+" * "+str(A2)+" = ")
        Y=[]
        for i in range(1, QL2+1):
            R=[]
            for j in range(1, QC2+1):
                x=A2[i-1][j-1]*A1
                R.append(x)
            Y.append(R)
        #print("="+str(Y))
    elif not isinstance(A1, list) and not isinstance(A2, list):
        Y=A1*A2
    if isinstance(Y, list) and isinstance(Y[1-1], list) and len(Y[i-1])==1:
        ly=len(Y)
        R=[]
        for i in range(ly):
            R.append(Y[i][1-1])
        Y=copy.deepcopy(R)
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





def GaussTriangularTransform(Me, vsh=0):
    if vsh==1:
        print("GaussTriangularTransform starts working")
        print("M:")
        print(Me)
    M=copy.deepcopy(Me)
    QL=len(M)
    QC=len(M[1-1])
    for i in range(1, QL+1):
        if vsh==1:
            print("M["+str(i)+", "+str(i)+"]="+str(M[i-1][i-1]))
            #print("M["+str(i)+", "+str(i)+", "+str(i)+"]="+str(M[i-1][i-1][i-1]))
        ci=-M[i-1][i-1]*1.0
        for j in range(i+1, QL+1):
            cj=M[j-1][i-1]*1.0
            for k in range(1, QC+1):
                M[j-1][k-1]=M[j-1][k-1]*ci*1.0+M[i-1][k-1]*cj*1.0
            if ci!=0:
                for k in range(1, QC+1):
                    M[j-1][k-1]/=ci*1.0
    if vsh==1:
        print("GaussTriangularTransform finishes working")
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

def MatrixScalarSubtractDiagonal(M, x, vsh=0):
    if vsh==1:
        print("MatrixScalarSubtractDiagonal x given = "+str(x))
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


def CalcEigenValError(M, eig, vsh=0):
    dets=[]
    if vsh==1:
        print("MatrixScalarSubtractDiagonal eig given = "+str(eig))
    if isinstance(eig, list):
        for val in eig:
            M1=MatrixScalarSubtractDiagonal(M, val, vsh)
            M2=np.array(M1)
            d=np.linalg.det(M2)
            dets.append(d)
    else:
        val=eig
        M1=MatrixScalarSubtractDiagonal(M, val,vsh)
        M2=np.array(M1)
        d=np.linalg.det(M2)
        dets.append(d)
    return dets
   
    
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

def Seidel(M, V, X0, eps=1e-6, maxQIters=20, howAnywaySeidel0NurIfDetET01AnywayMatrix2=0, vsh=0):
    lif(vsh, "Seidel starts working")
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
            lif(vsh,"Iteratio "+str(countIters))
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
                lif(vsh," X["+str(i)+"]="+str(X[i-1])+" X0["+str(i)+"]="+str(X0[i-1]))
                lif(vsh," X["+str(i)+"]="+str(X[i-1])+"- X0["+str(i)+"]="+str(X0[i-1])+" = "+str(X[i-1]-X0[i-1]))
                lif(vsh," X["+str(i)+"]="+str(X[i-1])+"- X0["+str(i)+"]="+str(X0[i-1])+" ^2 = "+str((X[i-1]-X0[i-1])*(X[i-1]-X0[i-1])))
                deltaSumQ=(X[i-1]-X0[i-1])*(X[i-1]-X0[i-1])
                X0[i-1]=X[i-1]
            #delta=math.sqrt(deltaSumQ)
            delta=math.sqrt(complex(deltaSumQ).real*complex(deltaSumQ).real+complex(deltaSumQ).imag*complex(deltaSumQ).imag)
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
    lif(vsh, "Answer: X="+str(X))
    lif(vsh, "Seidel finishes working")
    return X

def fKrylov(A, eps=1e-6, MaxQIters=10, vsh=0):
    if vsh==1:
        print("fKrylov starts working")
        print("A:")
        print(A)
    c=[]
    P=[]
    c.append(1)
    L=len(A)
    for i in range(2, L+1):
        c.append(0)
    contin=1
    c1=c
    chk1=multiply(-1, c1)
    print("-1*("+str(c1)+")="+str(chk1))
    print("c="+str(c))
    P=AddCol(P, multiply(-1, c1))
    if vsh==1:
        print("c1:")
        print(c1)
        print("P:")
        print(P)
    for i in range(1, L-1+1):
        c1=multiply(A, c1)
        P=AddCol(P, multiply(-1, c1))
        if vsh==1:
            print(str(i)+") c1:")
            print(c1)
            print("P:")
            print(P)
    F=multiply(A, c1)
    if vsh==1:
        print("F:")
        print(F)
        print("fKrylov comes to solution of SLAE")
    p=Seidel(P, F, c, eps, MaxQIters, 1)
    if vsh==1:
        print("fKrylov finishes working")
    return p

def fKrylovCharEq(M, eps=1e-6, MaxQIters=10, vsh=0):
    k=fKrylov(M, eps, MaxQIters, vsh)
    c=copy.deepcopy(k)
    #c=VectorReverse(c)
    C=[]
    L=len(c)
    for i in range(L):
        C.append(c[i])
    C.append(1)
    return C



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

#def HouseHolderFortran(A, N):
#    SX=[]
#    for I in range(1, N-2+1): # DO  I = 1, N-2
#        for K in range(1, N+1): # DO K = I, N
#            SXM=A[N-1][I-1]*A[N-1][K-1] # SX(K)=A(N,I)*A(N,K)
#            #SX.append(SXM) # same, 2
#        #END DO
#        J=N-1 -1               
#        while J != I+1:  # DO J = N-1, I+1, -1
#            J-=1
#            SX[I]=SX[I]+A[J][I]*A[J][I] # SX(I)=SX(I)+A(J,I)*A(J,I)
#        #END DO 
#        for K in range(I+1, N+1): # DO K = I+1, N
#            J=N-1-1  
#            while J != K: # DO J = N-1, K, -1
#                #
#                SX[K-1] = SX[K-1]+A[J-1][I-1]*A[J-1][K-1] # SX(K)=SX(K)+A(J,I)*A(J,K)
#            #END DO
#            J=N-1-1 #
#            while J != I+1:  # DO J = K-1,I+1,-1
#                SX[K-1]=SX[K-1]+A[J-1][I-1]*A[K-1][J-1] # SX(K)=SX(K)+A(J,I)*A(K,J)
#            #END DO
#        # END DO
#
#        ALPHA=math.sqrt(SX[i-1]) # ALPHA = SQRT (SX(I))
#               
#        if A[I+1-1][I-1] != 0: #  IF (A(I+1,I).NE.0.) THEN
#            BETA = 1./ALPHA #same
#            for J in range(I+2, N+1):  # DO J = I+2, N
#                 A[J-1][I-1]=A[J-1][I-1]*BETA # A(J,I)=A(J,I)*BETA
#            #END DO
#            SX[I-1] = A[I+1-1][I-1]*BETA+SIGN(1.,A(I+1,I)) #  SX(I) = A(I+1,I)*BETA+SIGN(1.,A(I+1,I))                     
#                A[I+1-1][I-1]=ALPHA # A(I+1,I)=ALPHA
#                G=1.0/math.abs(SX[i-1])  # ! is comment in fortran # G=1./ABS(SX(I)) ! 1/gamma
#                SX2=0.
#    from here   for K in range(I+2, N+1): # DO K = I+2, N
#                     SX(K)=SX(K)*BETA*G+SIGN(A(K,I+1),SX(I))
#                     SX2=SX(K)*A(K,I)+SX2                     
#                  END DO
#                  SX2=G*SX2
#                  DO K = I+2, N
#                     A(K,K) = A(K,K)-2*A(K,I)*SX(K)+SX2*A(K,I)**2
#                     DO J = K+1, N
#                       A (J,K) = A(J,K)-A(J,I)*SX(K)-A(K,I)*SX(I)+SX2*A(J,I)*A(K,I)
#                     END DO
#                  END DO
#               ELSE
#                  IF (ALPHA.NE.0.) THEN
#                     BETA = 1./ALPHA
#                     DO J = I+2, N
#                       A(J,I)=A(J,I)*BETA
#                     END DO
#                     SX(I) = -1. 
#                     A(I+1,I)=ALPHA
#                     G=1.! 1/gamma
#                     SX2=0.
#                     DO K = I+2, N
#                        SX(K)=SX(K)*BETA*G+SIGN(A(K,I+1),SX(I))
#                        SX2=SX(K)*A(K,I)+SX2                 
#                     END DO
#                     SX2=G*SX2
#                     DO K = I+2, N  
#                        A(K,K) = A(K,K)-2*A(K,I)*SX(K)+SX2*A(K,I)**2                   
#                        DO J = K+1, N
#                          A (J,K) = A(J,K)-A(J,I)*SX(K)-A(K,I)*SX(I)+SX2*A(J,I)*A(K,I)
#                        END DO
#                     END DO
#                  ELSE
#                     SX(I)=1.
#                  END IF
#               END IF               
#	END DO


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


def VectorLength(X, vsh=0):
    if vsh==1:
        print("VectorLength starts working")
        print("Vector given: "+str(X))
    Q=len(X)
    Z=0
    if vsh==1:
       print("Vector length: "+str(Q))
    for i in range(Q):
        #if vsh==1:
        #    print(str(i)+")  Y was "+str(Y)+" X["+str(i)+"]="+str(X[i]))
        component=X[i]
        lif(vsh, str(i+1)+"th component ="+str(component))
        if complex(component).imag==0:
            componentQuadrat=component*component
            lif(vsh, "Quadrat of real component ="+str(componentQuadrat))
        else:
            #componentQuadrat=math.sqrt(complex(component).real*complex(component).real+complex(component).imag*complex(component).imag)
            componentQuadrat=complex(component).real*complex(component).real+complex(component).imag*complex(component).imag
            lif(vsh, "Quadrat of complex component ="+str(componentQuadrat))
        Z+=componentQuadrat
        if vsh==1:
            print("now  X["+str(i)+"]="+str(X[i])+" Z = "+str(Z))
    Y=complex(Z).real
    lif(vsh, "Y^2 ="+str(Y)+" (Z="+str(Z)+")")
    Y=math.sqrt(Y)
    if vsh==1:
        print("sqrt= "+str(Y))
    if vsh==1:
        print("Answer: "+str(Y))
        print("VectorLength finishes working")
    return Y

def LinEqErrVec(C, Fi, S):
    Fs=multiply(C, S)
    D=Subtract(Fs, Fi)
    return D

def LinEqErr(C, Fi, S):
    D=LinEqErrVec(C, Fi, S)
    e=VectorLength(D)
    return e

def EigenValErr(M, v):
    MsEmL=MatrixScalarSubtractDiagonal(M, v)
    d=np.linalg.det(np.array(MsEmL))
    return d

def EigenVecByEigenValRelayMethod(M, eigval, eps=1e-6, maxQIters=10, vsh=0):
    lif(vsh, "EigenVecByEigenValRelayMethod starts working")
    lif(vsh, "eigval="+str(eigval)+" eps="+str(eps)+" maxQIters="+str(maxQIters))
    if vsh==1:
        printMatrix(M)
    QL=0
    if isinstance(M, list) and M!=[]:
        QL=len(M)
        if vsh==1:
            print("M is list, but not empty/ its length="+str(QL))
            printMatrix(M)
    imEig=complex.imag(eigval)
    b0=[]
    if imEig==0:
        for i in range (QL):
            b0.append(1)
    else:
        for i in range(QL):
            b0.append(0+1j)
    if vsh==1:
        print("ini vector="+str(b0))#fMyEigenVec(QM,lambda,eps,maxQIters
    N=0
    contin=1
    b2=[]
    while contin==1:
        N+=1
        Mi=Subtract(M, multiply(eigval, fE(QL)))
        eigi=eigval
        L0=VectorLength(b0)
        if complex.real(L0)!=0:
            b0=multiply(b0, 1/L0)
        #b0=multiply(b0, 1/L0)
        b1=Seidel(M, V, X0, eps=1e-6, maxQIters=20, howAnywaySeidel0NurIfDetET01AnywayMatrix2=0)
        L1=VectorLength(b1)
        db=Subtract(b1, b0)
        dL=VectorLength(db)
        b1=multiply(b1, 1/L1)
        b0=copy.deepcopy(b1)
        AddCol(b2, b1, vsh)
        numerator=multiply(multiply(transpose(b1),M), b1)
        denominator=multiply(transpose(b1), b1)
        li=Divide(numerator, denominator)
        if NL>=maxQIters or complex.real(li)<eps:
            contin=0
    lif(vsh, "Answer: "+str(b1))
    lif(vsh, "EigenVecByEigenValRelayMethod finishes working")
    return b1

def EigenVecByEigenValIterMethod(M, eigval, eps=1e-6, maxQIters=10, RelayMethodNo0Yes1=0, vsh=0):
    lif(vsh, "EigenVecByEigenValIterMethod starts working")
    li=eigval
    b0=[]
    QL=len(M)
    #if complex.imag(eigval)==0:
    #print("im("+str(eigval)+")="+str(complex.imag(eigval)))
    eigValAsComplex=complex(eigval)
    #imEig=complex.imag(eigval)
    imEig=eigValAsComplex.imag
    if imEig==0:
        for i in range (QL):
            b0.append(1)
    else:
        for i in range(QL):
            b0.append(0+1j)
    if vsh==1:
        print("ini vector="+str(b0))
    contin=1
    N=0
    b1=b0
    while contin==1:
        N+=1
        lif(vsh, "iteration "+str(N))
        lif(vsh, "lambda"+str(N)+"="+str(li))
        lif(vsh,"Mi=M-E*lambda:")
        Mi=MatrixScalarSubtractDiagonal(M, li, vsh)
        if(vsh==1):
            printMatrix(Mi)
        b2=Seidel(Mi, b1, b1, eps=1e-6, maxQIters=20, howAnywaySeidel0NurIfDetET01AnywayMatrix2=0, vsh=1)
        lif(vsh, "b2 = Mi^-1 * b1 = "+str(b2))
        norm_of_b2=VectorLength(b2, 1)
        lif(vsh, "norm(b2)="+str(norm_of_b2))
        b3=multiply(b2, 1/norm_of_b2)
        lif(vsh, "b3=b2/norm(b2)="+str(b3))
        dV=Subtract(b3, b1)
        lif(vsh, "dV="+str(dV))
        dL=VectorLength(dV, 1)
        lif(vsh, "dL="+str(dL))
        #if vsh==1:
        #    print("iteration "+str(N))
        #    print("lambda"+str(N)+"="+str(li))
        #    print("Mi=M-E*lambda:")
        #    printMatrix(Mi)
        #    print("b2 = Mi^-1 * b1 = "+str(b2))
        #    print("norm(b2)="+str(norm_of_b2))
        #    print("b3=b2/norm(b2)="+str(b3))
        #    print("b3-b1= = "+str(dV))
        #    print("dL="+str(dL))
        b1=b3
        if RelayMethodNo0Yes1==1:
            numerator=multiply(multiply(transpose(b3), M), b3)
            if vsh==1:
                print("b3^T*M*b3="+str(numerator))
            denominator=multiply(transpose(b3), b3)
            if vsh==1:
                print("b3^T*M*b3="+str(numerator))
            li=numerator/denominator
            if vsh==1:
                print("li="+str(li))
        if N>=maxQIters:
            contin=0
            if vsh==1:
                print("Stopping: iterations quantity too big = "+str(N))#+"(precision reached:"+str(dL)+")")

        if dL<=eps:
            contin=0
            if vsh==1:
                print("Stopping: required precision reached = "+str(dL)+" (<"+str(eps)+")")
    lif(vsh, "Iterations: "+str(N)+". Answer: "+str(b3))
    lif(vsh, "EigenVecByEigenValIterMethod finishes working")
    return b3

def EigenVecByEigenValIterMethod1(M, eigval, eps=1e-6, maxQIters=10, RelayMethodNo0Yes1=0, vsh=0):
    lif(vsh, "EigenVecByEigenValIterMethod starts working")
    li=eigval
    b0=[]
    QL=len(M)
    #if complex.imag(eigval)==0:
    #print("im("+str(eigval)+")="+str(complex.imag(eigval)))
    eigValAsComplex=complex(eigval)
    #imEig=complex.imag(eigval)
    imEig=eigValAsComplex.imag
    if imEig==0:
        for i in range (QL):
            b0.append(1)
    else:
        for i in range(QL):
            b0.append(0+1j)
    if vsh==1:
        print("ini vector="+str(b0))
    contin=1
    N=0
    b1=b0
    while contin==1:
        N+=1
        lif(vsh, "iteration "+str(N))
        lif(vsh, "lambda"+str(N)+"="+str(li))
        lif(vsh,"Mi=M-E*lambda:")
        Mi=MatrixScalarSubtractDiagonal(M, li, vsh)
        if(vsh==1):
            printMatrix(Mi)
        b2=Seidel(Mi, b1, b1, eps=1e-6, maxQIters=20, howAnywaySeidel0NurIfDetET01AnywayMatrix2=0, vsh=1)
        lif(vsh, "b2 = Mi^-1 * b1 = "+str(b2))
        norm_of_b2=VectorLength(b2, 1)
        lif(vsh, "norm(b2)="+str(norm_of_b2))
        b3=np.dot(b2, 1/norm_of_b2)
        lif(vsh, "b3=b2/norm(b2)="+str(b3))
        dV=np.subtract(b3, b1)
        lif(vsh, "dV="+str(dV))
        dL=VectorLength(dV, 1)
        lif(vsh, "dL="+str(dL))
        #if vsh==1:
        #    print("iteration "+str(N))
        #    print("lambda"+str(N)+"="+str(li))
        #    print("Mi=M-E*lambda:")
        #    printMatrix(Mi)
        #    print("b2 = Mi^-1 * b1 = "+str(b2))
        #    print("norm(b2)="+str(norm_of_b2))
        #    print("b3=b2/norm(b2)="+str(b3))
        #    print("b3-b1= = "+str(dV))
        #    print("dL="+str(dL))
        b1=b3
        if RelayMethodNo0Yes1==1:
            numerator=np.dot(np.dot(np.transpose(np.array(b3)), M), np.array(b3))
            if vsh==1:
                print("b3^T*M*b3="+str(numerator))
            #denominator=multiply(transpose(b3), b3)
            denominator=np.dot(np.transpose(np.array(b3)), np.array(b3))
            if vsh==1:
                print("b3^T*M*b3="+str(numerator))
            li=numerator/denominator
            if vsh==1:
                print("li="+str(li))
        if N>=maxQIters:
            contin=0
            if vsh==1:
                print("Stopping: iterations quantity too big = "+str(N))#+"(precision reached:"+str(dL)+")")

        if dL<=eps:
            contin=0
            if vsh==1:
                print("Stopping: required precision reached = "+str(dL)+" (<"+str(eps)+")")
    lif(vsh, "Iterations: "+str(N)+". Answer: "+str(b3))
    lif(vsh, "EigenVecByEigenValIterMethod finishes working")
    return b3, li

def EigenVectorErr(M, eigVal, eigVec, vsh=0):
    #if an arg s'np.array - ne arb't
    R=multiply(MatrixScalarSubtractDiagonal(M, eigVal, vsh), eigVec)
    return R

def EigenVectorErr_by_np(M, eigVal, eigVec, vsh=0):
    if vsh==1:
        print("M:")
        printMatrix(M)
        print("eigVal="+str(eigVal))
        print("eigVec="+str(eigVec))
    return np.dot(np.subtract(np.array(M), np.dot(np.eye(len(M)), eigVal)), np.array(eigVec))

def GivensRotationTransformMatrix(A, N1, N2):
    n=len(A)
    T=[]
    a11=A[N1-1][N1-1]
    a21=A[N2-1][N1-1]
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        T.append(l)
    for i in range(n):
        T[i][i]=1
    if a21==0:
        c12=1
        s12=0
    else:
        
        denom=math.sqrt(a11*a11+a21*a21)
        c12=a11/denom
        s12=a21/denom
    #print("n="+str(n))
    #print("_T=")
    #for row in T:
    #    print(row)
    T[N1-1][N1-1]=c12
    T[N2-1][N2-1]=c12
    T[N1-1][N2-1]=s12
    T[N2-1][N1-1]=-s12
    return T, a11, a21, c12, s12

def QRDecompositionByGivensTransform(M, vsh=0):
    n=len(A)
    R=copy.deepcopy(M)
    Q=MatrixOfDiagonalOnes(n)
    ns=[]
    Ts=[]
    if vsh==1:
        print("\nQRDecompositionByGivensTransform starts working")
    #for j in range(1, n-1+1):
    #    for i in range(j, n+1):
    for i in range(1, n-1+1):
        countTsInLine=0
        TL=[]
        for j in range(i+1, n+1):
            countTsInLine+=1
            #
            if vsh==1:
                print("Line "+str(i)+" Column "+str(j))
                print("R")
                for row in R:
                    print(row)
            T, a11, a21, c12, s12=GivensRotationTransformMatrix(R, i, j)
            #T, a11, a21, c12, s12=GivensRotationTransformMatrix(M, j, i)
            #print("a11="+str(a11)+" a21="+str(a21)+" c12="+str(c12)+" s12="+str(s12))
            if vsh==1:
                print(" a["+str(i)+","+str(i)+"]="+str(a11)+" a["+str(j)+","+str(i)+"]="+str(a21)+" c12="+str(c12)+" s12="+str(s12))
                print("T")
                for row in T:
                    print(row) 
            R=multiply(T, R)
            if vsh==1:
                print("M=T*M")
                for row in R:
                    print(row)
            TL.append(T)
        ns.append(countTsInLine)
        Ts.append(TL)
        #
    if vsh==1:
        print("Showing saved Ts and defining Q")
        for i in range(1, len(ns)+1):
            print("ns["+str(i)+"]="+str(ns[i-1]))
    for i in range(1, n-1+1):
        ii=n-1-i+1
        for j in range(1, ns[ii-1]+1):
            jj=ns[ii-1]-j+1
            if vsh==1:
                print(str(ii)+","+str(jj)+" ("+str(i)+","+str(j)+" ns="+str(ns[ii-1])+"): ")
            T=Ts[ii-1][jj-1]
            if vsh==1:
                print("T")
                for row in T:
                    print row
            Q=multiply(Q,  T)
            if vsh==1:
                print("now Q")
                for row in Q:
                    print row
    Q=transpose(Q)
    if vsh==1:
        print("Answer:")
        print("R:")
        for row in R:
            print(row)
        print("Q:")
        for row in Q:
            print(row)
        print("QRDecompositionByGivensTransform finishes working\n")
    return R, Q

def complex_gpt_qr_algorithm(A, num_iterations):
    A=np.array(A)
    n = A.shape[0]#list has no attribute Shape
    
    for i in range(num_iterations):
        Q, R = np.linalg.qr(A)
        A = np.matmul(R, np.conjugate(Q).T)
    eigenvalues = np.diag(A)
    return eigenvalues

def complex_qr_algorithm(A, num_iterations):
    n = A.shape[0]
    for i in range(num_iterations):
        Q, R = np.linalg.qr(A)
        A = np.matmul(R, np.conjugate(Q).T)
    eigenvalues = np.diag(A)
    return eigenvalues

        
def fGershgorinCircles(M, vsh=0):
    if vsh==1:
        print("fGershgorinCircles starts working")
        printMatrix(M)
    QL=len(M)
    rs=[]
    xs=[]
    circles=[]
    r=0
    for i in range(1, QL+1):
        circle=[]
        x=M[i-1][i-1]
        xs.append(x)
        r=0
        for j in range (1, QL+1):
            if i!=j:
                r+=math.fabs(M[i-1][j-1])
        rs.append(r)
        circle.append(xs[i-1])
        circle.append(rs[i-1])
        if vsh==1:
            print(str(i)+") x="+str(x)+" r="+str(r))
        circles.append(circle)
    if vsh==1:
        print("fGershgorinCircles finishes working")
    return circles
        
