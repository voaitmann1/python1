import copy
#
#import MyLib1
#

#def AssignArray(arr, arrNew):
#    del(arr[:])
#    Q=len(arrNew)
#    for i in range(1, Q+1):
#        arr.append(arrNew)

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

def Swap1DArrayElements(arr, N1, N2):
    Q=len(arr)
    if N1>=1 and N1<=Q and N2>=1 and N2<=Q:
        buf=copy.deepcopy(arr[N1-1])
        arr[N1-1]=copy.deepcopy(arr[N2-1])
        arr[N2-1]=buf

def Del1DArrayElement(arr, N):#new, ne checked
    del(arr[N-1:N-1+1])
    
def Reverse1DArray(arr):
    Q=len(arr)
    if Q%2==0:
        N=Q/2
    else:
        N=(Q-1)/2
    for i in range(1, N+1):
        N1=i
        N2=Q+1-N1
        Swap1DArrayElements(arr, N1, N2)

def GetSubArray1D_FromToN(arr, N1, N2):
    R=[]
    if N1>N2:
        buf=N1
        N1=N2
        N2=buf
    return arr[N1-1:N2-1+1]

def GetSubArray1D(arr, N1, L):
    N2=N1-1+L
    return GetSubArray1D_FromToN(arr, N1, N2)

def IsSubArray1D(Where, What, FromN):
    R=1
    Qwhere=len(Where)
    Qwhat=len(What)
    #if FromN-1+Qwhat<=Qwhere:
    #    for i in range(1, Qwhat):
    #        Nwhat=i
    #        Nwhere=FromN-1+Nwhat
    #        if not Where[Nwhere-1]==What[Nwhat-1]:
    #            R=0
    #if Where[FromN:FromN-1+Qwhat+1]==What[1:Qwhat+1]:
    if GetSubArray1D(Where, FromN, Qwhat)==What:
        R=1
    else:
        R=0
    return R

def SeekFromStart(Where, What, FromN, ToN=0, vsh=0):
    if vsh==1:
        print("SeekFromStart starts working: FromN="+str(FromN)+" ToN="+str(ToN))
    Ns=[]
    Qwhere=len(Where)
    Qwhat=len(What)
    LastN=ToN-Qwhat+1
    if vsh==1:
        print("Qwhere="+str(Qwhere)+" Qwhat="+str(Qwhat)+" LastN="+str(LastN))
    if ToN==0:
        ToN=LastN
    else:
        LastN=ToN-Qwhat+1
    if Qwhere>0 and Qwhat>0 and ToN-FromN+1>=Qwhat and LastN<=Qwhere:
        for i in range(FromN,LastN+1):
            if IsSubArray1D(Where, What, i):
                Ns.append(i)
    count=len(Ns)
    if vsh==1:
        print("Found="+str(count)+":")
        print(Ns)
        print("SeekFromStart finishes working")
    return Ns

def SeekFromEnd(Where, What, FromN, ToN=0, vsh=0):
    if vsh==1:
        print("SeekFromEnd starts working: FromN="+str(FromN)+" ToN="+str(ToN))
    Qwhat=len(What)
    if ToN==0:
        ToN=1
    ToN=ToN-Qwhat+1
    if ToN<1:
        ToN=1
    FromN=FromN-Qwhat+1
    if FromN<1:
        FromN=1
    if vsh==1:
        print("Qwhat="+str(Qwhat)+" FromN="+str(FromN)+" ToN="+str(ToN))
    Ns = SeekFromStart(Where, What, ToN, FromN, vsh)
    count=len(Ns)
    if vsh==1:
        print("Found="+str(count)+":")
        print(Ns)
    if count>0:
        for i in range(1, count+1):
            for j in range(i, count+1):
                if Ns[j-1]>Ns[i-1]:
                    buf=Ns[i-1]
                    Ns[i-1]=Ns[j-1]
                    Ns[j-1]=buf
    if vsh==1:
        print("sorted from end:")
        print(Ns)
        print("SeekFromEnd finishes working")
    return Ns

#def SeekFromEnd(Where, What, FromN, vsh=0):
#    if vsh==1:
#        print("SeekFromEnd starts working")
#    Ns=[]
#    #count=0
#    Qwhere=len(Where)
#    Qwhat=len(What)
#    #NLast=
#    if vsh==1:
#        print("Qwhere="+str(Qwhere)+" Qwhat="+str(Qwhat))#, " NLast=")
#    for i in range(1, FromN-Qwhat+1):
#        N=Qwhere-i
#        if vsh==1:
#            print("i="+str(i)+" N="+str(N))#, " NLast=")
#        if IsSubArray1D(Where, What, N):
#            if vsh==1:
#                print("is sub-array")
#            Ls.append(i)
#            #count-count+1
#        else:
#            if vsh==1:
#                print("is not sub-array")
#        if vsh==1:
#            print("Found sub-arrays: "+str(len(Ls)))
#            print(Ls)
#            print("SeekFromEnd finishes working")
#    return Ls

def ToString1DArray(arr, delim=" "):
    s=""
    Q=len(arr)
    for i in range(1, Q-1+1):
        #s=str((str)arr[i-1])# so writes error
        s=s+str(arr[i-1])
        s=s+delim
    if Q>0:
        #s=str((str)arr[Q-1])# so writes error
        s=s+str(arr[Q-1])
    return s
        

#  2D array functions ----------------------------------------------------

def Get2DArrayLengthes(arr, N=0, All0N1Min2Max3Q4=1):
    #print("Get2DArrayLengthesstarts working: N=",N," All0N1Min2Max3Q4=",All0N1Min2Max3Q4)
    R=0
    Ls=[]
    Lmin=0
    Lmax=0
    LN=0
    Q=0
    if N==0:
        N=Q
    if isinstance(arr, list):
        Q=len(arr)
    #print("Q=",Q)
    if All0N1Min2Max3Q4==4:
        R=Q
    elif Q>0:
        for i in range(1, Q+1):
            Lcur=0
            #print("i=",i, "Q=",Q)
            if isinstance(arr[i-1], list):
                Lcur=len(arr[i-1])
                #print("Get2DArrayLengthes: is list")
            else:
                #print("Get2DArrayLengthes: is not list")
                pass
            #print("Get2DArrayLengthes: Lcur=",Lcur)
            if i==1 or (i>1 and Lmin>Lcur):
                Lmin=Lcur
                #print("Lmin=",Lmin)
            if i==1 or (i>1 and Lmax<Lcur):
                Lmax=Lcur
                #print("Lmax=",Lmax)
            if i==N:
                LN=Lcur
                #print("LN=",LN)
            Ls.append(Lcur)
            #
            if All0N1Min2Max3Q4==0:
                R=Ls
            elif All0N1Min2Max3Q4==1:
                R=LN
            elif All0N1Min2Max3Q4==2:
                R=Lmin
            elif All0N1Min2Max3Q4==3:
                R=Lmax
            #elif All0N1Min2Max3Q4==4:
            #    R=Q
    #print("Get2DArrayLengthes finishes working: R=",R)
    return R

def Get2DArrayLengthN(arr, N=0):
    return Get2DArrayLengthes(arr, N, 1)

def Get2DArrayMinLength(arr):
    return Get2DArrayLengthes(arr, 0, 2)

def Get2DArrayMaxLength(arr):
    return Get2DArrayLengthes(arr, 0, 3)

def Get2DArrayLength(arr):
    return Get2DArrayLengthes(arr, 0, 4)
    #
    
def Stretch2DArray(arr, L=0, DfltVal=0):
    Q=Get2DArrayLength(arr)
    Lmin=Get2DArrayMinLength(arr)
    Lmax=Get2DArrayMaxLength(arr)
    if L==0:
        L=Lmax
    if Lmin<Lmax and L>=Lmax:
        for i in range(1, Q+1):
            Lcur=len(arr[i-1])
            for j in range(Lcur+1, L+1):
                arr[i-1].append(DfltVal)
    
#
def Get2DArrayElement_AsLink(arr, ExtRowN=1, IneRowN=1):
    R=0
    Q=0
    Lcur=0
    if isinstance(arr, list):
        Q=len(arr)
        if Q>0 and ExtRowN>=1 and IneRowN>=1 and ExtRowN<=Q:
            if isinstance(arr[ExtRowN-1], list):
                Lcur=len(arr[ExtRowN-1])
                if IneRowN<=Lcur:
                    R=arr[ExtRowN-1][IneRowN-1]
    return R
                
