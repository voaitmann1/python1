import copy
import math
import numpy as np
import sys
from MyLib import *



def myArctan(x, y):
    y=1.0*y
    x=1.0*x
    if math.fabs(x)>0:
        lar=math.atan(math.fabs(y)/math.fabs(x)) #local angle, radians
        if x>0 and self.im>0:
            r=lar
        elif x<0 and y>0:
            r=math.pi-lar
        elif x<0 and y<0:
            r=math.pi+lar
        elif x<0 and y>0:
            r=2.0*math.pi-lar
        #
        elif y==0:
            if x<0:
                r=math.pi
            else:
                r=0
    else:
        if y>0:
            r=math.pi/2
        elif y<0:
            r=3*math.pi/2
        else:
            r=0
    return r

class Complex:
    def __init__(self, re=0, im=0):
        self.re=1.0*re
        self.im=1.0*im

    def toString(self, showRe0Yes1No0=1, showIm0Yes1No0=1):
        s=""
        if(self.re!=0 or showRe0Yes1No0==1):
            s+=str(self.re)
        if(self.im!=0 or showIm0Yes1No0==1):
            if self.im>=0:
                s+="+"
            s+=str(self.im)+"*i"
        return s

    def get(self):
        re=1+0j
        im=0+1j
        return (re*self.re+im*self.im)        

    def getRe():
        return self.re

    def getArg():
        return myArctan(self.re, self.im)

    def getAbs():
        return math.sqrt(self.re*self.re+self.im*self.im)

    def getRe():
        return self.re
    
    def getIm():
        return self.im

    def add(self, x1, x2=0, self012=0):
        if self012==0:
            if isinstance(x1, Complex):
                if isinstance(x2, Complex):
                    y=Complex(x1.re+x2.re, x1.im+x2.im)
                else:
                    y=Complex(x1.re+x2, x1.im)
            else:
                if isinstance(x2, Complex):
                    y=Complex(x1+x2.re, x2.im)
                else:
                    y=Complex(x1+x2, 0)
        elif self012==1:
            if isinstance(x1, Complex):
                y=Complex(self.re+x1.re, self.im+x1.im)
            else:
                y=Complex(self.re+x1, self.im)
        elif self012==2:
            if isinstance(x1, Complex):
                y=Complex(x1.re+self.re, x1.im+self.im)
            else:
                y=Complex(x1+self.re, self.im)
        return y

    def subtract(self, x1, x2=0, self012=0):
        if self012==0:
            if isinstance(x1, Complex):
                if isinstance(x2, Complex):
                    y=Complex(x1.re-x2.re, x1.im-x2.im)
                else:
                    y=Complex(x1.re-x2, x1.im)
            else:
                if isinstance(x2, Complex):
                    y=Complex(x1-x2.re, x2.im)
                else:
                    y=Complex(x1-x2, 0)
        elif self012==1:
            if isinstance(x1, Complex):
                y=Complex(self.re-x1.re, self.im-x1.im)
            else:
                y=Complex(self.re-x1, self.im)
        elif self012==2:
            if isinstance(x1, Complex):
                y=Complex(x1.re-self.re, x1.im-self.im)
            else:
                y=Complex(x1-self.re, self.im)
        return y

    def multiply(self, x1, x2=0, self012=0):
        if self012==0:
            if isinstance(x1, Complex):
                if isinstance(x2, Complex):
                    y=Complex(x1.re*x2.re-x1.im*x2.im, x1.re*x2.im+x1.im*x2.re)
                else:
                    y=Complex(x1.re*x2, x1.im*x2)
            else:
                if isinstance(x2, Complex):
                    y=Complex(x1*x2.re, x1*x2.im)
                else:
                    y=Complex(x1*x2, 0)
        elif self012==1:
            if isinstance(x1, Complex):
                y=Complex(self.re*x1.re-self.im*x1.im, self.re*x1.im+self.im*x1.re)
            else:
                y=Complex(self.re*x1, self.im*x1)
        elif self012==2:
            if isinstance(x1, Complex):
                y=Complex(x1.re*self.re-x1.im*self.im, x1.im*self.re+x1.re*self.im)
            else:
                y=Complex(x1*self.re, x1*self.im)
        return y

    def getConjugated():
        return Complex(self.re, -self.im)

    def divide(self, x1, x2=0, self012=0):
        if self012==0:
            if isinstance(x1, Complex):
                if isinstance(x2, Complex):
                    z=x2.getConjugated()
                    numerator=multiply(x1, z)
                    denominator=x2.re*x2.re+x2.im*x2.im
                    if not (denominator==0):
                        y=Complex(numerator.getRe()/denominator, numerator.getIm()/denominator)
                else:
                    if not (x2==0):
                        y=Complex(x1.re/x2, x1.im/x2)
            else:
                if isinstance(x2, Complex):
                    z=x2.getConjugated()
                    numerator=multiply(x1, z)
                    denominator=x1.re*x1.re+x1.im*x1.im
                    if not (denominator==0):
                        y=Complex(numerator.getRe()/denominator, numerator.getIm()/denominator)
                else:
                    if x2!=0:
                        y=Complex(x1/x2, 0)
        elif self012==1:
            if isinstance(x1, Complex):
                z=x1.getConjugated()
                numerator=multiply(self, z)
                denominator=x1.re*x1.re+x1.im*x1.im
                if not (denominator==0):
                    y=Complex(numerator.getRe()/denominator, numerator.getIm()/denominator)
            else:
                if not (x1==0):
                    y=Complex(self.re/x1, self.im/x1)
        elif self012==2:
            z=self.getConjugated()
            x1=complexify(x1)
            numerator=multiply(x1, z)
            denominator=self.re*self.re+self.im*self.im
            y=Complex(numerator.getRe()/denominator, numerator.getIm()/denominator)
        return y

