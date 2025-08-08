# solving expr:  +8  +7  +6  *5  **2  *2  +10 
#                1   2   3   4   5    6   7
# ce vrn arb ver ac () ma n'arb ver co ()
#
#S calc't id in () ma in brackets op01 s'0. So not do ut num af recursio be ab recursio, ma op01 - ab pre-recursio
#ma operand aab recursio assign'tc pre all. 
#et operator ms'b re-assign'd nur if recursio wa cal'd ob (), et n're-assign'd if recursio wa cal'd ob oper priori

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
        if self.QShutBrackets>0:
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
        if OperatorN==0:
            OperatorString="."
        elif OperatorN==1:
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
    #print("Calc starts working/ x1="+str(x1)+" op="+str(op)+" x2="+str(x2))
    #print("Calc starts working")
    op=OperatorNToString(op)
    #print("Calc starts working/ x1="+str(x1)+" op="+str(op)+" x2="+str(x2))
    #print(" op="+str(op))
    opN=OperatorN(op)
    #print(" opN="+str(opN))
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
    #print("answer: y="+str(y)+ " Calc finishes working")
    #print("answer: y := "+str(x1)+" "+op+" "+str(x2)+" = "+str(y)+ " - Calc finishes working")
    print("Calc works: y := "+str(x1)+" "+op+" "+str(x2)+" = "+str(y)+ " (OpN="+str(opN)+" priority: "+str(OperOrder(opN))+")")
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
        self.RecursionCallN=0
    #
#

# In see 2 varns: 1) if bracket=0, no matter: ) shut recursio,  if wa (, operator s'., so af reda ab recursio opeg s' ab prev, call'n, recursio

