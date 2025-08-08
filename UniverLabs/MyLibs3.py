import copy

def PossInList(X, x):
    R=[]
    Q=len(X)
    for i in range(1, Q+1):
        if x==X[i-1]:
            R.append(i)
    return R

def PosInListFirst(X, x):
    R=PossInList(X, x)
    N=0
    if R!=[]:
        N=R[1-1]
    return N

def PossInListCount(X, x):
    R=PossInList(X, x)
    Q=0
    if R!=[]:
        Q=R[1-1]
    return Q

def ArePrsentAllInAnySucc(Where, What):
    Lwhere=len(Where)
    Lwhat=len(What)
    R=0
    if Lwhat<=Lwhere:
        R=1
        for i in range(1, Lwhat+1):
            curR=PosInListFirst(Where, What[i-1])
            if curR==0:
                R=0
    return R

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

def IsSubArray1D_AtPos(Where, What, FromN):
    R=1
    Qwhere=len(Where)
    if isinstance(What, list):
        wht=copy.deepcopy(What)
    else:
        wht=[]
        wht.append(What)
    Qwhat=len(wht)
    if GetSubArray1D(Where, FromN, Qwhat)==wht:
        R=1
    else:
        R=0
    return R

def IsSubArray1D(Where, What):
    R=0
    Q=len(Where)
    Q1=len(What)
    NLast=Q-Q1+1
    for i in range(1, NLast+1):
        if IsSubArray1D_AtPos(Where, What, i)==1:
            R=1
    return R

def ClearListFromNotUniqueVals(arr):
    list1=[]
    L=len(arr)
    if L>0:
        list1.append(arr[1-1])
        for i in range(2, L+1):
            x=arr[i-1]
            if PosInListFirst(list1, x)==0:
                list1.append(x)
    return list1

def AreListsOfSameMembers(list1, list2, vsh=0):
    if vsh==1:
        print("AreListsOfSameMembers starts working")
        print("Comparing "+str(list1)+" and "+str(list2))
    R=1
    Q=len(list1)
    if(len(list2)!=Q):
        R=0
        if vsh==1:
            print("NO: they are not of equal length")
    else:
        for i in range(1, Q+1):
            curPos=PosInListFirst(list1, list2[i-1])
            if curPos==0:
                R=0
                if vsh==1:
                    print("NO: "+str(i)+": "+str(list2[i-1])+" is NOT in "+str(list1))
            else:
                if vsh==1:
                    print("ok, "+str(i)+": X2["+str(i)+"]="+str(list2[i-1])+" =X1["+str(curPos)+"]="+str(list1))
    if vsh==1:
        print("AreListsOfSameMembers finishes working")
    return R

def ListIsPresentInListAsMember_AndSuccDoesNotMatter(where, what, vsh=0):
    if vsh==1:
        print("AreListsOfSameMembers starts working")
        print("Comparing if "+str(what)+" is member of "+str(where)+" (succession does not matter)")
    y=1
    Lwhere=len(where)
    Lwhat=len(what)
    for member in where:
        curL=len(member)
        if curL!=Lwhat:
            y=0
            if vsh==1:
                print("NO: "+str(curL)+"!="+str(Lwhat))
        else:
            if vsh==1:
                print("ok, "+str(curL)+"=="+str(Lwhat))
    if y==1:
        z=0
        for member in where:
            if AreListsOfSameMembers(member, what)==1:
                z=1
                if vsh==1:
                    print("NO: "+str(member)+" and "+str(what)+" consist of different members")
            else:
                if vsh==1:
                    print("ok, "+str(member)+" and "+str(what)+" consist of same members")
        y=z
    if vsh==1:
        if y==1:
            print("Answer: "+str(what)+" is member of "+str(where)+" (succession does not matter)")
        else:
            print("Answer: "+str(what)+" is member of "+str(where)+" (succession does not matter)")
        print("AreListsOfSameMembers finishes working")
    return y

