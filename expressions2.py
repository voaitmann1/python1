class QueryPart:
    def __init__(self):
        self.QOpenBrackets=0
        self.QShutBrackets=0
        self.val1=0
        self.val2=0
        self.Op_ET1NE2GT3LT4GE5LE6=1
        self.Af_Or1And2EqSgnCalc3=2

    def calc(self):
        y=0
        if self.Op_ET1NE2GT3LT4GE5LE6==1:
            if self.val1==self.val2:
                print("val1=",self.val1," = val2=",self.val2)
                y=1
            else:
                print("val1=",self.val1," != val2=",self.val2)
        elif self.Op_ET1NE2GT3LT4GE5LE6==2:
            if self.val1!=self.val2:
                print("val1=",self.val1," != val2=",self.val2)
                y=1
            else:
                print("val1=",self.val1," == val2=",self.val2)
        elif self.Op_ET1NE2GT3LT4GE5LE6==3:
            if self.val1>self.val2:
                print("val1=",self.val1," > val2=",self.val2)
                y=1
            else:
                print("val1=",self.val1," <= val2=",self.val2)
        elif self.Op_ET1NE2GT3LT4GE5LE6==4:
            if self.val1<self.val2:
                print("val1=",self.val1," < val2=",self.val2)
                y=1
            else:
                print("val1=",self.val1," >= val2=",self.val2)
        elif self.Op_ET1NE2GT3LT4GE5LE6==5:
            if self.val1>=self.val2:
                print("val1=",self.val1," >= val2=",self.val2)
                y=1
            else:
                print("val1=",self.val1," < val2=",self.val2)
        elif self.Op_ET1NE2GT3LT4GE5LE6==6:
            if self.val1<=self.val2:
                print("val1=",self.val1," <= val2=",self.val2)
                y=1
            else:
                print("val1=",self.val1," > val2=",self.val2)
        return y

    def ToString(self):
        s=""
        if self.QOpenBrackets>0:
            for i in range (1, self.QOpenBrackets+1):
                s=s+"("
            s=s+" "
        s=s+str(self.val1)
        s=s+" "
        s=s+self.OpToString()
        s=s+" "
        s=s+str(self.val2)
        if self.QOpenBrackets>0:
            s=s+" "
            for i in range (1, self.QOpenBrackets+1):
                s=s+")"
        s=s+" "
        s=s+self.AfToString()
        return s

    def OpToString(self):
        s=""
        if self.Op_ET1NE2GT3LT4GE5LE6==1:
            s=s+"=="
        elif self.Op_ET1NE2GT3LT4GE5LE6==2:
            s=s+"!="
        elif self.Op_ET1NE2GT3LT4GE5LE6==3:
            s=s+"> "
        elif self.Op_ET1NE2GT3LT4GE5LE6==3:
            s=s+"< "
        elif self.Op_ET1NE2GT3LT4GE5LE6==3:
            s=s+">="
        elif self.Op_ET1NE2GT3LT4GE5LE6==3:
            s=s+"<="
        else:
            s="(.unknown.)"
        return s

    def AfToString(self):
        s=""
        if self.Af_Or1And2EqSgnCalc3==1:
            s="or "
        elif self.Af_Or1And2EqSgnCalc3==2:
            s="and"
        elif self.Af_Or1And2EqSgnCalc3==3:
            s="="
        else:
            s="(..unknown..)"
        return s

def AfToString(Af_Or1And2EqSgnCalc3):
        s=""
        if Af_Or1And2EqSgnCalc3==1:
            s="or "
        elif Af_Or1And2EqSgnCalc3==2:
            s="and"
        elif Af_Or1And2EqSgnCalc3==3:
            s="="
        else:
            s="(..unknown..)"
        return s

