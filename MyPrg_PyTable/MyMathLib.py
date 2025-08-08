import copy
from MyLib1 import *
#
def fMin(X):
    if isinstance(X, list) and len(X):
        Q=len(X)
    if Q>0:
        for i in range(1, Q+1):
            if i==1 or (i>1 and X[i-1]<minimum):
                minimum=X[i-1]
    return minimum

def fMax(X):
    if isinstance(X, list) and len(X):
        Q=len(X)
    if Q>0:
        for i in range(1, Q+1):
            if i==1 or (i>1 and X[i-1]>maximum):
                maximum=X[i-1]
    return maximum

class PositionInSuccession:
    def __init__(self):
        self.less=0
        self.greater=0
        self.within=0
        self.EqualN=0
        self.LessN=0

    def get_as_list(self):
        Z=[["Less", self.less],
           ["Greater", self.greater],
           ["Within", self.within],
           ["EqualN", self.EqualN],
           ["LessN", self.LessN]
        ]
        return Z

    def __str__(self):
        s=" IsLess: "+str(self.less)+" IsGreater: "+str(self.greater)+" IsWithin: "+str(self.within)+" EqualN="+str(self.EqualN)+" LessN="+str(self.LessN)
        return s



def Sort(X):
    Q=len(X)
    Y=copy.deepcopy(X)#ac ne ne works
    minLoc=0
    maxLoc=0
    minN=0
    maxN=0
    for i in range(1, Q+1):
        for j in range(i, Q+1):
            first=i
            if j==first or (j>first and [j-1]<minLoc):
                minLoc=Y[j-1]
                minN=j
        if Y[minN-1]==minLoc:
            buf=X[i-1]
            Y[i-1]=Y[minN-1]
            Y[minN-1]=buf
    return Y
#            
def appr_ET(x1, x2, eps):
    y=0
    if abs(x1-x2)<=eps:
        y=1
    return y
#
def appr_GT(x1, x2, eps):
    y=0
    if x1>x2 and abs(x1-x2)>eps:
        y=1
    return y
#
def appr_LT(x1, x2, eps):
    y=0
    if x1<x2 and abs(x1-x2)>eps:
        y=1
    return y
#
def appr_NE(x1, x2, eps):
    y=0
    if abs(x1-x2)>eps:
        y=1
    return y
#
def appr_GE(x1, x2, eps):
    y=0
    if x1>x2 or abs(x1-x2)<eps:
        y=1
    return y
#
def appr_LE(x1, x2, eps):
    y=0
    if x1<x2 or abs(x1-x2)<eps:
        y=1
    return y
#                            
def PosInSucc(x,X, eps=0):
    #less=0
    #greater=0
    #within=0
    #EqualN=0
    #LessN=0
    Z=PositionInSuccession()
    Q=0
    if(isinstance(X, list) and len(X)>0):
        Q=len(X)
    if Q>0:
        Y=Sort(X)
        print('Y',Y)
        if x<Y[1-1]:
            Z.less=1
        elif x>Y[Q-1]:
            Z.greater=1
        else:
            Z.within=1
            for i in range(1, Q+1):
                if appr_ET(x, Y[i-1], eps)==1:
                    Z.EqualN=i
            if Z.EqualN==0:
                for i in range(1, Q-1+1):
                    if x>Y[i-1] and x<Y[i+1-1]:
                        Z.LessN=i
    return Z
#
def PosInSucc_Eq(x, X, eps=0):
    Z=PosInSucc(x, X, eps)
    R=Z.EqualN
    return R
#
def PosInSucc_LessN(x, X, eps=0):
    Z=PosInSucc(x, X, eps)
    R=Z.LessN
    return R

def LInterp(x, X, Y, eps=0):
    pos=PosInSucc(x, X, eps)
    Q=len(X)#
    if pos.EqualN>0:
        y=Y[pos.EqualN-1]
    else:
        if pos.less==1:
            x1=X[1-1]
            x2=X[2-1]
            y1=Y[1-1]
            y2=Y[2-1]
        elif pos.greater==1:
            x1=X[Q-1-1]
            x2=X[Q-1]
            y1=Y[Q-1-1]
            y2=Y[Q-1]
        elif pos.within==1:
            x1=X[pos.LessN-1]
            x2=X[pos.LessN+1-1]
            y1=Y[pos.LessN-1]
            y2=Y[pos.LessN+1-1]
        k=(y2-y1)/(x2-x1)
        y=y1+k*(x-x1)
    return y
#
#
X=[ 10,  20,  30,  40]
Y=[100, 200, 300, 400]
V=[5, 10, 13, 20, 31, 40, 55]
Q=len(V)
eps=0
for i in range (1, Q+1):
    x=V[i-1]
    Z=PosInSucc(x, X, eps)
    print(x," all: ",str(Z))
    #print(x," ",Z[4-1][1-1],": ",PosInSucc_Eq(x, X, eps)," = ",Z[4-1][2-1])
    #print(x," ",Z[5-1][1-1],": ",PosInSucc_LessN(x, X, eps)," = ",Z[5-1][2-1])
    print(x," EN=",Z.EqualN)
    print(x," LN=",Z.LessN)
    y=LInterp(x, X, Y)
    print(x," interpolated:=",y)
