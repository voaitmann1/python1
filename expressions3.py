class QueryPart:
    def __init__(self):
        self.QOpenBrackets=0
        self.QShutBrackets=0
        self.val1=0
        self.val2=0
        self.val3=0
        self.Op_ET1NE2GT3LT4GE5LE6=1
        self.Af_Or1And2EqSgnCalc3=2

    def setVal(self, val):
        self.val3=val

    def setOperatorN(self, operatorN):
        self.Af_Or1And2EqSgnCalc3=operatorN
        
    def getVal(self):#calc(self):
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

    def GetOperatorAsN(self):
        return self.Af_Or1And2EqSgnCalc3

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

    def GetOperatorAsN(self):
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
    
    def getVal(self):
        return self.val

    def setVal(self, val):
        self.val=val

    def setOperatorN(self, operatorN):
        self.Operator=operatorN
     
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
#
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
#
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
#
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
#         

            
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
#

def ExprToString(exprElementsList):
    s=""
    L=len(exprElementsList)
    for i in range(1, L+1):
        s=s+exprElementsList[i-1].ToString()
    return s

class CalcExprStrToTransmit:
    def __init__(self):
        self.N=0
    #   self.QOpenBrackets=0
    #   self.QShutBrackets=0
    #   self.PrevOperationN=0
        self.dataPart=0
    #
#


