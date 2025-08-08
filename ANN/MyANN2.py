import copy
import math
import numpy as np
from scipy.optimize import fmin_powell

#math.sqrt(i)

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
print("\nsin(pi/2)="+str(math.sin(3.1415927/2))+"\n")

#class ValInfo:
#    def __init__(self, LayerN=0, NeuronN=1, CoLayerN=1, CoNeuronN=1, Weight1Bias0=1):
#        self.LayerN=LayerN
#        self.NeuronN=NeuronN
#        self.CoLayerN=CoLayerN
#        self.CoNeuronN=CoNeuronN
#        self.Weight1Bias0

#class Acson:
#    def __init__(LayerN=-1, NeuronConnectedN=1, weight=0, ChangeForbidden0Allowed1=1):
#        self.LayerN=LayerN
#        self.NeuronConnectedN=NeuronConnectedN
#        self.weight=weight
#        self.ChangeForbidden0Allowed1=ChangeForbidden0Allowed1

class ValInfo:
    def __init__(self, LayerN=0, NeuronN=1, CoLayerN=1, CoNeuronN=1, Val=0, ChangingForbidden0Allowed1=1):
        self.LayerN=LayerN
        self.NeuronN=NeuronN
        self.CoLayerN=CoLayerN
        self.CoNeuronN=CoNeuronN
        self.Val=Val
        self.ChangingForbidden0Allowed1=ChangingForbidden0Allowed1

class Acson1:
    def __init__(self, LayerFromN=-1, NeuronFromN=1, LayerToN=-1, NeuronToN=1, weight=1, ChangeForbidden0Allowed1=1):
        self.LayerFromN=LayerFromN
        self.NeuronFromN=NeuronFromN
        self.LayerToN=LayerToN
        self.NeuronToN=NeuronToN 
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
        ParamIniRandvalFowOwnVal=1
        ParamIniRandvalForBias=0
        #
        self.ownVal=ParamIniRandvalFowOwnVal
        self.B=ParamIniRandvalForBias
        self.B_ChangingForbidden0Allowed1=1
        self.val_ChangingForbidden0Allowed1=1
        #
    #    
    def getVal(self):
        return self.ownVal

    def getBias(self):
        return self.B

    def getBias_ChangingForbidden0Allowed1(self):
        return self.B_ChangingForbidden0Allowed1

    def getVal_ChangingForbidden0Allowed1(self):
        return self.val_ChangingForbidden0Allowed1

    def setBias_ChangingForbidden0Allowed1(self, ChangeForbidden0Allowed1_RemainAsWas_m1=-1):
        if ChangeForbidden0Allowed1_RemainAsWas_m1!=-1:
            if ChangeForbidden0Allowed1_RemainAsWas_m1==0:
                self.B_ChangingForbidden0Allowed1=0
            else:
                self.B_ChangingForbidden0Allowed1=1

    def setVal_ChangingForbidden0Allowed1(self, ChangeForbidden0Allowed1_RemainAsWas_m1=-1):
        if ChangeForbidden0Allowed1_RemainAsWas_m1!=-1:
            if ChangeForbidden0Allowed1_RemainAsWas_m1==0:
                self.val_ChangingForbidden0Allowed1=0
            else:
                self.val_ChangingForbidden0Allowed1=1

    def setBias(self, val, ChangingForbidden0Allowed1_RemainAsWas_m1=-1):
        self.B=val
        self.setBias_ChangingForbidden0Allowed1(self, ChangingForbidden0Allowed1_RemainAsWas_m1)

    def setVal(self, val, ChangingForbidden0Allowed1_RemainAsWas_m1=-1):
        self.ownVal=val
        self.setVal_ChangingForbidden0Allowed1(ChangingForbidden0Allowed1_RemainAsWas_m1)

                                 
