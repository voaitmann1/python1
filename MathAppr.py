import math
import copy

class MathApprox:
    def __init__(self, Q=10, dL=1e-6, byWhat_Q1_dL2_And3_Or4=4, QIsQSects0QBounds1=0, QAny0Odd1Even2=0):
        if QIsQSects0QBounds1==0:
            self.Qscts=Q
        else:
            self.Qscts=Q-1
        if ((self.Qscts%2==0 and QAny0Odd1Even2==1) or(self.Qscts%2!=0 and QAny0Odd1Even2==2)):
            self.Qscts+=1
        self.dL=dL
        self.byWhat_Q1_dL2_And3_Or4=byWhat_Q1_dL2_And3_Or4

    def GetRealQAnddL(self, LB, HB, QAny0Odd1Even2=0):
        R=[]
        Q1=self.Qscts
        dL1=(HB-LB)/Q1
        if dL1>self.dL:
            if not (self.byWhat_Q1_dL2_And3_Or4==1 or self.byWhat_Q1_dL2_And3_Or4==4):
               while dL1>self.dL:
                   Q1+=1
                   dL1=(HB-LB)/Q1
        if ((Q1%2==0 and QAny0Odd1Even2==1) or(Q1%2!=0 and QAny0Odd1Even2==2)):
            Q1+=1
        R.append(Q1)
        R.append(dL1)
        return R

    def calcRange(self, LB, HB, QAny0Odd1Even2=0):
        R=[]
        p=self.GetRealQAnddL(LB, HB, QAny0Odd1Even2)
        Q=p[1-1]
        dL=p[2-1]
        R.append(LB)
        x=LB
        for i in range(1, Q):
            x+=dL
            R.append(x)
        R.append(HB)
        return R

def deriv1(fn, x, dx=1e-6, left1Right2Both3=3):
    if left1Right2Both3==3:
        LB=x-dx/2
        HB=x+dx/2
    elif left1Right2Both3==1:
        LB=x-dx
        HB=x
    elif left1Right2Both3==2:
        LB=x
        HB=x+dx
    x1=LB
    x2=HB
    y1=fn(x1)
    y2=fn(x2)
    dy=(y2-y1)/(x2-x1)
    return dy
    
#y=y0+v0t+at**2/2=> a=(2/t**2)*(y-y0-v0t)

def deriv21(fn, x, dx=1e-6, left1Right2Both3=3):
    y=fn(x)
    y0=fn(x-dx)
    v0=deriv1(fn, x-dx, dx, left1Right2Both3)
    d2y=2/dx/dx*(y-y0-v0*dx)
    return d2y

def deriv22(fn, x, dx=1e-6, left1Right2Both3=3):
    if left1Right2Both3==3:
        LB=x-dx/2
        HB=x+dx/2
    elif left1Right2Both3==1:
        LB=x-dx
        HB=x
    elif left1Right2Both3==2:
        LB=x
        HB=x+dx
    x1=LB
    x2=HB
    y1=deriv1(fn, x1, dx, left1Right2Both3)
    y2=deriv1(fn, x2, dx, left1Right2Both3)
    dy=(y2-y1)/(x2-x1)
    return dy
    

LB=0
HB=3*math.pi

mappr=MathApprox(20, 3)
p=mappr.GetRealQAnddL(LB, HB)
Q=p[1-1]
dL=p[2-1]
print("Params: Q="+str(Q)+" dL="+str(dL)+" LB="+str(LB)+" HB="+str(HB))
R=mappr.calcRange(LB, HB)
print("Range: "+str(R))
Q=len(R)
Y=[]
dY1=[]
dY2=[]
d2Y1=[]
d2Y2=[]
d2Y3=[]
for i in range(1, Q+1):
    x=R[i-1]
    Y.append(math.sin(x))
    dY1.append(math.cos(x))
    dY2.append(deriv1(math.sin, x, dL))
    d2Y1.append(-math.sin(x))
    d2Y2.append(deriv21(math.sin, x, dL))
    d2Y3.append(deriv22(math.sin, x, dL))
    print(str(i)+") fi="+str(x*180/math.pi)+" sin="+str(Y[i-1])+" cos="+str(dY1[i-1])+" == "+str(dY2[i-1]))#gut
    #print(str(i)+") fi="+str(x*180/math.pi)+" sin="+str(Y[i-1])+" -sin="+str(d2Y1[i-1])+"  == "+str(d2Y2[i-1]))#bad
    print(str(i)+") fi="+str(x*180/math.pi)+" sin="+str(Y[i-1])+" -sin="+str(d2Y1[i-1])+"  == "+str(d2Y3[i-1]))#gut