def Get2DArrayElement_AsCopy(arr, ExtRowN=1, IneRowN=1):
    x=Get2DArrayElement_AsLink(arr, ExtRowN, IneRowN)
    y=copy.deepcopy(x)
    return y

def Get2DArrayElement(arr, ExtRowN=1, IneRowN=1, AsLink0Copy1=0):
    if AsLink0Copy1==0:
        R=Get2DArrayElement_AsLink(arr, ExtRowN, IneRowN)
    else:
        R=Get2DArrayElement_AsCopy(arr, ExtRowN, IneRowN)
    return R

def Set2DArrayElement(arr, valExt, ExtRowN=1, IneRowN=1):
    element=copy.deepcopy(valExt)
    R=0
    Q=0
    Lcur=0
    if isinstance(arr, list):
        Q=len(arr)
        if Q>0 and ExtRowN>=1 and IneRowN>=1 and ExtRowN<=Q:
            if isinstance(arr[ExtRowN-1], list):
                Lcur=len(arr[ExtRowN-1])
                if IneRowN<=Lcur:
                    arr[ExtRowN-1][IneRowN-1]=copy.deepcopy(element)
#

def Set2DArrayExtRowN(arr, rowExt, N=0, DfltVal=0, NonRectAllowed=0):
    Q=0
    rowToSet=copy.deepcopy(rowExt)
    if isinstance(arr, list):
        Q=len(arr)
        Lmin=Get2DArrayMinLength(arr)
        Lmax=Get2DArrayMaxLength(arr)
        if N==0:
            N=Q
        if N>=1 and N<=Q:
            arr[N-1]=copy.deepcopy(DfltVal)
            if rowToSet==[]:
                rowToSet.append(DfltVal)
            if NonRectAllowed==0:
                LP=len(rowToSet)
                if LP<Lmax:
                    for i in range(LP+1, Lmax+1):
                        rowToSet.append(DfltVal)
                elif LP>Lmax:
                    del(rowToSet[LP+1:Lmax])
            arr[N-1]=copy.deepcopy(rowToSet)

def Set2DArrayIneRowN(arr, rowExt, N=0, DfltVal=0, NonRectAllowed=0):
    rows=[]
    Q=0
    row=copy.deepcopy(rowExt)
    if isinstance(arr, list):
        Q=len(arr)
        Lmin=Get2DArrayMinLength(arr)
        Lmax=Get2DArrayMaxLength(arr)
        if N==0:
            N=Q
        if N>=1 and N<=Lmin: # if N>Lmin - no action, stretch it first
            LP=0
            if isinstance(row, list):
                row1=row
            else:
                row1=[]
                row1.append(row)
            LP=len(row1)
            if NonRectAllowed==0:
                if LP>Q:
                    del(row1[Q:LP])
                elif LP<Q:
                    for i in range(LP, Q+1):
                        row1.append(DfltVal)
                # if N>Lmin - no action, stretch it first
            LP1=len(row1)
            for i in range(1, LP1+1):
                rowE=[]
                #if isinstance(arr[i-1], list):
                Lcur=len(arr[i-1])
                for j in range(1, N-1+1):
                    rowE.append(arr[i-1][j-1])
                rowE.append(row1[i-1])
                for j in range(N, Lcur+1):
                    rowE.append(arr[i-1][j-1])   
                arr[i-1]=copy.deepcopy(rowE)

def Add2DArrayExtRow(arr, rowExt=[], DfltVal=0, NonRectAllowed=0):
    rowToAdd=copy.deepcopy(extRow)
    arr.append(DfltVal)
    Q=len(arr)
    #def Set2DArrayExtRowN(arr, rowExt, N=0, DfltVal=0, NonRectAllowed=0)
    Set2DArrayExtRowN(arr, rowExt, Q, DfltVal, NonRectAllowed)

def Add2DArrayIneRow(arr, rowExt=[], DfltVal=0, NonRectAllowed=0):
    LE=Get2DArrayLength(arr)
    Lmin=Get2DArrayMinLength(arr)
    Lmax=Get2DArrayMaxLength(arr)
    rowToAdd=copy.deepcopy(rowExt)
    LP=len(rowToAdd)
    if N==0:
        N=Lmax
    if NonRectAllowed==0:
        if Lmin<Lmax: 
            Stretch2DArray(arr, Lmax, DfltVal)
        if LP<LE:
            for i in range(LP+1, LE+1):
                rowToAdd.append(DfltVal)
        elif LP>LE:
            del(rowToAdd[LE:LP])
    LP1=len(rowToAdd)
    for i in range(1, LP1):
        arr[i-1].append(rowToAdd[i-1])
        
def Ins2DArrayExtRow(arr, N=0, rowExt=[], DfltVal=0, NonRectAllowed=0, vsh=0):
    if vsh==1:
        print("Ins2DArrayExtRow starts working: N="+str(N))
        print("Task is to ins:")
        print(ToString1DArray(rowExt))
    rows=[]
    rowToIns=copy.deepcopy(rowExt)
    Q=len(arr)
    if Q>0 and N>=1 and N<=Q:
        if vsh==1:
            print("Q="+str(Q)+" N="+str(N))
        if vsh==1:
            print("copying rows before N")
        for i in range(1, N-1+1):
            rows.append(arr[i-1])
            L=len(rows)
            if vsh==1:
                sc=ToString1DArray(rows[L-1])
                print(sc)
        if vsh==1:
            print("copying row N")
        rows.append(rowToIns)
        L=len(rows)
        if vsh==1:
            sc=ToString1DArray(rows[L-1])
            print(sc)
        if vsh==1:
            print("copying rows after N")
        for i in range(N, Q+1):
            rows.append(arr[i-1])
            L=len(rows)
            if vsh==1:
                sc=ToString1DArray(rows[L-1])
                print(sc)
        # ma mab size of new row is ne satf'l
        Set2DArrayExtRowN(rows, rowToIns, N, DfltVal, NonRectAllowed)
        if vsh==1:
            print("corrected row N"+str(N)+":")
            print(ToString1DArray(rows[N-1], "; "))
        #arr=rows # vikt!: so ne returns outside fn
        #arr=copy.deepcopy(rows) # vikt!: so ne returns outside fn
        del(arr[:])# vikt!: so works 
        for i in range(1, len(rows)+1):
            arr.append(rows[i-1])# vikt!: so works
        #AssignArray(arr, rows)#so works bad, spoils russian letters
        if vsh==1:
            print("Ins2DArrayExtRow  finishes working")

def Ins2DArrayIneRow(arr, N=0, rowExt=[], DfltVal=0):
    LE=Get2DArrayLength(arr)
    Lmin=Get2DArrayMinLength(arr)
    Lmax=Get2DArrayMaxLength(arr)
    rowToIns=copy.deepcopy(rowExt)
    LP=len(rowToIns)
    if N==0:
        N=Lmax
    if N<=Lmin:
        #if NonRectAllowed==0:
            #if Lmin<Lmax:
            #    Stretch2DArray(arr, Lmax, DfltVal)
        if LP<LE:
            for i in range(LP+1, LE+1):
                rowToIns.append(DfltVal)
        elif LP>LE:
            del(rowToIns[LE:LP])
        LP1=len(rowToIns)
        for i in range(1, LP1+1):
            Lcur=len(arr[i-1])
            rowE=[]
            for j in range(1, N-1+1):
                rowE.append(arr[i-1][j-1])
            rowE.append(rowToIns[i-1])
            for j in range(N, Lcur+1):
                rowE.append(arr[i-1][j-1])
            arr[i-1]=copy.deepcopy(rowE)

def Del2DArrayExtRowN(arr, N):
    del(arr[N-1:N-1+1])
    #ShowToConsole2DArrayWhole(arr)
    #print("fin\n")

def Del2DArrayIneRowN(arr, N, vsh=0):
    if vsh==1:
        print("Del2DArrayIneRowN stats working: N="+str(N))
    LE=len(arr)
    Lmin=Get2DArrayMinLength(arr)
    if vsh==1:
        print("LE="+str(LE)+" Lmin="+str(Lmin))
    if N>=1 and N<=Lmin:
        if vsh==1:
            print("N="+str(N)+" >= 1 and <= Lmin="+str(Lmin))
        for i in range(1, LE+1):
            del((arr[i-1])[N-1:N-1+1])
            if vsh==1:
                print(ToString1DArray(arr[i-1]))
        #print("in:")
        #ShowToConsole2DArrayWhole(arr)
        #print("fin\n")
    if vsh==1:
        print("Del2DArrayIneRowN finishes working")