def CalcExpr(DataParts, trStrGiven):
    L=len(DataParts)
    Ngiven=trStrGiven.N
    if Ngiven>1:
        N=Ngiven
    #else Ngiven<L:#Ngiven=1
    elif Ngiven<L:#Ngiven=1
        N=Ngiven+1
    #
    RecursionCallN=trStrGiven.RecursionCallN+1
    
    #
    what_Alg1Query2=0
    curPart=0
    nextPart=0
    y1=0
    y2=0
    y3=0
    op01=1
    op12=0
    op23=0
    op23Order=0
    contin=0
    #lastAction=""
    rStr=CalcExprStrToTransmit()
    trStr=CalcExprStrToTransmit()
    print("CalcExpr starts working. N=",N)
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
    if Ngiven==1 or prePart.QOpenBrackets>0:
        op01=0
    else:
        op01=prePart.GetOperatorAsN()
    #
    op01Order=OperOrder(op01)
    if what_Alg1Query2==2:#uz typ'd langs os vikts!
        y1=prePart.getVal()
    elif what_Alg1Query2==1:
        y1=prePart.getVal()
    #
    if L>0 and N<=L:
        contin=1
    else:
        rStr=trStr
        print("returning: N too big") 
    #
    if RecursionCallN>2*L:
        print("stopping recursions - RecursionCallN="+str(RecursionCallN))
        contin=0
    #
    WasRecursio=0
    #
    while contin==1:
        print("Start point of cycle. N: ="+str(N))
        #
        if WasRecursio==0:
            curPart=DataParts[N-1]
            print("there was no recursion. Expr from dataFlow N "+str(N)+": "+curPart.ToString())
        else:#WasRecursio==1
            curPart=trStr.dataPart
            print("there was  recursion in jef cycle step (jef'l cycle step, jef-step o'cycle, jef-cycle-step). Expr an ef'y calc'd recursio data: "+curPart.ToString()+"( N="+str(N)+")")
            #if WasRecursio==2:#recursio wa ob ()#no, op01 s'assign'd n'hin
            #    
            ##
        #
        op12=curPart.GetOperatorAsN()
        op12Order=OperOrder(op12)       
        #
        if what_Alg1Query2==2:
            y2=curPart.getVal()
        elif what_Alg1Query2==1:
            y2=curPart.getVal()
        #
        if curPart.QShutBrackets==0 and N<L:
            #
            nextPart=DataParts[N+1-1]
            #
            op23=nextPart.GetOperatorAsN()
            op23Order=OperOrder(op23)
            #
            print("... "+operatorNToString(op01, what_Alg1Query2)+" "+str(y1)+" "+operatorNToString(op12, what_Alg1Query2)+" "+str(y2)+" "+operatorNToString(op23, what_Alg1Query2)+" ...")
        else:
            print("... "+operatorNToString(op01, what_Alg1Query2)+" "+str(y1)+" "+operatorNToString(op12, what_Alg1Query2)+" "+str(y2)+" .")
        #
        #print("... "+operatorNToString(op01, what_Alg1Query2)+" "+str(y1)+" "+operatorNToString(op12, what_Alg1Query2)+" "+str(y2)+" ...")
        #
        if trStrGiven.dataPart.QOpenBrackets>0:
            #trStr is kept
            trStr=trStrGiven
            trStr.N=N
            trStr.dataPart.QOpenBrackets-=1
            #trStr.setVal(0)
            trStr.dataPart.setOperatorN(0)
            trStr.RecursionCallN=RecursionCallN+1
            print("Case 1 - starting recursion without any calcs - bracket open (left: "+str(trStr.dataPart.QOpenBrackets)+"). Starting recursion (ob ()) with operand="+str(trStrGiven.dataPart.getVal())+", operator=0, N="+str(N))
            trStr=CalcExpr(DataParts, trStr)
            N=trStr.N
            print("Returning from recursion N="+str(N)+" to Ngiven="+str(Ngiven)+" and stopping recursion - expression will be at current N after no brackets left")
            WasRecursio=1
            contin=0#Q'tak?
            #
            rStr.dataPart.setOperatorN(op01)#arb ac ce
            rStr.dataPart.setVal(trStr.dataPart.getVal())#arb ac ce
            rStr.N=N#arb ac ce
        elif trStrGiven.dataPart.QShutBrackets>0 or (op01Order>=op12Order and prePart.QOpenBrackets==0) or (N==L and Ngiven>1):
            if trStrGiven.dataPart.QShutBrackets>0:
                print("Case 2.1 - finishing without any calcs: bracket shut at once")
                rStr.dataPart.QShutBrackets-=1
                trStr.dataPart.QShutBrackets-=1
                #trStr.setOperatorN(op01)#not here
            elif (op01Order>=op12Order and prePart.QOpenBrackets==0) or (N==L and Ngiven>1):
                if op01Order>=op12Order and prePart.QOpenBrackets==0: #ifwu prePart.QOpenBrackets>0, swu S n'abl adgo hin
                    print("Case 2.2 - finishing without any calcs: cur operator' priority ("+str(op12Order)+" opN="+str(op12)+" "+operatorNToString(op12, what_Alg1Query2)+") is NOT greater than of prev ("+str(op01Order)+" opN="+str(op01)+" "+operatorNToString(op01, what_Alg1Query2)+")")
                #
                if N==L and Ngiven>1:
                    print("Case 2.3 - finishing without any calcs: last expr reached but not in external function, but in some inner recursion")
                #
            #
            rStr=trStr
            rStr.N=N-1#rStr.N=N#if ac -1 anw=165, if co -1 anw=315. Ma ver=325 - ma es ety 1 gmut udce - nu arb ver
            #
            rStr.dataPart.setVal(y1)
            #if(N<L):
            rStr.dataPart.setOperatorN(op01)
            #
            contin=0
        else:#pre-brackets n'es, op01Order<op12Order
            print ("Analyzing")
            print("Brackets of parts: prePart: open: "+str(prePart.QOpenBrackets)+" shut: "+str(prePart.QShutBrackets)+"; cuPart: open: "+str(curPart.QOpenBrackets)+" shut: "+str(curPart.QShutBrackets))
            
            #if curPart.QShutBrackets>0 or (N==L and Ngiven==1):
            #    if curPart.QShutBrackets>0:
            #        print("case 3.1 - Immediate calc with stopping recursio")
            #if (op12Order>op01Order and prePart.QOpenBrackets==0 and (N==L or op12Order>=op23Order)) or curPart.QShutBrackets>0 or (N==L and Ngiven==1):#hin add avan: and curPart.QOpenBrackets==0
            if (((op12Order>op01Order and prePart.QOpenBrackets==0 and (N==L or op12Order>=op23Order)) or curPart.QShutBrackets>0)and  curPart.QOpenBrackets==0) or (N==L and Ngiven==1):#hin add avan: and curPart.QOpenBrackets==0
                print("cases 3 - immediate calc")
                WasRecursio=0
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
                #
                curPart.setVal(y1)
                #
                curPart.setOperatorN(op12)
                #
                #if N<L:#vikts: I adloc'te ce ad end et prog nu arb't ver
                #    N+=1
                ##
                if op12Order>op01Order:
                    print("Case 3.1 - Immediate calc - with continuing: priority of cur operator priority ("+str(op12Order)+" opN="+str(op12)+" "+operatorNToString(op12, what_Alg1Query2)+") IS higher than of prev ("+str(op01Order)+" opN="+str(op01)+" "+operatorNToString(op01, what_Alg1Query2)+")")
                    #
                    #contin=1
                #
                if (curPart.QShutBrackets>0)or(N==L and Ngiven==1):
                    if curPart.QShutBrackets>0:
                        print("Case 3.2.1 - Immediate calc - with stopping recursion: bracket shut in cur expr element")
                    elif N==L and Ngiven==1:
                        print("Case 3.2.2 - Immediate calc - with stopping recursion: : last expr reached - and it is not some inner recursion")
                    #
                    contin=0
                    #
                    curPart.setOperatorN(op01)
                    #
                    rStr.dataPart=curPart#
                    rStr.N=N#rStr.N=N#ce n'mut l'gefa#
                    #
                #
                if N<L:#os by id 4.1.1 et 5 nals
                    N+=1
                #
            elif op23Order>op12Order or curPart.QOpenBrackets>0:
                if N<L:
                    N+=1
                #
                trStr=trStr
                trStr.dataPart=curPart
                trStr.RecursionCallN=RecursionCallN+1
                #trStr.N=N+1#or +2? or := ?
                trStr.N=N
                print("starting recursion with ini expr data: N="+str(N)+" pre expr part: "+trStr.dataPart.ToString())
                #
                trStr=CalcExpr(DataParts, trStr)
                #jaf cycle step goe: curPart=trStr.dataPart
                #N=trStr.N-1# ja, ef-vrn wa irr: N=trStr.N
                N=trStr.N# ja, ef-vrn wa irr: N=trStr.N
                WasRecursio=1
                #contin=1
                print("returned from recursion to Ngiven="+str(Ngiven)+", from N="+str(trStr.N)+"-1="+str(N)+" now next part: "+trStr.dataPart.ToString())
            else:
                print("Not taken into consideration case!")
                print("Brackets of parts: prePart: open: "+str(prePart.QOpenBrackets)+" shut: "+str(prePart.QShutBrackets)+"; cuPart: open: "+str(curPart.QOpenBrackets)+" shut: "+str(curPart.QShutBrackets))
                print("N="+str(N)+" Ngiven="+str(Ngiven))
                if N<L:
                    print("pre oper "+operatorNToString(op01, what_Alg1Query2)+" cur oper: "+operatorNToString(op12, what_Alg1Query2)+" next oper: "+operatorNToString(op23, what_Alg1Query2))
                    print(prePart.ToString()+" "+prePart.ToString()+" "+operatorNToString(op23, what_Alg1Query2))
                else:
                    print("pre oper "+operatorNToString(op01, what_Alg1Query2)+" cur oper: "+operatorNToString(op12, what_Alg1Query2))
                    print(prePart.ToString()+" "+prePart.ToString())
                #
                print("exiting")
                contin=0
            #if
        #if
        if RecursionCallN>2*L:
            print("stopping recursions - RecursionCallN="+str(RecursionCallN))
            contin=0
        #
        if N>L:
            print("stopping cycle - N="+str(N))
            contin=0
        #
        print("End point of cycle N="+str(N)+" L="+str(L)+" contin="+str(contin))
    #while
    print("CalcExpr finishes working. Ngiven="+str(Ngiven)+" N="+str(N)+" yR="+str(rStr.dataPart.getVal())+"(full expr "+rStr.dataPart.ToString()+")")
    return rStr
#

#=====================================================================================================================