class AlgExprPart:
    def __init__(self):
        self.QOpenBrackets=0
        self.QShutBrackets=0
        self.val=0
        self.signPlus1Minus2=1
        self.Operator=1
        self.PreOperator=0

    def OperOrder():
        order=0
        if self.Operator==1 or self.Operator==2:
            order=1
        elif self.Operator==3 or self.Operator==4:
            order=2
        elif self.Operator==5 or self.Operator==6 or self.Operator==7:
            order=3
        return order
    
    def ToString(self):
        s=""
        if self.QOpenBrackets>0:
            for i in range (1, self.QOpenBrackets+1):
                s=s+"("
            s=s+" "
        #s=s+" "
        s=s+self.SignToString()
        #s=s+" "
        s=s+str(self.val)
        if self.QOpenBrackets>0:
            s=s+" "
            for i in range (1, self.QOpenBrackets+1):
                s=s+")"
        s=s+" "
        s=s+self.OpToString()
        return s

    def OpToString(self):
        s=""
        if isinstance(self.Operator, str):
            s=self.Operator
        elif isinstance(self.Operator, int):
            if self.Operator==1:
                s=s+"+"
            elif self.Operator==2:
                s=s+"-"
            elif self.Operator==3:
                s=s+"*"
            elif self.Operator==4:
                s=s+"/"
            elif self.Operator==5:
                s=s+"^"
            elif self.Operator==6:
                s=s+"R"
            elif self.Operator==7:
                s=s+"log"
            else:
                s="(.unknown.)"
        return s
    
    def SignToString(self):
        s=""
        if self.signPlus1Minus2==1:
            s=""
        elif self.signPlus1Minus2==2:
            s="-"
        else:
            s="(unknown)"
        return s

    def GetOperatorN(self):
        OperatorN=0
        if(isinstance(self.Operator, int)):
            OperatorN=self.Operator
        elif (isinstance(self.Operator, str)):
            if self.Operator=="+":
                OperatorN=1
            elif self.Operator=="-":
                OperatorN=2
            elif self.Operator=="*":
                OperatorN=3
            elif self.Operator=="/":
                OperatorN=4
            elif self.Operator=="**" or self.Operator=="^*":
                OperatorN=5
            elif self.Operator=="R" or self.Operator=="rad"or self.Operator=="Rad":
                OperatorN=6
            elif self.Operator=="log":
                OperatorN=7
            #
        #
        return OperatorN
    #//fn
#//class

def OperatorN(OperatorString):
    OperatorN=0
    if(isinstance(OperatorString, int)):
        OperatorN=OperatorString
    elif (isinstance(OperatorString, str)):
        if OperatorString=="+":
            OperatorN=1
        elif OperatorString=="-":
            OperatorN=2
        elif OperatorString=="*":
            OperatorN=3
        elif OperatorString=="/":
            OperatorN=4
        elif OperatorString=="**" or OperatorString=="^":
            OperatorN=5
        elif OperatorString=="R" or OperatorString=="rad"or OperatorString=="Rad":
            OperatorN=6
        elif OperatorString=="log":
            OperatorN=7
        #
    #
    return OperatorN
#

def OperatorNToString(OperatorN):
    OperatorString=""
    if(isinstance(OperatorN, str)):
        OperatorString=OperatorN
    elif (isinstance(OperatorN, int)):
        if OperatorN==1:
            OperatorString="+"
        elif OperatorN==2:
            OperatorString="-"
        elif OperatorN==3:
            OperatorString="*"
        elif OperatorN==4:
            OperatorString="/"
        elif OperatorN==5:
            OperatorString="**"
        elif OperatorN==6:
            OperatorString="R"
        elif OperatorN==7:
            OperatorString="log"
        #
    #
    return OperatorString
#

def operatorNToString(OperatorN, TypeN_Logical2Arythmetic1):
    OperatorString=""
    if TypeN_Logical2Arythmetic1==0:
        if isinstance(OperatorN, str):
            OperatorString=OperatorN
        else:
            if OperatorN==0:
                OperatorString="or"
            elif OperatorN==1:
                OperatorString="and"
            #
        #
    else:
        OperatorString=OperatorNToString(OperatorN)
    #
    return OperatorString
#
        

def OperOrder(OperatorN):
    order=0
    if OperatorN==1 or OperatorN==2:
        order=1
    elif OperatorN==3 or OperatorN==4:
        order=2
    elif OperatorN==5 or OperatorN==6 or OperatorN==7:
        order=3
    #
    return order

def AfToString(Af_Or1And2EqSgnCalc3):
        s=""
        if Af_Or1And2EqSgnCalc3==1:
            s="or "
        elif Af_Or1And2EqSgnCalc3==2:
            s="and"
        elif Af_Or1And2EqSgnCalc3==3:
            s="="
        else:
            s="(..unknown..)"
        return s

