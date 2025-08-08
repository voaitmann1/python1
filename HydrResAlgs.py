
QVals=3
QNumerats=3

DenRes=24

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

    def __str__(self):
        st=" QVals="+str(self.QVals)+" QNumerats="+str(self.QVals)+"; Denomin="+str(self.Denomin)+" Sum="+str(self.Sum)+" N="+str(self.N)+" size(p)="+str(len(self.p))
        return st



def RecSearch(data, Show1Hide0=1):
    #data=dataExt
    st=""
    Sum=0
    data.countAll=data.countAll+1
    countAll=data.countAll
    N=data.N
    if Show1Hide0==1:
        print("RecSearch Starts working. countAll=",countAll, " N=",data.N)
    for i in range(1, data.QNumerats+1):
        data.p[N-1]=i#vikt! so ob af recurs data.N wi alt, so nur ine N!
        st="countAll="+str(countAll)+" N="+str(N)+" i="+str(i)+": " 
        #if data.N==data.QVals:#NLim
        if N==data.QVals:#vikt! so ob af recurs data.N wi alt, so nur ine N!
            Sum=0
            for j in range(1, data.QVals+1):
                Sum=Sum+data.p[j-1]
                st=st+str(data.p[k-1])
                if(k<data.QVals):
                    st=st+" + "
                if Sum==DenRes:#get out rec
                    data.countGut=data.countGut+1
                    data.lst.append(data.p)
                st=st+" = "+str(data.Sum)+" "
        if Show1Hide0==1:
            print(st)
        data.N=1
    else:
        data.N=data.N+1
        data=RecSearch(countAll, countGut, data)
        if Show1Hide0==1:
            print("Return to prev. CountALl="+str(countAll)+" N="+str(N))
    if Show1Hide0==1:
        print("RecSearch Finishes working. countAll=",countAll, " N=",data.N)  
    return data

data=RecStr(QVals, QNumerats)
countAll=0
countGut=0
Lst=[]

countAll=0
countGut=0
st=""
QVals=4
Denomin=9
DenRes=24
for p1 in range (0, Denomin+1):
    for p2 in range (0, Denomin+1):
        for p3 in range (0, Denomin+1):
            for p4 in range (0, Denomin+1):
                s=0
                st=str(countAll)+") "
                for pN in range(1, QVals+1):
                    countAll=countAll+1
                    if pN==1:
                        s=s+p1
                        st=st+str(p1)
                    elif pN==2:
                        s=s+p2
                        st=st+str(p2)
                    elif pN==3:
                        s=s+p3
                        st=st+str(p3)
                    elif pN==4:
                        s=s+p4
                        st=st+str(p4)
                    if pN<QVals:
                        st=st+" + "
                    else:
                        st=st+" = "+str(s)+" "
                        if(s==DenRes):
                            countGut=countGut+1
                            LstElt=[]
                            LstElt.append(countGut)
                            LstElt.append(countAll)
                            for i in range(1, QVals+1):
                                if i==1:
                                    LstElt.append(p1)
                                elif i==2:
                                    LstElt.append(p2)
                                elif i==3:
                                    LstElt.append(p3)
                                elif i==4:
                                    LstElt.append(p4)
                            LstElt.append(DenRes)
                            Lst.append(LstElt)
            print(st)
print("\nResults for 24:")
for i in range (1, len(Lst)+1):
    print(Lst[i-1])
                    
                

#for i in range(1, data.Denomin+1):
#    data=RecSearch2(data)
#
print("StartRec")

print(data)
data=RecSearch(countAll, countGut, data)
print(data)
print("FinishRec")