#

def Get2DArrayExtRowN(arr, N):
    R=[]
    LE=Get2DArrayLength(arr)
    if(N>=1 and N<=LE):
        R=arr[N-1]
    return R

def Get2DArrayIneRowN(arr, N):
    R=[]
    LE=Get2DArrayLength(arr)
    Lmin=Get2DArrayMinLength(arr)
    Lmax=Get2DArrayMaxLength(arr)
    if(N>=1 and N<=Lmin):
        for i in range(1, LE+1):
            R.append(arr[i-1][N-1])
    return R

#

def Swap2DArrayElements(arr, ExtRow1N, IneRow1N, ExtRow2N, IneRow2N):
    Q=len(arr)
    L1=len(arr[ExtRow1N-1])
    L2=len(arr[ExtRow2N-1])
    if ExtRow1N>=1 and ExtRow1N<=Q and ExtRow2N>=1 and ExtRow2N<=Q and IneRow1N>=1 and IneRow1N<=L1 and IneRow2N>=1 and IneRow2N<=L2:
        buf=copy.deepcopy(arr[ExtRow1N-1][IneRow1N-1])
        arr[ExtRow1N-1][IneRow1N-1]=arr[ExtRow2N-1][IneRow2N-1]
        arr[ExtRow2N-1][IneRow2N-1]=buf

def Swap2DArrayExtRows(arr, ExtRow1N, ExtRow2N):
    #Q=len(arr)
    #if ExtRow1N>=1 and ExtRow1N<=Q and ExtRow2N>=1 and ExtRow2N<=Q:
    #    row1=Get2DArrayExtRowN(arr, ExtRow1N)
    #    row2=Get2DArrayExtRowN(arr, ExtRow2N)
    #    arr[ExtRow1N]=copy.deepcopy(row2)
    #    arr[ExtRow2N]=copy.deepcopy(row1)
    Swap1DArrayElements(arr, ExtRow1N, ExtRow2N)

def Swap2DArrayIneRows(arr, IneRow1N, IneRow2N, DfltVal=0, NonRectAllowed=0):
    Q=len(arr)
    Lmin=Get2DArrayMinLength(arr)
    Lmax=Get2DArrayMaxLength(arr)
    if IneRow1N>=1 and IneRow1N<=Lmin and IneRow2N>=1 and IneRow2N<=Lmin:
        for i in range(1, Q+1):
             Swap1DArrayElements(arr[i-1], IneRow1N, IneRow2N)

def Reverse2DArrayExtRowN(arr, N):
    Q=len(arr)
    if N>=1 and N<=Q:
        Reverse1DArray(arr[N-1])

def Reverse2DArrayIneRowN(arr, N, DfltVal=0, NonRectAllowed=0, vsh=0):
    if vsh==1:
        print("Reverse2DArrayIneRowN starts working")
    Q=len(arr)
    Lmin=Get2DArrayMinLength(arr)
    if vsh==1:
        print("Q="+str(Q)+" Lmin="+str(Lmin))
    if Q>0 and N>=1 and N<=Lmin:
        L=Q
        if L%2==0:
            NLim=L/2
        else:
            NLim=(L-1)/2
    for i in range(1, NLim+1):
        N1=i
        N2=L+1-N1
        Swap2DArrayElements(arr, N1, N, N2, N)
    #    row=Get2DArrayIneRowN(arr, N)#ne works
    #    Reverse1DArray(row)#ne works
    #    Set2DArrayIneRowN(arr, row, N, DfltVal, NonRectAllowed)#ne works
    if vsh==1:
        print("Reverse2DArrayIneRowN finishes working")

def Reverse2DArrayExtRows(arr):
    #Q=len(arr)
    #Lmin=Get2DArrayMinLength(arr)
    #if Q>0 and N>=1 and N<=Lmin:
    #    L=Q
    #    if L%2==0:
    #        NLim=L/2
    #    else:
    #        NLim=(L-1)/2
    #for i in range(1, N+1):
    #    N1=i
    #    N2=L+1-N1
    #    Swap2DArrayExtRows(arr, N1, N2)
    Reverse1DArray(arr)
            
def Reverse2DArrayIneRows(arr):
    LE=Get2DArrayLength(arr)
    Lmin=Get2DArrayMinLength(arr)
    Lmax=Get2DArrayMaxLength(arr)
    #if Lmin<Lmax:
    #    Stretch2DArray(arr, Lmax, DfltVal)
    #if N>=1 and N<=Lmax:
    #    L=Lmax
    #    if L%2==0:
    #        NLim=L/2
    #    else:
    #        NLim=(L-1)/2
    #for i in range(1, N+1):
    #    N1=i
    #    N2=L+1-N1
    #    Swap2DArrayIneRows(arr, N1, N2, DfltVal)
    if Lmax==Lmin:
        for i in range(1, LE+1):
            Reverse1DArray(arr[i-1])
    #else stretch it first to Lmax!
        
def Transpose2DArray(arr):
    rowR=[]
    Lmin=Get2DArrayMinLength(arr)
    Lmax=Get2DArrayMaxLength(arr)
    if Lmin<Lmax:
        Stretch2DArray(arr, Lmax)
    LE=len(arr)
    if LE>0:
        for i in range (1, Lmax+1):
            row=Get2DArrayIneRowN(arr, i)
            rowR.append(row)
        #arr=rowR
        #arr=copy.deepcopy(rowR)
        del(arr[:])
        for i in range(1, Lmax+1):
            arr.append(rowR[i-1])

def IsSubMatrixAt2DArray(arr, ExtRowN, IneRowN, What, vsh=0):
    #QWhat=Get2DArrayLength(What)
    #LMinWhat=Get2DArrayMinLength(What)
    #LMaxWhat=Get2DArrayMaxLength(What)
    #Q=Get2DArrayLength(arr)
    #Lmin=Get2DArrayMinLength(arr)
    #Lmax=Get2DArrayMaxLength(arr)
    #LrowGut=1
    #if ExtRowN-1+QWhat<=Q:
    #    QRowsGut=1
    #if QRowsGut==1:
    #    for i in range (1, QWhat+1):
    #        N=ExtRowN-1+i
    #        Larr=Get2DArrayLengthN(arr, N)
    #        Lwhat=Get2DArrayLengthN(What, i)
    #        if IneRowN-1+Lwhat>Larr:
    #            LrowGut=0
    #ValGut=1
    #if QRowsGut==1 and LrowGut==1:
    #    for i in range (1, QWhat+1):
    #        Ne=ExtRowN-1+i
    #        Lcur=len(What[i-1])
    #        for j in range(1, Lcur+1):
    #            Ni=IneRowN-1+j
    #            if arr[Ne-1][Ni-1]!=What[i-1][j-1]:
    #                ValGut=0
    #if QRowsGut==1 and LrowGut==1 and ValGut==1 :
    #    R=1
    #else:
    #    R=0
    #return R
    if vsh==1:
        print("IsSubMatrixAt2DArray starts working: ExtRowN="+str(ExtRowN)+"IneRowN="+str(IneRowN))
    R=1
    QWhere=Get2DArrayLength(arr)
    QWhat=Get2DArrayLength(What)
    if QWhere>0 and QWhat>0 and ExtRowN+QWhat-1<=QWhere:
        for i in range(1, QWhat+1):
            NE=ExtRowN+i-1
            #CurRowWhere=copy.deepcopy(arr[NE-1])
            #CurRowWhat=copy.deepcopy(What[i-1])
            if vsh==1:
                print("Is "+ToString1DArray(What[i-1])+" a sub-array of "+ToString1DArray(arr[NE-1])+" ?")
            if IsSubArray1D(arr[NE-1], What[i-1], IneRowN)==0:
                R=0
            if vsh==1:
                if R==1:
                    print("yes")
                else:
                    print("no")
    if vsh==1:
        print("verdict:")
        if R==1:
            print("yes")
        else:
            print("no")
        print("IsSubMatrixAt2DArray finishes working")
    return R

