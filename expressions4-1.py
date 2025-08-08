# solving expr:  +8  +7  +6  *5  **2  *2  +10 
#                1   2   3   4   5    6   7

class QueryPart:
    def __init__(self):
        self.QOpenBrackets=0
        self.QShutBrackets=0
        self.val1=0
        self.val2=0
        self.val3=0
        self.Op_ET1NE2GT3LT4GE5LE6=1
        self.Pre_Or1And2EqSgnCalc3=2

    def setVal(self, val):
        self.val3=val

    def setOperatorN(self, operatorN):
        self.Pre_Or1And2EqSgnCalc3=operatorN
        
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
        return self.Pre_Or1And2EqSgnCalc3

    def ToString(self):
        s=""
        if self.QOpenBrackets>0:
            for i in range (1, self.QOpenBrackets+1):
                s=s+"("
            #
            s=s+" "
        #
        s=s+str(self.val1)
        s=s+" "
        s=s+self.OpToString()
        s=s+" "
        s=s+str(self.val2)
        if self.QOpenBrackets>0:
            s=s+" "
            for i in range (1, self.QOpenBrackets+1):
                s=s+")"
            #
        #
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
        if self.Pre_Or1And2EqSgnCalc3==1:
            s="or "
        elif self.Pre_Or1And2EqSgnCalc3==2:
            s="and"
        elif self.Pre_Or1And2EqSgnCalc3==3:
            s="="
        else:
            s="(..unknown..)"
        return s

def AfToString(Pre_Or1And2EqSgnCalc3):
        s=""
        if Pre_Or1And2EqSgnCalc3==1:
            s="or "
        elif Pre_Or1And2EqSgnCalc3==2:
            s="and"
        elif Pre_Or1And2EqSgnCalc3==3:
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
        s=" "
        s=s+self.OpToString()
        if self.QOpenBrackets>0:
            for i in range (1, self.QOpenBrackets+1):
                s=s+"("
            #
        #
        s=s+self.SignToString()
        s=s+str(self.val)
        if self.QShutBrackets>0:
            #s=s+" "
            for i in range (1, self.QShutBrackets+1):
                s=s+")"
            #
        #
        s=s+" "
        #s=s+self.OpToString()
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
def AfToString(Pre_Or1And2EqSgnCalc3):
        s=""
        if Pre_Or1And2EqSgnCalc3==1:
            s="or "
        elif Pre_Or1And2EqSgnCalc3==2:
            s="and"
        elif Pre_Or1And2EqSgnCalc3==3:
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
        opN=QueryParts[i-1].Pre_Or1And2EqSgnCalc3
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