def CalcQuery_Simple(QueryParts, N):
    L=len(QueryParts)
    y=QueryParts[1-1].calc()
    c=0
    opN=0
    for i in range(2, L+1):
        c=QueryParts[i-1].calc()
        opN=QueryParts[i-1].Af_Or1And2EqSgnCalc3
        if opN==1:
            y=y+c
            if y>1:
                y=1
            #
        elif opN==2:
            y=y*c
        #
    #
    #y=QueryParts[N-1].calc()
    return y

def CheckDataBrackets(data):
    L=len(data)
    QOpenBrackets=0
    QShutBrackets=0
    QBrackets=0
    ErrorIsAtN=0
    for i in range(1, L+1):
        QOpenBrackets=data[i-1].QOpenBrackets
        QShutBrackets=data[i-1].QShutBrackets
        QBrackets=QBrackets+QOpenBrackets-QShutBrackets
        if QBrackets<0:
            ErrorIsAtN=i
    if QBrackets>0:
        ErrorIsAtN=L
    return ErrorIsAtN
         
def ExprToString(exprElementsList):
    s=""
    L=len(exprElementsList)
    for i in range(1, L+1):
        s=s+exprElementsList[i-1].ToString()
    return s
            
def Calc(x1, op, x2):
    y=0
    print("Calc starts working/ x1="+str(x1)+" op="+str(op)+" x2="+str(x2))
    op=OperatorNToString(op)
    print(" op="+str(op))
    opN=OperatorN(op)
    print(" opN="+str(opN))
    if opN==1:
        y=x1+x2
    elif opN==2:
        y=x1-x2
    elif opN==3:
        y=x1*x2
    elif opN==4:
        y=x1/x2
    elif opN==5:
        y=x1**x2
    else:
        print("operator="+str(opN))
        y=-666
    print("answer: y="+str(y)+ " Calc finishes working")
    return y

class CalcExprStrToTransmit:
    def __init__(self):
        self.N=0
        self.QOPenBrackets=0
        self.PrevOperationN=0



