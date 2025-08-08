import copy
import math

def ArrayOfSameVals(val, Q):
    R=[]
    if(Q>=1 and Q<=1000000000):
        for i in range(1, Q+1):
            R.append(val)
    return R

#def ArrayOfValsLabelledAs1(data, labels):
#    R=[]
#    Q=len(data)
#    if(Q>0 and len(labels)>=Q):
#       for i in range(1, Q+1):
#           if labels[i-1]!=0:
#               R.append(data[i-1])
#    return R

def ArrayOfNsLabelledAs1(labels):
    R=[]
    Q=len(labels)
    if(Q>0 and len(labels)>=Q):
       for i in range(1, Q+1):
           if labels[i-1]!=0:
               R.append(i)
    return R

def ArrayOfValsLabelledAs1(data, labels):
    R=[]
    Q=len(data)
    Ns=ArrayOfNsLabelledAs1(labels)
    NotQ=len(Ns)
    for i in range(1, NotQ+1):
        R.append(data[Ns[i-1]-1])
    return R

def NewDataToLabelledArray(IniData, NewData, labels, vsh=0):
    R=[]
    QAll=len(IniData)
    QNew=len(NewData)
    QLbls=len(labels)
    count0=0
    count1=0
    LastN=0
    if vsh==1:
        print("NewDataToLabelledArray starts working")
    for i in range(1, QLbls+1):
       if labels[i-1]==1:
           count1+=1
       if labels[i-1]==0:
           count0+=1
    QNewReal=count1
    if vsh==1:
        print(" QAll="+str(QAll)+" QNew="+str(QNew)+" QLbls="+str(QLbls)+" count0="+str(count0)+" count1="+str(count1))
    if QAll>0 and count0+count1==QLbls and QLbls==QAll and QNew>=count1:
        iniN=1
        for newN in range(1, QNewReal+1):
            if vsh==1:
                print("NewVal["+str(newN)+"]="+str(NewData[newN-1]))
            while labels[iniN-1]==0:
                iniN+=1
                print("IniVal["+str(iniN)+"]="+str(IniData[iniN-1])+" doesn't correspond")
            print("IniVal["+str(iniN)+"]="+str(IniData[iniN-1])+" - was")
            IniData[iniN-1]=NewData[newN-1]
            print("IniVal["+str(iniN)+"]="+str(IniData[iniN-1])+" - became")
            iniN+=1
    if vsh==1:
        print("NewDataToLabelledArray finishes working")
    return IniData

def PowNat(x, y):
    z=1
    for i in range(1, y+1):
        z*=x
    return z

def Array1DReverse(arr):
    R=[]
    L=len(arr)
    for i in range(1, L+1):
        N=L+1-i
        R.append(arr[N-1])
    return R

def IntNumToDigitsAscendingOrder(x, baseDec=10, vsh=1):
    digits=[]
    if x<0:
        y=-x
    else:
        y=x
    order=0
    if vsh==1:
        print("IntNumToDigits starts working")
        print("Number given: "+str(x))
        print("Defining order")
    while y>=baseDec and not ( (PowNat(baseDec,order) <= y) and ( PowNat(baseDec,order+1) > y) ):
        if vsh==1:
            if not ((PowNat(baseDec,order) <= y) and ( PowNat(baseDec,order+1) > y)):
                print(str(baseDec)+"^"+str(order)+"="+str(PowNat(baseDec,order))+" < "+str(y)+" and  "+str(baseDec)+"^"+str(order+1)+"="+str(PowNat(baseDec,order+1))+" < "+str(y))
            else:
                print(str(baseDec)+"^"+str(order)+"="+str(PowNat(baseDec,order))+" <= "+str(y)+" and "+str(baseDec)+"^"+str(order+1)+"="+str(PowNat(baseDec,order+1))+" > "+str(y))
        order+=1
    if vsh==1:
        print(str(x)+" is number of order: "+str(order))
    for i in range(1, order+1+1):
        digits.append(0)
    z=y
    for i in range(1, order+1):
        N=order+1-i
        IntPart=z/baseDec
        rest=z-IntPart*baseDec
        digit=rest
        z=(z-rest)/baseDec
        digits[i-1]=digit
        if vsh==1:
            print(str(i)+") N= "+str(N)+" div.IntPart= "+str(IntPart)+" div.rest= "+str(rest)+" digit= "+str(digit)+" z= "+str(z))
    digits[order+1-1]=z
    if vsh==1:
        print("So digits (ascending order): "+str(digits))
        print("IntNumToDigits finishes working")
    return digits

def IntNumToDigitsUsualOrder(x, baseDec=10, vsh=1):
    digitsAscending=IntNumToDigitsAscendingOrder(x, baseDec, vsh=1)
    digits=Array1DReverse(digitsAscending)
    return digits

def IntNumOfDigitsAscendingOrder(digits, baseDec=10):
    y=0
    order=len(digits)-1
    for i in range(1, order+1+1):
        y=y+digits[i-1]*PowNat(baseDec, i)
    return y

x=1023
BaseDec=10
print(str(x)+" 's digits (usual order): "+str(IntNumToDigitsUsualOrder(x, BaseDec, 0)))
x=1020
BaseDec=10
print(str(x)+" 's digits (usual order): "+str(IntNumToDigitsUsualOrder(x, BaseDec, 0)))
x=100
BaseDec=10
print(str(x)+" 's digits (usual order): "+str(IntNumToDigitsUsualOrder(x, BaseDec, 0)))
x=4
BaseDec=10
print(str(x)+" 's digits (usual order): "+str(IntNumToDigitsUsualOrder(x, BaseDec, 0)))
x=0
BaseDec=10
print(str(x)+" 's digits (usual order): "+str(IntNumToDigitsUsualOrder(x, BaseDec, 0)))
x=4
BaseDec=2
print(str(x)+" 's digits (usual order): "+str(IntNumToDigitsUsualOrder(x, BaseDec, 0)))
x=5
BaseDec=2
print(str(x)+" 's digits (usual order): "+str(IntNumToDigitsUsualOrder(x, BaseDec, 0)))

vsh=1
print("\nArrayOfSame ("+str(4)+")Vals="+str(3)+": "+str(ArrayOfSameVals(3, 4)))
bIni=[1, 2, 3, 4, 5, 6, 7, 8, 9]
lbls=[1, 0, 0, 0, 1, 1, 0, 1, 1]
bLbld=ArrayOfValsLabelledAs1(bIni, lbls)
Q=len(bLbld)
print("Ini array: ",bIni)
print("labels: ",lbls)
for i in range(1, Q+1):
    bLbld[i-1]*=10