def countComplexVals(X):
    count=0
    if isinstance(X, list):
        QL=len(X)
        if isinstance(X[0], list):
            QC=len(X[0])
            for i in range(QL):
                for j in range(QC):
                    x=X[i-1][j-1]
                    if complex(x).imag!=0 or (isinstance(x, Complex) and fabs(x.im)>0):
                        count+=1
        else:
            for i in range(QL):
                x=X[i-1]
                if complex(x).imag!=0 or (isinstance(x, Complex) and fabs(x.im)>0):
                    count+=1
    else:
        if complex(X).imag!=0 or (isinstance(X, Complex) and fabs(X.im)>0):
            count+=1
    return count

def complexify(A):
    #R=A
    if isinstance(A, list):
        R=[]
        print(R)
        QL=len(A)
        if isinstance(A[0], list):
            QC=len(A[0])
            for i in range(1, QL+1):
                row=[]
                for j in range(1, QC+1):
                    x=A[i-1][j-1]*(1+0j)
                    row.append(x)
                R.append(row)
        else:
            for i in range(1, QL+1):
                x=A[i-1]*(1+0j)
                #print("x="+str(x))
                R.append(x)
                #print("R="+str(R))
    else:
        R=A*(1+0j)
    return R

def Re(A):
    if isinstance(A, list):
        R=[]
        QL=len(A)
        if isinstance(A[0], list):
            QC=len(A[0])
            for i in range(1, QL+1):
                row=[]
                for j in range(1, QC+1):
                    xc=complex(A[i-1][j-1])
                    x=xc.real
                    row.append(x)
                R.append(row)
        else:
            for i in range(1, QL+1):
                xc=complex(A[i-1])
                x=xc.real
                R.append(x)
    else:
        xc=complex(A)
        x=xc.real
        R=x
    return R


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

