import copy
import math
import numpy as np
import sys

#reload(sys)
#sys.setdefaultencoding('ascii')
#
#print('Hi!')



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

def MatrixOfDiagonalOnes(n):
    A=[]
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        A.append(l)
    for i in range(n):
        A[i-1][i-1]=1
    return A




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

#def AddCol(Q, V):
#    L=len(Q)
#    M=copy.deepcopy(Q)
#    for i in range(1, L+1):
#        M[i-1].append(V[i-1])
#        
#    return M

            
def AddCol(M, V, vsh=0):
    Y=copy.deepcopy(M)
    if vsh==1:
        print("AddCol starts working")
        print("M")
        print(M)
        print("V="+str(V))
    if isinstance(Y, list):
        if vsh==1:
            print("M is list")
        if Y!=[]:
            if not isinstance(Y[1-1],list):
                if vsh==1:
                    print("M is 1D vector - maing it 2D matrix")
                Y=Make2DOf1D(Y)
            else:
                if vsh==1:
                    print("M is 2D matrix")
            QL=len(Y)
            QC=len(Y[1-1])
            if vsh==1:
                print("M is matrix "+str(QL)+" lines x "+str(QC)+" cols")
                print("New lines of matrix:")
            for i in range(1, QL+1):
                Y[i-1].append(V[i-1])
                print(str(i)+") "+str(Y[i-1]))
        else:
            QL=len(V)
            for i in range(QL):
                R=[]
                R.append(V[i])
                Y.append(R)
    if vsh==1:
        print("AddCol finishes working")
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
            if isinstance(Y, list) and isinstance(Y[1-1], list) and len(Y[1-1])==1:
                R=[]
                for i in range(QL1):
                    R.append(Y[i-1][1-1])
                Y=copy.deepcopy(R)
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
        print("fKrylov comes to solution of SLAE")
    p=Seidel(P, F, c, eps, MaxQIters, 1)
    if vsh==1:
        print("fKrylov finishes working")
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



class Succession:
    def __init__(self, LBnd, HBnd, Qe, dLe=1E-6, mode_Q1L2Or3And4=3, QVals0Sects1=0):
        self.LBnd=LBnd
        self.HBnd=HBnd
        self.Qi=Qe
        self.dLi=dLe
        self.mode_Q1L2Or3And4=mode_Q1L2Or3And4
        self.QVals0Sects1=QVals0Sects1
        self.Qw=self.Qi
        self.dLw=self.dLi
        #
        self.correctParams()

    def correctParams(self):
        QSects=0
        if self.QVals0Sects1==1:
            QSects=self.Qi
        else:
            QSects=self.Qi-1
        self.dLw=1.0*(self.HBnd-self.LBnd)/QSects
        if self.dLw>self.dLi:
            if self.mode_Q1L2Or3And4==2 or self.mode_Q1L2Or3And4==4:
                while self.dLw>self.dLi:
                    QSects+=1
                    self.dLw=1.0*(self.HBnd-self.LBnd)/QSects
        if self.QVals0Sects1==1:
           self.Qw=QSects
        else:
           self.Qw=QSects+1
        #return []
           
    def getValues(self):
        if self.QVals0Sects1==1:
            QVals=self.Qw+1
        else:
            QVals=self.Qw
        Y=[]
        #Y.append(self.LBnd)
        for n in range(1, QVals+1):
            x=self.LBnd+self.dLw*(n-1)
            if x>self.HBnd:
                x=self.HBnd
            Y.append(x)
        return Y

    def getQValsW(self):
        if self.QVals0Sects1==1:
            QVals=self.Qw+1
        else:
            QVals=self.Qw
        return QVals

    def getQSectsW(self):
        if self.QSects0Sects1==1:
            QSects=self.Qw
        else:
            QSects=self.Qw-1
        return QSects

    def getLw(self):
        return self.dLw



class DichotomyParams:
    def __init__(self, LBnd, HBnd, Qe, epsX=1E-6, epsY=1E-6, QPoints0Sects1=0):
        self.LBnd=LBnd
        self.HBnd=HBnd
        self.Qi=Qe
        self.QPoints0Sects1=QPoints0Sects1
        self.params=Succession(self.LBnd, self.HBnd, self.Qi)
        self.epsX=epsX
        self.epsY=epsY
           
    def getValues(self):
        R=self.params.getValues()
        return R

    def getSectL(self):
        return self.params.getLw()

            