print("New vals: ",bLbld)
bNew=NewDataToLabelledArray(bIni, bLbld, lbls, vsh)
print("result of exchange labelled vals: ", bNew)

class ValInfo:
    def __init__(self, LayerN=0, NeuronN=1, CoLayerN=1, CoNeuronN=1, Weight1Bias0=1):
        self.LayerN=LayerN
        self.NeuronN=NeuronN
        self.CoLayerN=CoLayerN
        self.CoNeuronN=CoNeuronN
        self.Weight1Bias0

class Acson:
    def __init__(LayerN=-1, NeuronConnectedN=1, weight=0, ChangeForbidden0Allowed1=1):
        self.LayerN=LayerN
        self.NeuronConnectedN=NeuronConnectedN
        self.weight=weight
        self.ChangeForbidden0Allowed1=ChangeForbidden0Allowed1

class Acson1:
    def __init__(LayerFromN=-1, NeuronFromN=1, LayerToN=-1, NeuronToN=1,weight=0, ChangeForbidden0Allowed1=1):
        self.LayerN=LayerN
        self.NeuronConnectedN=NeuronConnectedN
        self.weight=weight
        self.ChangeForbidden0Allowed1=ChangeForbidden0Allowed1
  
class ANNInfo:
    def __init__(self, QXs, QYs, QHs):
        self.QHs=[]
        self.QXs=QXs
        self.QYs=QYs
        if isinstance(QHs, list):
            self.QLayers=len(QHs)
            self.QHs=copy.deepcopy(QHs)
        else:
            self.QLayers=1
            self.QHs.append(QHs)

    def GetQNeuronsOfCurrentLayerN(self, N=-1):
        Q=0
        if N==0:
            Q=self.QXs
        elif N==-1 or N==self.QLayers+1:
            Q=self.QYs
        elif N>=1 and N<=self.QLayers:
            Q=self.QHs[N-1]
        return Q

    def GetQNeuronsOfPreviousLayerOfLayerN(self, N=-1):
        Q=0
        if N==-1:
            N=self.QLayers+1
        if N==1:
            Q=self.QXs
        elif N>1 or N<=self.QLayers:
            Q=self.QHs[N-1-1]
        return Q

    def GetQNeuronsOfNextLayerOfLayerN(self, N=0):
        Q=0
        if  N<=self.QLayers:
            Q=self.QYs
        elif  N>=0 and N<self.QLayers:
            Q=self.QHs[N+1-1]
        return Q

    def GetQValsOfNeuron(self, LayerN, NeuronN, Forward0Back1=0):
        Q=0
        if LayerN==-1:
            LayerN=self.QLayers+1
        if Forward0Back1==0:
            if LayerN==0:
                Q=self.QHs[1-1]#Q=self.QXs*self.QHs[1-1]
            if LayerN==self.QLayers:
                Q=self.QYs#Q=self.QHs[LayerN-1]*self.QYs
            elif LayerN>=1 and LayerN<self.QLayers:
                Q=self.QHs[LayerN-1]*self.QHs[LayerN-1]
        elif Forward0Back1==1:
            if LayerN==1:
                Q=self.QXs
            #elif LayerN=
        return count
        

         