def ItemIsPresentInMemberListsOfList(Where, what):
    R=0
    for memberList in Where:
        if PosInListFirst(memberList, what)>0:
            R=1
    return R
    

class PosInSuccData:
    def __init__(self, isLess=0, isGreater=0, isWithin=0, equalN=0, lessN=0):
        self.isLess=isLess
        self.isGreater=isGreater
        self.isWithin=isWithin
        self.equalN=equalN
        self.lessN=lessN

    def getPosition(self):
        s=""
        if self.isLess==1:
            s=" value "+str(x)+"is less than minimum"# ("+str(X[1-1])+")"
        elif self.isGreater==1:
            s=" value "+str(x)+"is greater than maximum"#("+str(X[1-1])+")"
        elif self.equalN>0:
            s=" value "+str(x)+"is equal to "+str(self.equalN)+"th element"
        elif self.lessN>0:
            s=" value "+str(x)+"is between elements ["+str(self.lessN)+" and "+str(self.lessN+1)+"]"
        else:
            s=" value "+str(x)+" not defined!"
        return s

def defPosInSucc(X, x, equalityError=0, vsh=0):
    if vsh==1:
        print("defPosInSucc starts working")
    R=PosInSuccData()
    Q=len(X)
    if x<X[1-1]:
        R.isLess=1
        if vsh==1:
            print("less than min")
    elif x>X[Q-1]:
        R.isGreater=1
        if vsh==1:
            print("greater than max")
    else:
        R.isWithin=1
        if vsh==1:
            print("is within range")
            print("checking for equality")
        for i in range(1, Q+1):
            N=Q-i+1
            if vsh==1:
                print("greater than max")
            if abs(X[N-1]-x)<=equalityError:
                R.equalN=N
                if vsh==1:
                    print(str(x)+"=X["+str(N)+"="+str(R.equalN)+"]="+str(X[N-1]))
            else:
                if vsh==1:
                    print(str(x)+"=X["+str(N)+"]!="+str(X[N-1]))
        if R.equalN==0:
            if vsh==1:
                print("Not equal to any. Searching position")
            for i in range(1, Q-1+1):
                if x>X[i-1] and x<X[i+1-1]:
                    R.lessN=i
    if vsh==1:
        print("defPosInSucc finishes working")
    return R

def ConcatLists(list1, list2):
    listR=[]
    L2=len(list2)
    listR=copy.deepcopy(list1)
    for i in range(1, L2+1):
        listR.append(list2[i-1])
    return listR

def isGreater(x1, x2, equalityError=0):
    R=0
    if x1>x2 and abs(x1-x2)>equalityError:
        R=1
    return R
def isLess(x1, x2, equalityError=0):
    R=0
    if x1<x2 and abs(x1-x2)>equalityError:
        R=1
    return R
def areEqual(x1, x2, equalityError=0):
    R=0
    if abs(x1-x2)>equalityError:
        R=1
    return R
def isGreaterOrEqual(x1, x2, equalityError=0):
    R=0
    GT=isGreater(x1, x2, equalityError)
    ET=areEqual(x1, x2, equalityError)
    if  GT==1 or ET==1:
        R=1
    return R
def isLessOrEqual(x1, x2, equalityError=0):
    LT=isLess(x1, x2, equalityError)
    ET=areEqual(x1, x2, equalityError)
    if  LT==1 or ET==1:
        R=1
    return R
def notEqual(x1, x2, equalityError=0):
    R=0
    ET=areEqual(x1, x2, equalityError)
    if  ET==0:
        R=1
    return R

def FirstPairOfFirstThenSecondIsGreaterThanSecond(list1, list2):
    R=0
    if list1[1-1]>list2[1-1] or (list1[1-1]==list2[1-1] and list1[2-1]>list2[2-1]):
        R=1
    return R
