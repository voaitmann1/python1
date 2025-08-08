import math
import copy
from MyLinAlgLibEn import *
import numpy as np

def polynome(t=0, c=[]):
    y=0
    pc=0
    xx=1
    if isinstance(c, list) and len(c)>0:
        pc=len(c)+1
        y=c[0]
        xx=1
        for i in range(1, pc+1):
            xx*=t
            y+=c[i]*xx
    return y
        
#       

class LinDifEqRightPart:
    def __init__(self, c=[], s=[], w, r):
        self.c=c
        self.s=s
        self.w=w
        self.r=r#exp

    def calc(self, t):
        pc=0
        C=1
        S=1
        e=math.exp(r*t)
        if isinstance(c, list) and len(c)>0:
            C=polynome(t, c)
        if isinstance(s, list) and len(s)>0:
            S=polynome(t, s)
        return e*(C*math.cos(w*t)+S*math.sin(w*t))

    def getCosCoefsMaxPow(self):
        pc=0
        if isinstance(c, list) and len(c)>0:
            pc=len(c)+1
        return pc

    def getSinCoefsMaxPow(self):
        ps=0
        if isinstance(s, list) and len(s)>0:
            ps=len(s)+1
        return ps

    def getPolinomesMaxPow(self):
        P=0
        pc=self.getCosCoefsMaxPow()
        ps=self.getSinCoefsMaxPow()
        if ic>=ps:
            P=pc
        else:
            P=ps
        return P
   
#      

class UsualDiffEqsLinSys:
    def __init__(self, A=[], soluts=[]):
        self.A=A
        self.soluts=soluts
        self.H=len(A)
        self.s=[]

    def getEigenVals(self):
        #return qr_eigenvalues(self.A, 10)
        v,w=np.linalg.eig(A)
        return w

    def getEigenVecs(self):
        v,w=np.linalg.eig(A)
        return w

    def getQEqsForIndefCoefs(self):
        y = 2 * (self.s + self.P + 1) * self.H
        return y

    def NInSysForIndefCoefs(self, eqN, coefN, varN, p, coefType_C0S1):
        P=self.SolutNPow(eqN)
        y=(P-1)*(varN-1)+p+1
        if coefType_C0S1==1:
            y+=H*P
        return y

    def CoefNParamsByN(self, SummandN, UndefCoefsEqN):
        QEqsForUndefCoef=self.getQEqsForIndefCoefs()
        P=self.SolutNPow(UndefCoefsEqN)
        if SummandN>self.H*P:
            coefType_C0S1=1
            p = (SummandN-H*P) % (P+1)
            iniEqN=(SummandN-H*P) % (P+1) +1
        else:
            coefType_C0S1=0
            p = SummandN % (P+1)
            iniEqN=(SummandN) % (P+1) +1
        if p==0:
            p=P
        else:
            p=p-1
        Y=[QEqsForUndefCoef, P, p, coefType_C0S1, iniEqN]
        #         1          2  3      4            5
        return Y
    
    def calcCoefsInSys(self, NInEqOfIndefCoefs, EqN):
        params = self.CoefNParamsByN()
        iniEqN = params[5-1]
        y=0
        P=self.SolutNPow(eqN)
        if eqN==NInEq:
            r=self.soluts[EqN-1].A[]

    def calcCoef(self, eqN, wholeMatrixCoefN):
        y=0
        #z=complex.imag(
        
        

                 