class MyNeuron:
    def __init__(self, LayerN_0in_m1out, inf):
        ParamIniRandval=0
        #
        self.acson_in=[]
        self.acson_out=[]
        self.B=0
        #self.W_in_Fixed0AllowedToChange1=[]
        #self.W_out_Fixed0AllowedToChange1=[]
        self.B_ChangeForbidden0Allowed1=1
        #
        self.OwnVal=ParamIniRandval
        #
        if LayerN_0in_m1out>=1 and LayerN_0in_m1out<=inf.QLayers:
            self.B=ParamIniRandval
            self.B_ChangeForbidden0Allowed1=1
            if LayerN_0in_m1out==1:
                for i in range(1, inf.QXs+1):
                    #self.W_in.append(ParamIniRandval)
                    #self.W_in_Fixed0AllowedToChange1.append(1)
                    #Acson:def __init__(LayerN=-1, NeuronConnectedN=1, weight=0, ChangeForbidden0Allowed1=1)
                    lnk=Acson(LayerN_0in_m1out-1, i, ParamIniRandval, 1)
                    self.acson_in.append(lnk)
                for i in range(1, inf.QHs[1+1-1]+1):
                    #self.W_out.append(ParamIniRandval)
                    #self.W_out_Fixed0AllowedToChange1.append(1)
                    lnk=Acson(LayerN_0in_m1out+1, i, ParamIniRandval, 1)
                    self.acson_out.append(lnk)
            elif LayerN_0in_m1out==inf.QLayers:
                for i in range(1, inf.QYs+1):
                    #self.W_out.append(ParamIniRandval)
                    #self.W_out_Fixed0AllowedToChange1.append(1)
                    lnk=Acson(LayerN_0in_m1out-1, i, ParamIniRandval, 1)
                    self.acson_in.append(lnk)
                for i in range(1, inf.QHs[inf.QLayers-1]+1):
                    #self.W_in.append(ParamIniRandval)
                    #self.W_in_Fixed0AllowedToChange1.append(1)
                    lnk=Acson(LayerN_0in_m1out+1, i, ParamIniRandval, 1)
                    self.acson_out.append(lnk)
            else:
                for i in range(1, inf.QHs[LayerN_0in_m1out-1-1]+1):
                    #self.W_in.append(ParamIniRandval)
                    #self.W_in_Fixed0AllowedToChange1.append(1)
                    lnk=Acson(LayerN_0in_m1out-1, i, ParamIniRandval, 1)
                    self.acson_in.append(lnk)
                for i in range(1, inf.QHs[LayerN_0in_m1out+1-1]+1):
                    #self.W_out.append(ParamIniRandval)
                    #self.W_out_Fixed0AllowedToChange1.append(1)
                    lnk=Acson(LayerN_0in_m1out+1, i, ParamIniRandval, 1)
                    self.acson_out.append(lnk)
        elif LayerN_0in_m1out==0:
            self.B=0
            self.B_ChangeForbidden0Allowed1=0
            for i in range(1, inf.QHs[1-1]+1):
                #self.W_out.append(ParamIniRandval)
                #self.W_out_Fixed0AllowedToChange1.append(1)
                lnk=Acson(LayerN_0in_m1out+1, i, ParamIniRandval, 1)
                self.acson_out.append(lnk)
        elif LayerN_0in_m1out==-1 or LayerN_0in_m1out==inf.QLayers+1:
            for i in range(1, inf.QHs[inf.QLayers-1]+1):
                #self.W_in.append(ParamIniRandval)
                #self.W_in_Fixed0AllowedToChange1.append(1)
                lnk=Acson(LayerN_0in_m1out-1, i, ParamIniRandval, 1)
                self.acson_in.append(lnk)

    def getQIn(self, ChangeForbidden0Allowed1=1):
        QAll=len(self.W_In)
        if ChangeForbidden0Allowed1==1:
            Q=QAll
        else:
            Q=0
            for i in range(1, QAll+1):
                if self.self.W_in_ChangeForbidden0Allowed1[i-1]==1:
                    Q+=1
        return Q

    def getQOut(self, ChangeForbidden0Allowed1=1):
        QAll=len(self.acson_out)
        if ChangeForbidden0Allowed1==1:
            Q=QAll
        else:
            Q=0
            for i in range(1, QAll+1):
                if self.acson_out[i-1].ChangeForbidden0Allowed1==1:
                    Q+=1
        return Q

    def getVal(self):
        return self.val

    def getWInN(self, N):
        R=0
        if N>=1 and N<=len(self.W_in):
            R=self.acson_in[N-1].weight
        return R

    def getWInN_ChangeForbidden0Allowed1(self, N):
        R=0
        if N>=1 and N<=len(self.acson_in):
            R=self.acson_in[N-1].ChangeForbidden0Allowed1
        return R

    def getWOutN(self, N):
        R=0
        if N>=1 and N<=len(self.W_in):
            R=self.acson_out[N-1].weight
        return R

    def getWOutN_ChangeForbidden0Allowed1(self, N):
        R=0
        if N>=1 and N<=len(self.W_in):
             R=self.acson_out[N-1].ChangeForbidden0Allowed1
        return R

    def setVal(self, val):
        self.val=val

    def setWInN(self, N, val, ChangeForbidden0Allowed1_RemainAsWas_m1=-1):
        R=0
        if N>=1 and N<=len(self.W_in):
             self.acson_in[N-1].weight=val
             if Fixed0AllowedToChange1RemainWhatWas_m1!=-1:
                 self.acson_in[N-1].ChangeForbidden0Allowed1=ChangeForbidden0Allowed1_RemainAsWas_m1
        
    def getWOutN(self, N, val, ChangeForbidden0Allowed1_RemainAsWas_m1=-1):
        R=0
        if N>=1 and N<=len(self.W_in):
            self.acson_out[N-1]=val
            if ChangeForbidden0Allowed1_RemainAsWas_m1!=-1:
                self.acson_out[N-1].ChangeForbidden0Allowed1=ChangeForbidden0Allowed1_RemainAsWas_m1   
    
        
    def GetAllWeightsIncomingAsSingleList(self, ChangeForbidden0Allowed1=1):
        R=[]
        Q=self.getQIn()
        if ChangeForbidden0Allowed1==1:
            for i in range(1,Q+1):
                R.append(self.W_In[i-1])
        else:
            R=ArrayOfValsLabelledAs1(self.W_In, self.W_in_ChangeForbidden0Allowed1)
        return R

    def GetAllWeightsOutcomingAsSingleList(self, ChangeForbidden0Allowed1=1):
        R=[]
        Q=self.getQOut()
        if ChangeForbidden0Allowed1==1:
            for i in range(1,Q+1):
                R.append(self.W_Out[i-1])
        else:
            R=ArrayOfValsLabelledAs1(self.W_Out, self.W_out_ChangeForbidden0Allowed1)
        return R

    def GetAllWeightsIncoming_ChangeForbidden0Allowed1_RemainAsWas_m1_AsSingleList(self):
        R=[]
        Q=self.getQIn()
        for i in range(1,Q+1):
            R.append(self.W_in_ChangeForbidden0Allowed1[i-1])
        return R

    def GetAllWeightsOutcoming_ChangeForbidden0Allowed1_RemainAsWas_m1_AsSingleList(self):
        R=[]
        Q=self.getQOut()
        for i in range(1,Q+1):
            R.append(W_out_Fixed0AllowedToChange1[i-1])
        return R

    def SetAllWeightsIncomingFromSingleList(self, Ws, Ws_ChangeForbidden0Allowed1_RemainAsWas_m1=[]):
        Q=self.getQIn()
        if Ws_ChangeForbidden0Allowed1_RemainAsWas_m1==[]:
            self.W_In=NewDataToLabelledArray(self.W_In, Ws, self.W_in_ChangeForbidden0Allowed1)
        else:
            for i in range(1,Q+1):
                self.W_In[i-1]=Ws[i-1]
                self.W_in_ChangeForbidden0Allowed1[i-1]=Ws_ChangeForbidden0Allowed1_RemainAsWas_m1[i-1]

    def SetAllWeightsOutcomingFromSingleList(self, Ws, Ws_Allowed=[]):
        Q=self.getQOut()
        if Ws_ChangeForbidden0Allowed1_RemainAsWas_m1==[]:
            self.W_Out=NewDataToLabelledArray(self.W_Out, Ws, self.W_out_ChangeForbidden0Allowed1)
        else:
            for i in range(1,Q+1):
                self.W_Out[i-1]=Ws[i-1]
                self.W_out_ChangeForbidden0Allowed1[i-1]=Ws_ChangeForbidden0Allowed1_RemainAsWas_m1[i-1]

    def GetBias(self):
        return self.B

    def GetBias_ChangeForbidden0Allowed1_RemainAsWas_m1(self):
        return self.B_ChangeForbidden0Allowed1

    def SetBias(self, val, ChangeForbidden0Allowed1_RemainAsWas_m1=-1):
        self.B=val
        if ChangeForbidden0Allowed1_RemainAsWas_m1!=-1:
            self.B_ChangeForbidden0Allowed1=ChangeForbidden0Allowed1_RemainAsWas_m1

    def Get_WeigthsIn_andBias_AsSingleList(self, ChangeForbidden0Allowed1=1):
        R=self.GetAllWeightsIncomingAsSingleList(ChangeForbidden0Allowed1)
        if not (ChangeForbidden0Allowed1==1 and self.B_ChangeForbidden0Allowed1==0):
            R.append(self.B)
        return R

    def Get_BiasAndWeigthsOut_AsSingleList(self, All0AllowedToChangeOnly1=0):
        R=self.GetAllWeightsOutcomingAsSingleList(All0AllowedToChangeOnly1)
        if not (All0AllowedToChangeOnly1==1 and self.B_Fixed0AllowedToChange1==0):
            R.append(self.B)
        return R


                                 