#def SubMatrix_ToExtRowsEnds(arr, N1, N2, N):#gut fn, ne tested on ne needed
#    rows=[]
#    Q=len(arr)
#    Qsub=N2-N1+1
#    if N1>=1 and N2<=Q and N2>=N1:
#        for i in range(N1, N2+1):
#            L1=len(arr[i-1])
#            L2=L1-N+1
#            row=copy.deepcopy(GetSubArray1D(arr[i-1],N,L2))
#            rows.append()
#    return rows
      
def SubMatrix(arr, ER1N, ER2N, IR1N, IR2N):
    rows=[]
    Q=len(arr)
    Qsub=ER2N-ER1N+1
    Lsub=IR2N-IR1N+1
    Lmin=Get2DArrayMinLength(arr)
    if ER1N>=1 and IR1N>=1 and ER2N<=Q and IR2N<=Lmin:
        for i in range(1, Qsub+1):
            NE=ER1N+i-1
            row=GetSubArray1D_FromToN(arr[NE-1], IR1N, IR2N)
            rows.append(row)
    return rows

def SeekSubMatrixOrVal(arr, SubArr, FromExtN=1, FromIneN=1, ToExtN=0, ToIneN=0, OrdEA1ED2IA3ID4=1, vsh=0):
    if vsh==1:
        print("SeekSubMatrix starts working: FromExtN"+str(FromExtN)+" FromIneN="+str(FromIneN)+" ToExtN="+str(ToExtN)+" ToIneN="+str(ToIneN))
    Ns=[]
    count=0
    QWhere=len(arr)
    Qwhat=0
    if isinstance(SubArr, list):
        Qwhat=len(SubArr)
        LWhatMin=Get2DArrayMinLength(SubArr)
        LWhatMax=Get2DArrayMaxLength(SubArr)
    else:
        Qwhat=1
        LWhatMin=1
        LWhatMax=1
    LWhereMin=Get2DArrayMinLength(arr)
    LWhereMax=Get2DArrayMaxLength(arr)
    if ToExtN==0:
        ToExtN=QWhere
    if ToIneN==0:
        ToIneN=LWhereMax
    LWhereMin=Get2DArrayMinLength(arr)
    LWhereMax=Get2DArrayMaxLength(arr)
    LastExtN=ToExtN-Qwhat+1
    LastLimIneN=ToIneN-LWhatMin+1
    if vsh==1:
        print("FromExtN"+str(FromExtN)+" FromIneN="+str(FromIneN)+" ToExtN="+str(ToExtN)+" ToIneN="+str(ToIneN))
        print("QWhere"+str(QWhere)+" Qwhat="+str(Qwhat)+" LWhereMin="+str(LWhereMin)+" LWhereMax="+str(LWhereMax))
        print("LastExtN"+str(LastExtN)+" LastLimIneN="+str(LastLimIneN))
    if FromExtN>=1 and ToExtN<=QWhere and FromExtN<=ToExtN and FromIneN>=1 and FromIneN<=LastLimIneN and LastLimIneN<=LWhereMax:
        if not isinstance(SubArr, list):
            SubMatrixRow=[]
            SubMatrixRow.append(SubArr)
            SubMatrix=[]
            SubMatrix.append(SubMatrixRow)
        else:
            SubMatrix=copy.deepcopy(SubArr)
        for i in range(FromExtN, LastExtN+1):
            for j in range(FromIneN, LastLimIneN+1):
                pair=[]
                y=IsSubMatrixAt2DArray(arr, i, j, SubMatrix, vsh)
                if y==1:
                    pair=[i, j]
                    Ns.append(pair)
                    if vsh==1:
                        print("("+str(i)+", "+str(j)+") - found "+str(count))
                else:
                    if vsh==1:
                        print("("+str(i)+", "+str(j)+") - not found")
    count=len(Ns)
    if count>1:
        if OrdEA1ED2IA3ID4==1:
            for i in range(1, count+1):
                for j in range(i, count+1):
                    p_i=Ns[i-1][1-1]
                    p_j=Ns[j-1][1-1]
                    if p_j<p_i:
                        buf=p_i
                        p_i=p_j
                        p_j=buf
        elif OrdEA1ED2IA3ID4==2:
            for i in range(1, count+1):
                for j in range(i, count+1):
                    p_i=Ns[i-1][1-1]
                    p_j=Ns[j-1][1-1]
                    if p_j>p_i:
                        buf=p_i
                        p_i=p_j
                        p_j=buf
        elif OrdEA1ED2IA3ID4==3:
            for i in range(1, count+1):
                for j in range(i, count+1):
                    p_i=Ns[i-1][2-1]
                    p_j=Ns[j-1][2-1]
                    if p_j<p_i:
                        buf=p_i
                        p_i=p_j
                        p_j=buf
        elif OrdEA1ED2IA3ID4==4:
            for i in range(1, count+1):
                for j in range(i, count+1):
                    p_i=Ns[i-1][2-1]
                    p_j=Ns[j-1][2-1]
                    if p_j>p_i:
                        buf=p_i
                        p_i=p_j
                        p_j=buf
    if vsh==1:
        ShowToConsole2DArrayWhole(Ns, "; ")
        print("SeekSubMatrix finishes working")
    return Ns
                        

    
    
#def Seek2DArrayVal(arr, What, SortByInnerRowN=0, Show1Hide0=1):
#    if Show1Hide0==1:
#        print("Seek (single val) starts working")
#    count=0#;
#    R=[]
#    ExtRowsNs=[]
#    IneRowsNs=[]
#    #T cur;
#    #Array2DSize Inf=DefInfo(InfoExt);
#    #//seek
#    if(not(isinstance(What, list))):
#        for i in range(1, len(arr)+1):
#            curC=len(arr[i-1])
#            for j in range(1, curC+1):
#                #pair=[]
#                cur=arr[i-1][j-1]
#                if Show1Hide0==1:
#                    print("i=",i,' j=',j," curC=",curC," cur=",cur)
#                if(cur==What):
#                    count=count+1;
#                    #if(count==1):
#                    ExtRowsNs.append(i)
#                    IneRowsNs.append(j)
##                    #}
#                    if Show1Hide0==1:
#                        print("cur=",cur,'== val=',What," count=",count)
#                else:
#                    if Show1Hide0==1:
#                        print("cur=",cur,'!= val=',What)
#            #}//for j
#    else:#list
#        for i in range(1, len(arr)+1):
#            curC=len(arr[i-1])
#            for j in range(1, curC+1):
#                pair=[]
#                if(self.IsSubMatrixAt(i, j, What)==1):
#                    count=count+1
#                    if(count==1):
#                        ExtRowsNs.append(i)
#                        IneRowsNs.append(j)
#                    #}
#                #}
#            #}//for j
#        #}//for i
#    #if What is list or single val
#    if(SortByInnerRowN==1):
#        for i in range(1, count+1):
#            for j in range(i, count+1):
#                if(IneRowsNs[j-1]<IneRowsNs[i-1]):
#                    eBuf=ExtRowsNs[i-1]
#                    iBuf=IneRowsNs[i-1]
#                    ExtRowsNs[i-1]=ExtRowsNs[j-1]
#                    IneRowsNs[i-1]=IneRowsNs[j-1]
#                    ExtRowsNs[j-1]=eBuf
#                    IneRowsNs[j-1]=iBuf
#                #}
#                #}
#            #}
#        #}
#    #//write finally to vectors
#    for i in range(1, count+1):
#        pair=[]
#        pair.append(ExtRowsNs[i-1])
#        pair.append(IneRowsNs[i-1])
#        R.append(pair)
#    if Show1Hide0==1:
#        print("Seek (single val) finishes working")
#    return R



def ToString2DArrayElement(arr, ExtRowN, IneRowN, ElementBef="", ElementAft=""):
    s=""
    L=Get2DArrayLength(arr)
    if ExtRowN>=1 and ExtRowN<=L:
        Lcur=Get2DArrayLengthN(arr, ExtRowN)
        if IneRowN>=1 and IneRowN<=Lcur:
            s=ElementBef
            s=s+str(arr[ExtRowN-1][IneRowN-1])
            s=s+ElementAft
    return s