def FirstPairOfFirstThenSecondIsLessThanSecond(list1, list2):
    R=0
    if list1[1-1]<list2[1-1] or (list1[1-1]==list2[1-1] and list1[2-1]<list2[2-1]):
        R=1
    return R
def FirstPairOfFirstThenSecondIsEqualToSecond(list1, list2):
    R=0
    if (list1[1-1]==list2[1-1] and list1[2-1]==list2[2-1]):
        R=1
    return R
def SortListOfPairsOfFirstThenSecondDescending(arr, vsh=0):
    data=copy.deepcopy(arr)
    if vsh==1:
        print("SortListOfPairsOfFirstThenSecondDescending staarts working")
        print("Given: "+str(data))
    Q=len(data)
    for i in range(1, Q-1+1):
        for j in range(i+1, Q+1):
            if FirstPairOfFirstThenSecondIsGreaterThanSecond(data[j-1], data[i-1])==1:
                if vsh==1:
                    print(str(data[j-1])+" is GT "+str(data[i-1]))
                buf=copy.deepcopy(data[i-1])
                data[i-1]=copy.deepcopy(data[j-1])
                data[j-1]=buf
                if vsh==1:
                    print("Now: item["+str(j)+"]="+str(data[j-1])+"item["+str(i)+"]="+str(data[i-1]))
            else:
                if vsh==1:
                    print(str(data[j-1])+" is not GT "+str(data[i-1]))
    if vsh==1:
        print("Answer: "+str(data))
        print("SortListOfPairsOfFirstThenSecondDescending finishes working")
    return data
def SortListOfPairsOfFirstThenSecondAscending(arr, vsh=0):
    data=copy.deepcopy(arr)
    if vsh==1:
        print("SortListOfPairsOfFirstThenSecondDescending staarts working")
        print("Given: "+str(data))
    Q=len(data)
    for i in range(1, Q-1+1):
        for j in range(i+1, Q+1):
            if FirstPairOfFirstThenSecondIsLessThanSecond(data[j-1], data[i-1])==1:
                if vsh==1:
                    print(str(data[j-1])+" is GT "+str(data[i-1]))
                buf=copy.deepcopy(data[i-1])
                data[i-1]=copy.deepcopy(data[j-1])
                data[j-1]=buf
                if vsh==1:
                    print("Now: item["+str(j)+"]="+str(data[j-1])+"item["+str(i)+"]="+str(data[i-1]))
            else:
                if vsh==1:
                    print(str(data[j-1])+" is not GT "+str(data[i-1]))
    if vsh==1:
        print("Answer: "+str(data))
        print("SortListOfPairsOfFirstThenSecondDescending finishes working")
    return data

#X=[10, 15, 5, 3, 8, 5, 6]
#x=5
#print("Pos of "+str(x)+" in "+str(X)+" is: "+str(PosInListFirst(X, 5)))
#print("Pos of "+str(x)+" in "+str(X)+" is: "+str(PossInList(X, 5)))
#X=[10, 20, 30, 40, 50, 60]
#x=5
#R=defPosInSucc(X, x)
#print("Pos of "+str(x)+R.getPosition())
#x=10
#R=defPosInSucc(X, x)
#print("Pos of "+str(x)+R.getPosition())
#x=27
#R=defPosInSucc(X, x)
#print("Pos of "+str(x)+R.getPosition())
#x=11
#R=defPosInSucc(X, x)
#print("Pos of "+str(x)+R.getPosition())
#x=59
#R=defPosInSucc(X, x)
#print("Pos of "+str(x)+R.getPosition())
#x=40
#R=defPosInSucc(X, x)
#print("Pos of "+str(x)+R.getPosition())
#x=60
#R=defPosInSucc(X, x)
#print("Pos of "+str(x)+R.getPosition())
#x=66
#R=defPosInSucc(X, x)
#print("Pos of "+str(x)+R.getPosition())
Where=['A', 'B', 'C', 'D', 'E']
What1=['D', 'B', 'A']
What2=['D', 'B', 'F']
What3=['A', 'B', 'C']
print("ArePrsentAllInAnySucc fn:")
print(str(What1)+" in "+str(Where)+" : "+str(ArePrsentAllInAnySucc(Where, What1)))
print(str(What2)+" in "+str(Where)+" : "+str(ArePrsentAllInAnySucc(Where, What2)))
print(str(What3)+" in "+str(Where)+" : "+str(ArePrsentAllInAnySucc(Where, What3)))
#
print("ConcatLists fn:")
print(str(What1)+" + "+str(What2)+" = "+str(ConcatLists(What1, What2)))
#
print("AreListsOfSameMembers fn:")
What3=['A', 'B', 'D']
if AreListsOfSameMembers(Where, What1)==1:
    print(str(Where)+" and "+str(What1)+" consist of same members")