class MyANN:
    def __init__(self, NNInf=0):
        curRow=[]
        #
        if isinstance(NInf, ANNInfo):
            self.inf=copy.deepcopy(NNInf)
        else:
            self.inf=ANNInfo()
        #
        InputLayerNeurons=[]
        OutputLayerNeurons=[]
        HiddenLayerNeurons=[]
        acsons=[]
        #
        for i in range(1, self.inf.QXs+1):
            curNeuron=MyNeuron(0, i, self.inf)
            self.InputLayerNeurons.append(ParamIniRandval)
        for i in range(1, self.inf.QYs+1):
            curNeuron=MyNeuron(0, i, self.inf)
            self.OutputLayerNeurons.append(ParamIniRandval)
        for i in range(1, self.inf.QLayers+1):
            curRow=[]
            QHs=self.inf.GetQNeuronsOfCurrentLayerN(i)
            for j in range(1, QHs+1):
                curNeuron=MyNeuron(0, j, self.inf)
                curRow.append(curNeuron)
            self.HiddenLayerNeurons.append(curRow)
        #
        for LayerN in range(0, self.inf.QLayers+1):
            for NeuronFromN in range(1, self.inf.QXs+1):
                for NeuronToN in range(1, self.inf.QHs[1-1]+1):
                    ParamIniRandval=0
                    acson=Acson1(LayerN, NeuronFromN, LayerN+1, NeuronToN, ParamIniRandval, 1)
                    acsons.append(acson)
        #
    #

    def getConnectionN(self, LayerFromN, NeuronFromN, LayerToN, NeuronToN):
        Q=len(acsons)
        N=0
        for i in range(1, Q+1):
            if acsons[i-1].LayerFromN==LayerFromN and acsons[i-1].NeuronFromN==NeuronFromN  and acsons[i-1].LayerToN==LayerToN and acsons[i-1].NeuronToN==NeuronToN:
                N=i
        return N

    def getConnectionWeight(self, LayerFromN, NeuronFromN, LayerToN, NeuronToN):
        W=0
        N=getConnectionN(LayerFromN, NeuronFromN, LayerToN, NeuronToN)
        if(N>0):
            W=acsons[i-1].weight
        return W

    def getIfConnectionToChangeForbidden0Allowed1(self, LayerFromN, NeuronFromN, LayerToN, NeuronToN):
        R=0
        N=getConnectionN(LayerFromN, NeuronFromN, LayerToN, NeuronToN)
        if(N>0):
            R=acsons[i-1].Fixed0AllowedToChange1
        return W

    def getSingleNeuronAllIncomingConnections(self, LayerN, NeuronN, ChangingForbidden0Allowed1_noMatter_m1=-1):
        Q=len(acsons)
        Ws=[]
        for i in range(1, Q+1):
            if acsons[i-1].LayerToN=LayerN and acsons[i-1].NeuronToN=NeuronN and (acsons[i-1]) 

    def ResetAllVals(self):
        pass
    
    def getNeuronQIn(self, LayerN, NeuronN, All0AllowedToChangeOnly1=0):
        Q=0
        if LayerN==-1:
            LayerN=self.inf.QLayers+1
        if LayerN==0:
            #if NeuronN>=1 and NeuronN<=self.inf.QXs:
            #    Q=self.InputLayerNeurons[NeuronN-1].getQIn(All0AllowedToChangeOnly1)
            pass
        elif LayerN==1:
            if NeuronN>=1 and NeuronN<=self.inf.QHs[LayerN-1]:
                Q=self.HiddenLayerNeurons[LayerN-1][NeuronN-1].getQIn(All0AllowedToChangeOnly1)
        elif LayerN==self.inf.QLayers:
            if NeuronN>=1 and NeuronN<=self.inf.QHs[LayerN-1]:
                Q=self.HiddenLayerNeurons[LayerN-1][NeuronN-1].getQIn(All0AllowedToChangeOnly1)
        elif LayerN==self.inf.QLayers+1:
            if NeuronN>=1 and NeuronN<=self.inf.QYs:
                Q=self.OutputLayerNeurons[NeuronN-1].getQIn(All0AllowedToChangeOnly1)
        elif LasyerN>1 and LayerN<self.inf.QLayers:
            if NeuronN>=1 and NeuronN<=self.inf.QHs[LayerN-1]:
                Q=self.HiddenLayerNeurons[LayerN-1][NeuronN-1].getQIn(All0AllowedToChangeOnly1)
        return R


    def getNeuronQOut(self, LayerN, NeuronN, All0AllowedToChangeOnly1=0):
        Q=0
        if LayerN==-1:
            LayerN=self.inf.QLayers+1
        if LayerN==0:
            if NeuronN>=1 and NeuronN<=self.inf.QXs:
                Q=self.InputLayerNeurons[NeuronN-1].getQOut(All0AllowedToChangeOnly1)
        elif LayerN==1:
            if NeuronN>=1 and NeuronN<=self.inf.QHs[LayerN-1]:
                Q=self.HiddenLayerNeurons[LayerN-1][NeuronN-1].getQOut(All0AllowedToChangeOnly1)
        elif LayerN==self.inf.QLayers:
            if NeuronN>=1 and NeuronN<=self.inf.QHs[LayerN-1]:
                Q=self.HiddenLayerNeurons[LayerN-1][NeuronN-1].getQOut(All0AllowedToChangeOnly1)
        elif LayerN==self.inf.QLayers+1:
            #if NeuronN>=1 and NeuronN<=self.inf.QHs[1-1]:
            #    Q=self.OutputLayerNeurons[NeuronN-1].getQOutn(All0AllowedToChangeOnly1)
            pass
        elif LasyerN>1 and LayerN<self.inf.QLayers:
            if NeuronN>=1 and NeuronN<=self.inf.QHs[LayerN-1]:
                Q=self.HiddenLayerNeurons[LayerN-1][NeuronN-1].getQOut(All0AllowedToChangeOnly1)
        return R

    def getLayerQIn(self, LayerN, All0AllowedToChangeOnly1=0):
        Q=0
        if LayerN==-1:
            LayerN=self.inf.QLayers+1
        if LayerN==0:
            #for NeuronN in range(1, self.inf.QXs+1):
            #    Q=Q+self.InputLayerNeurons[NeuronN-1].getQIn(All0AllowedToChangeOnly1)
            pass
        elif LayerN==1:
            for NeuronN in range(1, self.inf.QHs[LayerN-1]):
                Q=self.HiddenLayerNeurons[LayerN-1][NeuronN-1].getQIn(All0AllowedToChangeOnly1)
        elif LayerN==self.inf.QLayers:
            for NeuronN in range(1, self.inf.QHs[LayerN-1]):
                Q=self.HiddenLayerNeurons[LayerN-1][NeuronN-1].getQIn(All0AllowedToChangeOnly1)
        elif LayerN==self.inf.QLayers+1:
            for NeuronN in range(1, self.inf.QYs):
                Q=self.OutputLayerNeurons[NeuronN-1].getQIn(All0AllowedToChangeOnly1)
        elif LasyerN>1 and LayerN<self.inf.QLayers:
            for NeuronN in range(1, self.inf.QHs[LayerN-1]):
                Q=self.HiddenLayerNeurons[LayerN-1][NeuronN-1].getQIn(All0AllowedToChangeOnly1)
        return R

    def getLayerQOut(self, LayerN, All0AllowedToChangeOnly1=0):
        Q=0
        if LayerN==-1:
            LayerN=self.inf.QLayers+1
        if LayerN==0:
            for NeuronN in range(1, self.inf.QXs+1):
                Q=Q+self.InputLayerNeurons[NeuronN-1].getQOut(All0AllowedToChangeOnly1)
        elif LayerN==1:
            for NeuronN in range(1, self.inf.QHs[LayerN-1]):
                Q=self.HiddenLayerNeurons[LayerN-1][NeuronN-1].getQOut(All0AllowedToChangeOnly1)
        elif LayerN==self.inf.QLayers:
            for NeuronN in range(1, self.inf.QHs[LayerN-1]):
                Q=self.HiddenLayerNeurons[LayerN-1][NeuronN-1].getQOut(All0AllowedToChangeOnly1)
        elif LayerN==self.inf.QLayers+1:
            #for NeuronN in range(1, self.inf.QYs):
            #    Q=self.OutputLayerNeurons[NeuronN-1].getQOut(All0AllowedToChangeOnly1)
            pass
        elif LasyerN>1 and LayerN<self.inf.QLayers:
            for NeuronN in range(1, self.inf.QHs[LayerN-1]):
                Q=self.HiddenLayerNeurons[LayerN-1][NeuronN-1].getQOut(All0AllowedToChangeOnly1)
        return R

    def getLayerQWeightsInAndBiases(self, LayerN, All0AllowedToChangeOnly1=0):
        pass

    def getLayerQWeightsOutAndBiases(self, LayerN, All0AllowedToChangeOnly1=0):
        pass

    def getVal(self, LayerN, NeuronN):
        R=0
        if LayerN==-1:
            LayerN=self.inf.QLayers+1
        if LayerN==0:
            if NeuronN>=1 and NeuronN<=self.inf.QXs:
                R=self.InputLayerNeurons[NeuronN-1].getVal()
        elif LayerN==1:
            if NeuronN>=1 and NeuronN<=self.inf.QHs[LayerN-1]:
                R=self.HiddenLayerNeurons[LayerN-1][NeuronN-1].getVal()
        elif LayerN==self.inf.QLayers:
            if NeuronN>=1 and NeuronN<=self.inf.QHs[LayerN-1]:
                R=self.HiddenLayerNeurons[LayerN-1][NeuronN-1].getVal()
        elif LayerN==self.inf.QLayers+1:
            if NeuronN>=1 and NeuronN<=self.inf.QHs[1-1]:
                R=self.OutputLayerNeurons[NeuronN-1].getVal()
        elif LayerN>1 and LayerN<self.inf.QLayers:
            if NeuronN>=1 and NeuronN<=self.inf.QHs[LayerN-1]:
                R=self.HiddenLayerNeurons[LayerN-1][NeuronN-1].getVal()
        return R

    def getWInN(self, LayerN, NeuronToN, NeuronFromN):
        R=0
        if LayerN==-1:
            LayerN=self.inf.QLayers+1
        if LayerN==0:
            pass
            #if NeuronToN>=1 and NeuronToN<=self.inf.QXs and NeuronFromN>=1 and NeuronToN<=0:
            #    R=self.InputLayerNeurons[NeuronToN-1].getVal()
        elif LayerN==1:
            if NeuronToN>=1 and NeuronToN<=self.inf.QHs[LayerN-1] and NeuronFromN>=1 and NeuronFromN<=self.inf.QXs:
                R=self.HiddenLayerNeurons[LayerN-1][NeuronToN-1].getWInN(NeuronFromN)
        elif LayerN==self.inf.QLayers:
            if NeuronToN>=1 and NeuronToN<=self.inf.QHs[LayerN-1] and NeuronFromN>=1 and NeuronFromN<=self.inf.QHs[LayerN-1-1]:
                R=self.HiddenLayerNeurons[LayerN-1][NeuronToN-1].getWInN(NeuronFromN)
        elif LayerN==self.inf.QLayers+1:
            if NeuronToN>=1 and NeuronToN<=self.inf.QHs[1-1] and NeuronFromN>=1 and NeuronFromN<=self.inf.QHs[LayerN-1-1]:
                R=self.OutputLayerNeurons[NeuronToN-1].getWInN(NeuronFromN)
        elif LayerN>1 and LayerN<self.inf.QLayers:
            if NeuronToN>=1 and NeuronToN<=self.inf.QHs[LayerN-1] and NeuronFromN>=1 and NeuronFromN<=self.inf.QHs[LayerN-1-1]:
                R=self.HiddenLayerNeurons[LayerN-1][NeuronToN-1].getWInN(NeuronFromN)
        return R

    def getWOutN(self, LayerN, NeuronFrom, NeuronToNN):
        R=0
        if LayerN==-1:
            LayerN=self.inf.QLayers+1
        if LayerN==0:
            if NeuronToN>=1 and NeuronToN<=self.inf.QXs and NeuronFromN>=1 and NeuronToN<=self.inf.QHs[LayerN+1-1]:
                R=self.InputLayerNeurons[NeuronToN-1].getWOutN(NeuronToN)
        elif LayerN==1:
            if NeuronFromN>=1 and NeuronFromN<=self.inf.QHs[LayerN-1] and NeuronToN>=1 and NeuronToN<=self.inf.QHs[LayerN+1-1]:
                R=self.HiddenLayerNeurons[LayerN-1][NeuronToN-1].getWOutN(NeuronToN)
        elif LayerN==self.inf.QLayers:
            if NeuronFromN>=1 and NeuronFromN<=self.inf.QHs[LayerN-1] and NeuronToN>=1 and NeuronToN<=self.inf.QYs:
                R=self.HiddenLayerNeurons[LayerN-1][NeuronToN-1].getWOutN(NeuronToN)
        elif LayerN==self.inf.QLayers+1:
            pass
            #if NeuronFromN>=1 and NeuronFromN<=self.inf.QHs[1-1] and NeuronToN>=1 and NeuronToN<=self.inf.QHs[LayerN-1-1]:
            #    R=self.OutputLayerNeurons[NeuronToN-1].getWOutN(NeuronToN)
        elif LayerN>1 and LayerN<self.inf.QLayers:
            if NeuronFromN>=1 and NeuronFromN<=self.inf.QHs[LayerN-1] and NeuronToN>=1 and NeuronToN<=self.inf.QHs[LayerN+1-1]:
                R=self.HiddenLayerNeurons[LayerN-1][NeuronToN-1].getWOutN(NeuronToN)
        return R

    def getWInN_Fixed0AllowedToChange1(self, N):
        R=0
        if LayerN==-1:
            LayerN=self.inf.QLayers+1
        if LayerN==0:
            pass
            #if NeuronToN>=1 and NeuronToN<=self.inf.QXs and NeuronFromN>=1 and NeuronToN<=0:
            #    R=self.InputLayerNeurons[NeuronToN-1].getWInN_Fixed0AllowedToChange1()
        elif LayerN==1:
            if NeuronToN>=1 and NeuronToN<=self.inf.QHs[LayerN-1] and NeuronFromN>=1 and NeuronFromN<=self.inf.QXs:
                R=self.HiddenLayerNeurons[LayerN-1][NeuronToN-1].getWInN_Fixed0AllowedToChange1(NeuronFromN)
        elif LayerN==self.inf.QLayers:
            if NeuronToN>=1 and NeuronToN<=self.inf.QHs[LayerN-1] and NeuronFromN>=1 and NeuronFromN<=self.inf.QHs[LayerN-1-1]:
                R=self.HiddenLayerNeurons[LayerN-1][NeuronToN-1].getWInN_Fixed0AllowedToChange1(NeuronFromN)
        elif LayerN==self.inf.QLayers+1:
            if NeuronToN>=1 and NeuronToN<=self.inf.QHs[1-1] and NeuronFromN>=1 and NeuronFromN<=self.inf.QHs[LayerN-1-1]:
                R=self.OutputLayerNeurons[NeuronToN-1].getWInN(NeuronFromN)
        elif LayerN>1 and LayerN<self.inf.QLayers:
            if NeuronToN>=1 and NeuronToN<=self.inf.QHs[LayerN-1] and NeuronFromN>=1 and NeuronFromN<=self.inf.QHs[LayerN-1-1]:
                R=self.HiddenLayerNeurons[LayerN-1][NeuronToN-1].getWInN_Fixed0AllowedToChange1(NeuronFromN)
        return R

    def getWOutN_Fixed0AllowedToChange1(self, N):
        R=0
        if LayerN==-1:
            LayerN=self.inf.QLayers+1
        if LayerN==0:
            if NeuronToN>=1 and NeuronToN<=self.inf.QXs and NeuronFromN>=1 and NeuronToN<=self.inf.QHs[LayerN+1-1]:
                R=self.InputLayerNeurons[NeuronToN-1].getWOutN_Fixed0AllowedToChange1(NeuronToN)
        elif LayerN==1:
            if NeuronFromN>=1 and NeuronFromN<=self.inf.QHs[LayerN-1] and NeuronToN>=1 and NeuronToN<=self.inf.QHs[LayerN+1-1]:
                R=self.HiddenLayerNeurons[LayerN-1][NeuronToN-1].getWOutN_Fixed0AllowedToChange1(NeuronToN)
        elif LayerN==self.inf.QLayers:
            if NeuronFromN>=1 and NeuronFromN<=self.inf.QHs[LayerN-1] and NeuronToN>=1 and NeuronToN<=self.inf.QYs:
                R=self.HiddenLayerNeurons[LayerN-1][NeuronToN-1].getWOutN_Fixed0AllowedToChange1(NeuronToN)
        elif LayerN==self.inf.QLayers+1:
            pass
            #if NeuronFromN>=1 and NeuronFromN<=self.inf.QHs[1-1] and NeuronToN>=1 and NeuronToN<=self.inf.QHs[LayerN-1-1]:
            #    R=self.OutputLayerNeurons[NeuronToN-1].getWOutN_Fixed0AllowedToChange1(NeuronToN)
        elif LayerN>1 and LayerN<self.inf.QLayers:
            if NeuronFromN>=1 and NeuronFromN<=self.inf.QHs[LayerN-1] and NeuronToN>=1 and NeuronToN<=self.inf.QHs[LayerN+1-1]:
                R=self.HiddenLayerNeurons[LayerN-1][NeuronToN-1].getWOutN_Fixed0AllowedToChange1(NeuronToN)
        return R

    def setVal(self, val, LayerN, NeuronN):
        if LayerN==-1:
            LayerN=self.inf.QLayers+1
        if LayerN==0:
            if NeuronN>=1 and NeuronN<=self.inf.QXs:
                self.InputLayerNeurons[NeuronN-1].setVal(val)
        elif LayerN==1:
            if NeuronN>=1 and NeuronN<=self.inf.QHs[LayerN-1]:
                self.HiddenLayerNeurons[LayerN-1][NeuronN-1].setVal(val)
        elif LayerN==self.inf.QLayers:
            if NeuronN>=1 and NeuronN<=self.inf.QHs[LayerN-1]:
                self.HiddenLayerNeurons[LayerN-1][NeuronN-1].setVal(val)
        elif LayerN==self.inf.QLayers+1:
            if NeuronN>=1 and NeuronN<=self.inf.QHs[1-1]:
                self.OutputLayerNeurons[NeuronN-1].setVal(val)
        elif LayerN>1 and LayerN<self.inf.QLayers:
            if NeuronN>=1 and NeuronN<=self.inf.QHs[LayerN-1]:
                self.HiddenLayerNeurons[LayerN-1][NeuronN-1].setVal(val)
        return R

    def setWN_withNextLayer(self, val, LayerN, NeuronFromN, NeuronToN, Fixed0AllowedToChange1RemainWhatWas_m1=-1):
        if LayerN==-1:
            LayerN=self.inf.QLayers+1
        if LayerN==0:
            if NeuronFromN>=1 and NeuronFromN<=self.inf.QXs and NeuronToN>=1 and NeuronToN<=self.inf.QHs[LayerN+1-1]:
                if Fixed0AllowedToChange1RemainWhatWas_m1!=-1:
                    self.InputLayerNeurons[NeuronFromN-1].setWOutN(self, NeuronToN, val, self.InputLayerNeurons[NeuronFromN-1].getWOutN_Fixed0AllowedToChange1(self, NeuronFromN))
                    self.HiddenLayerNeurons[LayerN-1][NeuronToN-1].setWInN(self, NeuronFromN, val, self.HiddenLayerNeurons[LayerN-1][NeuronToN-1].getWInN_Fixed0AllowedToChange1(self, NeuronFromN))
                else:
                    self.InputLayerNeurons[NeuronFromN-1].setWOutN(self, NeuronToN, val, Fixed0AllowedToChange1RemainWhatWas_m1)
                    self.HiddenLayerNeurons[LayerN-1][NeuronToN-1].setWInN(self, NeuronFromN, val, Fixed0AllowedToChange1RemainWhatWas_m1N)
                #after this
        elif LayerN==1:
            if NeuronFromN>=1 and NeuronFromN<=self.inf.QHs[LayerN-1] and NeuronToN>=1 and NeuronToN<=inf.QHs[LayerN+1-1]:
                if Fixed0AllowedToChange1RemainWhatWas_m1!=-1:
                    self.HiddenLayerNeurons[LayerN-1][NeuronFromN-1].setWOutN(self, NeuronToN, val, self.HiddenLayerNeurons[LayerN-1][NeuronFromN-1].getWOutN_Fixed0AllowedToChange1(NeuronToN))
                    self.HiddenLayerNeurons[LayerN+1-1][NeuronToN-1].setWInN(self, NeuronFromN, val, self.HiddenLayerNeurons[LayerN+1-1][NeuronToN-1].getWInN_Fixed0AllowedToChange1(NeuronFromN))
                else:
                    self.HiddenLayerNeurons[LayerN-1][NeuronFromN-1].setWOutN(self, NeuronToN, val, Fixed0AllowedToChange1RemainWhatWas_m1)
                    self.HiddenLayerNeurons[LayerN+1-1][NeuronToN-1].setWInN(self, NeuronFromN, val, Fixed0AllowedToChange1RemainWhatWas_m1)
        elif LayerN==self.inf.QLayers:
            if NeuronFromN>=1 and NeuronFromN<=self.inf.QHs[LayerN-1] and NeuronToN>=1 and NeuronToN<=inf.QYs:
                if Fixed0AllowedToChange1RemainWhatWas_m1!=-1:
                    self.HiddenLayerNeurons[LayerN-1][NeuronFromN-1].setWOutN(self, NeuronToN, val, self.HiddenLayerNeurons[LayerN-1][NeuronFromN-1].getWOutN_Fixed0AllowedToChange1(NeuronToN))
                    self.OutputLayerNeurons[NeuronToN-1].setWInN(self, NeuronFromN, val, self.OutputLayerNeurons[NeuronToN-1].getWInN_Fixed0AllowedToChange1(NeuronFromN))
                else:
                    self.HiddenLayerNeurons[LayerN-1][NeuronFromN-1].setWOutN(self, NeuronToN, val, Fixed0AllowedToChange1RemainWhatWas_m1)
                    self.OutputLayerNeurons[NeuronToN-1].setWInN(self, NeuronFromN, val, Fixed0AllowedToChange1RemainWhatWas_m1)
        elif LayerN==self.inf.QLayers+1:
            pass
            #if NeuronFromN>=1 and NeuronFromN<=self.inf.QHs[LayerN-1] and NeuronToN>=1 and NeuronToN<=inf.QHs[LayerN+1-1]:
            #   if Fixed0AllowedToChange1RemainWhatWas_m1!=-1:
            #       self.HiddenLayerNeurons[LayerN-1][NeuronFromN-1].setWOutN(self, NeuronToN, val, self.HiddenLayerNeurons[LayerN-1][NeuronFromN-1].getWOutN_Fixed0AllowedToChange1(NeuronToN))
            #       self.HiddenLayerNeurons[LayerN+1-1][NeuronToN-1].setWInN(self, NeuronFromN, val, self.HiddenLayerNeurons[LayerN+1-1][NeuronToN-1].getWInN_Fixed0AllowedToChange1(NeuronFromN))
            #   else:
            #       self.HiddenLayerNeurons[LayerN-1][NeuronFromN-1].setWOutN(self, NeuronToN, val, Fixed0AllowedToChange1RemainWhatWas_m1)
            #       self.HiddenLayerNeurons[LayerN+1-1][NeuronToN-1].setWInN(self, NeuronFromN, val, Fixed0AllowedToChange1RemainWhatWas_m1)
        elif LayerN>1 and LayerN<self.inf.QLayers:
             if NeuronFromN>=1 and NeuronFromN<=self.inf.QHs[LayerN-1] and NeuronToN>=1 and NeuronToN<=inf.QHs[LayerN+1-1]:
                if Fixed0AllowedToChange1RemainWhatWas_m1!=-1:
                    self.HiddenLayerNeurons[LayerN-1][NeuronFromN-1].setWOutN(self, NeuronToN, val, self.HiddenLayerNeurons[LayerN-1][NeuronFromN-1].getWOutN_Fixed0AllowedToChange1(NeuronToN))
                    self.HiddenLayerNeurons[LayerN+1-1][NeuronToN-1].setWInN(self, NeuronFromN, val, self.HiddenLayerNeurons[LayerN+1-1][NeuronToN-1].getWInN_Fixed0AllowedToChange1(NeuronFromN))
                else:
                    self.HiddenLayerNeurons[LayerN-1][NeuronFromN-1].setWOutN(self, NeuronToN, val, Fixed0AllowedToChange1RemainWhatWas_m1)
                    self.HiddenLayerNeurons[LayerN+1-1][NeuronToN-1].setWInN(self, NeuronFromN, val, Fixed0AllowedToChange1RemainWhatWas_m1)
        return R

    def setWN_withPrevLayer(self, val, LayerN, NeuronFromN, NeuronToN, Fixed0AllowedToChange1RemainWhatWas_m1=-1):
        if LayerN==-1:
            LayerN=self.inf.QLayers+1
        if LayerN==0:
            pass
            #if NeuronToN>=1 and NeuronToN<=self.inf.QHs[LayerN-1] and NeuronFromN>=1 and NeuronFromN<=inf.QHs[LayerN+1-1]:
            #    if Fixed0AllowedToChange1RemainWhatWas_m1!=-1:
            #        self.InputLayerNeurons[NeuronFromN-1].setWOutN(self, NeuronToN, val, self.InputLayerNeurons[NeuronFromN-1].getWOutN_Fixed0AllowedToChange1(self, NeuronFromN))
            #        self.HiddenLayerNeurons[LayerN-1][NeuronToN-1].setWInN(self, NeuronFromN, val, self.HiddenLayerNeurons[LayerN-1][NeuronToN-1].getWInN_Fixed0AllowedToChange1(self, NeuronFromN))
            #    else:
            #        self.InputLayerNeurons[NeuronFromN-1].setWOutN(self, NeuronToN, val, Fixed0AllowedToChange1RemainWhatWas_m1)
            #        self.HiddenLayerNeurons[LayerN-1][NeuronToN-1].setWInN(self, NeuronFromN, val, Fixed0AllowedToChange1RemainWhatWas_m1N))
        elif LayerN==1:
            if NeuronToN>=1 and NeuronToN<=self.inf.QHs[LayerN-1] and NeuronFromN>=1 and NeuronFromN<=inf.QXs:
                if Fixed0AllowedToChange1RemainWhatWas_m1!=-1:
                    self.HiddenLayerNeurons[LayerN-1][NeuronToN-1].setWInN(self, NeuronFromN, val, self.HiddenLayerNeurons[LayerN-1][NeuronToN-1].getWInN_Fixed0AllowedToChange1(NeuronFromN))
                    self.InputLayerNeurons[NeuronToN-1].setWOutN(self, NeuronFromN, val, self.InputLayerNeurons[NeuronToN-1].getWOutN_Fixed0AllowedToChange1(NeuronFromN))
                else:
                    self.HiddenLayerNeurons[LayerN-1][NeuronToN-1].setWInN(self, NeuronFromN, val, Fixed0AllowedToChange1RemainWhatWas_m1)
                    self.InputLayerNeurons[NeuronToN-1].setWOutN(self, NeuronFromN, val, Fixed0AllowedToChange1RemainWhatWas_m1)
        elif LayerN==self.inf.QLayers:
            if NeuronToN>=1 and NeuronToN<=self.inf.QHs[LayerN-1] and NeuronFromN>=1 and NeuronFromN<=inf.QHs[LayerN-1-1]:
                if Fixed0AllowedToChange1RemainWhatWas_m1!=-1:
                    self.HiddenLayerNeurons[LayerN-1][NeuronToN-1].setWInN(self, NeuronFromN, val, self.HiddenLayerNeurons[LayerN-1][NeuronToN-1].getWInN_Fixed0AllowedToChange1(NeuronFromN))
                    self.HiddenLayerNeurons[LayerN-1-1][NeuronFromN-1].setWOutN(self, NeuronToN, val, self.InputLayerNeurons[NeuronFromN-1].getWOutN_Fixed0AllowedToChange1(NeuronToN))
                else:
                    self.HiddenLayerNeurons[LayerN-1][NeuronToN-1].setWInN(self, NeuronFromN, val, Fixed0AllowedToChange1RemainWhatWas_m1)
                    self.HiddenLayerNeurons[LayerN-1-1][NeuronFromN-1].setWOutN(self, NeuronToN, val, Fixed0AllowedToChange1RemainWhatWas_m1)
        elif LayerN==self.inf.QLayers+1:
           if NeuronToN>=1 and NeuronToN<=self.inf.QHs[LayerN-1] and NeuronFromN>=1 and NeuronFromN<=inf.QHs[LayerN-1-1]:
                if Fixed0AllowedToChange1RemainWhatWas_m1!=-1:
                    self.OutputLayerNeurons[NeuronToN-1].setWInN(self, NeuronFromN, val, self.OutputLayerNeurons[NeuronToN-1].getWInN_Fixed0AllowedToChange1(NeuronFromN))
                    self.HiddenLayerNeurons[LayerN-1-1][NeuronFromN-1].setWOutN(self, NeuronToN, val, self.HiddenLayerNeurons[LayerN-1-1][NeuronFromN-1].getWOutN_Fixed0AllowedToChange1(NeuronToN))
                else:
                    self.OutputLayerNeurons[NeuronToN-1].setWInN(self, NeuronFromN, val, Fixed0AllowedToChange1RemainWhatWas_m1)
                    self.HiddenLayerNeurons[LayerN-1-1][NeuronFromN-1].setWOutN(self, NeuronToN, val, Fixed0AllowedToChange1RemainWhatWas_m1)
        elif LayerN>1 and LayerN<self.inf.QLayers:
             if NeuronToN>=1 and NeuronToN<=self.inf.QHs[LayerN-1] and NeuronFromN>=1 and NeuronFromN<=inf.QHs[LayerN-1-1]:
                if Fixed0AllowedToChange1RemainWhatWas_m1!=-1:
                    self.HiddenLayerNeurons[LayerN-1][NeuronToN-1].setWInN(self, NeuronFromN, val, self.HiddenLayerNeurons[LayerN-1][NeuronToN-1].getWInN_Fixed0AllowedToChange1(NeuronFromN))
                    self.HiddenLayerNeurons[LayerN-1-1][NeuronFromN-1].setWOutN(self, NeuronToN, val, self.InputLayerNeurons[NeuronFromN-1].getWOutN_Fixed0AllowedToChange1(NeuronToN))
                else:
                    self.HiddenLayerNeurons[LayerN-1][NeuronToN-1].setWInN(self, NeuronFromN, val, Fixed0AllowedToChange1RemainWhatWas_m1)
                    self.HiddenLayerNeurons[LayerN-1-1][NeuronFromN-1].setWOutN(self, NeuronToN, val, Fixed0AllowedToChange1RemainWhatWas_m1)
        return R
        

    #def GetWeightsMatrixForwardWithNext(self, LayerN):
    #    pass
    #
    #def GetWeightsMatrixForwardWithPrev(self, LayerN):
    #    pass
    #
    #def GetWeightsMatrixBackwardWithNext(self, LayerN):
    #    pass
    #
    #def GetWeightsMatrixBackwardWithPrev(self, LayerN):
    #    pass
    #   
    #
    #def SetWeightsMatrixForwardWithNext(self, LayerN, WM):
    #    pass
    #
    #def SetWeightsMatrixForwardWithPrev(self, LayerN, WM):
    #    pass
    #
    #def SetWeightsMatrixBackwardWithNext(self, LayerN, WM):
    #    pass
    #
    #def SetWeightsMatrixBackwardWithPrev(self, LayerN, WM):
    #    pass
    
    
    def GetBias(self, LayerN, NeuronN):
        pass

    def GetBias_Fixed0AllowedToChange1(self, LayerN, NeuronN):
        pass

    def SetBias(self, val, LayerN, NeuronN, Fixed0AllowedToChange1RemainWhatWas_m1=-1):
        pass


    def GetAllBiasesAndWeigthsAsSingleList(self, All0AllowedToChangeOnly1=0):
        pass

    def GetAllBiasesAndWeigthsAsSingleListOfArrayOfParams(self, All0AllowedToChangeOnly1=0):
        pass

    def SetAllBiasesAndWeigthsAsSingleList(self, data, All0AllowedToChangeOnly1=0):
        pass

                                      
        
