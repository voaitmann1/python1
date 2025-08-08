import copy

def PolynomeToString(C, CoefsOrd_PowerETN0_PowerDecreasing1=0, showXInPower1=0, showXInPower0=0, showCoef1=1, showCoef0=1):
    L=len(C)
    order=L-1
    s=""
    if CoefsOrd_PowerETN0_PowerDecreasing1==0:
        p=0
        s+=str(C[order])+"*"+"X^"+str(order)
        for i in range(1, L):
            p=order-i
            if C[p]!=0 or showCoef0==1: 
                if C[p]>0 or (C[p]==0 and showCoef0==1):
                    s+="+"
                if C[p]!=1 or showCoef1==1:
                    s+=str(C[p])
                if p>1 or (p==1 and showXInPower1==1) or (p==0 and showXInPower0==1):
                    if C[p]!=1 or showCoef1==1:
                        s+="*"
                    s+="X^"+str(p)
                else:
                    if p==1 and showXInPower1==0:
                        if C[p]!=1 or showCoef1==1:
                            s+="*"
                        s+="X"
    else:#PowerDecreasing
        p=0
        s+=str(C[0])+"*"+"X^"+str(order)
        for i in range(1, L):
            p=order-i
            if C[i]!=0 or (C[i]==0 and showCoef0==1):
                if C[i]>0 or (C[i]==0 and showCoef0==1):
                    s+="+"
                if C[i]!=1 or showCoef1==1:
                    s+=str(C[i])
                if p>1 or (p==1 and showXInPower1==1) or (p==0 and showXInPower0==1):
                    if C[i]!=1 or showCoef1==1:
                        s+="*"
                    s+="X^"+str(p)
                else:
                    if p==1 and showXInPower1==0:
                        if C[i]!=1 or showCoef1==1:
                            s+="*"
                        s+="X"
    return s

def printListAsPolynome(C, CoefsOrd_PowerETN0_PowerDecreasing1=0, showXInPower1=0, showXInPower0=0, showCoef1=1, showCoef0=1):
    s=PolynomeToString(C, CoefsOrd_PowerETN0_PowerDecreasing1, showXInPower1, showXInPower0, showCoef1, showCoef0)
    print(s)

def printMatrix(M):
    L=len(M)
    for i in range(L):
        print(str(M[i]))

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

n=5
R = [[0.0] * n for _ in range(n)]
print(R)

def lif(vsh, lio):
    if vsh==1:
        print(lio)
