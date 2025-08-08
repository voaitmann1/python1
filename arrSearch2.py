import copy

def arr1D_ConstructFilling(val, Q):
    y=[]
    for i in range(1, Q+1):
        y.append(val)
    #
    return y
#

class TShiftData:
    def __init__(self):
        self.FromN=1
        self.QDefaultBefore=0
        self.QReq=-1
    #
#

class TArr1DExtractStruct:
    def __init__(self):
        self.PrevN1=0
        self.PrevN2=0
        self.OwnN1=0
        self.OwnN2=0
        self.ForOwnN1=0
        self.ForOwnN2=0
        self.PostN1=0
        self.PostN2=0
        self.Qreal=0
        self.PrevN12=0
        self.PostN12=0
    #
    def Calc1(self, Qexisting, QDefaultsBefore=0, FromN=1, Qreq=-1):
        Qbefore=0
        Qrest=0
        Qpost=0
        if FromN<0:
            FromN+=(Qexisting+1)
        #
        if FromN<Qexisting:
            QOwnLeftMax=Qexisting-FromN+1
            QOwnLeft=QOwnLeftMax
        else:
            QOwnLeft=0
        #
        if QDefaultsBefore>0:
            self.PrevN1=1
        #
        if Qreq<0:
            if QDefaultsBefore>0:
                Qbefore=QDefaultsBefore
                #self.PrevN2=QDefaultsBefore
            #
            if FromN<=Qexisting:
                self.Qreal=QDefaultsBefore+QOwnLeftMax
            else:
                QOwnLeft=0
                self.Qreal=QDefaultsBefore
             #
        else:
            if Qreq>0 and QDefaultsBefore>Qreq:
                Qbefore=Qreq
            else:
                Qbefore=QDefaultsBefore
                #
                if FromN<=Qexisting:
                    Qrest=Qreq-QDefaultsBefore
                    if Qrest>QOwnLeftMax:
                        QOwnLeft=QOwnLeftMax
                        Qpost=Qrest-QOwnLeft
                    else:
                        QOwnLeft=Qrest
                        Qpost=0
                    #
                else:
                    if Qreq>QDefaultsBefore:
                        Qpost=Qreq>QDefaultsBefore
                    #
                #
            #
        #
        if Qbefore>0:
            self.PrevN1=1
            self.PrevN2=PrevN1-1+Qbefore
        #
        if QOwnLeft>0:
            self.OwnN1=FromN
            self.ForOwnN1=self.PrevN2+1
            self.OwnN2=self.OwnN1-1+QOwnLeft
            self.ForOwnN1=self.ForOwnN1-1+QOwnLeft
        #
        if Qpost>0:
            self.PostN1=self.ForOwnN2+1
            self.PostN2=self.PostN1-1+Qpost
        # 
    #fn
    def Calc1(self, ShiftData, Qexisting):
        if isinstance(ShiftData, TShiftData):
            QDefaultsBefore=ShiftData.QDefaultsBefore
            FromN=ShiftData.FromN
            Qreq==ShiftData.Qreq
        else:
            QDefaultsBefore=0
            FromN=1
            Qreq=-1
        #
        self.Calc1(ShiftData, Qexisting, QDefaultsBefore, FromN, Qreq)
    #
    def Calc2(self, QFromNew, QExisting1, QDefaultsBefore=0, FromN=1, Qreq=-1):
        self.Calc1(QFromNew, QDefaultsBefore, FromN, Qreq)
        if self.PrevN2>0 and self.PrevN2>QExisting1:
            self.PrevN12=QExisting1
        elif self.PostN2>0 and self.PostN2>QExisting1:
            self.PostN12=QExisting1
        #if
    #
    def Calc2(self, ShiftData, QFromNew, QExisting1, ):
        if isinstance(ShiftData, TShiftData):
            QDefaultsBefore=ShiftData.QDefaultsBefore
            FromN=ShiftData.FromN
            Qreq==ShiftData.Qreq
        else:
            QDefaultsBefore=0
            FromN=1
            Qreq=-1
        #
        self.Calc2(QFromNew, QExisting1, QDefaultsBefore, FromN, Qreq)
    #
#cl