def ShowToConsole2DArrayElement(arr, ExtRowN, IneRowN, ElementBef="", ElementAft=""):
    L=Get2DArrayLength(arr)
    if ExtRowN>=1 and ExtRowN<=L:
        Lcur=Get2DArrayLengthN(arr, ExtRowN)
        if IneRowN>=1 and IneRowN<=Lcur:
            print(ElementBef,((str)(arr[ExtRowN-1][IneRowN-1])),ElementAft)
    
def ToString2DArrayLineN(arr, N, Delim="", ElementBef="", ElementAft=""):
    s=""
    L=Get2DArrayLength(arr)
    if N>=1 and N<=L:
        Lcur=Get2DArrayLengthN(arr, N)
        for i in range(1, Lcur-1+1):
            s=s+ToString2DArrayElement(arr, N, i, ElementBef, ElementAft)
            s=s+Delim
        if Lcur>0:
            s=s+ToString2DArrayElement(arr, N, Lcur, ElementBef, ElementAft)
    return s

def ShowToConsole2DArrayLineN(arr, N, Delim="", ElementBef="", ElementAft=""):
    s=""
    #L=Get2DArrayLength(arr)
    #if N>=1 and N<=L:
    #    Lcur=Get2DArrayLengthN(N)
    #    for i in range(1, Lcur-1+1):
    #        print(ElementBef,(str)(arr[ExtRowN-1][IneRowN-1]),ElementAft)
    #        s=s+Delim
    #    if Lcur>0:
    #        s=ElementBef+(str)(arr[N-1][Lcur-1])+ElementAft
    s=ToString2DArrayLineN(arr, N, Delim, ElementBef, ElementAft)
    print(s)
    
def ShowToConsole2DArrayWhole(arr, delim="; ", ElementBef="", ElementAft=""):
    L=Get2DArrayLength(arr)
    for i in range(1, L+1):
        ShowToConsole2DArrayLineN(arr, i, delim, ElementBef, ElementAft) 
            
                
#--------------------------------------------------------------------------------


class My1DArray:
    #
    def __init__(self, data=[]): #1
        self.row = []
        self.Set(data)
    #
    #def set, def get? Ma row nes private
    def Set(self, data):#ne test'd #2
        self.row = []
        #
        if isinstance(data,My1DArray):
            self.row=copy.deepcopy(data.row)
        elif isinstance(data,list):
            L=len(data)
            for i in range(1, L+1):
                element=copy.deepcopy(data[i-1])
                self.row.append(element)#in cycle
            #self.row=copy.deepcopy()# no ob need cells
        else:
            element=copy.deepcopy(data)
            self.row.append(element)
    #
    def GetElement_AsLink(self, N=0): #25
        R = 0
        #Q = self.ArrayLength(self.row)
        Q=len(self.row)
        if N==0:
            N=Q
        if N >= 1 and N <= Q:
            R = self.row[N - 1]
        return R

    def GetElement_AsCopy(self, N=0): #26
        R = 0
        #Q = self.ArrayLength(self.row)
        Q=len(self.row)
        if N==0:
            N=Q
        if N >= 1 and N <= Q:
            R = copy.deepcopy(self.row[N - 1])
        return R

    def GetElement(self, N=0, Link0Copy1=0, DefaultVal=0): #4
        R = DefaultVal
        if(Link0Copy1==1):
            R=self.GetElement_AsCopy(N)
        else:
             R=self.GetElement_AsLink(N)
        return R
    #
    #
    def SetElement(self, elementExt, N=0, ExistingVal_Allowed0Forbidden1=0): #5
        element=copy.deepcopy(elementExt)
        Q=len(self.row)
        if N==0:
            N=Q
        NE=self.Seek(element)
        if N >= 1 and N <= Q and (NE==0 or ExistingVal_Allowed0Forbidden1==0): 
            self.row[N - 1]=element
    #
    def Add(self, elementExt, ExistingVal_Allowed0Forbidden1=0): #6
        element=copy.deepcopy(elementExt)
        #ArrayAdd(self.row, cell)
        NE=self.Seek(element)
        if NE==0 or ExistingVal_Allowed0Forbidden1==0:
            self.row.append(element)
    #
    def Ins(self, elementExt, N=0, ExistingVal_Allowed0Forbidden1=0): #7
        Q=len(self.row)
        elementToIns=copy.deepcopy(elementExt)
        NE=self.Seek(elementToIns)
        if N==0:
            N=Q
        if N >= 1 and N <= Q and(NE==0 or ExistingVal_Allowed0Forbidden1==0): 
            row=[]
            for i in range(1, N-1+1):
                val=copy.deepcopy(self.row[i-1])
                row.append(val)
            row.append(elementToIns)
            for i in range(N, Q+1):
                val=copy.deepcopy(self.row[i-1])
                row.append(val)
            self.row=row
    #
    def Ins1(self, val, N=0, ExistingVal_Allowed0Forbidden1=0): #8
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
    def Del(self, N=0): #9
        Q=len(self.row)
        if N==0:
            N=Q
        if N >= 1 and N <= Q:
            #del self.row[N-1:N-1+1]
            del self.row[N-1:N-1+1]
    #
    def Clear(self): #10
        del self.row[:]
    #
    #
    #def SeekFirst(self, val, FromN=1, ToN=0):
    def SeekFirst(self, val, FromN=1): #11
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
    def SeekLast(self, val, ToN=0): #12
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
    def Seek(self, val, NLim=0, FirstNotLast=1): #13
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
    def DelFirstElement(self, val): #14
        N=self.SeekFirst(val)
        if N>0:
            self.Del(N)
    #
    def DelLastElement(self, val): #15
        N=self.SeekLast(val)
        if N>0:
            self.Del(N)
    #
    #
    def Swap(self, N1, N2): #16
        Q=len(self.row)
        if N1>=1 and N1<=Q and N2>=1 and N2<=Q:
            #print("Swapping: N1=",N1," = ",self.row[N1-1]," and N2=",N2," = ",self.row[N2-1])
            x=self.row[N1-1]
            self.row[N1-1]=self.row[N2-1]
            self.row[N2-1]=x
    #
    def Reverse(self): #order visa versa #17
        Q=len(self.row)
        if Q%2==0:
            N=Q/2
        else:
            N=(Q-1)/2
        #for N1 in range(1,N):
        for N1 in range(1,N+1):
            N2=Q-N1+1
            self.Swap(N1,N2)
    #
    def GetLength(self): #18
        return len(self.row)
    #
    #
    def SetLength(self, LNew, DefaultVal=0): # for stretch in 2DArray #19
        LOld=self.GetLength()
        if(LNew>=1 and LNew<=MaxInt):
            if L<LOld:
                self.row=self.row[1-1, LNew-1+1]
            elif LNew>LOld:
                for i in range(LOld-1+1, LNew-1+1):
                    self.row.append(DefaultVal)
    #
    def GetSubRow(self, N1, N2, Step=1): #20
        R=[]
        L=self.GetLength()
        if N1>=1 and N2>=1 and N1<=L and N2<=L and ((N1<N2 and Step>0)or(N1>N2 and Step<0)):
            if N1<N2:# and :
                #R=self.row[N1;N2;Step]
                for i in range(N1, N2+1):
                    R.append(self.row[i-1])
            elif N1==N2:
                R.append(self.row[N1-1])
            else:#exists > simple solution
                for i in range(N2, N1):
                    N=N1+(N1-N2)*(i-1)
                    R.append(self.row[N-1])
        return R
    #
    #
    def ToString_Element(self, N): #21
        R=""
        L=self.GetLength()
        if N>=1 and N<=L:
            element=self.GetElement(N)
            if isinstance(element, int) or isinstance(element, float) or isinstance(element, bool):
                R=str(element)
            elif isintance(element, str):
                R=copy.deepcopy(element)
            else:
                R=element.ToString()
        return R

    def ToString(self, sep="; "): #22
        s=""
        Q=self.GetLength()
        for i in range(1, Q):
            s=s+ToString_Element(i)
            s=s+sep
        if Q>0:
            s=s+ToString_Element(Q)
        return s

    def __str__(self): #23
        return self.ToString()
    
    #
    def ShowConsole(self, sep=" "): #24
        Q=len(self.row)
        #for i in range(1,Q):
        for i in range(1,Q+1):
            print(str(self.row[i-1]))
    

#-------------------------------------------------------------------------------

