import copy


def ArrayLength(arr):
    count = 0
    for element in arr:
        count = count + 1
    return count

def ArrayAdd(arr, val):
    arr.append(val)
    # return arr

def ArrayIns1(arr, N, val):  # works incorrect
    print("ArrayIns1 starts working")
    print("fn received: arr=", arr)
    arr1 = []
    OldLength = ArrayLength(arr)
    NewLength = OldLength + 1
    if N >= 1 and N <= OldLength:
        count = 0
        for element in arr:
            count = count + 1
            if count == N:
                arr1.append(val)
                arr1.append(arr[count - 1])
            else:
                arr1.append(arr[count - 1])
    print("arr1=", arr1)
    arr=arr1
    print("in fn: arr=", arr)
    print("ArrayIns1 finishes working")

def ArrayIns2(arr, N, val):  # works incorrect
    print("ArrayIns2 starts working")
    arr1 = []
    OldLength = ArrayLength(arr)
    NewLength = OldLength + 1
    if N >= 1 and N <= OldLength:
        count = 0
        for element in arr:
            count = count + 1
            if count == N:
                arr1.append(val)
                arr1.append(arr[count - 1])
            else:
                arr1.append(arr[count - 1])
    print("ArrayIns2 finishes working")

def ArrayIns3(arr, N, val):  # works incorrect
    print("ArrayIns3 starts working")
    arr1 = []
    OldLength = ArrayLength(arr)
    NewLength = OldLength + 1
    if N >= 1 and N <= OldLength:
        count = 0
        for element in arr:
            count = count + 1
            if count == N:
                arr1.append(val)
                arr1.append(arr[count - 1])
            else:
                arr1.append(arr[count - 1])
    del arr[:]
    # return arr1
    print("in fn: arr1", arr1)
    arr = arr1
    print("in fn: arr", arr)
    print("ArrayIns3 finishes working")

def ArrayIns4(arr, N, val): # works well
    #print("ArrayIns4 starts working")
    arr1 = []
    OldLength = ArrayLength(arr)
    NewLength = OldLength + 1
    if N >= 1 and N <= OldLength:
        count = 0
        for element in arr:
            count = count + 1
            if count == N:
                arr1.append(val)
                arr1.append(arr[count - 1])
            else:
                arr1.append(arr[count - 1])
    del arr[:]
    # return arr1
    #print("in fn: arr1", arr1)
    for element in arr1:
        arr.append(element)
    #print("in fn: arr", arr)
    #print("ArrayIns4 finishes working")

def ArrayIns5(arr, N, val): # works well
    #print("ArrayIns5 starts working")
    OldLength = ArrayLength(arr)
    NewLength = OldLength + 1
    if N >= 1 and N <= OldLength:
        #print("arr=",arr)
        arr.append(val)
        #print("arr=", arr)
        i=N
        #while i
        for i in [N+1,NewLength]:
            #i=i+1 # uz while
            j=NewLength-i+N+1
            #print("i=", i, " j=", j, "OL=", OldLength, " NL=", NewLength)
            #print("a[", j, "]=", arr[j - 1])
            val=arr[j-1]
            #print("val=", val)
            arr[j-1]=arr[j-1-1]
            #print("a[", j, "]=", arr[j - 1])
            arr[j-1-1]=val
            #print("a[", j-1, "]=", arr[j-1-1],'=val=',val)
    arr[N-1]=val
    # return arr1
    #print("in fn: arr", arr)
    #print("ArrayIns5 finishes working")

#--------------------------------------------------------------------------------

class MyCell:
    #def __init__(self, data=""):
    #def __init__(self, data=" "):
    def __init__(self, data=0):
        self.data = data
    def __str__(self):#Vikt qes: ne works. Why?
        return str(self.data)
    def Set(self, data):
        self.data = data

#-------------------------------------------------------------------------------