def arr1D_GetSubArr(arr1D, dataDefault=0, QDefaultsBefore=0, FromN=1, Qreq=-1, defaultRest=0):
    y=[]
    dataMarkup=TArr1DExtractStruct()
    if isinstance(arr1D, list):
        L1=len(arr1D)
        if isinstance(dataDefault, list):
            L2=len(dataDefault)
            dataMarkup.Calc1(Qexisting, QDefaultsBefore, FromN, Qreq)
            if dataMarkup.PrevN2>0:
                if dataMarkup.PrevN12>0:
                    for i in range(1, dataMarkup.PrevN12+1):
                        y.append(dataDefault[i-1])
                    #
                    for i in range(dataMarkup.PrevN12+1, dataMarkup.PrevN2+1):
                        y.append(defaultRest)
                    #
                else:
                   for i in range(1, dataMarkup.PrevN2+1):
                        y.append(dataDefault[i-1])
                    #
                #
            #
            if dataMarkup.OwnN2>0:
                for i  in range(dataMarkup.OwnN1, dataMarkup.OwnN2+1):
                    y.append(arr1D[i-1])
                #
            #
            if dataMarkup.PostN2>0:
                if dataMarkup.PostN12>0:
                    if dataMarkup.PostN12<dataMarkup.PostN1:
                        for i in range(1, dataMarkup.PostN12+1):
                            y.append(dataDefault[i-1])
                        #
                        for i in range(dataMarkup.PostN12+1, dataMarkup.PostN2+1):
                            y.append(defaultRest)
                        #
                    else:
                        for i in range(dataMarkup.PostN1, dataMarkup.PostN2+1):
                            y.append(defaultRest)
                        #
                else:#dataMarkup.PostN12==0:
                   for i in range(1, dataMarkup.PostN2+1):
                        y.append(dataDefault[i-1])
                    #
                #
            #
        else:
            dataMarkup.Calc1(Qexisting, QDefaultsBefore, FromN, Qreq)
            if dataMarkup.PrevN2>0:
                for i in range (dataMarkup.PrevN1, dataMarkup.PrevN2+1):
                    y.append(dataDefault)
                #
            #
            if dataMarkup.OwnN2>0:
                for i in range (dataMarkup.OwnN1, dataMarkup.OwnN2+1):
                    y.append(arr1D[i-1])
                #
            #
            if dataMarkup.PostN2>0:
                for i in range (dataMarkup.PostN1, dataMarkup.PostN2+1):
                    y.append(dataDefault)
                #
            #
        #
    #else NOp
    return y
#

def arr1D_GetSubArr(arr1D, ShiftData, dataDefault=0, defaultRest=0):
    if isinstance(ShiftData, TShiftData):
        QDefaultsBefore=ShiftData.QDefaultsBefore
        FromN=ShiftData.FromN
        Qreq=ShiftData.Qreq
    else:
        QDefaultsBefore=0
        FromN=1
        Qreq=-1
    #
    return arr1D_GetSubArr(arr1D, dataDefault, QDefaultsBefore, FromN, Qreq, defaultRest)
#

def arr1D_GetSubArr_Ns(arr1D, N1, N2, dfltVal="", ifNotInRange_Defaults1No0=0):
    y=[]
    if isinstance(arr1D, list) or isinstance(arr1D, str):
        Q=len(arr1D)
        if N1<0:
            N1+=(Q+1)
        #
        if N2<0:
            N2+=(Q+1)
        #
        if N1<=N2:
            if N1<0:
                if ifNotInRange_Defaults1No0==1:
                    if N2<0:
                        for i in range(-N2, -N1+1):
                            y.append(dfltVal)
                        #
                    else:#
                        if N2<=Q:
                            for i in range(1, N2+1):
                                y.append(arr1D[i-1])
                            #
                        else:
                            for i in range(1, Q+1):
                                y.append(arr1D[i-1])
                            #
                            for i in range(Q+1, N2+1):
                                y.append(dfltVal)
                            #
                        #
                    #
                else:
                    y=[]
            else:#N1>0
                if N1>Q:
                    for i in range(N1, N2+1):
                        y.append(dfltVal)
                    #
                else:
                    if N2<=Q:
                        for i in range(N1, N2+1):#NORM!
                            y.append(arr1D[i-1])
                        #
                    else:
                        for i in range(N1, Q+1):
                            y.append(arr1D[i-1])
                        #
                        for i in range(Q+1, N2+1):
                            y.append(dfltVal)
                        #
                    #
                #
            #
        else:#N1>N2, N2<N1
            if N1>=1 and N1<=Q and N2>=1 and N2<=Q:#NORM!
                for i in range(N2, N1+1):
                    N=Q-i+1
                    val=arr1D[N-1]
                    y.append(val)
                #
            else:#no matter val of ifNotInRange_Defaults1No0!
                pass
            #
        #
    #
    return y
#
            
                            
           
            

