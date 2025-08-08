#import numpy as np

A = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
    ]
print(A)

B=[[1],[-1],[1],[-1], [1]]

def GetMatrixVal(M, LineN, ColN):
    return M[LineN-1][ColN-1]

def SetMatrixVal(M, LineN, ColN, val):
    M[LineN-1][ColN-1]=val

SetMatrixVal(A, 3, 4, 34)

print(A)

def AddMatrices(M1, M2):
    M3=[]
    line=[]
    QL1=len(M1)
    QL2=len(M2)
    if QL1>0 and QL2>0:
        QC1=len(M1[1-1])
        QC2=len(M2[1-1])
        if QL1==QL2 and QC1==QC2 and QC1>0:
            for i in range(1, QL1):
                row=[]
                for j in range(1, QC1):
                    val1=GetMatrixVal(M1, i, j)
                    val2=GetMatrixVal(M2, i, j)
                    val3=val1+val2
                    row.append(val3)
                #
                M3.append(row)
            #
        #
    #
    return M3
#

def SubtractMatrices(M1, M2):
    M3=[]
    line=[]
    QL1=len(M1)
    QL2=len(M2)
    if QL1>0 and QL2>0:
        QC1=len(M1[1-1])
        QC2=len(M2[1-1])
        if QL1==QL2 and QC1==QC2 and QC1>0:
            for i in range(1, QL1):
                row=[]
                for j in range(1, QC1):
                    val1=GetMatrixVal(M1, i, j)
                    val2=GetMatrixVal(M2, i, j)
                    val3=val1-val2
                    row.append(val3)
                #
                M3.append(row)
            #
        #
    #
    return M3
#

def MultiplyMatrices(M1, M2, vsh=0):
    M3=[]
    s=""
    line=[]
    QL1=len(M1)
    QL2=len(M2)
    if(vsh==1):
        print("MultiplyMatrices starts working")
        print("Given:")
        print("M1:")
        print(M1)
        print("M2:")
        print(M2)
    #
    if QL1>0 and QL2>0:
        if(vsh==1):
            print("both matrices have 1 or more lines")
        #
        QC1=len(M1[1-1])
        QC2=len(M2[1-1])
        if QC1>0 and QC2>0:
            if(vsh==1):
                print("both matrices have 1 or more cols")
            #
            if QC1==QL2:
                Q=QC1
                QL3=QL1
                QC3=QC2
                if(vsh==1):
                    print("both matrices have same Q="+str(Q)+". New matrix will have size: "+str(QL3)+"x"+str(QC3))
                #
                for i in range(1, QL3+1):
                    row=[]
                    s=""
                    for j in range(1, QC3+1):
                        valS3=0
                        if(vsh==1):
                            print("element["+str(i)+","+str(j)+"]")
                        #
                        for k in range(1, Q+1):
                            val1=GetMatrixVal(M1, i, k)
                            val2=GetMatrixVal(M2, k, j)
                            valc3=val1*val2
                            s+="(M1("+str(i)+","+str(k)+")="+str(val1)+" * "+"M2("+str(k)+","+str(j)+")="+str(val2)+" = "+str(valc3)+")"
                            if k<Q:
                                s=s+"+"
                            valS3+=valc3
                        #
                        s+=s+"... = M3("+str(i)+","+str(j)+")="+str(valS3)
                        if vsh==1:
                            print(s)
                        #
                        row.append(valS3)
                    #
                    M3.append(row)
                #
            else:
                if vsh==1:
                    print("matrices have not characteristic size Q")
                #
            #
        else:
            if vsh==1:
                print("one or both matrices have 0 cols")
            #
        #
    else:
        if vsh==1:
            print("one or both matrices have 0 lines")
        #
    #
    return M3
#

print("B")
print(B)
vsh=0
C=MultiplyMatrices(A, B, vsh)
print(C)

def GetTransposed_simple(M):
    R=[]
    QL_Old_QC_New=len(M)
    if QL_Old_QC_New>0:
        QC_Old_QL_New=len(M[1-1])
        if QC_Old_QL_New>0:
            for i in range(1, QC_Old_QL_New+1):
                row=[]
                for j in range(1, QL_Old_QC_New+1):
                    val=GetMatrixVal(M, j, i)
                    row.append(val)
                #
                R.append(row)
            #
        #
    #
    return R
