import copy
import math

class HResSimple:
    def __init__(self, k=0, Conn_Suc0Par1=0, Ress=[]):
        self.SetDefault()#uz self.Elements=[]
        self.Conn_Suc0Par1=Conn_Suc0Par1
        self.k=k
        Q=len(Ress)
        for i in range(1, Q+1):
            Element=copy.deepcopy(Ress[i-1])
            self.Elements.append(Element)
            
    def SetDefault(self):
        self.Elements=[]
        self.Conn_Suc0Par1=0
        self.k=0

    def Calc(self, vsh=0):
        S=0
        C=0
        if(vsh==1):
            print('Calc starts working')
        R=self.k
        if(vsh==1):
            print('R='+str(R))
        L=len(self.Elements)
        if(vsh==1):
            print('L='+str(L))
        #if(L>0):#abl ac ce
        if self.Conn_Suc0Par1==0:
            if(vsh==1):
                print('succ conn')
            S=0
            for i in range(1, L+1):
                C=self.Elements[i-1].Calc()
                if(vsh==1):
                    print("prev Calc finished, external one continueing")
                C=C*C
                S=S+C
                if(vsh==1):
                    print("RN"+str(i)+" k="+str(self.Elements[1-1].k)+" C="+str(C)+" S="+str(S))
            R=R+math.sqrt(S)
        elif self.Conn_Suc0Par1==1:
            S=0
            if(vsh==1):
                print('parallel conn')
            for i in range(1, L+1):
                C=1/self.Elements[i-1].Calc()
                if(vsh==1):
                    print("prev Calc finished, external one continueing")
                S=S+C
                if(vsh==1):
                    print("RN"+str(i)+" k="+str(self.Elements[1-1].k)+" C="+str(C)+" S="+str(S))
            if(S!=0):
                R=R+1/S
        if(vsh==1):
            print('R='+str(R))
            print('Calc finishes working')
        return R

    def Add(self, ElementExt):
        Element=copy.deepcopy(ElementExt)
        self.Elements.append(Element)



QVals=4
QNumerats=4

DenRes=10

class RecStr:
    def __init__(self, QVals=0, QNumerats=0):
        self.QVals=0
        self.QNumerats=0
        self.Denomin=0
        self.p=[]
        self.lst=[]
        self.N=0
        self.countAll=0
        self.countGut=0
        if(QVals>0 and QNumerats>0):
            self.Set(QVals, QNumerats)
            self.N=1
        #print("RecStr created: QVals="+str(QVals)+"="+str(self.QVals)+" QNumerats="+str(QNumerats)+"="+str(self.QNumerats))
            
    def Set(self, QVals, QNumerats):
        self.QVals=QVals
        self.QNumerats=QNumerats
        self.Denomin=self.QVals*self.QVals*self.QNumerats
        #self.MaxNumerat=self.QVals*self.QNumerats
        self.N=1
        for i in range (1, self.QVals+1):
            #self.p[i-1]=i
            self.p.append(0)

    #def SetN(self, N):
    #    self.N=N

    def __str__(self):#works gut. Ma full idem fn o'alt class ne works in Py2
        #st=" QVals="+str(self.QVals)+" QNumerats="+str(self.QVals)+"; Denomin="+str(self.Denomin)+" Sum="+str(self.Sum)+" N="+str(self.N)+" size(p)="+str(len(self.p))
        st=" QVals="+str(self.QVals)+" QNumerats="+str(self.QVals)+" N="+str(self.N)+" size(p)="+str(len(self.p))
        return st



def RecSearch(dataExt, Show1Hide0=0):
    data=copy.deepcopy(dataExt)
    st=""
    Sum=0
    data.countAll=data.countAll+1
    countAll=data.countAll
    N=data.N
    if Show1Hide0==1:
        print("RecSearch Starts working. countAll=",countAll, " N=",data.N)
    for i in range(1, data.QNumerats+1):
        data.p[N-1]=i#vikt! so ob af recurs data.N wi alt, so nur ine N!
        st="countAll="+str(countAll)+" N="+str(N)+" i="+str(i)+" p["+str(N)+"]="+str(data.p[N-1])+" : " 
        if Show1Hide0==1 and N<data.QVals:
            print(st)
        #if data.N==data.QVals:#NLim
        if N==data.QVals:#vikt! so ob af recurs data.N wi alt, so nur ine N!
            Sum=0
            for j in range(1, data.QVals+1):
                Sum=Sum+data.p[j-1]
                st=st+str(data.p[j-1])
                if(j<data.QVals):
                    st=st+" + "
                #Elt=[]
                
            st=st+" = "+str(Sum)+" "
            if Show1Hide0==1:
                print(st)
            if Sum==DenRes:#get out rec
                data.countGut=data.countGut+1
                #Elt.append(
                pc=copy.deepcopy(data.p)
                data.lst.append(pc)
                if Show1Hide0==1:
                    print("Required Sum! ="+str(Sum)+" = "+str(DenRes))
            #if countAll<data.QVals*data.QNumerats:# no nod
            data.N=1
        else:
            if Show1Hide0==1:
                print("So, N="+str(N)+" data.N="+str(data.N))
            data.N=N+1 #vikt! so ob af recurs data.N wi alt, so nur ine N!
            if Show1Hide0==1:
                print("And now N="+str(N)+" data.N="+str(data.N))
            data=RecSearch(data, Show1Hide0)
            if Show1Hide0==1:
                print("Return to prev. CountAll="+str(countAll)+" N="+str(N))
    if Show1Hide0==1:
        print("RecSearch Finishes working. countAll=",countAll, " N=",data.N)  
    return data

