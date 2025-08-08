#import MyLinAlgLibEn

from MyLinAlgLibEn import *

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

M05=[[11, 21, 31, 41, 51],
     [12, 22, 32, 42, 52],
     [13, 23, 33, 43, 53],
     [14, 24, 43, 44, 54],
     [15, 25, 35, 45, 55]
    ]

M03=(M2, V2)
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
#print("Matrix Q:")
#print(Q)
#print(Matrix R:")
#print(R)
print("A:")
print(A)
print("Eigenvalues:")#it writes it  - in russian coding!
#print(eigenvalues)
print(v)
print("Eigen vectors")
print(w)    
Mde=MatrixScalarSubtractDiagonal(A,w[0])
print("A-x[0]="+str(Mde))
print("\nSeidel\n")
A=[[1.179, 0.887, 1.033, 2.2], [0.887, 0.668, 0.778, 1.656], [1.033, 0.778, 0.906, 1.928], [2.2, 1.656, 1.928, 4.105]]
An=np.array(A)
det=666#np.linalg.det(A)
B=[1.775,-1.336,-1.555,-3.312]
Bn=np.array(B)
print("A (det="+str(det)+")=\n",A,"\nB=\n",B)
X=Seidel(A, B, VectorOfZeros(len(A)) )
print("Seidel(A, B, 0)=",X)
X=Seidel(A, B, VectorOfOnes(len(A)) )
print("Seidel(A, B, 1)=",X)
Xn=np.linalg.solve(An, Bn)
print("Xn=",Xn)
import sys
print sys.getdefaultencoding()
print("Succession of 8 vals 1..10:")
a=Succession(1, 10, 8)
print(str(a.getValues()))
X=Dichotomy(math.sin, DichotomyParams(0, 7, 12))
print("sin(x) [0...4], 5 = "+str(X))