def CalcExpr_ConsiderOrder_NoBrackets(DataParts, trStrGiven):
    L=len(DataParts)
    Ngiven=trStrGiven.N
    if Ngiven>1:
        N=Ngiven
    else:
        N=Ngiven+1
    #
    what_Alg1Query2=0
    curPart=0
    nextPart=0
    #y0=0
    y1=0
    y2=0
    y3=0
    op01=1
    op12=0
    op23=0
    op34=0
    contin=0
    contini=0
    rStr=CalcExprStrToTransmit()
    trStr=CalcExprStrToTransmit()
    print("CalcExpr_ConsiderOrder_NoBrackets starts working. N=",N)
    print("length of expression = "+str(L))
    prePart=trStrGiven.dataPart
    if Ngiven==1:
        prePart.setVal(DataParts[1-1].getVal())
    #
    if isinstance(prePart, QueryPart):
        what_Alg1Query2=2
        LastOrder=3
        curPart=QueryPart()
        nextPart=QueryPart()
        rStr.dataPart=QueryPart()
        trStr.dataPart=QueryPart()
    elif isinstance(prePart, AlgExprPart):
        what_Alg1Query2=1
        LastOrder=4
        curPart=AlgExprPart()
        nextPart=AlgExprPart()
        rStr.dataPart=AlgExprPart()
        trStr.dataPart=AlgExprPart()
    #
    if isinstance(prePart, QueryPart):
        print("given (sub)structure has type QueryPart")
    elif isinstance(prePart, AlgExprPart):
        print("given (sub)structure has type AlgExprPart")
    elif isinstance(prePart, int):
        print("given (sub)structure has type int")
    else:
        print ("gi'd (sub)str n'ha types: QueryPart, AlgPart, int")
    #
    if Ngiven==1:
        op01=0
    else:
        op01=prePart.GetOperatorAsN()
    #
    op01Order=OperOrder(op01)
    if what_Alg1Query2==2:
        y1=prePart.getVal()
    elif what_Alg1Query2==1:
        y1=prePart.getVal()
    #
    if L>0 and N<=L:
        contin=1
    else:
        rStr=trStr
    #
    WasRecursio=0
    #
    while contin==1:
        print("N: ="+str(N))
        #
        #curPart=DataParts[N-1]
        if WasRecursio==0:
            curPart=DataParts[N-1]
            print("there was no recursion. Expr from dataFlow N "+str(N)+": "+curPart.ToString())
        else:
            curPart=trStr.dataPart
            print("there was  recursion in jef cycle step (jef'l cycle step, jef-step o'cycle, jef-cycle-step). Expr an ef'y calc'd recursio data: "+curPart.ToString()+"( N="+str(N)+")")
            #N-=1
            #print("N="+str(N))
        #
        op12=curPart.GetOperatorAsN()
        op12Order=OperOrder(op12)       
        #
        if what_Alg1Query2==2:
            y2=curPart.getVal()
        elif what_Alg1Query2==1:
            y2=curPart.getVal()
        #
        print("... "+operatorNToString(op01, what_Alg1Query2)+" "+str(y1)+" "+operatorNToString(op12, what_Alg1Query2)+" "+str(y2)+" ...")
        #
        if trStrGiven.dataPart.QOpenBrackets>0:
            #trStr is kept
            trStr=trStrGiven
            trStr.dataPart.QOpenBrackets-=1
            #trStr.setVal(0)
            trStr.dataPart.setOperatorN(0)
            print("Bracket open (left: "+str(trStr.dataPart.QOpenBrackets)+"). Starting recursion (ob ()) with operand="+str(trStrGiven.dataPart.getVal())+", operator=0")
            trStr=CalcExpr_ConsiderOrder_NoBrackets(DataParts, trStr)
            contin=0
        elif trStrGiven.dataPart.QShutBrackets>0:
            #pass
            # ob so n'msb. If tam wa shut prackets, to opegs ms'b gedo'd till brackets Q deqfc ad 0, et ad amda s'gi'd part ac shut brackets
            rStr=trStr
            rStr.N=N
            rStr.QShutBrackets-=1
            trStr.QShutBrackets-=1
            contin=0
        else:#no shut brackets ef
            print ("Analyzing")
            print("pre part - brackets: open: "+str(prePart.QOpenBrackets)+" shut: "+str(prePart.QShutBrackets))
            print("cur part - brackets: open: "+str(curPart.QOpenBrackets)+" shut: "+str(curPart.QShutBrackets))
            #if op01Order>=op12Order or N==L or curPart.QShutBrackets>0: #if N>L, L=0 - contin=0 et no tic cycle
            #if op01Order>=op12Order  or curPart.QShutBrackets>0: #if N>L, L=0 - contin=0 et no tic cycle
            #if op01Order>=op12Order or curPart.QShutBrackets>0 or N==L:#vikts: arb gut if no brackets
            if (op01Order>=op12Order and prePart.QOpenBrackets==0) or curPart.QShutBrackets>0 or N==L:
                #WasRecursio=0
                if op01Order>=op12Order:
                    print("case 3.1 order of cur oper "+OperatorNToString(op12)+" is NOT higher than of PREV oper "+OperatorNToString(op01)+" => returning")
                else:
                    print("(order of cur oper is NOT greater than of prev)")
                #
                if N==L:
                    print("case 3.2 last_expr_part reached")
                    #
                    if Ngiven==1:
                        #
                        if what_Alg1Query2==2:
                            if op12==1:
                                y3=y1+y2
                                if y3>1:
                                    y3=1
                                #
                                print(y1,"+",y2,"=",y3)
                            elif op12==2:
                                y3=y1*y2
                                print(y1,"*",y2,"=",y3)
                            #
                        elif what_Alg1Query2==1:
                            y3=Calc(y1, op12, y2)
                        #
                        y1=y3
                    else:
                        print("last expr reached, but not in ext fn - no calc provided")#qo?
                    #
                #
                if curPart.QShutBrackets>0:
                    print("case 3.3 brackets shut")
                #
                rStr.dataPart.setVal(y1)#mab exnot
                #rStr.dataPart.setOperatorN(op01)#mab exnot
                print("expr now is :"+rStr.dataPart.ToString())
                #
                if curPart.QShutBrackets>0:
                    print("shut brackets: "+str(curPart.QShutBrackets)+" -> "+str(curPart.QShutBrackets-1))
                    curPart.QShutBrackets-=1
                    trStr.N=N
                    trStr.QShutBrackets=curPart.QShutBrackets
                #
                if N<L:
                    #N+=1
                    #print("Now N="+str(N))
                    pass
                else:
                    print("(N="+str(N)+"=L="+str(L)+" - and last expr part reached)")
                    #contin=0
                #
                rStr.N=N
                contin=0#if comment ce - infin cycle
                WasRecursio=0
                #
                print("Now cur part="+curPart.ToString()+"( N="+str(N)+")")
            else:#N<L => N+1<=L and op01Order<op12Order#arb gut f'no brackets
            #elif (op01Order<op12Order or curPart.QOpenBrackets>0) and N<L: #mab no
                #print("N<L => N+1<=L and op01Order<op12Order")
                if N<L:
                    print("N="+str(N)+"<L="+str(L))
                else:
                    print("N="+str(N)+"=L="+str(L))
                #
                if(op01Order<op12Order):
                    print("order of cur oper "+operatorNToString(op12, what_Alg1Query2)+" is NOT greater than of cur oper "+operatorNToString(op23, what_Alg1Query2)+" => calculating this part")
                else:
                    print("(order of prev oper is NOT greater than of cur)")
                #
                if curPart.QOpenBrackets>0:
                    print("cur oper (after prev): brackets open: "+str(curPart.QOpenBrackets))
                #
                nextPart=DataParts[N+1-1]
                #
                op23=nextPart.GetOperatorAsN()
                op23Order=OperOrder(op23)
                #
                print("Now part of expr: ..."+operatorNToString(op01, what_Alg1Query2)+" "+str(y1)+" "+operatorNToString(op12, what_Alg1Query2)+" "+" "+str(y2)+" "+operatorNToString(op23, what_Alg1Query2)+" ...")
                # nouts ta y3 val, s'not nur operator order
                #
                if op12Order>=op23Order:#arb gut by no brackets
                #if op12Order>=op23Order and curPart.QOpenBrackets==0:
                    print("order of next oper "+operatorNToString(op12, what_Alg1Query2)+" is NOT greater than of cur oper "+operatorNToString(op23, what_Alg1Query2)+" => calculating this part")
                    if what_Alg1Query2==2:
                        if op12==1:
                            y3=y1+y2
                            if y3>1:
                                y3=1
                            #
                            print(y1,"+",y2,"=",y3)
                        elif op12==2:
                            y3=y1*y2
                            print(y1,"*",y2,"=",y3)
                        #
                    elif what_Alg1Query2==1:
                        y3=Calc(y1, op12, y2)
                    #
                    y1=y3
                    op12=op23
                    WasRecursio=0
                    #
                    curPart.setVal(y1)
                    curPart.setOperatorN(op12)
                    #if s'nod all ud:
                    rStr.dataPart.setVal(y1)
                    rStr.dataPart.setOperatorN(op12)
                    #
                    if N<L:
                        N=N+1#if comment ce - infin cycle
                        print("N=N+1="+str(N)+", (going to next cycle step)")
                    #else general
                else:#  op23Order>op12order or *y1*(y2
                    if op23Order>op12Order:
                        print("order of next oper "+operatorNToString(op12, what_Alg1Query2)+" IS greater than of cur oper "+operatorNToString(op23, what_Alg1Query2))
                    else:
                        print("(order of next oper "+operatorNToString(op12, what_Alg1Query2)+" is NOT greater than of cur oper "+operatorNToString(op23, what_Alg1Query2)+")")
                    #
                    if curPart.QOpenBrackets>0:
                        print("cur part: brackets open: "+str(curPart.QOpenBrackets))
                    else:
                        print("(cur part: 0brackets open)")
                    #
                    #trStr.dataPart.setVal(y2)
                    #trStr.dataPart.setOperator(op12)
                    trStr.dataPart=curPart
                    trStr.N=N+1#or +2? or := ?
                    print("starting recursion with ini expr data: N="+str(N)+" pre expr part: "+trStr.dataPart.ToString())
                    #
                    trStr=CalcExpr_ConsiderOrder_NoBrackets(DataParts, trStr)
                    #jaf cycle step goe: curPart=trStr.dataPart
                    N=trStr.N-1# ja, ef-vrn wa irr: N=trStr.N
                    WasRecursio=1
                    print("returned from recursion to Ngiven="+str(Ngiven)+", from N="+str(trStr.N)+"-1="+str(N)+" now next part: "+trStr.dataPart.ToString())
                #
                #if N<L:
                #    N=N+1
                #    print("N=N+1="+str(N)+", going to next cycle step")
                if N<L:
                    pass
                    print("(N="+str(N)+" L="+str(L)+" Ngiven="+str(Ngiven)+" -it is not last expr part)")
                else:
                    print("N="+str(N)+" L="+str(L)+" Ngiven="+str(Ngiven)+" -last expr reached now")
                    #
                    #contin=0
                    #
                    #rStr.N=N
                    #rStr.dataPart=curPart
                    #print("returned with: N="+str(N)+" expr part: "+rStr.dataPart.ToString())
                    #
                    print("going to next cycle step with: N="+str(N)+" Ngiven="+str(Ngiven)+" expr part: "+curPart.ToString())
                #
                #else:
                #    print("it is last expr part - calc immediately")
                ##    
            #operator cur and prev
        #
    #while
    print("CalcExpr_ConsiderOrder_NoBrackets finishes working. Ngiven="+str(Ngiven)+" N="+str(N)+" yR="+str(rStr.dataPart.getVal())+"(full expr "+trStr.dataPart.ToString()+")")
    return rStr
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
a.Pre_Or1And2EqSgnCalc3=1
data.append(a)