class My1DArray:
    #
    def __init__(self):
        self.row = []
    #
    #def set, def get? Ma row nes private
    def Set(self, data):#ne test'd
        if isinstance(data,list):
            self.row=copy.deepcopy(data)
        else:
            element=copy.deepcopy(data)
            self.row.append(element)
    #
    def SetCells(self, data):#ne tested, ma gut
        cell=MyCell()
        if isinstance(data,list):
            L=len(data)
            for i in range(1, L+1):
                element=copy.deepcopy(data[i-1])
                if isinstance(element,MyCell):
                    cell=copy.deepcopy(element)
                else:
                    cell.Set(element)
                self.row.append(cell)#in cycle
        else:
            element=copy.deepcopy(data)
            if isinstance(element,MyCell):
                cell=copy.deepcopy(element)
            else:
                cell.Set(element)
            self.row.append(cell)#once
    #
    def GetElement(self, N=0):
        R = 0
        #Q = self.ArrayLength(self.row)
        Q=len(self.row)
        if N==0:
            N=Q
        if N >= 1 and N <= Q:
            R = self.row[N - 1]
        return R
    #
    def SetElement(self, elementExt, N=0):
        element=copy.deepcopy(elementExt)
        Q=len(self.row)
        self.row[N - 1]=element
    #
    def Add(self, elementExt, ExistingVal_Allowed0Forbidden1=0):
        element=copy.deepcopy(elementExt)
        #ArrayAdd(self.row, cell)
        N=self.Seek(element)
        if N==0 or ExistingVal_Allowed0Forbidden1==0:
            self.row.append(element)
    #
    def Del(self, N=0):
        Q=len(self.row)
        if N==0:
            N=Q
        if N >= 1 and N <= Q:
            #del self.row[N-1:N-1+1]
            del self.row[N-1:N-1+1]
    #
    def Clear(self):
        del self.row[:]
    #
    #
    #def SeekFirst(self, val, FromN=1, ToN=0):
    def SeekFirst(self, val, FromN=1):
        N=0
        Q=len(self.row)
        ToN=0
        if ToN<1 or ToN>Q:
            ToN=Q
        count=0
        #for i in range(FromN,ToN):
        for i in range(FromN,ToN+1):
            if self.row[i-1]==val:
                count=count+1
                if count==1:
                    N=i+1
                    N=i
        return N
    #
    #def SeekLast(self, val, FromN=1, ToN=0):
    def SeekLast(self, val, ToN=0):
        N=0
        Q=len(self.row)
        count=0
        FromN=1
        if ToN<1 or ToN>Q:
            ToN=Q
        #for i in range(FromN,ToN):
        for i in range(FromN,ToN+1):
            if self.row[i-1]==val:
                N=i+1
                N=i
        return N
    #
    def Seek(self, val, NLim=0, FirstNotLast=1):
        N=0
        Q=len(self.row)
        #
        if FirstNotLast==1:
            FromN=NLim
            ToN=0
        else:
            FromN=1
            ToN=NLim
        #
        if FromN<1 or FromN>Q:
            FromN=1
        if ToN<1 or ToN>Q:
            ToN=Q
        if FirstNotLast==1:
            N=self.SeekFirst(val, FromN)
        else:
            N=self.SeekLast(val, TomN)
        #
        return N
    
    #
    #
    def DelFirstElement(self, val):
        N=self.SeekFirst(val)
        if N>0:
            self.Del(N)
    #
    def DelFirstElement(self, val):
        N=self.SeekLast(val)
        if N>0:
            self.Del(N)
    #
    #
    def Swap(self, N1, N2):
        Q=len(self.row)
        if N1>=1 and N1<=Q and N2>=1 and N2<=Q:
            #print("Swapping: N1=",N1," = ",self.row[N1-1]," and N2=",N2," = ",self.row[N2-1])
            x=self.row[N1-1]
            self.row[N1-1]=self.row[N2-1]
            self.row[N2-1]=x
    #
    def Ins(self, val, N=0, ExistingVal_Allowed0Forbidden1=0):
        #print("Ins starts working")
        Q=len(self.row)
        NE=self.Seek(val)
        if N==0:
            N=Q
        if N>=1 and N<=Q and (NE==0 or ExistingVal_Allowed0Forbidden1==0):
            self.Add(val)
            #print("Adding val to end, ha:")
            #self.ShowConsole()
            Q=len(self.row)
            i=Q;
            while(i>=N+1):
                self.Swap(i-1,i)
                i=i-1
            #print("Ins finishes working")
    #
    #
    def GetLength(self):
        return len(self.row)
    #
    def ShowConsole(self):
        Q=len(self.row)
        #for i in range(1,Q):
        for i in range(1,Q+1):
            print(str(self.row[i-1]))
    #
    def Reverse(self):
        Q=len(self.row)
        if Q%2==0:
            N=Q/2
        else:
            N=(Q-1)/2
        #for N1 in range(1,N):
        for N1 in range(1,N+1):
            N2=Q-N1+1
            self.Swap(N1,N2)

#-------------------------------------------------------------------------------