def arr1D_add(arr1D, val):
    if isinstance(arr1D, list):
        arr1D.append(val)
    #
#   return arr1D
#

#def arr1D_ShiftFromStartTowardsEndTillN(arr1D, N):
#    Q=len(arr1D)
#    #val=arr1D[N-1]
#    if N<0:
#       N+=(Q+1)
#    #
#    if N>=1 and N<=Q:
#        for i in range(1, Q-1+1):
#            j=Q-i+1
#            arr1D[j+1-1]=copy.deepcopy(arr1D[j-1])
#        #
#        arr1D[1-1]=val
##    return arr1D
#

#def arr1D_ShiftToStart(arr1D):
#    Q=len(arr1D)
#    val=arr1D[1-1]
#    for i in range(1, Q-1+1):
#        arr1D[i-1]=copy.deepcopy(arr1D[i+1-1])
#    #
#    arr1D[Q-1]=val
##    return arr1D
#

def arr1D_swapVals(arr1D, N1, N2):
    if isinstznce(arr1D, list):
        Q=len(arr1D)
        if N1<0:
            N1+=(Q+1)
        #
        if N2<0:
            N2+=(Q+1)
        #
        if N1>=1 and N1<=Q and N2>=1 and N2<=Q:
            buf=arr1D[N1-1]
            arr1D[N1-1]=arr1D[N2-1]
            arr1D[N2-1]=buf
        #
    #
    #return arr1D
#

def arr1D_reverse(arr1D):
    y=[]
    if isinstance(arr1D, list):
        L=len(arr1D)
        for i in range(1, L+1):
            N=L-i+1
            val=arr1D[L-1]
            y.append(val)
        #
    #
    return y
#
                

def arr1D_insert(arr1D, val, N=-1):
    if isinstznce(arr1D, list):
        Q=len(arr1D)
        if N<0:
           N+=(Q+1)
        #
        if N>=1 and N<=Q:
            arr1D.append(val)
            for i in range(N+1, Q+1+1):
                j=Q+1-i+1
                arr1D_swapVals(arr1D, j, j-1)
            #
        #
    #
    #return arr1D
#
            
def arr1D_SeekVal(arr1D, val):
    Ns=[]
    Q=0
    if isinstance(arr1D, list) or isinstance(arr1D, str):
        Q=len(arr1D)
        for N in range(1, Q+1):
            if arr1D[N-1]==val:
                Ns.append(N)
            #
        #
    #
    return Ns
#
def arr1D_SeekValsFirstN(arr1D, val):
    Ns=arr1D_SeekVal(arr1D, val)
    N=0
    if len(Ns)>0:
        N=Ns[1-1]
    #
    return N
#

def arr1D_arr1DIsInArr1DAtPosN(where, what, N, whatIsReversed=0, param=0):
    verdict=1
    if isinstance(where, list) and isinstance(where, list):
        whereL=len(where)
        whatL=len(what)
        if whatIsReversed==0:
            if N>=1 and N-1+whatL<=whereL:
                for i in range(1, whereL):
                    whatCurN=i
                    whereCurN=N+i-1
                    if where[whereCurN-1]!=what[whatCurN-1]:
                        verdict=0
            else:
                verdict=0
        else:#whatIsReversed
            if N<=whereL and N-whatL+1>=1:
                for i in range(1, whatL+1):
                    whatCurN=i
                    whereCurN=N-i+1
                    if where[whereCurN-1]!=what[whatCurN-1]:
                        verdict=0
            else:
                verdict=0
            #
        #
    else:
        verdict=0
    #
    return verdict

def arr1D_SeekArr1D(where, what, whatIsReversed=0, param=0):
    R=[]
    if isinstance(where, list) and isinstance(where, list):
        whereL=len(where)
        for N in range(1, whereL+1):
            if arr1D_arr1DIsInArr1DAtPosN(where, what, N, whatIsReversed, param)==1:
                R.append(N)
            #
        #
    #
    return R
#

#===========================================================================================================

def arr2D_isArr2D(arr2D, extRowOfArr2DMayBe_NonList=0, extRowOfArr2DMayBe_EmptyList=0):
    verdict=1
    Q=0
    if not isinstance(arr2D, list):
        verdict=0
    else:
        Q=len(arr2D)
        for i in range(1, Q+1):
            if arr2D[i-1]==[] and extRowOfArr2DMayBe_EmptyList!=1:
                verdict=0
            elif extRowOfArr2DMayBe_NonList!=1 and not(isinstance(arr2D[i-1], list)):
                verdict=0
            #
        #
    #
    return verdict