class My2DArray1:
    def __init__(self, data):
        self.row=[]
        self.Set(data)

    def Set(self, dataExt):#ne tested
        data=copy.deepcopy(dataExt)
        if isinstance(data, My2DArray1):
            self.row=copy.deepcopy(data.row)
        elif isinstance(data, list):
            LE=len(data)
            if LE>0:
                for i in range(1, LE+1):
                    rowE=[]
                    if isinstance(data[i-1],list):
                        rowE=copy.deepcopy(data[i-1])
                    else: #wi 1D-List, row of rows L=1
                       rowE.append(data[i-1])
                    self.row.append(rowE)
        else: # 1x1
            rowE=[]
            rowE.append(data)
            self.row.append(rowE)

    #def SetCells(self, dataExt):#ne tested
    #    data=copy.deepcopy(dataExt)
    #    cell=MyCell()
    #    if isinstance(data, list):
    #        LE=len(data)
    #        if LE>0:
    #            for i in range(1, LE+1):
    #                rowE=[]
    #                if isinstance(data[i-1],list):
    #                    L=len(data[i-1])
    #                    for j in range(1,L+1):
    #                        element=copy.deepcopy(data[i-1][j-1])
    #                        cell.Set(element)
    #                        rowE.append(cell)
    #                else:
    #                   element=copy.deepcopy(data[i-1])
    #                    cell.Set(element)
    #                    #rowE.append(data[i-1])
    #                    rowE.append(cell)
    #                self.row.append(rowE)
    #    else:
    #        rowE=[]
    #        element=copy.deepcopy(data)
    #        rowE.append(element)
    #        self.row.append(rowE)
    #
    #def SetArrayOf1DArrayOfCells(self, dataExt):#ne tested, ce wi bad ob indexes ne work'tl so not sep class
    #    data=copy.deepcopy(dataExt)
    #    #cell=MyCell()
    #    self.row=My1DArray()
    #    if isinstance(data, list):
    #        LE=len(data)
    #        if LE>0:
    #            for i in range(1, LE+1):
    #                rowE=My1DArray()
    #                if isinstance(data[i-1],My1DArray):
    #                    L=data[i-1].GetLength()
    #                    for j in range(1,L+1):
    #                        elenment=data[i-1].GetElement(j)
    #                        if isinstance(elenment,MyCell):
    #                            cell=elenment
    #                        else:
    #                            cell.Set(element)
    #                    #rowE=data[i-1]
    #                    #rowE.apend(cell)
    #                    rowE.Add(cell)
    #                elif isinstance(data[i-1],list):
    #                    L=len(data[i-1])
    #                    for j in range(1,L+1):
    #                        element=copy.deepcopy(data[i-1][j-1])
    #                        cell.Set(element)
    #                        rowE.Add(cell)
    #                else:
    #                    element=copy.deepcopy(data[i-1])
    #                    cell.Set(element)
    #                    rowE.Add(cell)
    #                #self.row.append(rowE)
    #                self.row.Add(rowE)
    #    else: # not isinstance(data, list), so obe cell in 2D table
    #        rowE=My1DArray()
    #        element=copy.deepcopy(data)
    #        #rowE.append(element)
    #        rowE.Add(element)
    #        #self.row.append(rowE)
    #        self.row.Add(rowE)
    #
    def SetElement(self, val, ExtRowN=1, IneRowN=1):
        LE=len(self.row)
        if(LE>0 and ExtRowN<=LE):
            if IneRowN<=len(self.row[ExtRowN-1]):
                self.row[ExtRowN-1][IneRowN-1]=copy.deepcopy(val)
            
    def GetElement_AsLink(self, ExtRowN=1, IneRowN=1):
        R=0
        LE=len(self.row)
        if(LE>0 and ExtRowN<=LE):
            if IneRowN<=len(self.row[ExtRowN-1]):
                R=self.row[ExtRowN-1][IneRowN-1]
        return R

    def GetElement_AsCopy(self, ExtRowN=1, IneRowN=1):
        R=0
        LE=len(self.row)
        if(LE>0 and ExtRowN<=LE):
            if IneRowN<=len(self.row[ExtRowN-1]):
                R=copy.deepcopy(self.row[ExtRowN-1][IneRowN-1])
        return R

    def GetElement(self, ExtRowN=1, IneRowN=1, ReturnLink0Copy1=0):
        R=0
        if ReturnLink0Copy1==0:
            R=self.GetElement_AsLink(ExtRowN, IneRowN)
        else:
            R=self.GetElement_AsCopy(ExtRowN, IneRowN)
        return R
    
    def GetLength():
        return len(row)

    def GetLengthN(self, RowN=1):
        LExt=len(self.row)
        LIne=0
        if RowN>=1 and RowN<=LExt and LExt>0:
            L=len(self.row[RowN-1])
        return L

    def GetMinLength(self):#ne test'd
        LE=len(self.row)
        Lmin=0
        for i in range(1, L+1):
           LI=len(self.row[i-1])
           if i==1 or (i>1 and LI<Lmin):
               Lmin=LI
        return Lmin

    def GetMaxLength(self):#ne test'd
        LE=len(self.row)
        Lmax=0
        for i in range(1, LE+1):
           LI=len(self.row[i-1])
           if i==1 or (i>1 and LI>Lmax):
               Lmax=LI
        return Lmax

    #duplicate all fns of 1row ror 2 rows: for ext and inner
    def AddExtRow(self, rowExt, tornAllowed=0):#, DfltVal=0, 
        rowP=copy.deepcopy(rowExt)
        #cell=MyCell()
        rowE=[]
        LP=len(rowP)
        LE=len(self.row)
        if LE>0:
            #LI=len(self.row[1-1])
            #LI=self.GetMaxLength()
            LI=self.GetLengthN(LE)#Length of last ext row
        else:
            LI=0
        #
        if LP==0 and LE==0:# add empty row to empty row of rows
            #zero=0#NOp
            pass
        elif LE==0 and LP>0:# add a row to empty row of rows
            self.row.append(rowP)
        elif LE>0:
            #if LP==0: # add empty row to a row of rows
            #    pass
            #    #for i in range(1, LI+1):
            #    #    rowE.append(cell)
            #    #rowP=rowE
            #if(tornAllowed==0):
            #    if LP<LI:
            #        for i in range(LP,LI):
            #            rowP.append(DfltVal)
            #    elif LI<LP:
            #        del(rowP[LI,LP])
            #    #else LI==LP - NOp
            #self.row.append(rowP)
            if LP==0: # add empty row to a row of rows
                pass
                #for i in range(1, LI+1):
                #    rowE.append(cell)
                #rowP=rowE
            else:
                if(tornAllowed==0):
                    if LP<LI:
                        for i in range(LP,LI):
                            rowP.append(DfltVal)
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
            #LI=len(self.row[1-1])
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
                    
    def InsExtRow(self, N=0, rowExt=[], DfltVal=0, NonRectAllowed=0, vsh=0):
        #if vsh!=0:
        #    print("InsExtRow Starts Working")
        #rowP=copy.deepcopy(rowExt)
        #LP=len(rowP)
        #LE=len(self.row)
        #rowR=[]
        ##cell=MyCell()
        #if LE>0:
        #    LI=len(self.row[1-1])
        #else:
        #    LI=0
        ##
        ##rowE=[]
        ##cell=MyCell()
        #if N==0:
        #    N=LE
        ##
        #if vsh!=0:
        #    print("N=",N," LP=",LP," LE=",LE," LI=",LI)
        ##
        #if LE==0 and LP==0: 
        #    if vsh!=0:
        #        print(" LE==0 and LP==0")
        #    if N>0:
        #        if vsh!=0:
        #            print("N>0")
        #        rowE=[]
        #        #cell=MyCell()
        #        rowE.append(cell)#LI=1
        #        rowP=rowE
        #        for i in range(1,N+1):
        #            self.row.append(rowP)
        #elif LE>0:# and LP==0:
        #    if vsh!=0:
        #        print("LE>0")
        #    #if N>=1 and N<=LI:
        #    if N>=1 and N<=LE:#alt'd
        #        if vsh!=0:
        #            #print("N>=1 and N<=LI")
        #            print("N>=1 and N<=LE")
        #        if LP==0:
        #            if vsh!=0:
        #                print("LP==0")
        #            rowE=[]
        #            #cell=MyCell()
        #            for i in range (1, LI+1):
        #                rowE.append(cell)
        #            rowP=rowE
        #        else:
        #            if vsh!=0:
        #                print("LP!=0")
        #            if tornAllowed==0:
        #                if vsh!=0:
        #                    print("tornAllowed==0")
        #                if LP<LI:
        #                    if vsh!=0:
        #                        print("LP<LI")
        #                    for i in range (LP+1, LI+1):
        #                        rowE.append(cell)
        #                    rowP=rowE
        #                elif LP>LI:
        #                    if vsh!=0:
        #                        print("LP>LI")
        #                    del(rowP[LI:LP])
        #        for i in range (1, N-1+1):#vikt qes: qob hin ne N-1+1?Anw: ja,+1
        #            rowR.append(self.row[i-1])#ef ins
        #        rowR.append(rowP)
        #        #for i in range(N,LE+1+1):
        #        for i in range(N,LE+1):
        #            #rowR.append(self.row[i-1-1])
        #            rowR.append(self.row[i-1])#af ins
        #        self.row=rowR
        #if vsh!=0:
        #    print("InsExtRow finishes Working")
        Ins2DArrayExtRow(self.row, N, rowExt, DfltVal, NonRectAllowed)
        
    def InsIneRow(self, rowExt, N=0, tornAllowed=0, DfltVal=0):
        #rowR=[]
        #rowE=[]
        #rowP=copy.deepcopy(rowExt)
        #LP=len(rowP)
        #LE=len(self.row)
        ##cell=MyCell()
        #if LE>0:
        #    LI=len(self.row[1-1])
        #else:
        #    LI=0
        #if N==0:
        #    N=LE
        ##
        #if LE==0 and LP==0:
        #    zero=0#NOp
        #elif LE==0 and LP>0:
        #    if N>0:
        #        for i in range(1,LP+1):
        #            rowE=[]
        #            cell=MyCell()
        #            for j in range (1,N-1+1):
        #                rowE.append(cell)
        #            rowE.append(rowP[i-1])
        #            self.row.append(rowE)
        #elif LE>0 and LP==0:
        #    if N>=1 and N<=LE:
        #        rowE=[]
        #        rowR=[]
        #        cell=MyCell()
        #        for i in range(1, LI+1):
        #            rowE.append(cell)
        #        rowP=rowE
        #        #LP=len(rowP)
        #        for i in range(1,LE+1):
        #            rowE=[]
        #            for j in range(1,N-1+1):
        #                rowE.append(self.row[i-1][j-1])
        #            rowE.append(rowP[i-1])
        #            #for j in range(N+1,LE+1+1):
        #            #    rowE.append(self.row[i-1][j-1-1])
        #            for j in range(N,LE+1):
        #                rowE.append(self.row[i-1][j-1])
        #            rowR.append(rowE)
        #        self.row=rowR        
        #else:
        #    if N>=1 and N<=LE:
        #        for i in range(1,LE+1):
        #            rowE=[]
        #            for j in range(1,N-1+1):
        #                rowE.append(self.row[i-1][j-1])
        #            rowE.append(rowP[i-1])
        #            for j in range(N+1,LE+1+1):
        #                rowE.append(self.row[i-1][j-1-1])
        #            rowR.append(rowE)
        #        self.row=rowR
            Ins2DArrayIneRow(self.row, N, rowExt, DfltVal)
                
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

    def Seek(self, valToSeek):
        count=0
        #print("Seek starts working")
        QE=len(self.row)
        #print("2D array has ",QE," ext rows")
        pairRow=[]
        for i in range(1, QE+1):
            QI=len(self.row[i-1])
            #print("Length of ",i," th row = ", QI)
            for j in range (1,QI+1):
                pair=[]
                curVal=copy.deepcopy(self.row[i-1][j-1])
                if curVal==valToSeek:
                    #print("i=",i," j=",j," CurVal=",curVal," == "," valToSeek= ",valToSeek)
                    pair.append(i)
                    pair.append(j)
                    #print(pair)
                    pairRow.append(copy.deepcopy(pair))
                    count=count+1
                    #print("Found at (",pair[1-1],",",pair[2-1],")")
                    #print("Found at (",pair[1-1],",",pair[2-1],")")
                else:
                    zero=0
                    #print("i=",i," j=",j," CurVal=",curVal," != "," valToSeek= ",valToSeek)
        #print("Seek finishes working")
        return pairRow

    def Seek_SortByExtRowN(self, val):
        return self.Seek(val)

    def Seek_SortByIneRowN(self, val):
        row=self.Seek(val)
        Q=len(row)
        for i in range(1, Q+1):
            for j in range(i, Q+1):
                #if j==i or (j>i and row[j-1][2-1]<row[i-1][2-1]):
                if row[j-1][2-1]<row[i-1][2-1]:
                    buf=row[j-1]
                    row[j-1]=row[i-1]
                    row[i-1]=buf
        return row
    

    def GetFoundInMinExtRow(self, val):
        #row=[]
        row=Seek(val)
        pair=[]
        Q=len(row)
        if Q>0:
            pair=row[1-1]
        return pair

    def GetFoundInMaxExtRow(self, val):
        #row=[]
        row=Seek(val)
        pair=[]
        Q=len(row)
        if Q>0:
            pair=row[1-1]
        return pair

    def GetFoundInMinIneRow(self, val):
        #row=[]
        row=Seek(val)
        pair=[]
        Q=len(row)
        if Q>0:
            pair=row[1-1]
        return pair
        
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

    #
    def IsSubMatrixAt(self, ExtRow1N, IneRow1N, SubMatrix=[], ValsShowHide=0):
        if ValsShowHide==1:
            print("\nIsSubMatrixAt starts working - fron position: (",ExtRow1N, ", ",IneRow1N,")")
        R=1
        QExtRowsIn=len(self.row);
        QExtRowsTo=0
        if isinstance(SubMatrix, list):
            QExtRowsTo=len(SubMatrix);
            if ValsShowHide==1:
                print("SubMatrix is list and has external rows: ", QExtRowsTo)
        #QIneRowsIn, QIneRowsTo;
        #ExtRowCurN, ExtRowLastN, IneRowCurN, IneRowLastN;
        ExtRowLastN=ExtRow1N+QExtRowsTo-1
        if ValsShowHide==1:
            print("Last row N is matri, where to seek: ", ExtRowLastN)
        if(ExtRowLastN<=QExtRowsIn and QExtRowsTo>0):
            if ValsShowHide==1:
                print("possible to seek ")
            for i in range(1, QExtRowsTo+1):
                ExtRowCurN=ExtRow1N+i-1
                QIneRowsIn=self.GetLengthN(ExtRowCurN)
                QIneRowsTo=len(SubMatrix[i-1]);
                IneRowLastN=IneRow1N+QIneRowsTo-1
                if ValsShowHide==1:
                    print(i,"th row of matrix what, L=", QIneRowsTo, "; ", ExtRowCurN,"th row of matrix where, L=", QIneRowsIn)
                if(IneRowLastN<=QIneRowsIn):
                    if ValsShowHide==1:
                        print("row of where to seek is long enough ")
                    for j in range(1, QIneRowsTo+1):
                        InetRowCurN=IneRow1N+j-1
                        CurTo=SubMatrix[i-1][j-1];
                        #CurIn=self.row[ExtRowCurN-1][IneRowLastN-1]
                        CurIn=self.row[ExtRowCurN-1][InetRowCurN-1]
                        if(CurTo!=CurIn):
                            R=0
                            if ValsShowHide==1:
                                print("Values: What[",i,", ",j,"]=",CurTo," NOT equal Where[",ExtRowCurN,", ",InetRowCurN,"]=",CurIn)
                        else:
                            if ValsShowHide==1:
                                print("Values: What[",i,", ",j,"]=",CurTo," == Where[",ExtRowCurN,", ",InetRowCurN,"]=",CurIn)
                       #}
                    #}
                else:
                    R=0
                #}
            #}
        else:
            R=0
            if ValsShowHide==1:
                print("Impossible to seek! ")
        #}
        if(R==1):
            if ValsShowHide==1:
                print("IsSubMatrixAt finishes working - answer: yes\n")
        else:
            if ValsShowHide==1:
                print("IsSubMatrixAt finishes working - answer: no\n")
        return R;
    #}//fn
    def Seek(self, What, SortByInnerRowN=0, Show1Hide0=1):
        #int *NE=NULL, *NI=NULL, curC, n;
        if Show1Hide0==1:
            print("Seek (single val) starts working")
        count=0#;
        R=[]
        ExtRowsNs=[]
        IneRowsNs=[]
        #T cur;
        #Array2DSize Inf=DefInfo(InfoExt);
        #//seek
        if(not(isinstance(What, list))):
            for i in range(1, len(self.row)+1):
                curC=len(self.row[i-1])
                for j in range(1, curC+1):
                    #pair=[]
                    cur=self.row[i-1][j-1]
                    if Show1Hide0==1:
                        print("i=",i,' j=',j," curC=",curC," cur=",cur)
                    if(cur==What):
                        count=count+1;
                        #if(count==1):
                        ExtRowsNs.append(i)
                        IneRowsNs.append(j)
                        #}
                        if Show1Hide0==1:
                            print("cur=",cur,'== val=',What," count=",count)
                else:
                    if Show1Hide0==1:
                        print("cur=",cur,'!= val=',What)
                #}//for j
        else:#list
            for i in range(1, len(self.row)+1):
                curC=len(self.row[i-1])
                for j in range(1, curC+1):
                    pair=[]
                    if(self.IsSubMatrixAt(i, j, What)==1):
                        count=count+1
                        if(count==1):
                            ExtRowsNs.append(i)
                            IneRowsNs.append(j)
                        #}
                    #}
                #}//for j
            #}//for i
        #if What is list or single val
        if(SortByInnerRowN==1):
            for i in range(1, count+1):
                for j in range(i, count+1):
                    if(IneRowsNs[j-1]<IneRowsNs[i-1]):
                        eBuf=ExtRowsNs[i-1]
                        iBuf=IneRowsNs[i-1]
                        ExtRowsNs[i-1]=ExtRowsNs[j-1]
                        IneRowsNs[i-1]=IneRowsNs[j-1]
                        ExtRowsNs[j-1]=eBuf
                        IneRowsNs[j-1]=iBuf
                    #}
                #}
            #}
        #}
        #//write finally to vectors
        for i in range(1, count+1):
            pair=[]
            pair.append(ExtRowsNs[i-1])
            pair.append(IneRowsNs[i-1])
            R.append(pair)
        if Show1Hide0==1:
            print("Seek (single val) finishes working")
        return R
    #}//fn
    #def Seek(self, val, SortByInnerRowN=0, Show1Hide0=1):
    #    #int *NE=NULL, *NI=NULL, curC, n;
    #    if Show1Hide0==1:
    #        print("Seek (single val) starts working")
    #    count=0#;
    #    R=[]
    #    ExtRowsNs=[]
    #    IneRowsNs=[]
    #    #T cur;
    #    #Array2DSize Inf=DefInfo(InfoExt);
    #    #//seek
    #    for i in range(1, len(self.row)+1):
    #        curC=len(self.row[i-1])
    #        for j in range(1, curC+1):
    #            pair=[]
    #            cur=self.row[i-1][j-1]
    #            if Show1Hide0==1:
    #                print("i=",i,' j=',j," curC=",curC," cur=",cur)
    #            if(cur==val):
    #                count=count+1;
    #                #if(count==1):
    #                ExtRowsNs.append(i)
    #                IneRowsNs.append(j)
    #                #}
    #                if Show1Hide0==1:
    #                    print("cur=",cur,'== val=',val," count=",count)
    #            else:
    #                if Show1Hide0==1:
    #                    print("cur=",cur,'!= val=',val)
    #        #}//for j
    #    #}//for i
    #    #//sort found
    #    if(SortByInnerRowN==1):
    #        for i in range(1, count+1):
    #            for j in range(i, count+1):
    #                if(IneRowsNs[j-1]<IneRowsNs[i-1]):
    #                    eBuf=ExtRowsNs[i-1]
    #                    iBuf=IneRowsNs[i-1]
    #                    ExtRowsNs[i-1]=ExtRowsNs[j-1]
    #                    IneRowsNs[i-1]=IneRowsNs[j-1]
    #                    ExtRowsNs[j-1]=eBuf
    #                    IneRowsNs[j-1]=iBuf
    #                #}
    #            #}
    #        #}
    #    #}
    #    #//write finally to vectors
    #    for i in range(1, count+1):
    #        pair=[]
    #        pair.append(ExtRowsNs[i-1])
    #        pair.append(IneRowsNs[i-1])
    #        R.append(pair)
    #    if Show1Hide0==1:
    #        print("Seek (single val) finishes working")
    #    return R
    ##}//fn
    #def Seek(self, submatrix, SortByInnerRowN=0):
    #    #int *NE=NULL, *NI=NULL, curC, n;
    #    count=0#;
    #    R=[]
    #    ExtRowsNs=[]
    #    IneRowsNs=[]
    #    #T cur;
    #    #Array2DSize Inf=DefInfo(InfoExt);
    #    #//seek
    #    for i in range(1, len(self.row)+1):
    #        curC=len(self.row[i-1])
    #        for j in range(1, curC+1):
    #            pair=[]
    #            if(self.IsSubMatrixAt(i, j, submatrix)==1):
    #                count=count+1
    #                if(count==1):
    #                    ExtRowsNs.append(i)
    #                    IneRowsNs.append(j)
    #                #}
    #            #}
    #        #}//for j
    #    #}//for i
    #    #//sort found
    #    if(SortByInnerRowN==1):
    #        for i in range(1, count+1):
    #            for j in range(i, count+1):
    #                if(IneRowsNs[j-1]<IneRowsNs[i-1]):
    #                    eBuf=ExtRowsNs[i-1]
    #                    iBuf=IneRowsNs[i-1]
    #                    ExtRowsNs[i-1]=ExtRowsNs[j-1]
    #                    IneRowsNs[i-1]=IneRowsNs[j-1]
    #                    ExtRowsNs[j-1]=eBuf
    #                    IneRowsNs[j-1]=iBuf
    #                #}
    #            #}
    #        #}
    #    #}
    #    #//write finally to vectors
    #    for i in range(1, count+1):
    #        pair=[]
    #        pair.append(ExtRowsNs[i-1])
    #        pair.append(IneRowsNs[i-1])
    #        R.append(pair)
    #    return R
    ##}//fn

    def SubMatrix(self, ER1N, ER2N, IR1N, IR2N, DfltVal=0):
        #CurRow=[]
        #T CurElement, DfltValFin;
        R=[]
        LIn=len(self.row)
        Lmax=self.GetMaxLength()
        #QString MsgTxtLine;
        #MsgTxtLine="SubMatrix starts working";
        #print(MsgTxtLine);
        ER2Ncorr=ER2N
        IR2Ncorr=IR2N
        #Lcur, Lmin, NewExtRowN;
        #InfIniSub.L=0;
        #//InfIniSub.Cs=NULL;
        #InfIniSub.C=0;
        if(ER2N>LIn):
            ER2Ncorr=LIn
        #}
        if(IR2N>Lmax):
            IR2Ncorr=Lmax
        #}
        if(len(self.row)>0 and ER1N>=1 and ER1N<=ER2Ncorr and IR1N>=1 and IR1N<=IR2Ncorr):
            LExtNew=ER2Ncorr-ER1N+1
            LIneNew=IR2Ncorr-IR1N+1
            #R.SetSize(&InfNew, WriteInfo, &InfIniSub);
            for i in range(ER1N, ER2Ncorr+1):
                NewExtRowN=i-ER1N+1
                CurRow=[]
                Lcur=self.GetLengthN(i)
                if(Lcur>LIneNew):
                    Lmin=LIneNew
                else:
                    Lmin=Lcur
                #}
                for j in range(IR1N, IR1N+Lmin-1+1):
                    CurElement=self.row[i-1][j-1]
                    CurRow.append(CurElement)
                #}
                for j in range(Lmin+1, LIneNew+1):
                    CurRow.append(DfltVal)
                #}
                #//
                #//void SetExtRow(int N, std::vector<T>arr, Array2DSize*InfoExt=NULL, TRowSetConfig*RowSetCfgExt=NULL, T*DfltVal=NULL){
                R.append(CurRow)
            #}
        #}
        #MsgTxtLine="SubMatrix finishes working";
        #print(MsgTxtLine);
        return R
    #}

# ---------------------------------------------------------------------------------------------------------------------------------------------------------
    

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
            
        
            
                