class MyANN:
    def __init__(self, NNInf=0):
        curRow=[]
        #
        if isinstance(NNInf, ANNInfo):
            self.inf=copy.deepcopy(NNInf)
        else:
            self.inf=ANNInfo()
        #
        self.InputLayerNeurons=[]
        self.OutputLayerNeurons=[]
        self.HiddenLayerNeurons=[]
        self.acsons=[]
        #self.teacherY=[]
        #
        #for i in range(1, self.inf.QXs+1):
        #    curNeuron=MyNeuron(0, self.inf)
        #    self.InputLayerNeurons.append(curNeuron)
        #for i in range(1, self.inf.QYs+1):
        #    curNeuron=MyNeuron(-1, self.inf)
        #    self.OutputLayerNeurons.append(curNeuron)
        #for i in range(1, self.inf.QLayers+1):
        #    curRow=[]
        #    QHs=self.inf.GetQNeuronsOfCurrentLayerN(i)
        #    for j in range(1, QHs+1):
        #        curNeuron=MyNeuron(i, self.inf)
        #        curRow.append(curNeuron)
        #    self.HiddenLayerNeurons.append(curRow)
        #
        #for LayerN in range(0, self.inf.QLayers+1):
        #    for NeuronFromN in range(1, self.inf.QXs+1):
        #        for NeuronToN in range(1, self.inf.QHs[1-1]+1):
        #            ParamIniRandval=0
        #            acson=Acson1(LayerN, NeuronFromN, LayerN+1, NeuronToN, ParamIniRandval, 1)
        #            self.acsons.append(acson)
        self.SetIni()
    #
    #
    def SetIni(self):
        curRow=[]#qly ce work'te ac ce?
        ParamIniRandvalForWeight=1
        #
        self.InputLayerNeurons=[]
        self.OutputLayerNeurons=[]
        self.HiddenLayerNeurons=[]
        self.acsons=[]
        #self.teacherY=[]
        #
        for i in range(1, self.inf.QXs+1):
            curNeuron=MyNeuron(0, self.inf)
            curNeuron.setBias_ChangingForbidden0Allowed1(0)
            self.InputLayerNeurons.append(curNeuron)
        for i in range(1, self.inf.QYs+1):
            curNeuron=MyNeuron(-1, self.inf)
            self.OutputLayerNeurons.append(curNeuron)
        for i in range(1, self.inf.QLayers+1):
            curRow=[]
            QHs=self.inf.GetQNeuronsOfCurrentLayerN(i)
            for j in range(1, QHs+1):
                curNeuron=MyNeuron(i, self.inf)
                curRow.append(curNeuron)
            self.HiddenLayerNeurons.append(curRow)
        #
        for LayerN in range(0, self.inf.QLayers+1):
            if LayerN==0:
                QNeuronsFrom=self.inf.QXs
                QNeuronsTo=self.inf.QHs[1-1]
            elif LayerN>=1 and LayerN<=self.inf.QLayers-1:
                QNeuronsFrom=self.inf.QHs[LayerN-1]
                QNeuronsTo=self.inf.QHs[LayerN+1-1]
            elif LayerN==self.inf.QLayers:
                QNeuronsFrom=self.inf.QHs[LayerN-1]
                QNeuronsTo=self.inf.QYs
            for NeuronFromN in range(1, QNeuronsFrom+1):
                for NeuronToN in range(1, QNeuronsTo+1):
                    ParamIniRandvalForWeight=ParamIniRandvalForWeight
                    acson=Acson1(LayerN, NeuronFromN, LayerN+1, NeuronToN, ParamIniRandvalForWeight, 1)
                    self.acsons.append(acson)
        self.SetWeightsByNs()
    
    def getAcsonsAllowed(self, ChangingAllowed1NoMatter0=1):
        count=0
        acsonsAllowed=[]
        QAll=len(self.acsons)
        if ChangingAllowed1NoMatter0==0:
            count=QAll
            acsonsAllowed=copy.deepcopy(self.acsons)
        else:
            for i in range(1, QAll+1):
                acson=copy.deepcopy(self.acsons[i-1])
                if acson.ChangeForbidden0Allowed1==1:
                    count+=1
                    acsonsAllowed.append(acson)
        return acsonsAllowed

    def getNeuronsWithBiasesAllowedToChange(self, ChangingAllowedOnly1NoMatter0=1, vsh=0):
        neurons=[]
        dataList=[]
        if vsh==1:
            print("getNeuronsWithBiasesAllowedToChange starts working")
        for LayerN in range(0, self.inf.QLayers+1+1):
            #QNeurons=self.getQNeuronsInLayerN(LayerN)
            if LayerN==0:
                QNeurons=self.inf.QXs
                if vsh==1:
                    print("Layer X")
            elif LayerN==self.inf.QLayers+1:
                QNeurons=self.inf.QYs
                if vsh==1:
                    print("Layer Y")
            else:
                QNeurons=self.inf.QHs[LayerN-1]
                if vsh==1:
                    print("Layer H"+str(LayerN))
            for NeuronN in range(1, QNeurons+1):
                if LayerN==0:
                    curNeuron=self.InputLayerNeurons[NeuronN-1]
                elif LayerN==self.inf.QLayers+1:
                    curNeuron=self.OutputLayerNeurons[NeuronN-1]
                else:
                    curNeuron=self.HiddenLayerNeurons[LayerN-1][NeuronN-1]
                allowed=curNeuron.getBias_ChangingForbidden0Allowed1()
                if vsh==1:
                    print("Neuron N "+str(NeuronN)+" bias="+str(curNeuron.getBias())+"(allowed: "+str(allowed)+")")
                if allowed==1 or ChangingAllowedOnly1NoMatter0==0:
                    notNeuron=ValInfo(LayerN, NeuronN, 0, 0, curNeuron.getBias(), allowed)
                    neurons.append(notNeuron)
                    if vsh==1:
                        print("allowed")
                else:
                    if vsh==1:
                        print("not allowed")
        if vsh==1:
            print("getNeuronsWithBiasesAllowedToChange finishes working")
        return neurons
                    

    def QNeuronsInLayerN(self, LayerN):
        Q=0
        if LayerN==-1 or LayerN==self.inf.QLayers+1:
            Q=self.inf.QYs
        elif LayerN==0:
            Q=self.inf.QXs
        elif LayerN>=1 and LayerN<=self.inf.QLayers:
            Q=self.inf.QHs[LayerN-1]
        return Q

    #def 
    #
    #
    def getNeuronVal(self, LayerN, neuronN):
        val=0
        if LayerN==0 and neuronN>=1 and neuronN<=self.inf.QXs:
            val=self.InputLayerNeurons[neuronN-1].getVal()
        elif (LayerN==-1 or LayerN==self.inf.QLayers+1) and neuronN>=1 and neuronN<=self.inf.QYs:
            val=self.OutputLayerNeurons[neuronN-1].getVal()
        elif LayerN>=1 and LayerN<=self.inf.QLayers and neuronN>=1 and neuronN<=self.inf.QHs[LayerN-1]:
            val=self.HiddenLayerNeurons[LayerN-1][neuronN-1].getVal()
        return val

    def getNeuronBias(self, LayerN, neuronN):
        val=0
        if LayerN==0 and neuronN>=1 and neuronN<=self.inf.QXs:
            val=self.InputLayerNeurons[neuronN-1].getBias()
        elif (LayerN==-1 or LayerN==self.inf.QLayers+1) and neuronN>=1 and neuronN<=self.inf.QYs:
            val=self.OutputLayerNeurons[neuronN-1].getBias()
        elif LayerN>=1 and LayerN<=self.inf.QLayers and neuronN>=1 and neuronN<=self.inf.QHs[LayerN-1]:
            val=self.HiddenLayerNeurons[LayerN-1][neuronN-1].getBias()
        return val

    def getNeuronVal_ChangingForbiddenoAllowed1(self, LayerN, neuronN):
        val=0
        if LayerN==0 and neuronN>=1 and neuronN<=self.inf.QXs:
            val=self.InputLayerNeurons[neuronN-1].getVall_ChangingForbiddenoAllowed1()
        elif (LayerN==-1 or LayerN==self.inf.QLayers+1) and neuronN>=1 and neuronN<=self.inf.QYs:
            val=self.OutputLayerNeurons[neuronN-1].getVall_ChangingForbiddenoAllowed1()
        elif LayerN>=1 and LayerN<=self.inf.QLayers and neuronN>=1 and neuronN<=self.inf.QHs[LayerN-1]:
            val=self.HiddenLayerNeurons[LayerN-1][neuronN-1].getVal_ChangingForbidden0Allowed1()
        return val

    def getNeuronBias(self, LayerN, neuronN):
        val=0
        if LayerN==0 and neuronN>=1 and neuronN<=self.inf.QXs:
            val=self.InputLayerNeurons[neuronN-1].getBias()
        elif (LayerN==-1 or LayerN==self.inf.QLayers+1) and neuronN>=1 and neuronN<=self.inf.QYs:
            val=self.OutputLayerNeurons[neuronN-1].getBias()
        elif LayerN>=1 and LayerN<=self.inf.QLayers and neuronN>=1 and neuronN<=self.inf.QHs[LayerN-1]:
            val=self.HiddenLayerNeurons[LayerN-1][neuronN-1].getBias()
        return val
    #
    #
    def getConnectionN(self, LayerFromN, NeuronFromN, LayerToN, NeuronToN):
        Q=len(self.acsons)
        N=0
        for i in range(1, Q+1):
            if self.acsons[i-1].LayerFromN==LayerFromN and self.acsons[i-1].NeuronFromN==NeuronFromN  and self.acsons[i-1].LayerToN==LayerToN and self.acsons[i-1].NeuronToN==NeuronToN:
                N=i
        return N

    def getConnectionWeight(self, LayerFromN, NeuronFromN, LayerToN, NeuronToN):
        W=0
        N=getConnectionN(LayerFromN, NeuronFromN, LayerToN, NeuronToN)
        if(N>0):
            W=acsons[N-1].weight
        return W

    def getIfConnectionToChangeForbidden0Allowed1(self, LayerFromN, NeuronFromN, LayerToN, NeuronToN):
        R=0
        N=getConnectionN(LayerFromN, NeuronFromN, LayerToN, NeuronToN)
        if(N>0):
            R=acsons[N-1].Fixed0AllowedToChange1
        return R

    def getSingleNeuronIncomingConnectionsNs(self, LayerN, NeuronN, ChangingAllowedOnly1NoMatter0=1):
        Q=len(self.acsons)
        Ns=[]
        for i in range(1, Q+1):
            if self.acsons[i-1].LayerToN==LayerN and self.acsons[i-1].NeuronToN==NeuronN and (ChangingAllowedOnly1NoMatter0==0 or self.acsons[i-1].ChangeForbidden0Allowed1==1):
                Ns.append(i)
        return Ns

    def getSingleNeuronIncomingConnectionsWeights(self, LayerN, NeuronN, ChangingAllowedOnly1NoMatter0=1):
        Ns=self.getSingleNeuronIncomingConnectionsNs(LayerN, NeuronN, ChangingAllowedOnly1NoMatter0)
        Q=len(Ns)
        Ws=[]
        for i in range(1, Q+1):
            Ws.append(self.acsons[Ns[i-1]-1].weight)
        return Ws

    def getSingleNeuronVal(self, LayerN, NeuronN):
        if LayerN==0:
            val=self.InputLayerNeurons[NeuronN-1].getVal()
            valChangingForbidden0Allowed1=self.InputLayerNeurons[NeuronN-1].getVal_ChangingForbidden0Allowed1()
        elif LayerN==-1 or LayerN==self.inf.QLayers+1:
            val=self.OutnputLayerNeurons[NeuronN-1].getVal()
            valChangingForbidden0Allowed1=self.OutnputLayerNeurons[NeuronN-1].getVal_ChangingForbidden0Allowed1()
        elif LayerN>=1 and LayerN<=self.inf.QLayers:
            val=self.HiddenLayerNeurons[LayerN-1][NeuronN-1].getVal()
            valChangingForbidden0Allowed1=self.HiddenLayerNeurons[LayerN-1][NeuronN-1].getVal_ChangingForbidden0Allowed1()
            #if ChangingAllowedOnly1NoMatter0==0 or valChangingForbidden0Allowed1==1:
            #    Vals.append(val)
        return val

    def getSingleNeuronIncomingConnectionsNeuronsVals(self, LayerN, NeuronN, ChangingAllowedOnly1NoMatter0=1):
        Ns=self.getSingleNeuronIncomingConnectionsNs(LayerN, NeuronN, ChangingAllowedOnly1NoMatter0)
        Qs=len(Ns)
        Vals=[]
        for i in range(1, Qs+1):
            CoLayerN=self.acsons[Ns[i-1]-1].LayerFromN
            CoNeuronN=self.acsons[Ns[i-1]-1].NeuronFromN
            val=self.getSingleNeuronVal(CoLayerN, CoNeuronN)
            Vals.append(val)
        return Vals

    def getSingleNeuronOutcomingConnectionsNeuronsVals(self, LayerN, NeuronN, ChangingAllowedOnly1NoMatter0=1):
        Ns=self.getSingleNeuronAllOutcomingConnectionsNs(LayerN, NeuronN, ChangingAllowedOnly1NoMatter0)
        Qs=len(Ns)
        Vals=[]
        for i in range(1, Qs+1):
            CoLayerN=self.acsons[Ns[i-1]-1].LayerFromN
            CoNeuronN=self.acsons[Ns[i-1]-1].NeuronFromN
            val=self.getSingleNeuronVal(CoLayerN, CoNeuronN)
            Vals.append(val)
        return Vals

    def getSingleNeuronBias(self, LayerN, NeuronN):
        if LayerN==0:
            val=self.InputLayerNeurons[NeuronN-1].getBias()
            valChangingForbidden0Allowed1=self.InputLayerNeurons[NeuronN-1].getBias_ChangingForbidden0Allowed1()
        elif LayerN==-1 or LayerN==self.inf.QLayers+1:
            val=self.OutnputLayerNeurons[NeuronN-1].getBias()
            valChangingForbidden0Allowed1=self.OutnputLayerNeurons[NeuronN-1].getBias_ChangingForbidden0Allowed1()
        elif LayerN>=1 and LayerN<=self.inf.QLayers:
            val=self.HiddenLayerNeurons[LayerN-1][NeuronN-1].getBias()
            valChangingForbidden0Allowed1=self.HiddenLayerNeurons[LayerN-1][NeuronN-1].getBias_ChangingForbidden0Allowed1()
        return val

    def getAllNeuronsValsAsList(self, ChangingAllowedOnly1NoMatter0=1, vsh=0):
        Q=len(Ns)
        Vals=[]
        if vsh==1:
            print("getAllNeuronsValsAsList starts working")
            print("ChangingAllowedOnly1NoMatter0="+str(ChangingAllowedOnly1NoMatter0))
        for LayerN in range(0, self.inf.QLayers+1):
            if LayerN==0:
                QNeurons=self.inf.QXs
            elif LayerN==self.inf.QLayers+1:
                QNeurons=self.inf.QYs
            else:
                QNeurons=self.inf.QHs[LayerN-1]
            for NeuronN in range(1, QNeurons+1):
                if LayerN==0:
                    val=self.InputLayerNeurons[NeuronN-1].getVal()
                    valChangingForbidden0Allowed1=self.InputLayerNeurons[NeuronN-1].getVal_ChangingForbidden0Allowed1()
                    NeededVal=val
                    if ChangingAllowedOnly1NoMatter0==0 or valChangingForbidden0Allowed1==1:
                        Vals.append(NeededVal)
                elif LayerN==-1 or LayerN==self.inf.QLayers+1:
                    for NeuronN in range(1, self.QYs+1):
                        val=self.OutputLayerNeurons[NeuronN-1].getVal()
                        valChangingForbidden0Allowed1=self.OutputLayerNeurons[NeuronN-1].getVal_ChangingForbidden0Allowed1()
                        NeededVal=val
                    if ChangingAllowedOnly1NoMatter0==0 or valChangingForbidden0Allowed1==1:
                        Vals.append(NeededVal)
                elif LayerN>=1 and LayerN<=self.inf.QLayers:
                    for NeuronN in range(1, self.QHs[LayerN-1]+1):
                        val=self.HiddenLayerNeurons[LayerN-1][NeuronN-1].getVal()
                        valChangingForbidden0Allowed1=self.HiddenLayerNeurons[LayerN-1][NeuronN-1].getVal_ChangingForbidden0Allowed1()
                        NeededVal=val
                        if ChangingAllowedOnly1NoMatter0==0 or valChangingForbidden0Allowed1==1:
                            Vals.append(NeededVal)
            if vsh==1:
                print("getAllNeuronsValsAsList finishets working")
        return Vals

    def getAllNeuronsBiasesAsList(self, ChangingAllowedOnly1NoMatter0=1, vsh=0):
        Q=len(Ns)
        Vals=[]
        if vsh==1:
            print("getAllNeuronsBiasesAsList starts working")
            print("ChangingAllowedOnly1NoMatter0="+str(ChangingAllowedOnly1NoMatter0))
        for LayerN in range(0, self.inf.QLayers+1):
            if LayerN==0:
                QNeurons=self.inf.QXs
            elif LayerN==self.inf.QLayers+1:
                QNeurons=self.inf.QYs
            else:
                QNeurons=self.inf.QHs[LayerN-1]
            for NeuronN in range(1, QNeurons+1):
                if LayerN==0:
                    val=self.InputLayerNeurons[NeuronN-1].getVal()
                    valChangingForbidden0Allowed1=self.InputLayerNeurons[NeuronN-1].getVal_ChangingForbidden0Allowed1()
                    NeededVal=valChangingForbidden0Allowed1
                    if ChangingAllowedOnly1NoMatter0==0 or valChangingForbidden0Allowed1==1:
                        Vals.append(NeededVal)
                elif LayerN==-1 or LayerN==self.inf.QLayers+1:
                    for NeuronN in range(1, self.QYs+1):
                        val=self.OutputLayerNeurons[NeuronN-1].getVal()
                        valChangingForbidden0Allowed1=self.OutputLayerNeurons[NeuronN-1].getVal_ChangingForbidden0Allowed1()
                        NeededVal=valChangingForbidden0Allowed1
                    if ChangingAllowedOnly1NoMatter0==0 or valChangingForbidden0Allowed1==1:
                        Vals.append(NeededVal)
                elif LayerN>=1 and LayerN<=self.inf.QLayers:
                    for NeuronN in range(1, self.QHs[LayerN-1]+1):
                        val=self.HiddenLayerNeurons[LayerN-1][NeuronN-1].getVal()
                        valChangingForbidden0Allowed1=self.HiddenLayerNeurons[LayerN-1][NeuronN-1].getVal_ChangingForbidden0Allowed1()
                        NeededVal=valChangingForbidden0Allowed1
                        if ChangingAllowedOnly1NoMatter0==0 or valChangingForbidden0Allowed1==1:
                            Vals.append(NeededVal)
            if vsh==1:
                print("getAllNeuronsBiasesAsList finishets working")
        return Vals

    def getSingleNeuronOutcomingConnectionsNs(self, LayerN, NeuronN, ChangingAllowedOnly1NoMatter0=1):
        Q=len(self.acsons)
        Ns=[]
        for i in range(1, Q+1):
            if self.acsons[i-1].LayerFromN==LayerN and self.acsons[i-1].NeuronFromN==NeuronN and (ChangingAllowedOnly1NoMatter0==0 or self.acsons[i-1].ChangeForbidden0Allowed1==1):
                Ns.append(i)
        return Ns

    def getSingleNeuronOutcomingConnectionsWeights(self, LayerN, NeuronN, ChangingAllowedOnly1NoMatter0=1):
        Ns=self.getSingleNeuronAllOutcomingConnectionsNs(LayerN, NeuronN, ChangingAllowedOnly1NoMatter0)
        Q=len(Ns)
        Ws=[]
        for i in range(1, Q+1):
            W.append(acson[i-1].weight)
        return Ws

    def getSingleNeuronOutcomingConnectionsNeuronsVals(self, LayerN, NeuronN, ChangingAllowedOnly1NoMatter0=1):
        Ns=self.getSingleNeuronAllOutcomingConnectionsNs(LayerN, NeuronN, ChangingAllowedOnly1NoMatter0)
        Q=len(Ns)
        Vals=[]
        for i in range(1, Q+1):
            LayerN=acsons[i-1].LayerToN
            NeuronN=acsons[i-1].NeuronToN
            if LayerN==0:
                val=self.InputLayerNeurons[NeuronN-1].getVal()
            elif LayerN==-1 or LayerN==self.inf.QLayers+1:
                val=self.OutnputLayerNeurons[NeuronN-1].getVal()
            elif LayerN>=1 and LayerN<=self.inf.QLayers:
                val=self.HiddenLayerNeurons[LayerN-1][NeuronN-1].getVal()
            Vals.append(val)
        return Vals

    def getNeuronQIn(self, LayerN, NeuronN, ChangingAllowedOnly1NoMatter0=1):
        Ns=self.getSingleNeuronIncomingConnectionsNs(LayerN, NeuronN, ChangingAllowedOnly1NoMatter0)
        L=len(Ns)
        return L

    def getNeuronQOut(self, LayerN, NeuronN, ChangingAllowedOnly1NoMatter0=1):
        Ns=self.getSingleNeuronOutcomingConnectionsNs(LayerN, NeuronN, ChangingAllowedOnly1NoMatter0)
        L=len(Ns)
        return L

    def SetConnectionWeight(self, LayerFromN, NeuronFromN, LayerToN, NeuronToN, weight, ChangingForbidden0Allowed1_RemainAsWas_m1=-1):
        N=getConnectionN(self, LayerFromN, NeuronFromN, LayerToN, NeuronToN)
        if N>0:
            self.acsons[N-1].weight=weight
            if ChangingForbidden0Allowed1_RemainAsWas_m1!=-1:
                if ChangingForbidden0Allowed1_RemainAsWas_m1==0:
                    self.acsons[N-1].ChangingForbidden0Allowed1=0
                else:
                    self.acsons[N-1].ChangingForbidden0Allowed1=1

    def SetIfConnectionWeightChangingIsAllowed(self, LayerFromN, NeuronFromN, LayerToN, NeuronToN, ChangingForbidden0Allowed1_RemainAsWas_m1=-1):
        N=getConnectionN(self, LayerFromN, NeuronFromN, LayerToN, NeuronToN)
        if N>0:
            if ChangingForbidden0Allowed1_RemainAsWas_m1!=-1:
                if ChangingForbidden0Allowed1_RemainAsWas_m1==0:
                    self.acsons[N-1].ChangingForbidden0Allowed1=0
                else:
                    self.acsons[N-1].ChangingForbidden0Allowed1=1

    def SetNeuronVal(self, LayerN, NeuronN, val, ChangingForbidden0Allowed1_RemainAsWas_m1=-1):
        if LayerN>=1 and LayerN<=self.inf.QLayers:
            self.HiddenLayerNeurons[LayerN-1][NeuronN-1].setVal(val, ChangingForbidden0Allowed1_RemainAsWas_m1)
        elif LayerN==0:
            self.InputLayerNeurons[NeuronN-1].setVal(val, ChangingForbidden0Allowed1_RemainAsWas_m1)
        elif LayerN==-1 or LayerN==self.inf.QLayers+1:
            self.OutputLayerNeurons[NeuronN-1].setVal(val, ChangingForbidden0Allowed1_RemainAsWas_m1)

    def SetNeuronVal_ChangingForbidden0Allowed1(self, LayerN, NeuronN, ChangingForbidden0Allowed1_RemainAsWas_m1=-1):
        if LayerN>=1 and LayerN<=self.inf.QLayers:
            self.HiddenLayerNeurons[LayerN-1][NeuronN-1].setVal_ChangingForbidden0Allowed1(ChangingForbidden0Allowed1_RemainAsWas_m1)
        elif LayerN==0:
            self.InputLayerNeurons[NeuronN-1].setVal_ChangingForbidden0Allowed1(ChangingForbidden0Allowed1_RemainAsWas_m1)
        elif LayerN==-1 or LayerN==self.inf.QLayers+1:
            self.OutputLayerNeurons[NeuronN-1].setVal_ChangingForbidden0Allowed1(ChangingForbidden0Allowed1_RemainAsWas_m1)
            
    def SetNeuronBias(self, LayerN, NeuronN, bias, ChangingForbidden0Allowed1_RemainAsWas_m1=-1):
        if LayerN>=1 and LayerN<=self.inf.QLayers:
            self.HiddenLayerNeurons[LayerN-1][NeuronN-1].setBias(bias, ChangingForbidden0Allowed1_RemainAsWas_m1)
        elif LayerN==0:
            self.InputLayerNeurons[NeuronN-1].setBias(val, ChangingForbidden0Allowed1_RemainAsWas_m1)
        elif LayerN==-1 or LayerN==self.inf.QLayers+1:
            self.OutputLayerNeurons[NeuronN-1].setBias(val, ChangingForbidden0Allowed1_RemainAsWas_m1)
            
    def SetNeuronBias_ChangingForbidden0Allowed1(self, LayerN, NeuronN, bias, ChangingForbidden0Allowed1_RemainAsWas_m1=-1):
        if LayerN>=1 and LayerN<=self.inf.QLayers:
            self.HiddenLayerNeurons[LayerN-1][NeuronN-1].setBias_ChangingForbidden0Allowed1(ChangingForbidden0Allowed1_RemainAsWas_m1)
        elif LayerN==0:
            self.InputLayerNeurons[NeuronN-1].setBias_ChangingForbidden0Allowed1(ChangingForbidden0Allowed1_RemainAsWas_m1)
        elif LayerN==-1 or LayerN==self.inf.QLayers+1:
            self.OutputLayerNeurons[NeuronN-1].setBias_ChangingForbidden0Allowed1(ChangingForbidden0Allowed1_RemainAsWas_m1)
    #
    #
    def GetAllValsOfWeightsAndBiasesAsSingleList(self, ChangingAllowedOnly1NoMatter0=1, vsh=1):
        if vsh==1:
            print("GetAllValsOfWeightsAndBiasesFromSingleList starts working")
        acsonsAllowed=self.getAcsonsAllowed(ChangingAllowedOnly1NoMatter0)
        neuronsAllowed=self.getNeuronsWithBiasesAllowedToChange(ChangingAllowedOnly1NoMatter0)
        QWeightsToChange=len(acsonsAllowed)
        QBiasesToChange=len(neuronsAllowed)
        if vsh==1:
            print("Acsons weights: ("+str(QWeightsToChange)+")")
            for i in range(1, QWeightsToChange+1):
                print("Acson between Neuron[LayerN "+str(acsonsAllowed[i-1].LayerFromN)+" N "+str(acsonsAllowed[i-1].NeuronFromN)+" And Neuron: LayerN "+str(acsonsAllowed[i-1].LayerToN)+" N "+str(acsonsAllowed[i-1].NeuronToN)+" has weight="+str(acsonsAllowed[i-1].weight)+" (allowed: "+str(acsonsAllowed[i-1].ChangeForbidden0Allowed1)+")")
        Vals=[]
        #
        for i in range(1, QWeightsToChange+1):
            N=i
            Vals.append(acsonsAllowed[N-1].weight)
        for i in range(1, QBiasesToChange+1):
            N=i+QWeightsToChange
            #Vals.append(neuronsAllowed[N-1].val)
            Vals.append(neuronsAllowed[i-1].Val)
        if vsh==1:
            print("Neurons biases: ("+str(QBiasesToChange)+")")
            for i in range(1, QBiasesToChange+1):
                print("Neuron (allowed "+str(i)+") of LayerN "+str(neuronsAllowed[i-1].LayerN)+" NeuronN "+str(neuronsAllowed[i-1].NeuronN)+" bias="+str(neuronsAllowed[i-1].Val)+" (allowed:"+str(neuronsAllowed[i-1].ChangingForbidden0Allowed1)+")")
            print("GetAllValsOfWeightsAndBiasesFromSingleList finishes working")
        return Vals

    def GetAllParamsOfWeightsAndBiasesAsSingleList(self, ChangingAllowedOnly1NoMatter0=1):
        acsonsAllowed=self.getAcsonsAllowed(ChangingAllowedOnly1NoMatter0)
        neuronsAllowed=self.getNeuronsWithBiasesAllowedToChange(ChangingAllowedOnly1NoMatter0)
        QWeightsToChange=len(acsonsAllowed)
        QBiasesToChange=len(neuronsAllowed)
        Vals=[]
        #
        for i in range(1, QWeightsToChange+1):
            N=i
            if acsonsAllowed[i-1].LayerFromN==0:
                LayerFromName="X"
            elif acsonsAllowed[i-1].LayerFromN==inf.QLayers+1:
                LayerFromName="Y"
            else:
                LayerFromName="H"+str(acsonsAllowed[i-1].LayerFromN)
            if acsonsAllowed[i-1].LayerToN==0:
                LayerToName="X"
            elif acsonsAllowed[i-1].LayerToN==inf.QLayers+1:
                LayerToName="Y"
            else:
                LayerToName="H"+str(acsonsAllowed[i-1].LayerToN)
            val=str(i)+") Acson (allowed "+str(i)+") From Layer "+LayerFromName+" NeuronN "+str(acsonsAllowed[i-1].NeuronFromN)+" To Layer "+LayerToName+" NeuronN "+str(acsonsAllowed[i-1].LayerToN)+" weight="+str(acsonsAllowed[i-1].weight)+" (allowed: "+str(acsonsAllowed[i-1].ChangeForbidden0Allowed1)+")"
            #Vals.append(acsonsAllowed[N-1].weight)
            Vals.append(val)
        for i in range(1, QBiasesToChange+1):
            N=i+QWeightsToChange#No need
            val=val=str(i)+") Neuron (allowed "+str(i)+") of LayerN "+str(neuronsAllowed[i-1].LayerN)+" NeuronN "+str(neuronsAllowed[i-1].NeuronN)+" bias="+str(neuronsAllowed[i-1].Val)+" (allowed:"+str(neuronsAllowed[i-1].ChangingForbidden0Allowed1)+")"
            Vals.append(val)
        return Vals
    
    def SetAllWeightsAndBiasesFromSingleList(self, Vals, ChangingAllowedOnly1NoMatter0=1, vsh=0):
        if(vsh==1):
            print("SetAllWeightsAndBiasesFromSingleList starts working")
            print("Vals="+str(Vals))
        acsonsAllowed=self.getAcsonsAllowed(ChangingAllowedOnly1NoMatter0)
        neuronsAllowed=self.getNeuronsWithBiasesAllowedToChange(1)#(ChangingAllowedOnly1NoMatter0)
        QWeightsToChange=len(acsonsAllowed)
        QBiasesToChange=len(neuronsAllowed)
        QExtVals=len(Vals)
        #
        LayerFromN=0
        NeuronFromN=0
        LayerToN=0
        NeuronToN=0
        LayerN=0
        NeuronN=0
        ErstWeightN=0
        LastWeightN=0
        ErstBiasN=0
        LastBiastN=0
        N=0
        N1=0
        #ifAlowed=-2
        #
        if QExtVals==QWeightsToChange+QBiasesToChange:
            ErstWeightN=1
            LastWeightN=QWeightsToChange
            ErstBiasN=LastWeightN+1
            LastBiasN=QExtVals
            for i in range(ErstWeightN, LastWeightN+1):
                N=i
                LayerFromN=acsonsAllowed[N-1].LayerFromN
                LayerToN=acsonsAllowed[N-1].LayerToN
                NeuronFromN=acsonsAllowed[N-1].NeuronFromN
                NeuronToN=acsonsAllowed[N-1].NeuronToN
                N1=self.getConnectionN(LayerFromN, NeuronFromN, LayerToN, NeuronToN)
                self.acsons[N1-1].weight=Vals[i-1]
            for i in range(ErstBiasN, LastBiasN+1):
                N=i-ErstBiasN+1
                LayerN=neuronsAllowed[N-1].LayerN
                NeuronN=neuronsAllowed[N-1].NeuronN
                self.SetNeuronBias(self, LayerN, NeuronN, Vals[i-1])
            #    
        #
        if(vsh==1):
            NewVals=self.GetAllParamsOfWeightsAndBiasesAsSingleList(ChangingAllowedOnly1NoMatter0)
            print("Vals are set:")
            print (NewVals)
            print("SetAllWeightsAndBiasesFromSingleList finishes working")
    #                 
    #
    def ActivationFunction(self, x):
        return math.atan(10*x)/math.asin(1)/2+0.5
    
    def CalcNeuronValForward(self, LayerN, NeuronN, WsAll=[], WriteWsIfGivenNo0Yes1=0, vsh=0):
        Vals=[]
        WsIn=[]
        if vsh==1:
            print("CalcNeuronValForward starts working")
            print("LayerN="+str(LayerN)+" NeuronN="+str(NeuronN)+" WsAll="+str(WsAll)+" vsh="+str(vsh))
        val=self.getSingleNeuronBias(LayerN, NeuronN)
        QVals=self.getNeuronQIn(LayerN, NeuronN)
        if LayerN>=1 and LayerN<=self.inf.QLayers:
            QNeurons=self.inf.QHs[LayerN-1]
        elif LayerN==-1 or LayerN==self.inf.QLayers+1:
            QNeurons=self.inf.QYs
        #LayerExists=(LayerN>=1 and LayerN<=self.inf.QLayers+1)
        #NeuronNExists=(NeuronN>=1 and NeuronN<=QNeurons)
        #ValChangingForbiddenoAllowed1=(self.getNeuronVal_ChangingForbiddenoAllowed1( LayerN, NeuronN)==1)
        if LayerN>=1 and LayerN<=self.inf.QLayers+1:
            LayerExists=1
        else:
            LayerExists=0         
        if NeuronN>=1 and NeuronN<=QNeurons:
            NeuronNExists=1
        else:
            NeuronNExists=0         
        if self.getNeuronVal_ChangingForbiddenoAllowed1(LayerN, NeuronN)==1:
            ValChangingForbidden0Allowed1=1
        else:
            ValChangingForbidden0Allowed1=0
        if LayerExists==1 and NeuronNExists==1 and ValChangingForbidden0Allowed1==1:
            Vals=self.getSingleNeuronIncomingConnectionsNeuronsVals(LayerN, NeuronN, 0)#D utf'tc ut get ir vals, ne set
            WsIn=self.getSingleNeuronIncomingConnectionsWeights(LayerN, NeuronN, 0)
            QIncoming=len(WsIn)
            if(len(Vals)!=len(WsIn)):
                print("error: found incoming acsons: "+str(len(WsIn))+"  not equal to incoming connected neurons: "+str(len(Vals)))
            if vsh==1:
                for i in range(1, QIncoming+1):
                    print("Incoming connection "+str(i)+" LayerN "+str("?")+" N "+str("?")+" weight= "+str(WsIn[i-1])+" val= "+str(Vals[i-1]))
            if WsAll==[]:
                pass
                if vsh==1:
                   print("WsAll given=[] - normal situation") 
            else:
                NsAll=self.getSingleNeuronIncomingConnectionsNs(LayerN, NeuronN, 0)#ChangingAllowedOnly1NoMatter0=1)
                NsAllowed=self.getSingleNeuronIncomingConnectionsNs(LayerN, NeuronN, 1)#ChangingAllowedOnly1NoMatter0=1)
                QAllowed=len(NsAllowed)
                if vsh==1:
                    print("Here now: WsAll= "+str(WsAll)+" WsIn="+str(WsIn))
                if(len(WsAll)!=len(WsIn)):
                    print("len(WsAll)="+str(len(WsAll))+" != len(WsIn)="+str(len(WsIn)))
                for i in range(1, QAllowed+1):
                    WsIn[i-1]=WsAll[NsAll[i-1]-1]
                    if vsh==1:
                        print("Weights: "+str(WsIn))
            if vsh==1:
                print("Calculating: ")
                print("val at start = bias: val="+str(val))
            for i in range(1, QVals+1):
                cur=Vals[i-1]*WsIn[i-1]
                val=val+cur
                if vsh==1:
                    print(str(i)+") val + "+str(Vals[i-1])+" * "+str(WsIn[i-1])+" = val + "+str(cur)+" = "+str(val))
            val=self.ActivationFunction(val)
            self.SetNeuronVal(LayerN, NeuronN, val)
        if vsh==1:
            print("answer="+str(val))
            print("CalcNeuronValForward finishes working")
        return val

    def ForwardPropagation(self, Vals=[], X=[], ChangingAllowedOnly1NoMatter0=1, vsh=0):
        WriteWsIfGivenNo0Yes1=1
        if vsh==1:
            print("ForwardPropagation starts working")
        if X==[]:
            if vsh==1:
                print("X=[] - normal situation")
        else:
            #if vsh==1:
            #    print("X (must be "+str(self.inf.QXs)+", given "+str(len(X))+" - "+str(X))
            for NeuronN in range(1, self.inf.QXs+1):# no matter qq Xs ext, vikt, qq X neurons, so - not less!
                val=X[NeuronN-1]
                self.SetNeuronVal(self, 0, NeuronN, val)
            if vsh==1:
                print("X="+str(X))
        if Vals==[]:
            if vsh==1:
                print("Vals=[] ")
        else:
            self.SetAllWeightsAndBiasesFromSingleList(Vals, ChangingAllowedOnly1NoMatter0, vsh)
            if vsh==1:
                print("Vals="+str(Vals))
        for LayerN in range(1, self.inf.QLayers+1):
            QNeurons=self.QNeuronsInLayerN(LayerN)
            for NeuronN in range(1, QNeurons+1):
                if vsh==1:
                    print("LayerN: "+str(LayerN)+" NeuronN: "+str(NeuronN))
                curVal=self.CalcNeuronValForward(LayerN, NeuronN, Vals, WriteWsIfGivenNo0Yes1, vsh)
                #CalcNeuronValForward(self, LayerN, NeuronN, WsAll=[], WriteWsIfGivenNo0Yes1=0, vsh=0)
            #
        if vsh==1:
            print("ForwardPropagation finishes working")
    #
    def LossFunction(self, Vals, X, teacherY, vsh=0):
        if vsh==1:
            print("LossFunction starts working")
            print("Vals="+str(Vals)+" X="+str(X)+" teacherY="+str(teacherY))
        #ForwardPropagation(self, Vals=[], X=[], ChangingAllowedOnly1NoMatter0=1, vsh=0):
        self.ForwardPropagation(Vals, X, 1, 1)
        err=0
        predictedY=[]
        for i in range(1, self.inf.QYs+1):
            predictedY.append(self.OutputLayerNeurons[i-1].getVal())
            #predictedY=self.OutputLayerNeurons[i-1].getVal()
            cur=predictedY[i-1]*predictedY[i-1]-teacherY[i-1]*teacherY[i-1]
            #cur=predictedY*predictedY-teacherY[i-1]*teacherY[i-1]
            err+=cur
        err=math.sqrt(err)
        if vsh==1:
            if X==[]:
                for i in range(1, self.inf.QXs+1):
                    val=self.InputLayerNeurons[i-1].getVal()
                    X.append(val)
            print("predictedY="+str(predictedY))
            print("teacherY="+str(teacherY))
            print("answer: err = sqrt( S(Yp^2-Yt^2) ) = "+str(err))
            print("LossFunction finishes working")
        return err

    def LearnOneLesson(self, X, teacherY, vsh=0):
        print("LearnOneLesson starts working")
        print("Lesson: X: "+str(X)+" teacherY: "+str(teacherY))
        if vsh==1:
            print("LearnOneLesson starts working")
            print("Lesson: X: "+str(X)+" teacherY: "+str(teacherY))
        ChangingAllowedOnly1NoMatter0=1
        #def GetAllValsOfWeightsAndBiasesAsSingleList(self, ChangingAllowedOnly1NoMatter0=1, vsh=1)
        ValsPrev=self.GetAllValsOfWeightsAndBiasesAsSingleList(ChangingAllowedOnly1NoMatter0, vsh)
        print("Ini vals: "+str(ValsPrev))
        if vsh==1:
            print("Ini vals: "+str(ValsPrev))
            print("Optimizing...")
        Vals1=fmin_powell(self.LossFunction, np.array(ValsPrev), (X, teacherY,))
        print("Optimized vals calc'd in single lesson: "+str(Vals1))
        if vsh==1:
            print("Optimized vals calc'd in single lesson: "+str(Vals1))
        Q=len(Vals1)
        Vals2=[]
        for i in range(1, Q+1):
            Vals2.append((Vals1[i-1]+ValsPrev[i-1])/2)
        print("New vals calc'd: "+str(Vals2))
        print("LearnOneLesson finishes working")
        #Write new val
        if vsh==1:
            print("New vals calc'd: "+str(Vals2))
            print("LearnOneLesson finishes working")
        return Vals2

    def Show(self):
        print("QXs="+str(self.inf.QXs)+" QYs="+str(self.inf.QXs)+" HiddenLayers: "+str(self.inf.QLayers)+" : "+str(self.inf.QHs))
        s=""
        for i in range(1, self.inf.QXs):
            s=s+" X"+str(i)+": val="+str(self.getNeuronVal(0, i))+"; bias="+str(self.getNeuronBias(0, i))+"; "
            print(s)
        for i in range(1, self.inf.QYs):
            s=s+" Y"+str(i)+": val="+str(self.getNeuronVal(-1, i))+"; bias="+str(self.getNeuronBias(-1, i))+"; "
            print(s)
        print("Hidden layers:")
        for i in range(1, self.inf.QLayers+1):
            print("Layer "+str(i)+" :")
            for j in range(1, self.inf.QHs[i-1]+1):
                s=s+" H"+str(i)+": val="+str(self.getNeuronVal(i, j))+"; bias="+str(self.getNeuronBias(i, j))+"; "
            print(s)
        print("Acsons:")
        print("Input Layer:")
        for i in range(1, self.inf.QXs+1):
            print("X"+str(i)+":")
            s=""
            for j in range(1, self.inf.QHs[1-1]+1):
                N=self.getConnectionN(0, i, 1, j)
                s=s+str(j)+") weight="+str(self.acsons[N-1].weight)+" ChangingForbidden0Allowed1: "+str(self.acsons[N-1].ChangeForbidden0Allowed1)+"; "
            print(s)
        print("Hidden Layers:")
        for LayerN in range(1, self.inf.QLayers+1):
            #LayerToN=LayerFromN+1
            #QInLayerFrom=self.inf.QHs[LayerFromN-1]
            #QInLayerTo=self.inf.QHs[LayerToN-1]
            print("Layer "+str(LayerN)+"+:")
            for NeuronN in range(1, self.inf.QHs[LayerN-1]+1):
                QOut=self.getNeuronQOut(LayerN, NeuronN)
                QIn=self.getNeuronQIn(LayerN, NeuronN)
                print("H"+str(NeuronN)+" (of Layer "+str(LayerN)+")")
                print("input connected with "+str(QIn)+" neurons:")
                Ns=self.getSingleNeuronIncomingConnectionsNs(LayerN, NeuronN)
                for i in range(1, QIn+1):
                    print("Connection "+str(i)+" LayerN: "+str(self.acsons[Ns[i-1]-1].LayerFromN)+" NeuronN: "+str(self.acsons[Ns[i-1]-1].NeuronFromN)+" weight: "+str(self.acsons[Ns[i-1]-1].weight))
                print("output connected with "+str(QIn)+" neurons:")
                #
                s=""
                for CoNeuronN in range(1, QOut+1):
                    N=self.getConnectionN(LayerN, NeuronN, LayerN+1, CoNeuronN)
                    s=s+str(CoNeuronN)+") weight="+str(self.acsons[N-1].weight)+" ChangingForbidden0Allowed1: "+str(self.acsons[N-1].ChangeForbidden0Allowed1)+"; "
                print(s)
                Ns=self.getSingleNeuronOutcomingConnectionsNs(LayerN, NeuronN)
                print("output connected with "+str(QOut)+" neurons:")
                for i in range(1, QOut+1):
                    CoLayerN=self.acsons[Ns[i-1]-1].LayerToN
                    if CoLayerN==self.inf.QLayers+1:
                        print("Connection "+str(i)+" Output Layer (N: "+str(CoLayerN)+") NeuronN: "+str(self.acsons[Ns[i-1]-1].NeuronToN)+" weight: "+str(self.acsons[Ns[i-1]-1].weight))
                    else:
                        print("Connection "+str(i)+" LayerN: "+str(CoLayerN)+" NeuronN: "+str(self.acsons[Ns[i-1]-1].NeuronToN)+" weight: "+str(self.acsons[Ns[i-1]-1].weight))
        print("Output Layer:")
        LayerN=self.inf.QLayers+1
        for NeuronN in range(1, self.inf.QYs+1):
            QOut=self.getNeuronQOut(LayerN, NeuronN)
            QIn=self.getNeuronQIn(LayerN, NeuronN)
            print("H"+str(NeuronN))
            print("input connected with "+str(QIn)+" neurons:")
            Ns=self.getSingleNeuronIncomingConnectionsNs(LayerN, NeuronN)
            for i in range(1, QIn+1):
                print("Connection "+str(i)+" LayerN: "+str(self.acsons[Ns[i-1]-1].LayerFromN)+" NeuronN: "+str(self.acsons[Ns[i-1]-1].NeuronFromN)+" weight: "+str(self.acsons[Ns[i-1]-1].weight))
            print("output connected with "+str(QIn)+" neurons:")
            #
            #for CoNeuronN in range(1, QOut+1):
            #    N=self.getConnectionN(LayerN, NeuronN, LayerN+1, CoNeuronN)
            #    s=s+str(CoNeuronN)+") weight="+str(self.acsons[N-1].weight)+" ChangingForbidden0Allowed1: "+str(self.acsons[N-1].ChangeForbidden0Allowed1)+"; "
            #print(s)
            Ns=self.getSingleNeuronOutcomingConnectionsNs(LayerN, NeuronN)
            print("output connected with "+str(QOut)+" neurons:")
            for i in range(1, QOut+1):
                CoLayerN=self.acsons[Ns[i-1]-1].LayerToN
                print("Connection "+str(i)+" LayerN: "+str(CoLayerN)+" NeuronN: "+str(self.acsons[Ns[i-1]-1].NeuronToN)+" weight: "+str(self.acsons[Ns[i-1]-1].weight))
        
    def ShowValsToChange(self, ChangingAllowedOnly1NoMatter0=1, vsh=0):
        vals=self.GetAllValsOfWeightsAndBiasesAsSingleList(ChangingAllowedOnly1NoMatter0, vsh)
        Q=len(vals)
        for i in range(1, Q+1):
            print(str(i)+") "+str(vals[i-1]))
    #
    #
    def SetWeightsByNs(self):
        QLnks=len(self.acsons)
        for i in range(1, QLnks+1):
            NFrom=self.acsons[i-1].NeuronFromN
            NTo=self.acsons[i-1].NeuronToN
            self.acsons[i-1].weight=NFrom+1.0*NTo/1000

    def getQAcsonsAllowed(self, ChangeAllowedOnly1NoMatter0=1):
        count=0
        Q=len(self.acsons)
        for i in range(1, Q+1):
            if self.acsons[i-1].ChangeForbidden0Allowed1==1 or ChangeAllowedOnly1NoMatter0==0:
                 count+=1
        return count
               
    def getQNeuronsBiasesAllowed(self, ChangeAllowedOnly1NoMatter0=1):
        count=0
        for i in range(1, self.inf.QXs+1):
            if self.InputLayerNeurons[i-1].getBias_ChangingForbidden0Allowed1()==1 or ChangeAllowedOnly1NoMatter0==0:
               count+=1
        for i in range(1, self.inf.QYs+1):
            if self.OutputLayerNeurons[i-1].getBias_ChangingForbidden0Allowed1()==1 or ChangeAllowedOnly1NoMatter0==0:
               count+=1
        for i in range(1, self.inf.QLayers+1):
            for j in range(1, self.inf.QHs[i-1]+1):
                if self.HiddenLayerNeurons[i-1][j-1].getBias_ChangingForbidden0Allowed1()==1 or ChangeAllowedOnly1NoMatter0==0:
                    count+=1
        return count