#

def arr2D_GetLengthes(arr2D, N_if0OrMoreThanLength_NotConcreteLAndExtremeLsButAllLs=-1, extRowOfArr2DMayBe_NonList=0, extRowOfArr2DMayBe_EmptyList=0):
    Ls=[]
    Lmin=0
    Lmax=0
    LoN=-1
    if arr2D_isArr2D(arr2D, extRowOfArr2DMayBe_NonList, extRowOfArr2DMayBe_EmptyList):
        QER=len(arr2D)
        if(N_if0OrMoreThanLength_NotConcreteLAndExtremeLsButAllLs<0):
            N_if0OrMoreThanLength_NotConcreteLAndExtremeLsButAllLs+=(QER+1)
        #
        for i in range(1, QER+1):
            L=len(arr2D[i-1])
            Ls.append(L)
            if i==1 or (i>1 and L>Lmax):
                Lmax=L
            #
            if i==1 or (i>1 and L<Lmin):
                Lmin=L
            #
        #
        if(N_if0OrMoreThanLength_NotConcreteLAndExtremeLsButAllLs>=1 and N_if0OrMoreThanLength_NotConcreteLAndExtremeLsButAllLs<=QER):
            Ls=[]
            LoN=len(arr2D[N_if0OrMoreThanLength_NotConcreteLAndExtremeLsButAllLs-1])
            Ls.append(LoN)
            Ls.append(Lmin)
            Ls.append(Lmax)
        #    
    #
    return R
#

def arr2D_isForTranspose(arr2D):
    Ls=[]
    QER=0
    verdict=arr2D_isArr2D(arr2D)
    if verdict==1:
        QER=len(arr2D)
        Ls=arr2D_GetLengthes(arr2D, 0)
        for i in range(1, QER-1+1):
            Lprev=len(arr2D[i-1])
            Lnext=len(arr2D[i+1-1])
            if Lprev<Lnext:
                verdict=0
            #
        #
    #
    return verdict
#
            
def arr2D_GetVal(arr2D, ExtRowN, IneRowN):
    val=[]
    Ls=[]
    if arr2D_arr2D_isArr2D(arr2D)==1:
        QER=len(arr2D)
        Ls=arr2D_GetLengthes(arr2D, -1)
        if(ExtRowN<0):
            ExtRowN+=(QER+1)
        #                                
        if ExtRowN>=1 and ExtRowN<=QER:
            L=len(arr2D[ExtRowN-1])
            if(IneRowN<0):
                IneRowN+=(L+1)
            #
            if IneRowN>=1 and IneRowN<=Ls[ExtRowN-1]:
                val=arr2D[ExtRowN-1][IneRowN-1]
            #
        #
    #
    return val
#    

def arr2D_getIneRowN(arr2D, N, ifN_GT_Lmin_ignore0FillByDefaultVal1=1, defaultVal=0):
    row=[]
    if arr2D_isArr2D(arr2D)==1:
        minL=arr2D_GetLengthMin(arr2D)
        maxL=arr2D_GetLengthMax(arr2D)
        Q=len(arr2D)
        if N>=1 and N<=maxL:
            if N<=minL:
                for i in range(1, Q+1):
                    val=copy.deepcopy(arr2D[i-1][N-1])
                    #row.append(arr2D[i-1][N-1])
                    row.append(val)
            else:
                if ifN_GT_Lmin_ignore0FillByDefaultVal1==1:
                    for i in range(1, Q+1):
                        curL=len(arr2D[i-1])
                        if curL<=minL:
                            val=copy.deepcopy(arr2D[i-1][N-1])
                            #row.append(arr2D[i-1][N-1])
                            row.append(val)
                        else:
                            row.append(defaultVal)
    return row