#

def Transpose_simple(M, vsh=0):#n'arb!
    R=[]
    if vsh==1:
        print("Transpose_simple starts working")
    #
    QL_Old_QC_New=len(M)
    if QL_Old_QC_New>0:
        QC_Old_QL_New=len(M[1-1])
        if QC_Old_QL_New>0:
            for i in range(1, QC_Old_QL_New+1):
                row=[]
                for j in range(1, QL_Old_QC_New+1):
                    val=GetMatrixVal(M, j, i)
                    row.append(val)
                #
                R.append(row)
            #
        #
    #
    if vsh==1:
        print("transposed")
        print(R)
    #
    M=R
    if vsh==1:
        print("try")
        print(M)
    #
    M=[]
    for i in range(1, QC_Old_QL_New+1):
        row=[]
        for j in range(1, QL_Old_QC_New+1):
            val=GetMatrixVal(R, i, j)
            row.append(val)
        #
        M.append(row)
    #
    if vsh==1:
        print("Answer")
        print(M)
        print("Transpose_simple finishes working")
    #
#

D=[[11,12,13],[21,22,23],[31,32,33]]
print(D)

D=GetTransposed_simple(D)
print("getting transposed:")
print(D)
D=GetTransposed_simple(D)
print("getting transposed:")
print(D)
Transpose_simple(D, 1)
print("transposing:")
print(D)

def arr2D_SetExtRow_simple(arr2D, row, N):
    Q=len(arr2D)
    if Q>0 and N>=1 and N<=Q:
        L=len(row)
        if L>0:
            arr2D[N-1]=[]
            for i in range(1, L+1):
                arr2D[N-1].append(row[i-1])
            #
        #
    #
#

def arr2D_SetIneRow_simple(arr2D, row, N):
    Q=len(arr2D)
    if Q>0 and N>=1 and N<=Q:
        L=len(row)
        if L>0:
            arr2D[N-1]=[]
            for i in range(1, Q+1):
                arr2D[i-1][N-1]=row[i-1]
            #
        #
    #
#

row=[210, 220, 230]
N=2
print("settinh "+str(N)+" row:")
print(row)
arr2D_SetExtRow_simple(D, [210, 220, 230], 2)
print(D)

from __future__ import print_function, division  # для совместимости с Python 2.7
import numpy as np

def householder_reflection(a):
    v = a.copy()
    v[0] += np.sign(a[0]) * np.linalg.norm(a)
    v = v / np.linalg.norm(v)
    H = np.eye(len(a)) - 2.0 * np.outer(v, v)
    return H

def givens_rotation(a, b):
    if b == 0:
        c = 1.0
        s = 0.0
    else:
        r = np.hypot(a, b)
        c = a / r
        s = -b / r
    return c, s

def qr_decomposition(A, method='householder'):
    A = A.copy()
    m, n = A.shape
    Q = np.eye(m)

    if method == 'householder':
        for i in range(min(m, n)):
            x = A[i:, i]
            H = np.eye(m)
            H_i = householder_reflection(x)
            H[i:, i:] = H_i
            A = np.dot(H, A)
            Q = np.dot(Q, H)

    elif method == 'givens':
        for j in range(n):
            for i in range(m-1, j, -1):
                a, b = A[i-1, j], A[i, j]
                c, s = givens_rotation(a, b)
                G = np.eye(m)
                G[[i-1, i], [i-1, i]] = c
                G[i-1, i] = -s
                G[i, i-1] = s
                A = np.dot(G, A)
                Q = np.dot(Q, G)

    else:
        raise ValueError("Method must be 'householder' or 'givens'")

    return Q, A

# Пример
A = np.array([[12.0, -51.0, 4.0, 1.0, 0.0],
              [6.0, 167.0, -68.0, 0.0, 2.0],
              [-4.0, 24.0, -41.0, 0.0, 0.0],
              [1.0, 0.0, 0.0, 2.0, 3.0]])

Q, R = qr_decomposition(A, method='householder')
print("Q =\n", Q)
print("R =\n", R)

