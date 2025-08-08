class RecStr:
    def __init__(self, QVals=0, QNumerats=0):
        self.QVals=0
        self.QNumerats=0
        self.Denomin=0
        #self.MaxNumerat=0
        self.Sum=0
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

QVals=4
QNumerats=100
Denomin=9
DenRes=24
data=RecStr(QVals, QNumerats)
countAll=0
countGut=0
Lst=[]
p=[]
for i in range (1, QVals+1):
    p.append(0)
Denomin=9
DenRes=24
countAll=0
countGut=0
st=""

for p[1-1] in range (0, Denomin+1):
    for p[2-1] in range (0, Denomin+1):
        for p[3-1] in range (0, Denomin+1):
            for p[4-1] in range (0, Denomin+1):
                s=0
                st=str(countAll)+") "
                for pN in range(1, QVals+1):
                    countAll=countAll+1
                    s=s+p[pN-1]
                    st=st+str(p[pN-1])
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
                                LstElt.append(p[i-1])
                            LstElt.append(DenRes)
                            Lst.append(LstElt)
            print(st)
print("\nResults for ",DenRes,": ")
for i in range (1, len(Lst)+1):
    print(Lst[i-1])
                    
                

#for i in range(1, data.Denomin+1):
#    data=RecSearch2(data)
#
print("StartRec")
print(data)
#data=RecSearch1(countAll, countGut, data)
print(data)
print("FinishRec")