def CalcExpr_ConsiderOrder_NoBrackets1(DataParts, trStrGiven):
    L=len(DataParts)
    Ngiven=trStrGiven.N
    N=Ngiven
    what_Alg1Query2=0
    dataPart=0
    trStr=CalcExprStrToTransmit()
    if(L>0):
        dataPart=DataParts[1-1]
        if isinstance(dataPart, QueryPart):
            what_Alg1Query2=2
            LastOrder=3
        elif isinstance(dataPart, AlgExprPart):
            what_Alg1Query2=1
            LastOrder=4
        #
    #wu gut allmove under this, ma I n'vil waste time f'ce
    y2=0
    y3=0
    op01=trStrGiven.PrevOperationN
    op01Order=OperOrder(op01)
    op12Order=0
    op23Order=0
    if what_Alg1Query2==2:
        y1=DataParts[N-1].calc()
    elif what_Alg1Query2==1:
        y1=DataParts[N-1].val
    #
    if(what_Alg1Query2==2):
        op12=DataParts[N-1].Af_Or1And2EqSgnCalc3
        op12Order=op12
    elif(what_Alg1Query2==1):
        op12=DataParts[N-1].GetOperatorN()
        op12Order=OperOrder(op12)
    #
    op23=0
    contin=1
    print("CalcExpr_ConsiderOrder_NoBrackets starts working. N=",N)
    #if N>1:
    #    print("..."+OperatorNToString(op01)+"... "+str(y1)+" "+operatorNToString(op12, what_Alg1Query2))
    #else:
    #    print("..."+OperatorNToString(op01)+"... "+str(y1)+" "+operatorNToString(op12, what_Alg1Query2))
    #
    if(what_Alg1Query2==2):
        print("Expr y1: "+DataParts[N-1].ToString()+" = "+str(DataParts[N-1].calc()))
    elif(what_Alg1Query2==1):
        print("Expr y1: "+DataParts[N-1].ToString())
    #
    while contin==1:
        print("N="+str(N))
        print("..."+OperatorNToString(op01)+"... "+str(y1)+" "+operatorNToString(op12, what_Alg1Query2))
        #
        if N==L or N>L or op12==LastOrder or DataParts[N-1].QShutBrackets>0:
            print("Solving immediately")
            y3=y1
            print("y3="+str(y3))
            contin=0
        else:
            print("Analyzing")
            if(what_Alg1Query2==2):
                y2=DataParts[N+1-1].calc()
            elif(what_Alg1Query2==1):
                y2=DataParts[N+1-1].val
            #
            if(what_Alg1Query2==2):
                print("next Expr y2: "+DataParts[N+1-1].ToString()+" = "+ str(DataParts[N+1-1].calc()))
            elif(what_Alg1Query2==1):
                print("next Expr y2: "+DataParts[N+1-1].ToString())
            #
            if(what_Alg1Query2==2):
                op23=DataParts[N+1-1].Af_Or1And2EqSgnCalc3
                op23Order=op23
            elif(what_Alg1Query2==1):
                op23=DataParts[N+1-1].GetOperatorN()
                op23Order=OperOrder(op23)
            #
            if op12Order>=op23Order:
                if(what_Alg1Query2==2):
                    print("priority of next "+DataParts[N+1-1].AfToString()+" is NOT higher than of previous (cur) "+DataParts[N-1].AfToString())
                elif(what_Alg1Query2==1):
                    print("priority of next "+DataParts[N+1-1].OpToString()+" is NOT higher than of previous (cur) "+DataParts[N-1].OpToString())
                #
                #if op01Order>=op23Order:
                #    y3=y1
                #    contin=0
                #    print("Order of operation before is NOT LOWER than next. so y3="+str(y3))
                #else:
                if what_Alg1Query2==2:
                    if op12==1:
                        y3=y1+y2
                        if y3>1:
                            y3=1
                        print(y1,"+",y2,"=",y3)
                    elif op12==2:
                        y3=y1*y2
                        print(y1,"*",y2,"=",y3)
                    #
                elif what_Alg1Query2==1:
                    y3=Calc(y1, op12, y2)
                    print("y1="+str(y1)+" op12="+str(op12)+" y2="+str(y2)+" = y3 = "+str(y3))
                #
                #if N+2<=L:
                #     N=N+2
                #
                if N+1<=L:
                    N=N+1#ob y2=y[N+1], = y[(Ngiven+1)+1]
                    y1=y3
                    op12=op23
                    if(what_Alg1Query2==2):
                        op12Order=op12
                    elif(what_Alg1Query2==1):
                        op12Order=OperOrder(op12)
                    #
                    if(what_Alg1Query2==2):
                        print("_Now y1 = "+str(y1)+" op12 = "+str(DataParts[N+1-2-1].AfToString())+"="+AfToString(op12))
                    elif(what_Alg1Query2==1):
                        print("Now_ y1 = "+str(y1)+" op12 = "+str(DataParts[N+1-2-1].OpToString())+"="+OperatorNToString(op12))
                    #
                else:
                    print("_last expr reached")
                    contin=0
                #
            #
            else: #op12Order<op23Order:
                if(what_Alg1Query2==2):
                    print("priority of next "+DataParts[N+1-1].AfToString()+" IS higher than of previous (cur) "+DataParts[N-1].AfToString())
                elif(what_Alg1Query2==1):
                    print("priority of next "+DataParts[N+1-1].OpToString()+" IS higher than of previous (cur) "+DataParts[N-1].OpToString())
                #
                if N+1<=L:
                    N=N+1
                    trStr.N=N
                    trStr.PrevOperationN=op12
                    y2, N = CalcExpr_ConsiderOrder_NoBrackets1(DataParts, trStr)
                    print("returninhg(0th) to fn Ngiven="+str(Ngiven)+" now N="+str(N)+" y2="+str(y2))
                    if(what_Alg1Query2==2):
                        if op12==1:
                            y3=y1+y2
                            #if y3>1:
                            #    y3=1
                            #
                        elif op12==2:
                            y3=y1*y2
                        #
                    elif(what_Alg1Query2==1):
                        y3=Calc(y1, op12, y2)
                    #
                    y1=y3
                    op12=op23
                    #
                    if N==L:
                        print("___last expr reached")
                        contin=0
                    #
                    #if N==L:
                    #    N=N-1
                    #    if(what_Alg1Query2==2):
                    #        y2=DataParts[N+1-1].calc()
                    #    elif(what_Alg1Query2==1):
                    #        y2=DataParts[N+1-1].val
                    #    
                    #    y3=Calc(y1, op12, y2)
                    #    print("Now__ y1 = "+str(y1)+" op12 = "+str(DataParts[N+1-2-1].OpToString())+"="+OperatorNToString(op12))
                    #    print("___last expr reached")
                    #    contin=0
                    #
                    #print("returninhg(1) to fn Ngiven="+str(Ngiven)+" now N="+str(N)+" y3="+str(y3))
                else:
                    print("last expr reached_")
                    contin=0
                #
            #if order <>
            print("returninhg(2) to fn N",Ngiven)
        #if N==L or >
    #while
    print("CalcExpr_ConsiderOrder_NoBrackets finishes working. N-=",Ngiven," y3=",y3)
    #return y3
    return y3, N
   