def arr2D_CoordsTransform(arr2D, whereExtRowN, whereIneRowN, whatExtRowN, whatIneRowN, isTransposed=0, ExtRowsSuccIsReversed=0, EachExtRowIsReversed=0):
    Ls=arr2D_GetLengthes(arr2D, -1)
    if isTransposed==0:
        if ExtRowsSuccIsReversed==0:
            if eachExtRowIsReversed==0:
                # 11 12 13
                # 21 22 23
                # 31 32 33
                soughtExtRowN=whereExtRowN+whatExtRowN-1
                soughtIneRowN=whereIneRowN+whatIneRowN-1
            else:#eachExtRowIsReversed==1:
                # 13 12 11
                # 23 22 21
                # 33 32 31
                #
                # 15 14 13 12 11
                # 25 24 23 22 21
                # 35 34 33 32 31
                # 45 44 34 42 41
                # 55 54 53 52 51
                # 65 64 63 62 61
                #where (2,2)
                #what (4,3)
                #where no changes: (5,4)
                #where with changes: (5,2)
                soughtExtRowN=whereExtRowN+whatExtRowN-1#2+4-1=5
                soughtIneRowN=QIneRowsWhere-(whereIneRowN+whatIneRowN-1)+1#5-(2+3-1)+1=5-4+1=2
            #
        else:#ExtRowsSuccIsReversed==1:
            if eachExtRowIsReversed:
                # 31 32 33
                # 21 22 23
                # 11 12 13
                #
                # 61 62 63 64 65
                # 51 52 53 54 55
                # 41 42 43 44 45
                # 31 32 33 34 35
                # 21 22 23 24 25
                # 11 12 13 14 15
                #where (2,2)
                #what (4,3)
                #where no changes: (5,4)
                #where with changes: (2,4)
                soughtExtRowN=QExtRowsWhere-(whereExtRowN+whatExtRowN-1)+1#6-(2+4-1)+1=6-5+1=2
                soughtIneRowN=whereIneRowN+whatIneRowN-1#2+3-1=4# 
            else:#eachExtRowIsReversed==1:
                # 33 32 31
                # 23 22 21
                # 13 12 11
                #
                # 65 64 63 62 61
                # 55 54 53 52 51
                # 45 44 43 42 41
                # 35 34 33 32 31
                # 25 24 23 22 21
                # 15 14 13 12 11
                #where (2,2)
                #what (4,3)
                #where no changes: (5,4)
                #where with changes: (2,2)
                soughtExtRowN=ExtRowsWhere-(whereExtRowN+whatIneRowN-1)+1#6-(2+4-1)+1=5-5+1=2
                soughtIneRowN=IneRowsWhere-(whereIneRowN+whatIneRowN-1)+1#5-(2+3-1)+1=5-4+1=2
            #
        #
    else:#isTransposed==1:
        if ExtRowsSuccIsReversed==0:
            if eachExtRowIsReversed==0:
                # 11 21 31
                # 12 22 32
                # 13 23 33
                #
                # 11 21 31 41 51 61
                # 12 22 32 42 52 62
                # 13 23 33 43 53 63
                # 14 24 34 44 54 64
                # 15 25 35 45 55 65
                #where (2,2)
                #what (4,3)
                #where no changes: (5,4)
                #where with changes: (4,5)
                soughtExtRowN=whereExtRowN+whatIneRowN-1  # 2+3-1=4
                soughtIneRowN=whereIneRowN+whatExtRowN-1  # 2+4-1=5
            else:#eachExtRowIsReversed==1:
                # 13 12 11
                # 23 22 21
                # 33 32 31
                #
                # 15 25 35 45 55 65
                # 14 24 34 44 54 64
                # 13 23 33 43 53 63
                # 12 22 32 42 52 62
                # 11 21 31 41 51 61
                #where (2,2)
                #what (4,3)
                #where no changes: (5,4)
                #where with changes: (2,5)
                soughtExtRowN=QIneRowsWhere-(whereExtRowN+whatIneRowN-1)+1#5-(2+3-1)+1=5-4+1=2
                soughtIneRowN=whereIneRowN+whatExtRowN-1# 2+4-1=5
            #
        else:#ExtRowsSuccIsReversed==1:
            if eachExtRowIsReversed==0:
                # 31 32 33
                # 21 22 23
                # 11 12 13
                #
                # 61 51 41 31 21 11
                # 62 52 42 32 22 12
                # 63 53 43 33 23 13
                # 64 54 44 34 24 14
                # 65 55 45 35 25 15
                #where (2,2)
                #what (4,3)
                #where no changes: (5,4)
                #where with changes: (4,2)
                soughtExtRowN=whereExtRowN+whatIneRowN-1#2+3-1=4
                soughtIneRowN=QExtRowsWhere-(whereIneRowN+whatExtRowN-1)+1   #6-(2+4-1)+1=6-5+1=2
            else:#eachExtRowIsReversed==1:
                # 33 32 31
                # 23 22 21
                # 13 12 11
                #
                # 65 55 45 35 25 15
                # 64 54 44 34 24 14
                # 63 53 43 33 23 13
                # 62 52 42 32 22 12
                # 61 51 41 31 21 11
                #where (2,2)
                #what (4,3)
                #where no changes: (5,4)
                #where with changes: (2,2)
                soughtExtRowN=QIneRowsWhere-(whereExtRowN+whatIneRowN-1)#5-(2+3-1)+1=5-4+1=2
                soughtIneRowN=QExtRowsWhere-(whereIneRowN+whatExtRowN-1)+1#6-(2+4-1)+1=6-5+1=2#invalid syntax
            #
        #  
    #if isTransposed
    return soughtExtRowN, soughtIneRowN
