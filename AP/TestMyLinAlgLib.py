from MyLinAlgLibEn import *

M05=[[11, 21, 31, 41, 51],
     [12, 22, 32, 42, 52],
     [13, 23, 33, 43, 53],
     [14, 24, 43, 44, 54],
     [15, 25, 35, 45, 55]
    ]

M03=(M2, V2)
M03=AddCol(M2, V2)
print("SLAE as single matrix: ")
printMatrix(M03)
print("Triangular transformation by Gauss")
X=GaussTriangularTransform(M03)
printMatrix(X)
print("Solution by Gauss Transform:")
M4=GaussSolutionTransform(M03)
printMatrix(M4)
print("Gauss's matix:")
X=GaussSolution(M03)
printMatrix(X)
print("")
print("Linearly dependent lines and rank analysis:")
cl=LinearLines(M3)
print(cl)
print("Matrix: ")
printMatrix(M3)
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
printMatrix(A)
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
print ("solving sin(x)=0, x=[0...4]")
X=Dichotomy(math.sin, DichotomyParams(0, 7, 12))
print("sin(x) [0...4], 5 = "+str(X))

def fPoly(x, coefs):
    L=len(coefs)
    maxPow=L-1
    xp=1
    y=coefs[0]
    for i in range(1, maxPow+1):
        xp*=x
        y+=coefs[i]*xp
    return y
arr=[-8, 14, -7, 1]
print("Solving "+PolynomeToString(arr)+" =0")
X=Dichotomy(fPoly, DichotomyParams(0, 2, 5), arr, 1)
#print("1*X^3-8*X^2+19*X-12 [0...2], 5) = "+str(X))
print("1*X^3-7*X^2+14*X-8 [0...2], 5) = "+str(X))
for x in X:
    #print(str(x)+" -> 1*X^3-8*X^2+19*X-12="+str(1*x**3-8*x**2+19*x-12))
    print(str(x)+" -> 1*X^3-7*X^2+14*X-8="+str(1*x**3-7*x**2+14*x-8))
#
X=fPolynome_coefsOrderNEqualToPower(10, arr)
print("Poly ="+str(X))
X=Dichotomy(fPolynome_coefsOrderNEqualToPower, DichotomyParams(0, 2, 5), arr, 1)
#print("1*X^3-8*X^2+19*X-12 [0...2], 5) = "+str(X))
print("1*X^3-7*X^2+14*X-8 [0...2], 5) = "+str(X))
for x in X:
    #print(str(x)+" -> 1*X^3-8*X^2+19*X-12="+str(1*x**3-8*x**2+19*x-12))
    print(str(x)+" -> 1*X^3-7*X^2+14*X-8="+str(1*x**3-7*x**2+14*x-8))
#Gorner
cr=X[0]
cDecr=fGorner_forRoot_coefsOrderNEqualToPower(arr, cr)
print( PolynomeToString(arr)+"=(x-"+str(X[0])+")*("+PolynomeToString(cDecr)+")")
x=5
y1=fPolynome_coefsOrderNEqualToPower(x, arr)
y2=(x-cr)*fPolynome_coefsOrderNEqualToPower(x, cDecr)
y3=fPolynomeGorner_coefsOrderNEqualToPower(arr, x, cr)
print(PolynomeToString(arr)+" (by x="+str(x)+") = "+str(y1))
print(PolynomeToString(arr)+" = (x-"+str(cr)+")*("+PolynomeToString(cDecr)+")"+" (by x="+str(x)+") = "+str(y2)+" = "+str(y3))