class My2DArray1:
    def __init__(self):
        self.row=[]

    def Set(self, dataExt):#ne tested
        data=copy.deepcopy(dataExt)
        if isinstance(data, list):
            LE=len(data)
            if LE>0:
                for i in range(1, LE+1):
                    rowE=[]
                    if isinstance(data[i-1],list):
                        rowE=copy.deepcopy(data[i-1])
                    else:
                       rowE.append(data[i-1])
                    self.row.append(rowE)
        else:
            rowE=[]
            rowE.append(data)
            self.row.append(rowE)

    def SetCells(self, dataExt):#ne tested
        data=copy.deepcopy(dataExt)
        cell=MyCell()
        if isinstance(data, list):
            LE=len(data)
            if LE>0:
                for i in range(1, LE+1):
                    rowE=[]
                    if isinstance(data[i-1],list):
                        L=len(data[i-1])
                        for j in range(1,L+1):
                            element=copy.deepcopy(data[i-1][j-1])
                            cell.Set(element)
                            rowE.append(cell)
                    else:
                        element=copy.deepcopy(data[i-1])
                        cell.Set(element)
                        #rowE.append(data[i-1])
                        rowE.append(cell)
                    self.row.append(rowE)
        else:
            rowE=[]
            element=copy.deepcopy(data)
            rowE.append(element)
            self.row.append(rowE)

    def SetArrayOf1DArrayOfCells(self, dataExt):#ne tested, ce wi bad ob indexes ne work'tl so not sep class
        data=copy.deepcopy(dataExt)
        cell=MyCell()
        self.row=My1DArray()
        if isinstance(data, list):
            LE=len(data)
            if LE>0:
                for i in range(1, LE+1):
                    rowE=My1DArray()
                    if isinstance(data[i-1],My1DArray):
                        L=data[i-1].GetLength()
                        for j in range(1,L+1):
                            elenment=data[i-1].GetElement(j)
                            if isinstance(elenment,MyCell):
                                cell=elenment
                            else:
                                cell.Set(element)
                        #rowE=data[i-1]
                        #rowE.apend(cell)
                        rowE.Add(cell)
                    elif isinstance(data[i-1],list):
                        L=len(data[i-1])
                        for j in range(1,L+1):
                            element=copy.deepcopy(data[i-1][j-1])
                            cell.Set(element)
                            rowE.Add(cell)
                    else:
                        element=copy.deepcopy(data[i-1])
                        cell.Set(element)
                        rowE.Add(cell)
                    #self.row.append(rowE)
                    self.row.Add(rowE)
        else:
            rowE=My1DArray()
            element=copy.deepcopy(data)
            #rowE.append(element)
            rowE.Add(element)
            #self.row.append(rowE)
            self.row.Add(rowE)

    def SetElement(self, val, ExtRowN=1, IneRowN=1):
        LE=len(self.row)
        if(LE>0 and ExtRowN<=LE):
            if IneRowN<=len(self.row[ExtRowN-1]):
                self.row[ExtRowN-1][IneRowN-1]=copy.deepcopy(val)
            
    def GetElement(self, ExtRowN=1, IneRowN=1):
        return self.row[ExtRowN-1][IneRowN-1]

    def GetLength():
        return len(row)

    def GetLengthOfInnerRow(self, IneRowN=1):
        LExt=len(row)
        LIne=0
        if IneRowN>=1 and IneRowN<=LExt and LExt>0:
            LIne=len(row[IneRowN-1])
        return LIne
    #duplicate all fns of 1row ror 2 rows: for ext and inner
    def AddExtRow(self, rowExt, tornAllowed=0):
        rowP=copy.deepcopy(rowExt)
        cell=MyCell()
        rowE=[]
        LP=len(rowP)
        LE=len(self.row)
        if LE>0:
            LI=len(self.row[1-1])
        else:
            LI=0
        #
        if LP==0 and LE==0:
            zero=0#NOp
        elif LE==0 and LP>0:
            self.row.append(rowP)
        elif LE>0:
            if LP==0:
                for i in range(1, LI):
                    rowE.append(cell)
                rowP=rowE
            if(tornAllowed==0):
                if LP<LI:
                    for i in range(LP,LI):
                        rowP.append(cell)
                elif LI<LP:
                    del(rowP[LI,LP])
                #else LI==LP - NOp
            self.row.append(rowP)
    #
    def AddIneRow(self, rowExt):
        rowP=copy.deepcopy(rowExt)
        LP=len(rowP)
        LE=len(self.row)
        #cell=MyCell()
        if LE>0:
            LI=len(self.row[1-1])
        else:
            LI=0
        #
        if LE==0 and LP==0:
            zero=0#NOp
        elif LE==0 and LP>0:
            for i in range(1,LP+1):
                rowE=[]
                rowE.append(rowP[i-1])
                self.row.append(rowE)
        elif LE>0 and LP==0:
            cell=MyCell()
            rowE=[]
            for i in range (1, LE):
                rowE.append(cell)
            rowP=rowE
            for i in range(1, LP+1):
                self.rowP[i-1].append(rowP[i-1])        
        else:#both>0
            if LP<LE:
                cell=MyCell()
                for i in range(LP, LE):
                    rowP.append(cell)
            for i in range(1,LE+1):#vikt qes: qob hun LE+1?
                self.row[i-1].append(rowP[i-1])
                    
    def InsExtRow(self, rowExt, N=0, tornAllowed=0, vsh=0):
        if vsh!=0:
            print("InsExtRow Starts Working")
        rowP=copy.deepcopy(rowExt)
        LP=len(rowP)
        LE=len(self.row)
        rowR=[]
        cell=MyCell()
        if LE>0:
            LI=len(self.row[1-1])
        else:
            LI=0
        #
        #rowE=[]
        #cell=MyCell()
        if N==0:
            N=LE
        #
        if vsh!=0:
            print("N=",N," LP=",LP," LE=",LE," LI=",LI)
        #
        if LE==0 and LP==0: 
            if vsh!=0:
                print(" LE==0 and LP==0")
            if N>0:
                if vsh!=0:
                    print("N>0")
                rowE=[]
                #cell=MyCell()
                rowE.append(cell)#LI=1
                rowP=rowE
                for i in range(1,N+1):
                    self.row.append(rowP)
        elif LE>0:# and LP==0:
            if vsh!=0:
                print("LE>0")
            #if N>=1 and N<=LI:
            if N>=1 and N<=LE:#alt'd
                if vsh!=0:
                    #print("N>=1 and N<=LI")
                    print("N>=1 and N<=LE")
                if LP==0:
                    if vsh!=0:
                        print("LP==0")
                    rowE=[]
                    #cell=MyCell()
                    for i in range (1, LI+1):
                        rowE.append(cell)
                    rowP=rowE
                else:
                    if vsh!=0:
                        print("LP!=0")
                    if tornAllowed==0:
                        if vsh!=0:
                            print("tornAllowed==0")
                        if LP<LI:
                            if vsh!=0:
                                print("LP<LI")
                            for i in range (LP+1, LI+1):
                                rowE.append(cell)
                            rowP=rowE
                        elif LP>LI:
                            if vsh!=0:
                                print("LP>LI")
                            del(rowP[LI:LP])
                for i in range (1, N-1+1):#vikt qes: qob hin ne N-1+1?Anw: ja,+1
                    rowR.append(self.row[i-1])#ef ins
                rowR.append(rowP)
                #for i in range(N,LE+1+1):
                for i in range(N,LE+1):
                    #rowR.append(self.row[i-1-1])
                    rowR.append(self.row[i-1])#af ins
                self.row=rowR
        if vsh!=0:
            print("InsExtRow finishes Working")
                    
    def InsIneRow(self, rowExt, N=0, tornAllowed=0):
        rowR=[]
        rowE=[]
        rowP=copy.deepcopy(rowExt)
        LP=len(rowP)
        LE=len(self.row)
        #cell=MyCell()
        if LE>0:
            LI=len(self.row[1-1])
        else:
            LI=0
        if N==0:
            N=LE
        #
        if LE==0 and LP==0:
            zero=0#NOp
        elif LE==0 and LP>0:
            if N>0:
                for i in range(1,LP+1):
                    rowE=[]
                    cell=MyCell()
                    for j in range (1,N-1+1):
                        rowE.append(cell)
                    rowE.append(rowP[i-1])
                    self.row.append(rowE)
        elif LE>0 and LP==0:
            if N>=1 and N<=LE:
                rowE=[]
                rowR=[]
                cell=MyCell()
                for i in range(1, LI+1):
                    rowE.append(cell)
                rowP=rowE
                #LP=len(rowP)
                for i in range(1,LE+1):
                    rowE=[]
                    for j in range(1,N-1+1):
                        rowE.append(self.row[i-1][j-1])
                    rowE.append(rowP[i-1])
                    for j in range(N+1,LE+1+1):
                        rowE.append(self.row[i-1][j-1-1])
                    rowR.append(rowE)
                self.row=rowR        
        else:
            if N>=1 and N<=LE:
                for i in range(1,LE+1):
                    rowE=[]
                    for j in range(1,N-1+1):
                        rowE.append(self.row[i-1][j-1])
                    rowE.append(rowP[i-1])
                    for j in range(N+1,LE+1+1):
                        rowE.append(self.row[i-1][j-1-1])
                    rowR.append(rowE)
                self.row=rowR 
                
    def DelExtRow(self, N=0):
        LE=len(self.row)
        if N==0:
            N=LE
        if LE>0 and N>=1 and N<=LE:
            del(self.row[N-1:N+1-1])

    def DelIneRow(self,N=0):
        LE=len(self.row)
        if LE>0:
            LI=len(self.row[1-1])
        else:
            LI=0
        if N==0:
            N=LE
        #
        if LI>0 and N>=1 and N<=LI:
            LR=[]
            LI=[]
            #for i in range(1,N-1):
            for i in range(1,LE+1):
                del((self.row[i-1])[N-1:N-1+1])

    def GetExtRowN_usual(self, N):
        LE=len(self.row)
        R=[]
        if(N>=1 and N<=LE):
            R=self.row[N-1]
        return R
    
    def GetIneRowN_usual(self, N):#, IfTornLessLength_Zero0SpaceString12Cell3ExcludePositionOther=3):
        LE=len(self.row)
        LIMax=self.GetMaxLengthOfExtRow()
        R=[]
        if(N>=1 and N<=LE):
            for i in range(1,LE+1):
                LI=self.GetLengthOfExtRowN(i)
                if LI>=N:
                    R.append(self.row[i-1][N-1])
                else:
                    cell=MyCell()
                    R.append(cell)
                    #if IfTornLessLength_Zero1SpaceString2ExcludePositionOther==0:
                    #    R.append(0)
                    #elif IfTornLessLength_Zero1SpaceString2ExcludePositionOther==1:
                    #    R.append("")
                    #elif IfTornLessLength_Zero1SpaceString2ExcludePositionOther==2:
                    #    cell=MyCell()
                    #    R.append(cell)
                    #else:
                    #    zero=0#NOP
        return R

    def SetExtRow(self, rowExt, N=0, tornAllowed=0):
        rowP=copy.deepcopy(rowExt)
        LE=len(self.row)
        if N==0:
            N=LE
        LP=len(rowP)
        if LE==0 and LP==0:
            zero=0#NOp
        elif LE==0 and LP>0:
            cell=MyCell()
            for i in range(1,N-1):
                rowE=[]
                for j in range(1,LP):
                    rowE.append(cell)
                self.row.append(rowE)
            self.row.append(rowP)
        else:
            if(N>=1 and N<=LE):
                Lcur=len(self.row[N-1])
                if tornAllowed==0:
                    if LP<Lcur:
                        cell=MyCell()
                        for i in range(Lcur,LP+1):
                            rowP.append(cell)
                    elif LP>Lcur:
                        del(rowP[Lcur:LP])
                self.row[N-1]=rowP
                
    def SetIneRow(self, rowExt, N=0):
        rowP=copy.deepcopy(rowExt)
        cell=MyCell()
        LE=len(self.row)
        if N==0:
            N=LE
        LP=len(rowP)
        Lmax=GetMaxLengthOfExtRow()
        if N>=1 and N<=LE:
            if LE==0:
                if LP>0:
                    cell=MyCell()
                    for i in range(1,LP):
                        rowE=[]
                        for j in range (1, N-1):
                            rowE.append(cell)
                        rowE.append(rowP[i-1])
                        self.row.append(rowE)
                 #else NOp       
            else:
                for i in range (1,LE+1):
                    Lcur=len(self.row[i-1])
                    if Lcur>=N:
                        if LP>0:
                            self.row[i-1][N-1]=rowP[i-1]
                        else:
                            self.row[i-1][N-1]=cell
                    else:#Lcur<N
                        if LP>0:
                            for j in range (Lcur+1,N-1+1):
                                self.row[i-1].append(cell)
                            self.row[i-1].append(rowP[i-1])
                        else:
                            for j in range (Lcur+1,N+1):
                                self.row[i-1].append(cell)
                   
    def GetLengthOfIneRow(self):
         return len(self.row)

    def GetLengthOfExtRowN(self, N):
        R=0
        LE=len(self.row)
        if N>=1 and N<=LE:
            R=len(self.row[N-1])
        return R

    def __GetExtremeLengthOfExtRow(self, Max0Minther=0):
        R=0
        LE=len(self.row)
        if(LE>0):
            #MinL=self.row[1-1]
            #MaxL=self.row[1-1]
            for i in range(1,LE+1):
                if isinstance(self.row[i-1],list):
                    L=len(self.row[i-1])
                else:
                    L=1#L=0
                if i==1 or (i>1 and MinL>L):
                    MinL=L
                if i==1 or (i>1 and MaxL<L):
                    MaxL=L
            if Max0Minther==0:
                R=MaxL
            else:
                R=MinL
        return R

    def GetMaxLengthOfExtRow(self):
        return self.__GetExtremeLengthOfExtRow()

    def GetMinLengthOfExtRow(self):
        return self.__GetExtremeLengthOfExtRow(1)

    def SetBySingleExtRow(self, rowExt):
        self.row=[]
        rowP=copy.deepcopy(rowExt)
        LP=len(rowP)
        if LP>0:
            self.row.append(rowP)

    def SetBySingleIneRow(self, rowExt):
        self.row=[]
        rowP=copy.deepcopy(rowExt)
        LP=len(rowP)
        if LP>0:
            for i in range(1,LP+1):
                self.row.append(rowP[i-1])

    def MakeRectTo(self, ifNonRectangular_CutToMin1StretchToMax2=1):
        rowR=[]
        cell=MyCell()
        #rowE=[]
        MinL=self.GetMinLengthOfExtRow()
        MaxL=self.GetMaxLengthOfExtRow()
        LE=len(self.row)
        if LE>0 and MinL!=MaxL:
            for i in range(1,LE+1):
                rowE=self.row[i-1]
                #if isinstance(self.row[i-1],list):
                #    Lcur=len(self.row[i-1])
                #else:
                #    Lcur=1
                Lcur=len(self.row[i-1])
                if Lcur>MinL:
                    rowE=copy.deepcopy(self.row[i-1])
                    if ifNonRectangular_CutToMin1StretchToMax2==1:
                        del(rowE[MinL+1:Lcur])
                elif ifNonRectangular_CutToMin1StretchToMax2==2:
                    for j in range(Lcur+1, MaxL+1):
                        rowE.append(cell)
                        #rowE.append("cell")
                rowR.append(rowE)
        else:
            rowR=self.row
        return rowR

    def Transpose(self, ifNonRectangular_Nil0CutToMin1StretchToMax2=0):
        rowR=[]
        MinL=self.GetMinLengthOfExtRow()
        MaxL=self.GetMaxLengthOfExtRow()
        LE=len(self.row)
        if LE==0 or (LE>0 and MinL!=MaxL and ifNonRectangular_Nil0CutToMin1StretchToMax2==0):
            rowR=self.row
        else:
            modContentRect=self.MakeRectTo(ifNonRectangular_Nil0CutToMin1StretchToMax2)
            LI=len(modContentRect[1-1])
            for i in range(1, LI+1):
                rowE=[]
                for j in range(1, LE+1):
                    rowE.append(modContentRect[j-1][i-1])#1
                rowR.append(rowE)
        self.row=rowR

    def TransposeTo(self, ifNonRectangular_Nil0CutToMin1StretchToMax2=0):
        #ini=self.MakeRectTo(ifNonRectangular_Nil0CutToMin1StretchToMax2)
        rowR=[]
        MinL=self.GetMinLengthOfExtRow()
        MaxL=self.GetMaxLengthOfExtRow()
        LE=len(self.row)
        if LE==0 or (LE>0 and MinL!=MaxL and ifNonRectangular_Nil0CutToMin1StretchToMax2==0):
            rowR=self.row
        else:
            modContentRect=self.MakeRectTo(ifNonRectangular_Nil0CutToMin1StretchToMax2)
            LI=len(modContentRect[1-1])
            for i in range(1, LI+1):
                rowE=[]
                for j in range(1, LE+1):
                    rowE.append(modContentRect[j-1][i-1])#1
                rowR.append(rowE)
        return rowR
                            
    def Stretch(self, L=0):#StretchToMinLengthTo #vikt: not tested, us'tc self=StretchTo
        cell=MyCell()
        LE=len(self.row)
        MinL=self.GetMinLengthOfExtRow()
        MaxL=self.GetMaxLengthOfExtRow()
        if L==0:
            L=MaxL
        if MinL<L:
            for i in range(1,LE+1):
                #rowE=[]
                #if(isinstance(C[i-1],list)):
                #    rowE
                #else:
                #    rowE=copy.deepcopy(C[i-1])
                rowE=copy.deepcopy(C[i-1])
                LCur=len(rowE)
                if(LCur<L):
                    for j in range(LCur+1, L+1):
                        rowE.append(cell)
                    self.row[i-1]=copy.deepcopy(rowE)

    def StretchTo(self, L=0):#StretchToMinLengthTo
        cell=MyCell()
        C=self.row
        LE=len(self.row)
        MinL=self.GetMinLengthOfExtRow()
        MaxL=self.GetMaxLengthOfExtRow()
        if L==0:
            L=MaxL
        if MinL<L:
            for i in range(1,LE+1):
                rowE=copy.deepcopy(C[i-1])
                LCur=len(rowE)
                if(LCur<L):
                    for j in range(LCur+1, L+1):
                        rowE.append(cell)
                    C[i-1]=copy.deepcopy(rowE)
        return C
        
    #def SwapExtRowsTo(self, N1, N2):
    #    C=self.row
    #    LE=len(self.row)
    #    if LE>0 and N1>=1 and N2>=1 and N1<=LE and N2<NE:
    #        TR=copy.deepcopy(C[N1-1])
    #        C[N1-1]=copy.deepcopy(C[N2-1])
    #       C[N2-1]=copy.deepcopy(TR)
    #    return C

    def SwapCells(self, ExtRowN1, IneRowN1, ExtRowN2, IneRowN2):
        LE=len(self.row)
        if LE>0:
            maxL=self.GetMaxLengthOfExtRow()
            minL=self.GetMinLengthOfExtRow()
            L1=self.GetLengthOfExtRowN(ExtRowN1)
            L2=self.GetLengthOfExtRowN(ExtRowN2)
            if IneRowN1>=1 and IneRowN1<=L1 and IneRowN2>=1 and IneRowN2<=L2:
                buf=copy.deepcopy(self.row[ExtRowN1-1][IneRowN1-1])
                self.row[ExtRowN1-1][IneRowN1-1]=copy.deepcopy(self.row[ExtRowN2-1][IneRowN2-1])
                self.row[ExtRowN2-1][IneRowN2-1]=copy.deepcopy(buf)

    def SwapExtRows(self, N1, N2):
        LE=len(self.row)
        if LE>0 and N1>=1 and N2>=1 and N1<=LE and N2<=LE:
            r=copy.deepcopy(self.row[N1-1])
            self.row[N1-1]=copy.deepcopy(self.row[N2-1])
            self.row[N2-1]=copy.deepcopy(r)
        
    def SwapIneRows(self, N1, N2, ifTornAndNotFullRow_Refuse0Stretch1=0):
        LE=len(self.row)
        maxL=self.GetMaxLengthOfExtRow()
        minL=self.GetMinLengthOfExtRow()
        CondCorrectPosition=(LE>0 and N1>=1 and N2>=1 and N1<=maxL and N2<=maxL)
        CondAllowedToExchangeRows=((N1<=minL and N2<=minL) or ifTornAndNotFullRow_Refuse0Stretch1==1)
        if CondCorrectPosition and CondAllowedToExchangeRows:
            if N1>minL:
                self.row=self.StretchTo(N1)
            if N2>minL:
                self.row=self.StretchTo(N2)
            for i in range(1,LE+1):
                self.SwapCells(i, N1, i, N2)

    #def SwapIneRowsTo(self, N1, N2, ifTornAndNotFullIneRow_Refuse0Stretch1=0):
    #    rowR=self.row
    #    LE=len(self.row)
    #    maxL=self.GetMaxLengthOfExtRow()
    #    #minL=self.GetMinLengthOfExtRow()
    #    L1=self.GetLengthOfExtRowN(N1)
    #    L2=self.GetLengthOfExtRowN(N2)
    #    CondCorrectPosition=(LE>0 and N1>=1 and N2>=1 and N1<=maxL and N2<=maxL)
    #    CondAllowedToExchangeRows=(L1==L2 or ifTornAndNotFullIneRow_Refuse0Stretch1==1)
    #    if CondCorrectPosition and CondAllowedToExchangeRows:
    #        if L1<L2:
    #            self.row=self.StretchTo(L2)
    #        elif L2<L1:
    #            self.row=self.StretchTo(L1)
    #        rowR=[]
    #        for i in range(1,LE):
    #            rowE=[]
    #            curL=self.GetLengthOfExtRowN(i)
    #            for j in range(1,curL):
    #                if j==N1:
    #                    rowE.append(self.row[i-1][N2-1])
    #                elif j==N2:
    #                   rowE.append(self.row[i-1][N1-1])
    #                else:
    #                    rowE.append(self.row[i-1][j-1])
    #            rowR.append(rowE)
    #    return rowR

    def OrderVisaVersaExtRows(self):
        LE=len(self.row)
        if LE>0:
            if LE%2==0:
                N=LE/2
            else:
                N=(LE-1)/2
            for i in range(1,N+1):
                N1=i
                N2=LE-N1+1
                #print("Swapping: rows ", N1, " and ",N2," of ",LE)
                self.SwapExtRows(N1,N2)
        
    #def OrderVisaVersaExtRowN(self, N):
    #    print("OrderVisaVersaExtRowN starts working "+str(N))
    #    LE=len(self.row)
    #    if LE>0:
    #        L=self.GetLengthOfExtRowN(N)
    #        if(N>=1 and N<=L):
    #            if L%2==0:
    #                n=L/2
    #            else:
    #                n=(L-1)/2
    #            for i in range(1,n+1):
    #               N1=i
    #                N2=L-i+1
    #                print("swapping: (",N1,") = ",self.row[i-1][N1-1]," and ",N2,") = ",self.row[i-1][N2-1])
    #                self.SwapCells(N, N1, N, N2)
    #    print("OrderVisaVersaExtRowN finishes working")

    def OrderVisaVersaExtRowN(self, N):
        LE=len(self.row)
        if LE>0 and N>=1 and N<=LE:
            L=self.GetLengthOfExtRowN(N)
            if L%2==0:
                n=L/2
            else:
                n=(L-1)/2
            for i in range(1,n+1):
                N1=i
                N2=L-i+1
                self.SwapCells(N, N1, N, N2)
        
    def OrderVisaVersaIneRowN(self, N, ifTornAndNotFullIneRow_Refuse0EachRowSeparately12Stretch2=0):
        LE=len(self.row)
        if LE>0:
            maxL=self.GetMaxLengthOfExtRow()
            minL=self.GetMinLengthOfExtRow()
            if N<maxL:
                if ifTornAndNotFullIneRow_Refuse0EachRowSeparately12Stretch2!=0:
                    if N<maxL and ifTornAndNotFullIneRow_Refuse0EachRowSeparately12Stretch2==2:
                        self.StretchTo(maxL)
                    if LE%2==0:
                        n=LE/2
                    else:
                        n=(LE-1)/2
                    for i in range(1, n+1):
                        N1=i
                        N2=LE-i+1
                        self.SwapCells(N1, N, N2, N)
                        
    def OrderVisaVersaIneRows(self, ifTornAndNotFullIneRow_Refuse0EachRowSeparately12Stretch2=2):
        LE=len(self.row)
        maxL=self.GetMaxLengthOfExtRow()
        minL=self.GetMinLengthOfExtRow()
        if LE>0:
            if minL!=maxL and  ifTornAndNotFullIneRow_Refuse0EachRowSeparately12Stretch2==0:
                zero=0
            else:
                if minL!=maxL and ifTornAndNotFullIneRow_Refuse0EachRowSeparately12Stretch2==2:
                    self.StretchTo(maxL)
                for i in range(1,LE+1):
                    #print("swaping row ",i)
                    self.OrderVisaVersaExtRowN(i)
                    
    def ShowConsole(self, sep=" "):
        curLine=""
        LE=len(self.row)
        if LE==0:
            curLine="Empty"
            print(curLine)
        #if LE>0:
        #    LI=len(self.row[1-1])
        #else:
        #    LI=0
        for i in range(1, LE+1):
            curLine=""
            LI=len(self.row[i-1])
            for j in range(1, LI): 
                curLine=curLine+str(self.row[i-1][j-1])
                curLine=curLine+sep
            curLine=curLine+str(self.row[i-1][LI-1])
            print(curLine)

    