a= QueryPart()
a.val1=12
a.val2=12
a.Op_ET1NE2GT3LT4GE5LE6=1#==, 1
a.Pre_Or1And2EqSgnCalc3=1
data.append(a)

a= QueryPart()
a.val1=13
a.val2=12
a.Op_ET1NE2GT3LT4GE5LE6=2#!=, 
a.Pre_Or1And2EqSgnCalc3=2
data.append(a)

a= QueryPart()
a.val1=14
a.val2=15
a.Op_ET1NE2GT3LT4GE5LE6=3#>
a.Pre_Or1And2EqSgnCalc3=2#3
data.append(a)

a= QueryPart()
a.val1=16
a.val2=16
a.Op_ET1NE2GT3LT4GE5LE6=1#==, 1
a.Pre_Or1And2EqSgnCalc3=1
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
rstr=CalcExpr_ConsiderOrder_NoBrackets(data, trstr)#work't ety tak, ac y,n=... # n'int isinstance
y=rstr.dataPart.getVal()
N=rstr.N
print("Answer: y="+str(y)+" (last N="+str(N)+")")

#=========================================================================================

data=[]

#a= AlgExprPart()
#a.val=8
#a.Operator="+"
#data.append(a)

#a= AlgExprPart()
#a.val=7
#a.Operator="+"
#data.append(a)

