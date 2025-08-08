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
            print(i,"=>",self.p[i-1])

    #def SetN(self, N):
    #    self.N=N

    def __str__(self):
        st=" QVals="+str(self.QVals)+" QNumerats="+str(self.QVals)+"; Denomin="+str(self.Denomin)+" Sum="+str(self.Sum)+" N="+str(self.N)+" size(p)="+str(len(self.p))
        return st

DenRes=80

QVals=4
QNumerats=4
data=RecStr(QVals, QNumerats)
data.countAll=0
data.countGut=0
DenRes=data.Denomin

def RecursForNestedCycles(data):
    print("wait... ")
    for data.p[1-1] in range (0, data.Denomin+1):
    #for data.p[1-1] in range (1, 3+1):
        for data.p[2-1] in range (0, data.Denomin+1):
        #for data.p[2-1] in range (1, 3+1):
            for data.p[3-1] in range (0, data.Denomin+1):
            #for data.p[3-1] in range (1, 3+1):
                for data.p[4-1] in range (0, data.Denomin+1):
                #for data.p[4-1] in range (1, 3+1):
                    s=0
                    data.countAll=data.countAll+1
                    st=str(data.countAll)+") "
                    print(data.countAll," of ", data.Denomin*data.Denomin*data.Denomin*data.Denomin)
                    for pN in range(1, data.QVals+1):
                        s=s+data.p[pN-1]
                        st=st+str(data.p[pN-1])
                        if pN<QVals:
                            st=st+" + "
                        else:
                            st=st+" = "+str(s)+" "
                            if(s==DenRes):
                                data.countGut=data.countGut+1
                                LstElt=[]
                                LstElt.append(data.countGut)
                                LstElt.append(data.countAll)
                                for i in range(1, data.QVals+1):
                                    LstElt.append(data.p[i-1])
                                LstElt.append(DenRes)
                                data.lst.append(LstElt)
                                print("\ncountGut=",data.countGut,"\n")
                    print(st)
    print("\nResults for ",DenRes,": ")
    for i in range (1, len(data.lst)+1):
        print(data.lst[i-1])
    return data

data=RecursForNestedCycles(data)
print("\n\nAfter fn\n")
print("\nResults for ",DenRes,": ")
for i in range (1, len(data.lst)+1):
    print(data.lst[i-1])
    