def fPolynome_coefsOrderNEqualToPower(x, C):
    L=len(C)
    y=C[0]
    xp=1
    for p in range(1, L-1+1):
        xp*=x
        y=y+C[p]*xp
    return y


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
    #fp=fGorner_forRoot_coefsOrderNEqualToPower(apw, cp)
    fp=fGorner_forRoot_coefsOrderNEqualToPower(ap, cr)
    if(vsh==1):
        print("fGorner_forRoot_coefsOrderNEqualToPower="+str(fp))
    yr=copy.deepcopy(fp)
    yr.append(bp[len(bp)-1])
    if(vsh==1):
        print("Answer="+str(yr))
    return yr


def fPolynomeGorner_coefsOrderPowerDecrease(Cp, x, cr, vsh=1):
    if(vsh==1):
        print("fPolynomeGorner_coefsOrderPowerDecrease starts working")
        print("given: cr="+str(cr)+" coefs: "+str(Cp))
    ord1=len(Cp)
    #bp=fGorner_forRoot(Cp, c)
    bp=fGorner_forRoot_coefsOrderPowerDecrease(Cp, cr)
    if(vsh==1):
        print(" Coefs of decreased order polynome: "+str(bp))
    PolLesOrd=fPolynomeIni_coefsOrderPowerDecrease(bp, x)
    if(vsh==1):
        print(" Coefs of decreased order polynome: "+str(bp))
    y=PolLesOrd*(x-cr)
    return y