def CalcExpr_ConsiderOrder_NoBrackets1(DataParts, trStrGiven):
    L=len(DataParts)
    Ngiven=trStrGiven.N
    N=Ngiven
    what_Alg1Query2=0
    curPart=0
    nextPart=0
    trPart="shit!"
    trStr=CalcExprStrToTransmit()
    print("length of expression = "+str(L))
    if(L>0):
        curPart=DataParts[1-1]
        #if isinstance(nextPart, QueryPart):
        if isinstance(curPart, QueryPart):
            what_Alg1Query2=2
            LastOrder=3
            curPart=QueryPart()
            nextPart=QueryPart()
            trPart=QueryPart()
            
        #elif isinstance(nextPart, AlgExprPart):
        elif isinstance(curPart, AlgExprPart):
            what_Alg1Query2=1
            LastOrder=4
            curPart=AlgExprPart()
            nextPart=AlgExprPart()
            trPart=AlgExprPart()
        #
        if isinstance(trStrGiven.dataPart, QueryPart):
            print("given (sub)structure has type QueryPart")
        elif isinstance(trStrGiven.dataPart, AlgExprPart):
            print("given (sub)structure has type AlgExprPart")
        elif isinstance(trStrGiven.dataPart, int):
            print("given (sub)structure has type int")
        else:
            print ("gi'd (sub)str n'ha types: QueryPart, AlgPart, int")
        #
    #wu gut allmove under this, ma I n'vil waste time f'ce
    y1=0
    y2=0
    y3=0
    #op01=trStrGiven.PrevOperationN
    #op01Order=OperOrder(op01)
    curPart=DataParts[N-1]
    if N==1:
        op01=0
    else:
        op01=DataParts[N-1-1].GetOperatorAsN()
        if N<L:
            nextPart=DataParts[N+1-1]
        else:
            pass
        #
    #
    op01Order=OperOrder(op01)
    op23Order=0
    if what_Alg1Query2==2:
        y1=curPart.getVal()
    elif what_Alg1Query2==1:
        y1=curPart.getVal()
    #
    op12=curPart.GetOperatorAsN()
    op12Order=OperOrder(op12)
    #
    op23=0
    contin=1
    print("CalcExpr_ConsiderOrder_NoBrackets starts working. N=",N)
    print("Expr y1: "+DataParts[N-1].ToString())   
    #
    while contin==1:
        print("N: ="+str(N))
        print("..."+OperatorNToString(op01)+"... "+str(y1)+" "+operatorNToString(op12, what_Alg1Query2))
        #
        #if N==L or N>L or op12==LastOrder or DataParts[N-1].QShutBrackets>0:
            #print("Solving immediately")
            #y3=y1
            #print("y3="+str(y3))
            #contin=0
        #else:
        if op12!=[]:
            print("Analyzing")
            if trStrGiven.dataPart.QOpenBrackets>0:
                pass
            elif trStrGiven.dataPart.QShutBrackets>0:
                pass
            else:
                if op01Order>=op12Order or N==L or trStrGiven.dataPart.QShutBrackets>0:
                    #y3=y1
                    contin=0
                    #return y1, op12
                    #print("next operation "+operatorNToString(op12, what_Alg1Query2)+"has NOT higher priority than prev: "+operatorNToString(op01, what_Alg1Query2)+". y3=y1="+str(y3))
                    if(op01Order>=op12Order):
                        print("order of prev oper "+OperatorNToString(op01)+" IS higher than of cur oper "+OperatorNToString(op12))
                    elif N==L:
                        print("N="+str(N)+"=L="+str(L))
                    elif trStrGiven.QShutBrackets>0:
                        print("Q shut brackets >0 = "+str(trStrGiven.QShutBrackets))
                    #
                    if N<L:
                        #N+=1
                        #print("Now N="+str(N))
                        pass
                    else:
                        print("and last expr reached")
                    #
                else:#op01order<op12Order:
                    #N<L ob else cond or N==L
                    N=N+1
                    #trStr.N=N
                    #trStr.PrevOperationN=op12
                    #nextPart, N = CalcExpr_ConsiderOrder_NoBrackets1(DataParts, trStr)
                    nextPart=DataParts[N-1]
                    #print("returning(0th) to fn Ngiven="+str(Ngiven)+" now N="+str(N)+" y2="+str(y2))
                    print("next Expr y2: (N="+str(N)+"): "+nextPart.ToString())
                    y2=nextPart.getVal()
                    op23=nextPart.GetOperatorAsN()
                    op23Order=OperOrder(op23)
                    #
                    if op12Order>=op23Order or N==L:#mab 'or...' s'exnot
                        print("priority of next "+nextPart.OpToString()+" is NOT higher than of cur "+curPart.OpToString())#   
                        if what_Alg1Query2==2:
                            if op12==1:
                                y3=y1+y2
                                if y3>1:
                                    y3=1
                                #
                                print(y1,"+",y2,"=",y3)
                            elif op12==2:
                                y3=y1*y2
                            #
                            print(y1,"*",y2,"=",y3)
                        elif what_Alg1Query2==1:
                            y3=Calc(y1, op12, y2)
                        #
                        print("y1="+str(y1)+" op12="+str(op12)+" y2="+str(y2)+" = y3 = "+str(y3))
                        if N==L:
                            print("_last expr reached")
                            contin=0
                        else:#N<L
                            N+=1
                            y1=y3
                            op12=op23
                            #return y1, op23
                        #
                    elif op12Order<op23Order and N<L:#=>waiting 
                        print("priority of next "+nextPart.OpToString()+" IS higher than of cur "+curPart.OpToString())# 
                        if N+1<=L:
                            N=N+1
                            trStr.N=N
                            if what_Alg1Query2==2:
                                trStr.dataPart=QueryPart()
                            elif what_Alg1Query2==1:
                                trStr.dataPart=AlgExprPart()
                            #
                            #trStr.dataPart.PrevOperationN=op12#no tal field in to class, to oper wi lir'd ab DartaParts co ver N
                            trStr.dataPart.setVal(y1)
                            print("struct transmitted before recursive call")
                            if isinstance(trStr.dataPart, QueryPart):
                                print("transmitted (sub)str has type QueryPart")
                            elif isinstance(trStr.dataPart, AlgExprPart):
                                print("transmitted (sub)str has type AlgExprPart")
                            elif isinstance(trStr.dataPart, int):
                                print("transmitted (sub)str has type int")
                            else:
                                print ("transmitted (sub)str n'ha types: QueryPart, AlgPart, int")
                            #
                            nextPart, N = CalcExpr_ConsiderOrder_NoBrackets1(DataParts, trStr)
                            print("struct returned after recursive call")
                            if isinstance(nextPart, QueryPart):
                                print("next calc'd structure has type QueryPart")
                            elif isinstance(nextPart, AlgExprPart):
                                print("next calc'd structure has type AlgExprPart")
                            elif isinstance(nextPart, int):
                                print("next calc'd structure has type int")
                            else:
                                print ("next calc'd str n'ha types: QueryPart, AlgPart, int")
                            #
                            y2=nextPart.getVal()
                            op23=nextPart.GetOperatorAsN()
                            print("returninhg(0th) to fn Ngiven="+str(Ngiven)+" now N="+str(N)+" y2="+str(y2))
                            if(what_Alg1Query2==2):
                                if op12==1:
                                    y3=y1+y2
                                    if y3>1:
                                        y3=1
                                    #
                                elif op12==2:
                                    y3=y1*y2
                                #
                            elif(what_Alg1Query2==1):
                                y3=Calc(y1, op12, y2)
                            #
                        #
                        else:#N==L:
                            print("___last expr reached")
                            contin=0
                        #
                        y1=y3
                        op01=op12
                        op12=op23
                        #
                        print("returninhg(2) to fn N",Ngiven)
                    #
                #if order <>?
            #if order <>?
        #if N==L or >
    #while
    nextPart.setVal(y3)
    nextPart.setOperatorN(op23)
    trStr.dataPart=nextPart
    trStr.N=N
    print("Answer:")
    if isinstance(trStr, CalcExprStrToTransmit):
        print("Returned structure has type CalcExprStrToTransmit")
    else:
        print ("Returned str n'ha types: CalcExprStrToTransmitt")
    #
    if isinstance(trStr.dataPart, QueryPart):
        print("next calc'd str'SubStr has type QueryPart")
    elif isinstance(trStr.dataPart, AlgExprPart):
        print("next calc'd str'SubStr has type AlgExprPart")
    elif isinstance(trStr.dataPart, int):
        print("next calc'd str'SubStr has type int")
    else:
        print ("next calc'd str'SubStr n'ha types: QueryPart, AlgPart, int")
    #
    print("CalcExpr_ConsiderOrder_NoBrackets finishes working. N-=",Ngiven," y3=",y3)
    #return y3
    return trPart, N
