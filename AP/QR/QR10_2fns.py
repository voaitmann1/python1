import math
import numpy as np
import copy
from MyLinAlgLibEn import *

def copysign(x, y):
    return math.fabs(x) * (1 if y >= 0 else -1)

def householder_vector(A, k):
    R=copy.deepcopy(A)
    n=len(A)
    #Householder vector:
    v=[]
    rkk=[]
    nrm_rkk=0
    for j in range(1, n+1):
        if j<k:
            rkk.append(0)
        else:
            rkk.append(R[j-1][k-1])
            nrm_rkk+=rkk[j-1]*rkk[j-1]
        #
    #
    nrm_rkk=math.sqrt(nrm_rkk)
    mns=nrm_rkk
    if R[k-1][k-1]<0:
        mns=-mns
    xk=R[k-1][k-1]+mns
    #
    for j in range(1, n+1):
        if j!=k:#j<=k:
            v.append(0)
        else:
            v.append(xk)
        #
    return v

def householderReflectionMatrix(A, N, vsh=0):
    n=len(A)
    I=MatrixOfDiagonalOnes(n)
    x=householder_vector(A, N)
    numerat=VVT(x)
    denom=VTV_NoBrackets(x)
    coef=2/denom
    M2=multiply(numerat, coef)
    H_k=Subtract(I, M2)
    return H_k

def myHouseholderDecomposition(A, vsh=1):
    n=len(A)
    R=copy.deepcopy(A)
    Q=MatrixOfDiagonalOnes(n)
    for i in range(1, n+1):
        print("Step: "+str(i))
        print("R:")
        print(R)
        v=householder_vector(R, i)
        print("v=",v)
        H_k=householderReflectionMatrix(R, i)
        print("H_k=",H_k)
        print("After action:")
        Q=multiply(Q, H_k)
        print("Q:")
        print(Q)
        R=multiply(H_k, R)
        print("R:")
        print(R)
    return Q, R
    

def householder_transform(A, i):
    m = len(A)
    n = len(A[0])
    
    x = [A[j][i] for j in range(i, m)]
    e = [1.0 if j == i else 0.0 for j in range(i, m)]
    sign_x = copysign(1.0, x[0])
    norm_x = math.sqrt(sum(val * val for val in x))
    v = [val + sign_x * norm_x for val in x]

    beta = 2.0 / sum(val * val for val in v)

    for j in range(i, n):
        dot_product = sum(v[k - i] * A[k][j] for k in range(i, m))
        for k in range(i, m):
            A[k][j] -= beta * v[k - i] * dot_product

    return A, v


def householder_my(A, i):
    R=copy.deepcopy(A)
    n=len(A)
    #Householder vector:
    x=[]
    rkk=[]
    nrm_rkk=0
    for k in range(1, n+1):
        if k<i:
            rkk.append(0)
        else:
            rkk.append(R[k-1][i-1])
            nrm_rkk+=rkk[k-1]*rkk[k-1]
        #
    #
    nrm_rkk=math.sqrt(nrm_rkk)
    mns=nrm_rkk
    if R[k-1][k-1]<0:
        mns=-mns
    xk=R[i-1][i-1]+mns
    #
    for j in range(1, n+1):
        if j!=i:
            v.append(0)
        else:
            v.append(xk)
        #
    #
    
                
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
            

def transformRorQR(A, i):
    return householder_transform(A, i)

def qr_decomposition(A):
    m = len(A)
    n = len(A[0])
    Q = [[0.0] * m for _ in range(m)]
    
    for i in range(n):
        A, v = transformRorQR(A, i)
        for j in range(i, m):
            Q[j][i] = v[j - i]

    R = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            R[i][j] = A[i][j]

    return Q, R

def qr_eigenvalues(A, num_iterations=50):
    #if not isinstance(A, np.array):
    #A=np.array(A)
    #n = A.shape[0]
    #B = A.copy()
    n=len(A)
    B = copy.deepcopy(A)

    for _ in range(num_iterations):
        R, Q = QRDecompositionByGivensTransform(B)
        #B = np.dot(R, Q)
        B=multiply(R, Q)

    #eigenvalues = [B[i, i] for i in range(n)]
    eigenvalues = [B[i][i] for i in range(n)]
    return eigenvalues

def complex_qr_algorithm(A, num_iterations):
    n = A.shape[0]
    for i in range(num_iterations):
        Q, R = np.linalg.qr(A)
        A = np.matmul(R, np.conjugate(Q).T)
    eigenvalues = np.diag(A)
    return eigenvalues





# Пример использования
A = [
      [12.0, -51.0, 4.0],
      [6.0, 167.0, -68.0],
      [-4.0, 24.0, -41.0]
    ]
print "A:"
print(A)
Q, R = qr_decomposition(A)
#
print "Manually Automatically:"
print "Q:"
for row in Q:
    print row

print "\nR:"
for row in R:
    print row
print "\nAutomatically:"
q,r=np.linalg.qr(A)
print "Q:"
print(q)
print "\nR:"
print(r)
#print("\n\nI5:")
#print(MatrixOfDiagonalOnes(5))
#print("\n\VVT3:")
#print(VVT([1,2,3]))
#print("\n\VTV3:")
#print(VTV([1,2,3]))
#print("\n\VTV3:")
#print(VTV_NoBrackets([1,2,3]))
print "\nManually:"
vsh=1
print("A:")
print(A)
Q, R = myHouseholderDecomposition(A, vsh)
print "Q:"
print(Q)
print "\nR:"
print(R)
#
Q=[[26.0, 0.0, 0.0],[20.0, 181.79674435411016, 0.0],[10.0, 77.13007768744347, -1.3050296560745416]]
R=[[-5.333333333333332, -150.66666666666669, 77.66666666666667],[0.0, -52.466855607959985, 16.984201873743753],[0.0, 0.0, 0.6525148280372708]]
QR=multiply(Q,R)
QQT=multiply(Q,transpose(Q))
print("QQT=",QQT)
print("QR=",QR)
print("\nQRDecompositionByGivensTransform")
print("M")
for row in A:
    print(row)
print("starting")
R, Q=QRDecompositionByGivensTransform(A)
print("Answer")
print("R:")
for row in R:
    print(row)
print("Q:")
for row in Q:
    print(row)
QR=multiply(Q,R)
QQT=multiply(Q,transpose(Q))
print("QQT=")
for row in QQT:
    print(row)
print("QR=")
for row in QR:
    print(row)
A=[[2,-9, 5],[1.2, -5.4, 6],[1, -1, -7.5]]
print("\nA:")
for row in A:
    print(row)
R, Q=QRDecompositionByGivensTransform(A)
print("Answer")
print("R:")
for row in R:
    print(row)
print("Q:")
for row in Q:
    print(row)
QR=multiply(Q,R)
QQT=multiply(Q,transpose(Q))
print("QQT=")
for row in QQT:
    print(row)
print("QR=")
for row in QR:
    print(row)
print("\n\n____________________________________\nA:")
for row in A:
    print(row)
print("Eigenvals - manually:")
eigValsM=qr_eigenvalues(A)
print(eigValsM)
A1=MatrixScalarSubtractDiagonal(A, eigValsM)

print("Eigenvals - automatically:")
eigValsA, eigVecs=np.linalg.eig(A)
print(eigValsA)
# Пример использования
#A = np.array([[1, 2], [3, 4]], dtype=complex)
A = np.array(A, dtype=complex)
num_iterations = 10
eigenvalues = complex_qr_algorithm(A, num_iterations)
print("Eigen vals:", eigenvalues)