def fPolynomeGorner_coefsOrderNEqualToPower(Cp, x, cr):
    ord1=len(Cp)
    #bp=fGorner_forRoot(Cp, cr)
    bp=fGorner_forRoot_coefsOrderNEqualToPower(Cp, cr)
    PolLesOrd=fPolynomeIni_coefsOrderPowerDecrease(bp, x)
    y=PolLesOrd*(x-cr)
    return y


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

            
def Dichotomy(fn, dichotomyParams, fnParams=[], vsh=0):
    QSects=dichotomyParams.Qi
    LBnd=dichotomyParams.LBnd
    HBnd=dichotomyParams.HBnd
    sectL=dichotomyParams.getSectL()
    if(vsh==1):
        print("Dichotomy starts working")
        print(str(QSects)+" sections: "+str(dichotomyParams.LBnd)+"..."+str(dichotomyParams.HBnd))
    X=[]
    Y=[]
    #B=[]
    #for n in range(1, QSects+1):
    #    cLBnd=LBnd+sectL*(n-1)
    #    cHBnd=cLBnd+sectL
   
    B=dichotomyParams.getValues()
    if(vsh==1):
        print("Sects bounds: "+str(B))
        print(str(QSects))

    if fnParams==[]:
        fa=fn(dichotomyParams.LBnd)
        #fa=fn(cLBnd)
    else:
        fa=fn(dichotomyParams.LBnd, fnParams)
        #fa=fn(cLBnd, fnParams)
    N1=-1
    if math.fabs(fa) < dichotomyParams.epsY:
        X.append(dichotomyParams.LBnd)
        Y.append(fa)
        if(vsh==1):
            #print(" solution found: x="+str(cLBnd)+" f(x)="+str(fa))
            print(" solution found: x="+str(dichotomyParams.LBnd)+" f(x)="+str(fa))
            N1=2
    else:
        N1=1
        
    for n in range(N1, QSects-1+1):
        if(vsh==1):
            print("Sect "+str(n))
        cLBnd=B[n-1]
        cHBnd=cLBnd+sectL
        if(vsh==1):
            print(" cLBnd="+str(cLBnd)+"cHBnd="+str(cHBnd))
        
        #if fnParams==[]:
        #    fa=fn(cLBnd)
        #else:
        #    fa=fn(cLBnd, fnParams)
        #if math.fabs(fa) < dichotomyParams.epsY:
        #    X.append(cLBnd)
        #    Y.append(fa)
        #    if(vsh==1):
        #        print(" solution found: x="+str(cLBnd)+" f(x)="+str(fa))
        #if n==1:
        #    if fnParams==[]:
        #       #fa=fn(dichotomyParams.LBnd)
        #        fa=fn(cLBnd)
        #    else:
        #        #fa=fn(dichotomyParams.LBnd, fnParams)
        #        fa=fn(cLBnd, fnParams)
        #        if math.fabs(fa) < dichotomyParams.epsY:
        #            X.append(dichotomyParams.LBnd)
        #            Y.append(fa)
        #            if(vsh==1):
        #                print(" solution found: x="+str(cLBnd)+" f(x)="+str(fa))
        #                #print(" solution found: x="+str(dichotomyParams.LBnd)+" f(x)="+str(fa))
        if 4>5:
            pass
        else:    
            a=cLBnd
            b=cHBnd
            if(vsh==1):
                print(" a="+str(a)+"b="+str(b))
                print(" fa=fn("+str(a)+")")
            if fnParams==[]:
                fa=fn(a)
                fb=fn(b)
            else:
                fa=fn(a, fnParams)
                fb=fn(b, fnParams)
            if(vsh==1):
                print("Sect "+str(n)+" f("+str(a)+")="+str(fa)+", f("+str(b)+")="+str(fb))
            #
            if(fa*fb<0 or math.fabs(fa*fb)<dichotomyParams.epsY):
                if(vsh==1):
                    print(str(fa)+"*"+str(fb)+"="+str(fa*fb)+"<0 => here is solution to find")
                contin=1
                countIters=0
                while contin==1:
                    countIters+=1
                    c=(a+b)/2.0
                    #
                    if fnParams==[]:
                        fa=fn(a)
                        fb=fn(b)
                        fc=fn(c)
                    else:
                        fa=fn(a, fnParams)
                        fb=fn(b, fnParams)
                        fc=fn(c, fnParams)
                    if(vsh==1):
                        print(" f(a="+str(a)+")="+str(fa)+" f(b="+str(b)+")="+str(fb)+" f(c="+str(c)+")="+str(fc))
                    #
                    if b-a<dichotomyParams.epsX:
                        X.append(c)
                        Y.append(fc)
                        contin=0
                        if(vsh==1):
                            print(" b="+str(b)+" - a="+str(a)+" ="+str(b-a)+" <eps= "+str(dichotomyParams.epsX)+" => found: "+str(c))
                    elif math.fabs(fa)<dichotomyParams.epsY and (n==1 or a!=cLBnd):
                    #elif math.fabs(fa)<dichotomyParams.epsY:
                        X.append(a)
                        Y.append(fa)
                        contin=0
                        if(vsh==1):
                            print(" fa="+str(fa)+" <eps= "+str(dichotomyParams.epsY)+" => found: "+str(a))
                    elif math.fabs(fb)<dichotomyParams.epsY:
                        X.append(b)
                        Y.append(fb)
                        contin=0
                        if(vsh==1):
                            print(" fb="+str(fb)+" <eps= "+str(dichotomyParams.epsY)+" => found: "+str(b))
                    elif math.fabs(fc)<dichotomyParams.epsY:
                        X.append(c)
                        Y.append(fc)
                        contin=0
                        if(vsh==1):
                            print(" fc="+str(fc)+" <eps= "+str(dichotomyParams.epsY)+" => found: "+str(c))
                    elif countIters>dichotomyParams.Qi*5:
                        contin=0
                        print("Stopped because too many iteraions: "+str(countIters))
                    else:
                        if fa*fc<0:
                            b=c
                            if(vsh==1):
                                print(" fa*fc<0="+str(fa*fc)+" b=c="+str(b) )
                        elif fb*fc<0:
                            a=c
                            if(vsh==1):
                                print(" fb*fc<0="+str(fb*fc)+" b=c="+str(b) )
            else:
                if(vsh==1):
                    print(str(fa)+"*"+str(fb)+"="+str(fa*fb)+">=0 => here is NO solution")
    if(vsh==1):
        print("Dichotomy finishes working")
    return X
