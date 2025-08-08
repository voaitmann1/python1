import math
import copy

def SolveSquareEquation(a, b, c):
    d=b*b-4*a*c
    if d>=0:
        x1=(-b-math.sqrt(d))/(2*a)
        x2=(-b+math.sqrt(d))/(2*a)
        print("x1="+str(x1)+" x2="+str(x2))
    else:
        ReX1=(-b/(2*a))
        ReX2=ReX1
        ImX1=math.sqrt(-d)/(2*a)
        ImX2=math.sqrt(-d)/(2*a)
        print("x1="+str(ReX1)+"+i*"+str(ImX1)+" x2="+str(ReX2)+"+i*"+str(ImX2))

class PolynomialEquation:
    def __init__(self, C):
        self.C=[]
        self.ReX=[]
        self.ImX=[]
        self.Set(C)

    def Set(self, C):
        if isinstance(C, list):
            self.C=copy.deepcopy(C)

    def Solve(self):
        order=len(self.C)-1
        self.ReX=[]
        self.ImX=[]
        if(order<1):
            print("too small quantity of coefficients")
        elif order==1:
            b=self.C[0]
            k=self.C[1]
            y=-b/k
            self.ReX.append(y)
            self.ImX.append(0)
        elif order==2:
            a=self.C[2]
            b=self.C[1]
            c=self.C[0]
            d=b*b-4*a*c
            if d>=0:
                y=(-b-math.sqrt(d))/(2*a)
                self.ReX.append(y)
                y=(-b+math.sqrt(d))/(2*a)
                self.ReX.append(y)
                self.ImX.append(0)
                self.ImX.append(0)
        
    def getRes(self):
        return self.ReX

    def getIms(self):
        return self.ImX

    def getOrder(self):
        return len(ReX)-1

    def EquationToString(self):
        s=""
        order=len(self.C)-1
        if order<1:
            s="too little data for any equation"
        elif order==1:
            s="linear equation "
            for i in range(1, order+1+1):
                N=order+1-i
                s=s+str(C[N-1])+"*x^"+str(N)
        return s

    def SolutionToString(self):
        s=""
        order=len(self.C)-1
        #for i in range(1, order+1):
        #    if(Im(

C=[1,2,1]
equation=PolynomialEquation(C)
equation.Solve()
SolveSquareEquation(1, 2, 20)
        