else:
    print(str(Where)+" and "+str(What1)+" consist of NOT same members")
if AreListsOfSameMembers(What1, What2)==1:
    print(str(What1)+" and "+str(What2)+" consist of same members")
else:
    print(str(What1)+" and "+str(What2)+" consist of NOT same members")
if AreListsOfSameMembers(What1, What3, 0)==1:
    print(str(What1)+" and "+str(What3)+" consist of same members")
else:
    print(str(What1)+" and "+str(What3)+" consist of NOT same members")
#
print("ListIsPresentInListAsMember_AndSuccDoesNotMatter fn:")
Where=[['A', 'B', 'C'], ['A', 'B', 'D'], ['C', 'F', 'D']]
What1=['A', 'B']
What2=['C', 'D', 'F']
What3=['G', 'D', 'F']
if ListIsPresentInListAsMember_AndSuccDoesNotMatter(Where, What1)==1:
    print(str(What1)+" IS member of "+str(Where))
else:
    print(str(What1)+" is NOT member of "+str(Where))
if ListIsPresentInListAsMember_AndSuccDoesNotMatter(Where, What2)==1:
    print(str(What2)+" IS member of "+str(Where))
else:
    print(str(What2)+" is NOT member of "+str(Where))
if ListIsPresentInListAsMember_AndSuccDoesNotMatter(Where, What3)==1:
    print(str(What3)+" IS member of "+str(Where))
else:
    print(str(What3)+" is NOT member of "+str(Where))
#def ItemIsPresentInMemberListsOfList(Where, what)
Where=[['A','B','C'],['A', 'B', 'D'], ['B', 'C', 'D']]
what1='A'
what2='G'
print("ItemIsPresentInMemberListsOfList fn:")
if ItemIsPresentInMemberListsOfList(Where, what1)==1:
    print(str(what1)+" IS member of "+str(Where))
else:
    print(str(what1)+" is NOT member of "+str(Where))
if ItemIsPresentInMemberListsOfList(Where, what2)==1:
    print(str(what2)+" IS member of "+str(Where))
else:
    print(str(what2)+" is NOT member of "+str(Where))

Where=[['A','B','C'],['A', 'B', 'D'], ['B', 'C', 'D']]
what1=[['A','B','C'],['A', 'B', 'D']]
what2=[['A','B','C'],['A', 'B', 'G']]
what2=[['A','B','G'],['A', 'B', 'D']]
print("IsSubArray1D fn:")
if IsSubArray1D(Where, what1)==1:
    print(str(what1)+" IS member of "+str(Where))
else:
    print(str(what1)+" is NOT member of "+str(Where))
if IsSubArray1D(Where, what2)==1:
    print(str(what2)+" IS member of "+str(Where))
else:
    print(str(what2)+" is NOT member of "+str(Where))
print('link to array element is by essence, not by N')
arr=[1,2,3,4,5]
a4=arr[4-1]
print(arr)
print(a4)
del(arr[2-1:2+1-1])
print(arr)
print a4