def CalcEqualBounds(a, b, QSects):
    Y=[]
    dx=(b-a)/QSects
    for i in range(1, QSects+1):
        c=(i-1)*dx
        Y.append(c)
    return Y

class PositionInSuccession:
    def __init__(self, IsLess=0, IsGreater=0, EqualN=0, LessN=0):
        #self.LessN=LessN#.LessN=0
        #self.EqualN=EqualN#self.EqualN=0
        #self.IsLess=IsLess#self.IsLess=0
        #self.IsGreater=IsGreater#self.IsGreater=0
        self.SetIni()

    def SetIni(self):
        self.LessN=0
        self.EqualN=0
        self.IsLess=0
        self.IsGreater=0

    def __str__(self):#ne works in Py2. Ma full idem fn o'alt class  works in Py2 gut
        st=" IsLess="+str(self.IsLess)+" IsGreater="+str(self.IsGreater)+" EqualN="+str(self.EqualN)+" LessN="+str(self.LessN)
        print("Info:  "+st)
        return st########
   #def __str__(self):

    #def Show(self):
    #    st=" IsLess="+str(self.IsLess)+" IsGreater="+str(self.IsGreater)+" EqualN="+str(self.EqualN)+" LessN="+str(self.LessN)
    #    print("Info:  "+st)
        


def DefPositionInSuccession(x, Xe, ValsShow1Hide0=0):
    pos=PositionInSuccession()
    X=copy.deepcopy(Xe)
    if ValsShow1Hide0==1:
        print("DefPositionInSuccession starts working. Before work:")
        print("pos: ", pos)
        print("pos: ", pos.__str__())
        print("X: ", X)
        if isinstance(X, list):
            print("X is List, Length="+str(len(X)))
        else:
            print("X: ", X)
            print("X is NOT List")
    if(isinstance(X, list) and len(X)>0):
        Q=len(X)
        if ValsShow1Hide0==1:
            print("Q=", Q)
        if x<X[1-1]:
            pos.IsLess=1
            if ValsShow1Hide0==1:
                print("x IsLess: "+str(x)+"<"+str(X[1-1]))
        elif x>X[Q-1]:
            pos.IsGreater=1
            if ValsShow1Hide0==1:
                print("x is IsGreater: "+str(x)+">"+str(X[Q-1]))
        else:
            for i in range(1, Q+1):
                if x==X[i-1]:
                    pos.EqualN=i
                    if ValsShow1Hide0==1:
                        print("x="+str(x)+"=X["+str(i)+"]="+str(X[i-1]))
            #if pos.EqualN>0:
            #    Y=X
            #else:
            if pos.EqualN==0:
                for i in range(1, Q-1+1):
                    if x>X[i-1] and x<X[i+1-1]:
                        pos.LessN=i
                        if ValsShow1Hide0==1:
                            print("X["+str(i)+"]="+str(X[i-1])+"<x="+str(x)+"<X["+str(i+1)+"]="+str(X[i+1-1]))
        if pos.EqualN==0 and pos.LessN==0 and pos.IsLess==0 and pos.IsGreater==0 and ValsShow1Hide0==1:
            print("unknown vrn")
    else:
        if ValsShow1Hide0==1:
            print("X is not a list or is an empty list")
    if ValsShow1Hide0==1:
        print("So Pos: ", pos.__str__())
        print("DefPositionInSuccession finishes working")
    return pos
            
def Sort(Xe, SortDir_Asc0Desc1=0):
    X=copy.deepcopy(Xe)
    Q=len(X)
    if SortDir_Asc0Desc1==0:
        for i in range (1, Q+1):
            for j in range (i, Q+1):
                if X[j-1]<X[i-1]:
                    buf=X[j-1]
                    X[j-1]=X[i-1]
                    X[i-1]=buf
    else:
        for i in range (1, Q+1):
            for j in range (i, Q+1):
                if X[j-1]>X[i-1]:
                    buf=X[j-1]
                    X[j-1]=X[i-1]
                    X[i-1]=buf
    return X        

def InsToSucc(x, Xe):
    X=copy.deepcopy(Xe)
    Y=[]
    Q=len(X)
    pos=DefPositionInSuccession(x, X)
    #print("pos: ",x," ",pos)
    if(pos.IsLess==1):
        Y.append(x)
        for i in range(1, Q+1):
            Y.append(X[i-1])
    elif(pos.IsGreater==1):
        for i in range(1, Q+1):
            Y.append(X[i-1])
        Y.append(x)
    elif pos.LessN>0:
        for i in range(1, pos.LessN+1):
            Y.append(X[i-1])
        Y.append(x)
        for i in range(pos.LessN+1, Q+1):
            Y.append(X[i-1])
    else:#EqualN>0
        #Y=X
        Y=copy.deepcopy(X)
    return Y
    



        