#a= AlgExprPart()
#a.val=6
#a.Operator="*"
#data.append(a)

#a= AlgExprPart()
#a.val=5
#a.Operator="**"
#data.append(a)

#a= AlgExprPart()
#a.val=2
#a.Operator="*"
#data.append(a)

#a= AlgExprPart()
#a.val=2
#a.Operator="+"
#data.append(a)

#a= AlgExprPart()
#a.val=10
#a.Operator="*"
#data.append(a)

#

a= AlgExprPart()
a.Operator="+"#n'utf in expr
a.val=8
data.append(a)

a= AlgExprPart()
a.Operator="+"
a.val=7
data.append(a)

a= AlgExprPart()
a.Operator="+"
a.val=6
data.append(a)

a= AlgExprPart()
a.Operator="*"
a.val=5
data.append(a)

a= AlgExprPart()
a.Operator="**"
a.val=2
a.QOpenBrackets=1
data.append(a)

a= AlgExprPart()
a.Operator="*"
a.val=2
a.QShutBrackets=1
data.append(a)

a= AlgExprPart()
a.Operator="+"
a.val=10
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
rstr=CalcExpr_ConsiderOrder_NoBrackets(data, trstr)#work't ety tak, ac y,n=... # n'int isinstance
y=rstr.dataPart.getVal()
N=rstr.N
print("Answer: y="+str(y)+" (last N="+str(N)+")")