#   

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

#L=len(data)
#s=""
#for i  in range(1, L+1):
#    s=s+data[i-1].ToString()
#print("solving expr: "+s)#so worked
#print("solving expr: "+data.ToString())#ce n'arb
print("solving expr: "+ExprToString(data))

trstr=CalcExprStrToTransmit()
trstr.N=1
trstr.dataPart=data[1-1]

#rstr=AlgExprPart()
rstr=data[1-1]
#trstr.PrevOperationN=0

#y, N=CalcQuery_ConsiderOrder_NoBrackets(data, 1)#work't ety tak, ac y,n=...
#y, N=CalcExpr_ConsiderOrder_NoBrackets(data, 1)#work't ety tak, ac y,n=... # n'int isinstance #works somehow
rstr, N=CalcExpr_ConsiderOrder_NoBrackets1(data, trstr)#work't ety tak, ac y,n=... # n'int isinstance
y=rstr.getVal()
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

#L=len(data)
#s=""
#for i  in range(1, L+1):
#    s=s+data[i-1].ToString()
#print("solving expr: "+s)#so worked
#print("solving expr: "+data.ToString())#ce n'arb
print("solving expr: "+ExprToString(data))

trstr=CalcExprStrToTransmit()
trstr.N=1
trstr.dataPart=data[1-1]
#trstr.PrevOperationN=0

#y, N=CalcQuery_ConsiderOrder_NoBrackets(data, 1)#work't ety tak, ac y,n=...
#y, N=CalcExpr_ConsiderOrder_NoBrackets(data, 1)#work't ety tak, ac y,n=... # n'int isinstance #works somehow
rstr, N=CalcExpr_ConsiderOrder_NoBrackets1(data, trstr)#work't ety tak, ac y,n=... # n'int isinstance
y=rstr.getVal()
print("Answer: y="+str(y)+" (last N="+str(N)+")")