#

def arr2D_GetSubArr(arr2D, whereStartExtRowN, whereStartIneRowN, whatLs, isTransposed=0, ExtRowsSuccIsReversed=0, EachExtRowIsReversed=0, defaultVal=0, ifNotInArray_WriteDefault1_SetNull0=1 ):
    y=[]
    row=[]
    whereLs=[]
    contin=1
    if arr2D_isArr2D(arr2D):#, extRowOfArr2DMayBe_NonList=0, extRowOfArr2DMayBe_EmptyList=0)
        whereQExtRows=len(arr2D)
        for i in range(1, whereQExtRows+1):
            curWhereL=len(arr2D[i-1])
            whereLs.append(curWhereL)
        #
        if isinstance(whatLs, list) and len(whatLs)>0:
            whatQExtRows=len(Ls)
            whatExtRowN=0
            while whatExtRowN<=whatQExtRows and contin==1:
                whatExtRowN+=1
                curWhatL=whatLs[whatExtRowN-1]
                row=[]
                whatIneRowN=0
                while whatIneRowN<=curWhatL and contin==1:
                    whereCurExtRowN, whereCurIneRowN = arr2D_CoordsTransform(arr2D, whereExtRowN, whereIneRowN, whatExtRowN, whatIneRowN, isTransposed, ExtRowsSuccIsReversed, EachExtRowIsReversed)
                    if whereCurExtRowN>=1 and whereCurExtRowN<=whereQExtRows and whereCurInetRowN>=1 and whereCurIneRowN<=whereLs[whereCurExtRowN-1]:
                        val=arr2D_GetVal(arr2D, whereCurExtRowN, whereCurIneRowN)
                        row.append(val)
                    else:
                        if(ifNotInArray_WriteDefault1_SetNull0==1):
                            row.append(defaultVal)
                        else:
                            row=[]
                            y=[]
                            contin=0
                        #
                    #if
                #while ine
                if contin==1:
                    y.append(row)
                #
            #while ext
        #if
    #if
    return y
#

def arr2D_GetIfSubArrIsAtPos(arr2D, whereStartExtRowN, whereStartIneRowN, whatLs, isTransposed=0, ExtRowsSuccIsReversed=0, EachExtRowIsReversed=0, defaultVal=0, ifNotInArray_WriteDefault1_SetNull0=1 ):
    #alter ce!
    y=[]
    row=[]
    whereLs=[]
    contin=1
    if arr2D_isArr2D(arr2D):#, extRowOfArr2DMayBe_NonList=0, extRowOfArr2DMayBe_EmptyList=0)
        whereQExtRows=len(arr2D)
        for i in range(1, whereQExtRows+1):
            curWhereL=len(arr2D[i-1])
            whereLs.append(curWhereL)
        #
        if isinstance(whatLs, list) and len(whatLs)>0:
            whatQExtRows=len(Ls)
            whatExtRowN=0
            while whatExtRowN<=whatQExtRows and contin==1:
                whatExtRowN+=1
                curWhatL=whatLs[whatExtRowN-1]
                row=[]
                whatIneRowN=0
                while whatIneRowN<=curWhatL and contin==1:
                    whereCurExtRowN, whereCurIneRowN = arr2D_CoordsTransform(arr2D, whereExtRowN, whereIneRowN, whatExtRowN, whatIneRowN, isTransposed, ExtRowsSuccIsReversed, EachExtRowIsReversed)
                    if whereCurExtRowN>=1 and whereCurExtRowN<=whereQExtRows and whereCurInetRowN>=1 and whereCurIneRowN<=whereLs[whereCurExtRowN-1]:
                        val=arr2D_GetVal(arr2D, whereCurExtRowN, whereCurIneRowN)
                        row.append(val)
                    else:
                        if(ifNotInArray_WriteDefault1_SetNull0==1):
                            row.append(defaultVal)
                        else:
                            row=[]
                            y=[]
                            contin=0
                        #
                    #if
                #while ine
                if contin==1:
                    y.append(row)
                #
            #while ext
        #if
    #if
    return y
#