#a= QueryPart()
#a.val1=12
#a.val2=12

#quer=[]
#quer.append(a)

#y=Calc(quer, 1)
#print("y=",y)

#a.val1=12
#a.val2=14
#a.Op_ET1NE2GT3LT4GE5LE6=4

#quer=[]
#quer.append(a)

#y=Calc(quer,1)
#print("y=",y)

# 1+1*0=  (order)  =1+(1*0)=1+0=1
# 1+1*0= (no order)=(1+1)*0=2*0=0

# 10==11 or 12==12 or 13!=12 and 14>14 and 16==16
#    0   +     1   +    1     *    0    *    1

data=[]

a= QueryPart()
a.val1=10
a.val2=11
a.Op_ET1NE2GT3LT4GE5LE6=1#==, 1
a.Af_Or1And2EqSgnCalc3=1
data.append(a)

a= QueryPart()
a.val1=12
a.val2=12
a.Op_ET1NE2GT3LT4GE5LE6=1#==, 1
a.Af_Or1And2EqSgnCalc3=1
data.append(a)

a= QueryPart()
a.val1=13
a.val2=12
a.Op_ET1NE2GT3LT4GE5LE6=2#!=, 
a.Af_Or1And2EqSgnCalc3=2
data.append(a)

a= QueryPart()
a.val1=14
a.val2=15
a.Op_ET1NE2GT3LT4GE5LE6=3#>
a.Af_Or1And2EqSgnCalc3=2#3
data.append(a)

a= QueryPart()
a.val1=16
a.val2=16
a.Op_ET1NE2GT3LT4GE5LE6=1#==, 1
a.Af_Or1And2EqSgnCalc3=1
data.append(a)


print("Calculating Query\n")

L=len(data)
s=""
for i  in range(1, L+1):
    s=s+data[i-1].ToString()
print("solving expr: "+s)

trstr=CalcExprStrToTransmit()
trstr.N=1
trstr.QOpenBrackets=data[1-1].QOpenBrackets
trstr.QShutBrackets=data[1-1].QShutBrackets

#y, N=CalcQuery_ConsiderOrder_NoBrackets(data, 1)#work't ety tak, ac y,n=...
#y, N=CalcExpr_ConsiderOrder_NoBrackets(data, 1)#work't ety tak, ac y,n=... # n'int isinstance #works somehow
y, N=CalcExpr_ConsiderOrder_NoBrackets1(data, trstr)#work't ety tak, ac y,n=... # n'int isinstance
print("Answer: y="+str(y)+" (last N="+str(N)+")")

#=========================================================================================

data=[]

a= AlgExprPart()
a.val=8
a.Operator="+"
data.append(a)

a= AlgExprPart()
a.val=7
a.Operator="+"
data.append(a)

a= AlgExprPart()
a.val=6
a.Operator="*"
data.append(a)

a= AlgExprPart()
a.val=5
a.Operator="**"
data.append(a)

a= AlgExprPart()
a.val=2
a.Operator="*"
data.append(a)

a= AlgExprPart()
a.val=2
a.Operator="+"
data.append(a)

a= AlgExprPart()
a.val=10
a.Operator="*"
data.append(a)

print("\n\nCalculating AlgExpr\n")

L=len(data)
#s=""
#for i  in range(1, L+1):
#    s=s+data[i-1].ToString()
#print("solving expr: "+s)
print("solving expr: "+ExprToString(data))

trstr=CalcExprStrToTransmit()
trstr.N=1
trstr.QOpenBrackets=data[1-1].QOpenBrackets
trstr.QShutBrackets=data[1-1].QShutBrackets
trstr.PrevOperationN=0

#y, N=CalcQuery_ConsiderOrder_NoBrackets(data, 1)#work't ety tak, ac y,n=...
#y, N=CalcExpr_ConsiderOrder_NoBrackets(data, 1)#work't ety tak, ac y,n=... # n'int isinstance #works somehow
y, N=CalcExpr_ConsiderOrder_NoBrackets1(data, trstr)#work't ety tak, ac y,n=... # n'int isinstance
print("Answer: y="+str(y)+" (last N="+str(N)+")")
