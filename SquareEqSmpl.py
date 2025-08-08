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
        ImX1=-math.sqrt(-d)/(2*a)
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
            y=-1.0*b/k
            #print(" k="+str(k)+" b="+str(b)+" y="+str(y))
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
            else:
                y=(-b/(2*a))
                self.ReX.append(y)
                self.ReX.append(y)
                y=-math.sqrt(-d)/(2*a)
                self.ImX.append(y)
                y=math.sqrt(-d)/(2*a)
                self.ImX.append(y)
        
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
            s="too little data for any equation: "
        elif order==1:
            s="linear equation: "
        elif order==2:
            s="square equation: "
        else:
            s="Polynomial equation of "+str(order)+" order: "
        for i in range(2, order+1+1):
            N=order+1-i+1 # ord 2 i 2 N 2; ord 2 i 3 N 1
            s=s+str(self.C[N])+"*x"
            if N>1:
                s=s+"^"+str(N)
            s=s+"+"
        s=s+str(self.C[0])+"=0"
        return s

    def SolutionToString(self):
        s=""
        order=len(self.C)-1
        for i in range(1, order+1):
            if(self.ImX[i-1]==0):
                s=s+"x"+str(i)+"="+str(self.ReX[i-1])+" "
            else:
                s=s+"x"+str(i)+"="+str(self.ReX[i-1])+"+i*"+str(self.ImX[i-1])+" "
        return s

C=[1,2]#order 0, 1, 2
equation=PolynomialEquation(C)
print("Equation: "+equation.EquationToString())
equation.Solve()
print("Solution: "+equation.SolutionToString())
C=[1,2, 4]#order 0, 1, 2
equation=PolynomialEquation(C)
print("Equation: "+equation.EquationToString())
equation.Solve()
C=[1,2, 1]#order 0, 1, 2
equation=PolynomialEquation(C)
print("Equation: "+equation.EquationToString())
equation.Solve()
print("Solution: "+equation.SolutionToString())
print("Function: ")
SolveSquareEquation(4, 2, 1)
        