def arr2D_GetVal(arr2D, ExtRowN, IneRowN):
    val=[]
    Ls=[]
    if arr2D_arr2D_isArr2D(arr2D)==1:
        QER=len(arr2D)
        Ls=arr2D_GetLengthes(arr2D, -1)
        if(ExtRowN<0):
            ExtRowN+=(QER+1)
        #                                
        if ExtRowN>=1 and ExtRowN<=QER:
            L=len(arr2D[ExtRowN-1])
            if(IneRowN<0):
                IneRowN+=(L+1)
            #
            if IneRowN>=1 and IneRowN<=Ls[ExtRowN-1]:
                val=arr2D[ExtRowN-1][IneRowN-1]
            #
        #
    #
    return val
#
                                             
def arr2D_by1D_GetPosN(Ls, ExtRowN, IneRowN):
    PosN=0
    Lmax=0
    if isinstance(Ls, list):
        QER=len(Ls)
        if(QER>0):
            if(ExtRowN<0):
               ExtRowN+=(QER+1)
            #
            if ExtRowN>=1 and ExtRowN<=QER:
                for i in range(1, QER+1):
                    L=Ls[i-1]
                    if i==1 or (i>1 and L>Lmax):
                        Lmax=L
                    #
                #
                if IneRowN<0:
                   IneRowN+=(Lmax+1)
                #
                if(IneRowN>=1 and IneRowN<=Ls[ExtRowN-1]):
                    for i in range(1, ExtRowN-1+1):
                        PosN+=Ls[i-1]
                    #                         
                    PosN+=IneRowN
                #
            #
        #
    #
    return PosN
#
                                             
def arr2D_GetVal(arr2D, ExtRowN, IneRowN, Ls=[]):
    val=[]
    Lmax=0
    L=0
    QER=0
    PosN=0
    if arr2D_arr2D_isArr2D(arr2D)==1:
        QER=len(arr2D)
        Ls=arr2D_GetLengthes(arr2D, -1)
        if(ExtRowN<0):
            ExtRowN+=(QER+1)
        #                                
        if ExtRowN>=1 and ExtRowN<=QER:
            #L=len(arr2D[ExtRowN-1])
            for i in range(1, QER+1):
                L=Ls[i-1]
                if i==1 or (i>1 and L>Lmax):
                    L=Lmax
                #
            #
            if(IneRowN<0):
                IneRowN+=(Lmax+1)
            #
            if IneRowN>=1 and IneRowN<=Ls[ExtRowN-1]:
                val=arr2D[ExtRowN-1][IneRowN-1]
            #
        #   
    elif isinstance(arr2D, list) and isinstance(Ls, list):
        QElts=0
        QER=len(Ls)
        if QER>0:
            for i in range(1, QER+1):
                L=Ls[i-1]
                QElts+=L
            #
            if QElts==len(arr2D):
                if(ExtRowN<0):
                    ExtRowN+=(QER+1)
                #
                if ExtRowN>=1 and ExtRowN<=QER:
                    #L=len(arr2D[ExtRowN-1])
                    for i in range(1, QER+1):
                        L=Ls[i-1]
                        if i==1 or (i>1 and L>Lmax):
                            L=Lmax
                        #
                    #
                    if(IneRowN<0):
                        IneRowN+=(Lmax+1)
                    #
                    if IneRowN>=1 and IneRowN<=Ls[ExtRowN-1]:
                        PosN=arr2D_by1D_GetPosN(Ls, ExtRowN, IneRowN)
                        val=arr2D[PosN-1]
                    #
                #
            #
        #
    #
    return val
#

def arr2D_SetVal(arr2D, val, ExtRowN, IneRowN, Ls=[]):
    val=[]
    Lmax=0
    L=0
    QER=0
    PosN=0
    if arr2D_arr2D_isArr2D(arr2D)==1:
        QER=len(arr2D)
        Ls=arr2D_GetLengthes(arr2D, -1)
        if(ExtRowN<0):
            ExtRowN+=(QER+1)
        #                                
        if ExtRowN>=1 and ExtRowN<=QER:
            #L=len(arr2D[ExtRowN-1])
            for i in range(1, QER+1):
                L=Ls[i-1]
                if i==1 or (i>1 and L>Lmax):
                    L=Lmax
                #
            #
            if(IneRowN<0):
                IneRowN+=(Lmax+1)
            #
            if IneRowN>=1 and IneRowN<=Ls[ExtRowN-1]:
                arr2D[ExtRowN-1][IneRowN-1]=val
            #
        #   
    elif isinstance(arr2D, list) and isinstance(Ls, list):
        QElts=0
        QER=len(Ls)
        if QER>0:
            for i in range(1, QER+1):
                L=Ls[i-1]
                QElts+=L
            #
            if QElts==len(arr2D):
                if(ExtRowN<0):
                    ExtRowN+=(QER+1)
                #
                if ExtRowN>=1 and ExtRowN<=QER:
                    #L=len(arr2D[ExtRowN-1])
                    for i in range(1, QER+1):
                        L=Ls[i-1]
                        if i==1 or (i>1 and L>Lmax):
                            L=Lmax
                        #
                    #
                    if(IneRowN<0):
                        IneRowN+=(Lmax+1)
                    #
                    if IneRowN>=1 and IneRowN<=Ls[ExtRowN-1]:
                        PosN=arr2D_by1D_GetPosN(Ls, ExtRowN, IneRowN)
                        arr2D[PosN-1]=val
                    #
                #
            #
        #
    #
    #return val