def Dichotomy(fn, params, vsh=0):
    QSects=params.Qi
    LBnd=params.LBnd
    HBnd=params.HBnd
    sectL=params.getSectL()
    if(vsh==1):
        print("Dichotomy starts working")
        print(str(QSects)+" sections: "+str(params.LBnd)+"..."+str(params.HBnd))
    X=[]
    Y=[]
    #B=[]
    #for n in range(1, QSects+1):
    #    cLBnd=LBnd+sectL*(n-1)
    #    cHBnd=cLBnd+sectL
    B=params.getValues()
    if(vsh==1):
        print("Sects bounds: "+str(B))
        print(str(QSects))
    for n in range(1, QSects-1+1):
        cLBnd=B[n-1]
        cHBnd=cLBnd+sectL
        a=cLBnd
        b=cHBnd
        fa=fn(a)
        fb=fn(b)
        if(vsh==1):
            print("Sect "+str(n)+" f("+str(a)+")="+str(fa)+", f("+str(b)+")="+str(fb))
        #if(fa*fb<params.epsY):
        #    if math.fabs(fa)<params.epsY and (n==1 or a!=cLBnd):
        #        X.append(a)
        #        Y.append(fa)
        #        contin=0
        #    elif math.fabs(fb)<params.epsY:
        #        X.append(b)
        #        Y.append(fb)
        #        contin=0
        if(fa*fb<0 or math.fabs(fa*fb)<params.epsY):
            if(vsh==1):
                print(str(fa)+"*"+str(fb)+"="+str(fa*fb)+"<0 => here is solution to find")
            contin=1
            while contin==1:
                c=(a+b)/2.0
                fa=fn(a)
                fb=fn(b)
                fc=fn(c)
                if b-a<params.epsX:
                    X.append(c)
                    Y.append(fc)
                    contin=0 
                elif math.fabs(fa)<params.epsY and (n==1 or a!=cLBnd):
                    X.append(a)
                    Y.append(fa)
                    contin=0
                elif math.fabs(fb)<params.epsY:
                    X.append(b)
                    Y.append(fb)
                    contin=0
                elif math.fabs(fc)<params.epsY:
                    X.append(c)
                    Y.append(fc)
                    contin=0
                else:
                    if fa*fc<0:
                        b=c
                    elif fb*fc<0:
                        a=c
        else:
            if(vsh==1):
                print(str(fa)+"*"+str(fb)+"="+str(fa*fb)+">=0 => here is NO solution")
    if(vsh==1):
        print("Dichotomy finishes working")
    return X


        

#print("\n\nHouseHolderQR:")


def VectorLength(X, vsh=0):
    if vsh==1:
        print("VectorLength starts working")
        print("Vector given: "+str(X))
    Q=len(X)
    Y=0
    if vsh==1:
       print("Vector length: "+str(Q))
    for i in range(Q):
        if vsh==1:
            print(str(i)+")  Y was "+str(Y)+" X["+str(i)+"]="+str(X[i]))
        Y+=X[i]*X[i]
        if vsh==1:
            print("now  X["+str(i)+"]="+str(X[i])+" Y = "+str(Y))
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

def EigenVecByEigenValRelayMethod(M, eigval, eps=1e-6, maxQIters=10):
    QL=len(M)
    imEig=complex.imag(eigval)
    b0=[]
    if imEig==0:
        for i in range (QL):
            b0.append(1)
    else:
        for i in range(QL):
            b0.append(0+1j)
    N=0
    contin=1
    while contin==1:
        N+=1
        Mi=Subtract(M, multiply(eigval, fE(QL)))
        eigi=eigval
        L0=VectorLength(b0)
        b0=multiply(b0, 1/L0)
        b1=Seidel(M, V, X0, eps=1e-6, maxQIters=20, howAnywaySeidel0NurIfDetET01AnywayMatrix2=0)


def VVT(V):
    VT=transpose(V)
    y=multiply(V, VT)
    return y

def VTV(V):
    VT=transpose(V)
    y=multiply(VT, V)
    return y

def VTV_NoBrackets(V):
    VT=transpose(V)
    y=multiply(VT, V)
    return y[1-1]


        
    