class Table:
    def __init__(self):
        self.Content=[]
        self.LineOfColHeader=[]
        self.ColOfLineHeader=[]
        self.LC_0_CL_1=0
        self.TableHeader=[]
        self.LinesGeneralHeader=[]
        self.ColumnsGeneralHeader=[]
        self.tornAllowed=0

    def SetNull(self):
        self.Content=[]
        self.LineOfColHeader=[]
        self.ColOfLineHeader=[]
        self.LC_0_CL_1=0
        self.TableHeader=[]
        self.LinesGeneralHeader=[]
        self.ColumnsGeneralHeader=[]
        self.tornAllowed=0

    def SetNullContent(self):
        Content=[]

    def SetNullLineOfColHeader(self):
        LineOfColHeader=[]

    def SetNullColOfLineHeader(self):
        ColOfLineHeader=[]   
        
    def Set(self, ContentRowsExt, LineOfColHeader=[], ColOfLineHeader=[], TableHeader=[], LinesGeneralHeader=[], LColumnsGeneralHeader=[], toGet_LC_0_CL_1=0, toSet_LC_0_CL_1=0, tornAllowed=0, NullMeansLeaveUnchanged1Del0=1):
        rowE=[]
        #self.row=[]
        self.row=My2DArray1()
        cell=MyCell()
        #ContentRows=copy.deepcopy(ContentRowsExt)
        ContentRows=My2DArray1()
        ContentRows.SetCells(ContentRowsExt)#so now ce guaranteed 1) D array, 2) of cells - even if it s' 1 row or 1 cell
        #ma ce ne gut ob cell is not Cell!
        extLE=len(ContentRows)
        if extLE==0:
            if len(self.row)>0 and NullMeansLeaveUnchanged1Del0==0:
                #self.row=[]
                self.row=My2DArray1()
            #else NOp
        else: #if possible to work
            minL=ContentRows.GetMinLengthOfExtRow()
            maxL=ContentRows.GetMaxLengthOfExtRow()
            #table ms'b rect'l! Mer, abl, not to transpose
            if(minL!=maxL):
                ContentRows.Stretch(maxL)
            #if to transpse - stretch to max
            if MinL!=MaxL and toGet_LC_0_CL_1!=toSet_LC_0_CL_1:
                for i in range(1, extLE+1):
                    Lcur=len(ContentRows[i-1])
                    rowE=[]
                    if Lcur<MaxL:
                        rowE=copy.deepcopy(ContentRows[i-1])
                        for j in range(Lcur+1, extLE+1):
                            rowE.append(suplCell)
                        ContentRows[i-1]=copy.deepcopy(rowE)
            #    
            if toGet_LC_0_CL_1==0:
                QLinesToGet=len(ContentLines)
                if tornAllowed==0 or MinL==MaxL:
                    QColumnsToGet=MinL
                else:
                    QColumnsToGet=-1
                if (toSet_LC_0_CL_1==0):#LC_CL == LC_CL
                    QLines=QLinesToGet
                    QColumns=QColumnsToGet
                    if MinL==MaxL or tornAllowed!=0:
                        self.row=ContentRows
                    else:
                        for i in range(1,QLines+1):
                            rowE=[]
                            if(isinstance(ContentRows[i-1],list)):
                                Lcur=len(ContentRows[i-1])
                                for j in range(1,Lcur):
                                    rowE.append(ContentRows[i-1][j-1])
                            else:
                                Lcur=1
                                rowE.append(ContentRows[i-1])
                            self.row.append(rowE)
                else:#LC_CL != LC_CL
                    QLines=QColumnsToGet
                    QColumns=QLinesToGet
                    if MinL==MaxL or tornAllowed!=0:
                        for i in range(1,QLines+1):
                            rowE=[]
                            if(isinstance(ContentRows[i-1],list)):
                                Lcur=len(ContentRows[i-1])
                                for j in range(1,Lcur+1):
                                    rowE.append(ContentRows[j-1][i-1])
                            else:
                                Lcur=1
                                rowE.append(ContentRows[i-1])
                                self.row.append(rowE)
                    #else NOp: non-rectangular table can't be transposed, such situazs sl'be avoided
            
        
            
                