#
        
                                             
def arr2D_subArr2DIsAtPos(whereData, whatData, whereExtRowN, whereIneRowN, isTransposed=0, ExtRowsSuccIsReversed=0, EachExtRowIsReversed=0, whereLs=[], whatLs=[], extRowOfArr2DMayBe_NonList=0, extRowOfArr2DMayBe_EmptyList=0):
    verdictTrue=1
    whereLsExtr=[]
    whatLsExtr=[]
    whereExtRowN_found=0
    whatIneRowN_found=0
    #whereCurVal, whatCurVal
    #def arr2D_isArr2D(arr2D, extRowOfArr2DMayBe_NonList=0, extRowOfArr2DMayBe_EmptyList=0):
    if arr2D_isArr2D(whereData, extRowOfArr2DMayBe_NonList=0, extRowOfArr2DMayBe_EmptyList=0) and arr2D_isArr2D(what, extRowOfArr2DMayBe_NonList=0, extRowOfArr2DMayBe_EmptyList=0):
        whereQER=len(whereData)
        whatQER=len(whatData)
        whereLs=arr2D_GetLengthes(whereData, 0)
        whatLs= arr2D_GetLengthes(whatData, 0)
        whereLsExtr=arr2D_GetLengthes(whereData, 1)
        whatLsExtr= arr2D_GetLengthes(whatData, 1)
        whereLmax=whereLsExtr[3-1]
        whatLmax=whatLsExtr[3-1]
        for whatExtRowN in range (1, whatQER+1):
            for whatIneRowN in range (1, whatLs[whatExtRowN-1]+1):
                #
                whereExtRowN_found, whereIneRowN_found = arr2D_CoordsTransform(whereData, whereExtRowN, whereIneRowN, whatExtRowN, whatIneRowN, isTransposed, ExtRowsSuccIsReversed, EachExtRowIsReversed)
                #
                whatCurVal=arr2D_GetVal(whatData, whatExtRowN, whatIneRowN, whatLs)
                if not(whereExtRowN_found >= 1 and whereExtRowN_found <= whereQER and whatIneRowN_found >= 1 and whatIneRowN_found <= whereLs[whereExtRowN_found-1]):
                    verdictTrue=0
                else:
                    whereCurVal=arr2D_GetVal(whereData, whereExtRowN_found, whereIneRowN_found, whereLs)
                    if(whatCurVal!=whereCurVal):
                        verdictTrue=0
                    #
                #
            #
        #
    #
    return verdictTrue
#

#def arr2D_SeekSubArr2D(whereData, whatData, isTransposed=0, ExtRowsSuccIsReversed=0, EachExtRowIsReversed=0, whereLs=[], whatLs=[], extRowOfArr2DMayBe_NonList=0, extRowOfArr2DMayBe_EmptyList=0):
#    Ns=[]
#    pair=[]
#    QER=0
#    #whereExtRowN, whereIneRowN,
#    #def arr2D_isArr2D(arr2D, extRowOfArr2DMayBe_NonList=0, extRowOfArr2DMayBe_EmptyList=0):
#    if arr2D_isArr2D(whereData, extRowOfArr2DMayBe_NonList, extRowOfArr2DMayBe_EmptyList)==1 and  arr2D_isArr2D(whatData, extRowOfArr2DMayBe_NonList, extRowOfArr2DMayBe_EmptyList)==1:
#        #
#        
#    elif isinstance(whereData, list) and isinstance(whereL, list) and isinstance(whateData, list) and isinstance(whatL, list) and len(whereL>0) and len(whatL>0):
#        #
#    #
        
                        
                    
                                             
                                             