vsh=1
ChangingAllowedOnly1NoMatter0=0
#----------------------------------------------------------
#inf=ANNInfo(8, 3, [9,9])
#ann=MyANN(inf)
#print("\n\nNeural network:")
#ann.Show()
#print("\nVals:")
#ann.ShowValsToChange(ChangingAllowedOnly1NoMatter0, vsh)
#X=[1, 2, 3, 4, 5, 6, 7, 8]
#teacherY=[1, 0, 0]
#print("\Loss function of Forward propagation: W,B=[], X="+str(X)+" teacherY= "+str(teacherY)+" : ")
#err=ann.LossFunction([], X, teacherY, vsh)
#print("error="+str(err))
#print("allowed weights: "+str(ann.getQAcsonsAllowed()))
#print("allowed biases: "+str(ann.getQNeuronsBiasesAllowed()))
#print("all weights: "+str(ann.getQAcsonsAllowed(0)))
#print("all biases: "+str(ann.getQNeuronsBiasesAllowed(0)))
#print("\n\n\n-------------------------------------------------------------------------------------------------\n\n\n")
inf=ANNInfo(3, 3, [3])
ann=MyANN(inf)
print("\n\nNeural network:")
ann.Show()
print("\nVals:")
ann.ShowValsToChange(ChangingAllowedOnly1NoMatter0, vsh)
#X=[1, 2, 3, 4, 5, 6, 7, 8]
X=[1, 2, 3]
teacherY=[1, 0, 0]
print("\Loss function of Forward propagation: W,B=[], X="+str(X)+" teacherY= "+str(teacherY)+" : ")
err=ann.LossFunction([], X, teacherY, vsh)
print("error="+str(err))
print("allowed weights: "+str(ann.getQAcsonsAllowed()))
print("allowed biases: "+str(ann.getQNeuronsBiasesAllowed()))
print("all weights: "+str(ann.getQAcsonsAllowed(0)))
print("all biases: "+str(ann.getQNeuronsBiasesAllowed(0)))
vsh=0
print("allowed weights: "+str(ann.getQAcsonsAllowed()))
print("allowed biases: "+str(ann.getQNeuronsBiasesAllowed()))
print("all weights: "+str(ann.getQAcsonsAllowed(0)))
print("all biases: "+str(ann.getQNeuronsBiasesAllowed(0)))
#
vals=ann.GetAllValsOfWeightsAndBiasesAsSingleList(1)
Q=len(vals)
print("\nVals ("+str(Q)+"):")
print(vals)
print("Vals*1000:")
for i in range(1, Q+1):
    vals[i-1]*=1000
    #vals[i-1]=vals[i-1]*1000
print(vals)
ann.SetAllWeightsAndBiasesFromSingleList(vals)
vals=ann.GetAllValsOfWeightsAndBiasesAsSingleList(1)
Q=len(vals)
print("\nVals after change ("+str(Q)+"): "+str(vals))
print("\Loss function of Forward propagation: NEW weights and biases, X="+str(X)+" teacherY= "+str(teacherY)+" : ")
err=ann.LossFunction(vals, X, teacherY, vsh)
print("allowed weights: "+str(ann.getQAcsonsAllowed()))
print("allowed biases: "+str(ann.getQNeuronsBiasesAllowed()))
print("all weights: "+str(ann.getQAcsonsAllowed(0)))
print("all biases: "+str(ann.getQNeuronsBiasesAllowed(0)))
#
print("\n\n\nTrying to learn a lesson:\n\n")
ann.LearnOneLesson(X, teacherY, vsh)
print("Finish")
        
