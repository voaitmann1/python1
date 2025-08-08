import math
import numpy as np

class UDE_FRP:
    def __init__(self, exP=0, tff=0, c=[0], s=[0]):
        self.exP=exP#0#xponent power
        self.tff=tff#0#trig functions phase
        #self.mpc=0#max power of polnome by cos
        #self.mps=0#max power of polnome by sin
        self.c=c#[]#polnome by cos
        self.s=s#[]#polnome by sin

    def getMaxCosPower(self):
        y=0
        if len(c)>0:
            y=len(c)-1
        return y#polnome by cos)+1

    def getMaxSinPower(self):
        y=0
        if len(s)>0:
            y=len(s)-1
        return y#polnome by sin)+1

    def getF(self, t):
        y=math.exp(self.exP*t)
        Sc=0
        Ss=0
        mpc=self.getMaxCosPower()
        mps=self.getMaxCosPower()
        if tff>0:
            cosinus=math.cos(tff*t)
            sinus=math.sin(tff*t)
            Sc=c[0]
            tp=1
            for p in range(1, mpc+1):
                tp*=t
                Sc+=c[p]*tp
            Sc*=cosinus
            Ss=s[0]
            tp=1
            for p in range(1, mpc+1):
                tp*=t
                Sc+=c[p]*tp
            Ss*=sinus
            y*=(Sc+Ss)
        else:
            Sc=c[0]
            tp=1
            for p in range(1, mpc+1):
                tp*=t
                Sc+=c[p]*tp
            y*=Sc
        return y

def AllRPCoefsTo1DArray(fRPs, maxP):
    QEqs=len(fRPs)
    C=[]
    N=0
    for i in range(1, QEqs+1):
        for j in range(0, maxP+1):
            for k in range(1, 2+1):
                N+=1
                if k==1:
                    C.append(fRPs[i-1].c[j])
                else:
                    C.append(fRPs[i-1].s[j])



#  1  2  3  4
# co c1 c2 c3
# s0 s1 s2 s3
# 5  6  7  8
#
# 1  2  3  4
#
#
#  9 10 11 12 
# c0 c1 c2 c3
# s0 s1 s2 s3
# 13 14 15 16
#
# 5  6  7  8
#
#
# 17 18 19 20
# c0 c1 c2 c3
# s0 s1 s2 s3
# 21 22 23 24
#
# 9 10 11 12
#
#--------------
#
#  1  3  5  7
# co c1 c2 c3
# s0 s1 s2 s3
# 2  4  6  8
#
# 1  2  3  4
#
#
#  9 11 13 15 
# c0 c1 c2 c3
# s0 s1 s2 s3
# 10 12 14 16
#
# 5  6  7  8
#
#
# 17 19 21 23
# c0 c1 c2 c3
# s0 s1 s2 s3
# 18 20 22 24
#
# 9 10 11 12
#
#--------------
#
#  1  2  3  4
# co c1 c2 c3
#
# 5  6  7  8
# c0 c1 c2 c3
#
#  9 10 11 12
# c0 c1 c2 c3
# 
# 13 14 15 16
# s0 s1 s2 s3
#
# 17 18 19 20
# s0 s1 s2 s3
#
# 21 22 23 24
# S0 s1 s2 s3




                    
                
def Array1DToRPCoefs(NInArr, QEqs, maxP, tff, vsh=0):
    #QEqs=len(fRPs)
    if vsh==1:
        print("Array1DToRPCoefs starts working")
        print(str(NInArr)+"; maxP="+str(maxP)+" QEqs="+str(QEqs)+" tff="+str(tff))
    N=NInArr
    #if tff!=0 and NInArr%2==0:
    if tff!=0 and NInArr>QEqs*(maxP+1):
        if vsh==1:
            print("tff="+str(tff)+"!=0 and "+str(NInArr)+">"+str(QEqs*(maxP+1)))
        #N=NInArr/2
        N=NInArr-QEqs*(maxP+1)
        C1S2=2
        if vsh==1:
            print(str(NInArr)+"; N="+str(N)+" C1S2="+str(C1S2))
    else:
        C1S2=1
        if vsh==1:
            print(str(NInArr)+"; N="+str(N)+" C1S2="+str(C1S2))
    #
    p=N%(maxP+1)#-1
    EqN=N/(maxP+1)+1#correct it!
    if p==0:
        p=maxP
        EqN-=1
    else:
        p-=1
    if vsh==1:
        print(str(N)+"%("+str(maxP+1)+"+1)="+str(N%(maxP+1)))
    
    if vsh==1:
        print(str(NInArr)+"; pow="+str(p)+" EqN="+str(EqN))
        print("Array1DToRPCoefs starts working")
    return [EqN, C1S2, p]


def RPCoefsToArray1D(EqN, QEqs, p, maxP, C1S2):
    QPs=maxP+1
    N=QPs*(EqN-1)+p+1
    if C1S2==2:
        N+=QPs*QEqs
    return N



def complex_qr_algorithm(A, num_iterations):
    n = A.shape[0]
    for i in range(num_iterations):
        Q, R = np.linalg.qr(A)
        A = np.matmul(R, np.conjugate(Q).T)
    eigenvalues = np.diag(A)
    return eigenvalues

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
            

#rint("5/2="+str(5/2))#ja, ak C++
QEqs=3
maxP=3
tff=0.1
vsh=0
for N in range (QEqs*(maxP+1)*2):
    #NInArr+=1#seems to work, ma I ne vid any logic
    NInArr=N+1
    #print("N="+str(N)+" NatN in arr = "+str(NInArr)+" : ")
    y=Array1DToRPCoefs(NInArr, QEqs, maxP, tff, vsh)
    if y[2-1]==2:
        print(str(NInArr)+": EqN="+str(y[1-1])+" power="+str(y[3-1])+" (S)")
    else:
        print(str(NInArr)+": EqN="+str(y[1-1])+" power="+str(y[3-1])+" (C)")
print("Now 1D to equations:")
for eqN in range(1, QEqs+1):
    print("Eq: "+str(eqN))
    for C1S2 in range (1, 2+1):
        for p in range(0, maxP+1):
            N=RPCoefsToArray1D(eqN, QEqs, p, maxP, C1S2)
            if C1S2==1:
                print("C^p="+str(p)+" => N in arr: "+str(N))
            else:
                print("S^p="+str(p)+" => N in arr: "+str(N))

                
print("Eig vals")
#A = np.array([[1, 2], [3, 4]], dtype=complex)#array([ 5.37228132+0.j, -0.37228132+0.j]
A = np.array([[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 0, -34], [41, 42, 43, -44]], dtype=complex)
print("A="+str(A))
AT=np.linalg.T
print("AT")
print(AT)
num_iterations = 10
eigenvalues = complex_qr_algorithm(A, num_iterations)
Mev=MatrixScalarSubtractDiagonal(A, eigenvalues[0])
#print("Комплексные собственные значения:", eigenvalues)
print("Eigenvalues:", eigenvalues)
print("det=", np.linalg.det(A))
print("M of eigen: "+str(Mev))
print("det of eigen: "+str(np.linalg.det(Mev)))
        
        
            
        
        
