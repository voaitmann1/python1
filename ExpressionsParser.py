#expressions_for

import copy

from expressions4_2 import *
from arrSearch2 import *

Const_BracketOpen_TypeN=1
Const_BracketShut_TypeN=2
Const_Number_TypeN=3
Const_Variable_TypeN=31
const_OperatorOf2Operands=4
const_OperatorOf1Operand=5
const_BooleanOperatorOf2OperandsConnectingParts=6
const_BooleanOperatorOf2OperandsInternacCalc=7
const_BooleanOperatorOf1Operand=8

  
StandardWordsAll=[
 "arcsin", "arccos", "arctan", "arcctg", 
 "arctg", "asinh", "acosh", "atanh", "log10", "floor", "trunc", "round",
 "Arsh", "Arch",  "Arth", "asin", "acos", "atan", "log2", "log3", "fact", 
 "sin", "cos", "tan", "ctg", "exp", "log", "pow", "rad", "and", "not", "xor",
 "ln", "lg", "tg" "th", "**", "or", ">=", "<=", "!=", "==",
 "!", "^", "*", "^", "+", "-", "(", ")", "=", ">", "<", "!"]

BooleanWords=[
 "and", "not", "xor",
 "or", ">=", "<=", "!=", "==",
 "=", ">", "<", "!", "(", ")"
]

BooleanWordsOnly=[
 "and", "not", "xor",
 "or", ">=", "<=", "!=", "==",
 "=", ">", "<"
]

BooleanOperatorOf2Operands=[
 "and",  "xor",
 "or", ">=", "<=", "!=", "==",
 "=", ">", "<"
]

BooleanOperatorOf2OperandsConnectingParts=[
 "and",  "xor",
 "or"
]

BooleanOperatorOf2OperandsInternalCalc=[
 ">=", "<=", "!=", "==",
 "=", ">", "<"
]

BooleanOperatorOf1Operand=[
 "not",
 "!"
]

BooleanOperatorOf1OperandOnly=[
 "not"
]

StandardWords=[
 "arcsin", "arccos", "arctan", "arcctg", 
 "arctg", "asinh", "acosh", "atanh", "log10", "floor", "trunc", "round",
 "Arsh", "Arch",  "Arth", "asin", "acos", "atan", "log2", "log3", "fact", 
 "sin", "cos", "tan", "ctg", "exp", "log", "pow", "rad",
 "ln", "lg", "tg" "th", "**",
 "!", "^", "*", "^", "+", "-", "(", ")"]

OperatorsOfOneOperand=[
 "arcsin", "arccos", "arctan", "arcctg", 
 "arctg", "asinh", "acosh", "atanh", "log10", "floor", "trunc", "round",
 "Arsh", "Arch",  "Arth", "asin", "acos", "atan", "log2", "log3", "fact", 
 "sin", "cos", "tan", "ctg", "exp", 
 "ln", "lg", "tg", "th",
 "!", "+", "-"]

OperatorsOfOneOperandOnly=[
 "arcsin", "arccos", "arctan", "arcctg", 
 "arctg", "asinh", "acosh", "atanh", "log10", "floor", "trunc", "round",
 "Arsh", "Arch",  "Arth", "asin", "acos", "atan", "log2", "log3", "fact", 
 "sin", "cos", "tan", "ctg", "exp", 
 "ln", "lg", "tg", "th",
 "!"]

OperatorsOfTwoOperands=[
 "log", "pow", "rad",
 "**",
 "^", "*", "/", "+", "-"]

OperatorsOfTwoOperandsOnly=[
 "log", "pow", "rad",
 "**",
 "^", "*", "/"]

SignsSoOperatorsOfTwoOrOneOperands=[
 "+", "-"]

Brackets=[
 "(", ")"]



def SubStrIsAtPos(where, what, PosN, vsh=0):
    countNotSame=0
    verdict=1
    whereL=0
    whatL=0
    whereCur=""
    whatCur=""
    if vsh!=0:
        print("SubStrIsAtPos starts working: trying to find "+what+" in "+where)
    #
    if isinstance(where, str) and isinstance(what, str):
        whereL=len(where)
        whatL=len(what)
        if whereL>=whatL and PosN+whatL-1<=whereL:
            for whatN in range(1, whatL+1):
                whereN=PosN+whatN-1
                whereCur=where[whereN-1]
                whatCur=what[whatN-1]
                #
                #if lowercase(where)!=lowercase(what):
                #if where!=what:
                if whereCur!=whatCur:
                    countNotSame+=1
                    verdict=0
                #
                if vsh!=0:
                    print("Comparing where["+str(whereN)+"] = "+whereCur+" with what["+str(whatN)+"]="+whatCur+" => "+str(verdict))
            #
        else:
            verdict=0
        #
    else:
        verdict=0
    #
    #return countNotSame
    if vsh!=0:
        print("SubStrIsAtPos finishes working - asnswer: "+str(verdict))
    #
    return verdict
#
            

def FindSubStr(where, what, vsh=0):
    Ns=[]
    whereL=0
    whatL=0
    r=0
    if vsh!=0:
        print("FindSubStr starts working: search "+what+" in "+where)
    #
    if isinstance(where, str) and isinstance(what, str):
        whereL=len(where)
        whatL=len(what)
        if whereL>=whatL:
            whereLastN=whereL-whatL+1
            for PosN in range(1, whereLastN+1):
                r= SubStrIsAtPos(where, what, PosN, vsh)
                if r==1:
                    Ns.append(PosN)
                #
                if vsh!=0:
                    print("Pos "+str(PosN)+": "+where[PosN-1:PosN+whatL-1-1+1]+" ?: "+what+" => "+str(r))
                #
            #
        #
    #
    if vsh!=0:
        print("FindSubStr finishes working - answer: "+str(Ns))
    #
    return Ns
#

def FindSubStr_bnd(where, what, Nini=1, vsh=0):
    R=[]
    whatN1s=[]
    whatN2s=[]
    whereN1s=[]
    whereN2s=[]
    whatPairs=[]
    wherePairs=[]
    whatPair=[]
    wherePair=[]
    whatL=len(what)
    whatN1s=FindSubStr(where, what, vsh)
    #whatN1s=FindSubStr(where, what, 0)
    Q=len(whatN1s)
    if(Q>0):
        for i in range(1, Q+1):
            N1=whatN1s[i-1]+Nini-1
            N2=N1+whatL-1
            whatN2s.append(N2)
            whatPair=[]
            whatPair.append(N1)
            whatPair.append(N2)
            whatPairs.append(whatPair)
        #
    #
    return whatPairs
#

def FindSubStr_bnd_where_after_what(where, what, Nini=1, vsh=0):
    s=""
    Pair=[]
    if vsh!=0:
        print("FindSubStr_bnd_where_after_what starts working. Splitting "+ where+" with "+what)#+" (Nini="+str(Nini)+")")
    #
    whatPairs=FindSubStr_bnd(where, what, Nini, vsh)
    if vsh!=0:
        print(what+" was found in "+where+" "+str(len(whatPairs))+" times:")
        for i in range(1, len(whatPairs)+1):
            #Pair=[]
            #Pair=whatPairs[i-1]
            s=s+str(whatPairs[i-1])
            #s=s+str(whatPairs[i-1])
        #
        print(s)
    #
    wherePairs=[]
    L=len(where)
    LastN=L+Nini-1
    if vsh!=0:
        print("Nini="+str(Nini)+" LastN="+str(LastN)+" L="+str(L))
    #
    Qwhat=len(whatPairs)
    if Qwhat>0:
        if vsh!=0:
            s="part before first: "
        #
        #if whatPairs[1-1][1-1]>1:
        if whatPairs[1-1][1-1]>Nini:
            Pair=[]
            Pair.append(Nini)#Pair.append(1)
            Pair.append(whatPairs[1-1][1-1]-1)
            wherePairs.append(Pair)
            if vsh!=0:
                #s=s+" "+str(Pair)+": "+where[Pair[1-1]:Pair[2-1]|+1]
                s=s+" "+str(Pair)+": "+where[Pair[1-1]:Pair[2-1]+1]
                print(s)
            #
        else:
            if vsh!=0:
                s=s+" No"
                print(s)
            #
        #
        if vsh!=0:
            s="parts between first and last: "
            if Qwhat<2:
                s1="No"
            else:
                s1=""
            #
        #
        for i in range(2, Qwhat+1):
            Pair=[]
            Pair.append(whatPairs[i-1-1][2-1]+1)
            Pair.append(whatPairs[i-1][1-1]-1)
            wherePairs.append(Pair)
            if vsh!=0:
                #s1=s1+" "+str(Pair)+": "+where[Pair[1-1]:Pair[2-1]|+1]
                s1=s1+" "+str(Pair)+": "+where[Pair[1-1]:Pair[2-1]+1]
            #
        #
        if vsh!=0:
            s=s+s1
            print(s)
            s="part after last: "
        #
        if whatPairs[Qwhat-1][2-1]<LastN:
            Pair=[]
            Pair.append(whatPairs[Qwhat-1][2-1]+1)
            Pair.append(LastN)
            wherePairs.append(Pair)
            if vsh!=0:
                #s=s+" "+str(Pair)+": "+where[Pair[1-1]:Pair[2-1]|+1]
                s=s+" "+str(Pair)+": "+where[Pair[1-1]:Pair[2-1]+1]
                print(s)
            #
        else:
            if vsh!=0:
                s=s+" No"
                print(s)
            #
        #
    #
    if vsh!=0:
        print("FindSubStr_bnd_where_after_what finishes working.")
    #
    return wherePairs
#

def FindSubStr_bnd_both(where, what, Nini=1, vsh=0):
    whatPairs=FindSubStr_bnd(where, what, Nini, vsh)
    wherePairs=FindSubStr_bnd_where_after_what(where, what, Nini, vsh)
    print("FindSubStr_bnd_both Answer: word "+what+" is found in word "+where+" "+str(len(whatPairs))+" times and splitted it into "+str(len(wherePairs))+" parts (Nini="+str(Nini)+")")
    return whatPairs, wherePairs

def SplitExpr(where_ini, What_ini, vsh=0, vshExt=0):
    # ce arb n'ver et I mem qod: ob ev mal 
    wherePairs2=[]
    whatPairs=[]
    whatPairsCur=[]
    wherePairsCur=[]
    Qwhat=len(What_ini)
    wherePairs1=[[1, len(where_ini)]]
    Qwhere=len(wherePairs1)
    whereQcur=0
    whatQcur=0
    where=""
    what=""
    whereN=0
    print("SplitExpr startds working") 
    for i in range(1, Qwhat+1):
        what=What_ini[i-1]
        print("\nSt.word N "+str(i)+" to split with: "+what+"\n")
        Qwhere=len(wherePairs1)
        print(" Q words to split: "+str(Qwhere)+"="+str(len(wherePairs1)))
        whereN=0
        while whereN<Qwhere:
            whereN+=1
            print("\nword curN "+str(whereN)+":")
            where=where_ini[wherePairs1[whereN-1][1-1]:wherePairs1[whereN-1][2-1]+1]
            print("- word curN "+str(whereN)+" to split: "+where+"("+str(wherePairs1[whereN-1][1-1])+"..."+str(wherePairs1[whereN-1][2-1])+")")
            #whatPairsCur, wherePairsCur= FindSubStr_bnd_both(where, what, wherePairs1[whereN-1][1-1], vsh)
            whatPairsCur, wherePairsCur= FindSubStr_bnd_both(where, what, wherePairs1[whereN-1][1-1], 0)
            #
            print(whatPairsCur, wherePairsCur)
            #
            whatQcur=len(whatPairsCur)
            whereQcur=len(wherePairsCur)
            #
            print("so word N "+str(whereN)+" - "+where+" is splitted with st.word "+what+". It was found "+str(whatQcur)+" times and splitted it into "+str(whereQcur)+" parts")
            if whatQcur>0:
                print("rest parts ("+str(whereQcur)+") are: ")
                for i1 in range(1, whereQcur+1):
                    print(str(wherePairsCur[i1-1][1-1])+"..."+str(wherePairsCur[i1-1][2-1])+": "+where_ini[wherePairsCur[i1-1][1-1]:wherePairsCur[i1-1][2-1]+1])
                #
                #I vil'te do id ud anyway, n'nur if Q found>0, ma n'arb
                print("Words were")
                for k in range(1, Qwhere+1):
                    pair=[]
                    pair=wherePairs1[k-1]
                    print(str(k)+") "+str(pair[1-1])+"..."+str(pair[2-1])+": "+where_ini[pair[1-1]:pair[2-1]+1])
                #
                print("Now. Deleting splitted word "+where+" from list")
                wherePairs2=[]
                count=0
                if whereN<2:
                    print("no words before")
                else:
                    print("writing words before (whereN="+str(whereN)+")")
                #
                for k in range (1, whereN-1+1):
                    #print(".")
                    pair=[]
                    pair=wherePairs1[k-1]
                    wherePairs2.append(pair)
                    count=k
                    print(str(count)+") "+str(pair[1-1])+"..."+str(pair[2-1])+" "+where_ini[pair[1-1]:pair[2-1]+1])
                #
                whereQcur=len(wherePairsCur)
                if whereQcur==0:
                    print("no words to del and write instead")
                else:
                    print("writing words instead deleted")
                #
                for k in range(1, whereQcur+1):
                    #print("#")
                    pair=[]
                    pair=wherePairsCur[k-1]
                    wherePairs2.append(pair)
                    count+=1
                    print(str(count)+") (newly found: "+str(k)+") "+str(pair[1-1])+"..."+str(pair[2-1])+" "+where_ini[pair[1-1]:pair[2-1]+1])
                #
                if whereN==Qwhere:
                    print("No words after")
                else:
                    print("writing words after")
                #
                for k in range (whereN+1, Qwhere+1):
                    #print("@")
                    pair=[]
                    pair=wherePairs1[k-1]
                    count+=1
                    wherePairs2.append(pair)
                    print(str(count)+") "+str(pair[1-1])+"..."+str(pair[2-1])+" "+where_ini[pair[1-1]:pair[2-1]+1])
                #
                #whereQ=len(wherePairs2)
                ##
                #print("so now "+str(whereQ)+" words are (list wherePairs2):")
                #for k in range(1, whereQ+1):
                #    print(str(wherePairs2[k-1][1-1])+"..."+str(wherePairs2[k-1][2-1])+": "+where_ini[wherePairs2[k-1][1-1]:wherePairs2[k-1][2-1]+1])
                ##    
                #nu wherePairs2 s' list o'words, qam stWords 1..j sn'da
                wherePairs1=[]
                wherePairs1=wherePairs2
                ##
                #whereQ=len(wherePairs1)
                ##
                #print("so now "+str(whereQ)+" words are (list wherePairs1 jaf assign 2):")
                #for k in range(1, whereQ+1):
                #    print(str(wherePairs1[k-1][1-1])+"..."+str(wherePairs1[k-1][2-1])+": "+where_ini[wherePairs1[k-1][1-1]:wherePairs1[k-1][2-1]+1])
                ## 
                wherePairs2=[]
                Qwhere=len(wherePairs1)
                #
                print("_so in word "+where+" st. word "+what+" is found "+str(whatQcur)+" times and splitted it into "+str(whereQcur)+" parts_")
                for k in range (1, whatQcur+1):
                    pair=[]
                    pair=whatPairsCur[k-1]
                    whatPairs.append(pair)
                    print(str(whatPairs[k-1][1-1])+"..."+str(whatPairs[k-1][2-1])+": "+where_ini[whatPairs[k-1][1-1]:whatPairs[k-1][2-1]+1])
                #
                Qwhat=len(whatPairs)
                print("in all "+str(Qwhat)+" parts of expression are st. words")
            #if whatQcur>0
            print("so now "+str(Qwhere)+" words are (list wherePairs1 af wherePairs2 s'clear'd):")
            for k in range(1, Qwhere+1):
                print(str(wherePairs1[k-1][1-1])+"..."+str(wherePairs1[k-1][2-1])+": "+where_ini[wherePairs1[k-1][1-1]:wherePairs1[k-1][2-1]+1])
            # 
            #Qwhere=len(wherePairs1)
            #ety lif StWords
            print("and list of ("+str(Qwhat)+" items) st.words found:")
            for k in range (1, Qwhat+1):
                print(str(whatPairs[k-1][1-1])+"..."+str(whatPairs[k-1][2-1])+": "+where_ini[whatPairs[k-1][1-1]:whatPairs[k-1][2-1]+1])
            #
        #
    #
    CommonList=[]
    print("Nu da parts:")
    print("ne std parts:")
    for i in range(1, Qwhere+1):
        print(str(wherePairs1[i-1][1-1])+"..."+str(wherePairs1[i-1][2-1])+": "+where_ini[wherePairs1[i-1][1-1]:wherePairs1[i-1][2-1]+1])
        Pair=[]
        Pair=wherePairs1[i-1]
        CommonList.append(Pair)
    #
    whatQ=len(whatPairs)
    print("std parts:")
    for i in range(1, whatQ+1):
        print(str(whatPairs[i-1][1-1])+"..."+str(whatPairs[i-1][2-1])+": "+where_ini[whatPairs[i-1][1-1]:whatPairs[i-1][2-1]+1])
        Pair=[]
        Pair=whatPairs[i-1]
        CommonList.append(Pair)
    #
    CommonLength=len(CommonList)
    for i in range(1, CommonLength-1+1):
        for j in range(i+1, CommonLength+1):
            if CommonList[j-1][1-1]<CommonList[i-1][1-1]:
                Pair=copy.deepcopy(CommonList[i-1])
                CommonList[i-1]=copy.deepcopy(CommonList[j-1])
                CommonList[j-1]=copy.deepcopy(Pair)
            #
        #
    #
    print("Final splitting - united and sorted parts:")
    for i in range(1, CommonLength+1):
        Pair=CommonList[i-1]
        print(str(i)+") "+str(CommonList[i-1][1-1])+"..."+str(CommonList[i-1][2-1])+" => "+where_ini[CommonList[i-1][1-1]:CommonList[i-1][2-1]+1])
    #
    print("SplitExpr finishes working")
    return CommonList
#

def SplitExpr_CorrSignsMath(expr, stdMathWords):
    iniparts=SplitExpr(expr, stdMathWords)
    NsToDel=[]
    NToDel=0
    finalParts=[]
    pchar="01234567890"
    QIni=len(iniparts)
    if QIni>0:
        for i in range (1, QIni+1):
            inipart=iniparts[i-1]
            if inipart=="+" or inipart=="-":
                if i>1:
                    pL=len(iniparts[i-1-1])
                    pchar=iniparts[i-1-1][pL-1]
                #
                if i==1 or (i>1 and iniparts[i-1-1]=="("):
                    iniparts[i-1+1]=iniparts[i-1]+iniparts[i-1+1]
                    NsToDel.append(i)
                elif i>1 and i<QIni and(pchar=="E" or pchar=="e" or pchar=="@"):
                    iniparts[i-1+1]=iniparts[i-1-1]+iniparts[i-1]+iniparts[i-1+1]
                    NsToDel.append(i-1)
                    NsToDel.append(i)
                #
            #
        #
        Mode_Del1Sel2=2
        QToDel=len(NsToDel)
        if Mode_Del1Sel2==1:
            for i in range(1, NsToDel):
                NToDel=QToDel-i+1
                del(rowP[NToDel:NToDel+1])
            #
            newParts=iniParts
        elif Mode_Del1Sel2==2:
            isMarkedN=0
            for i in range(1, QIni+1):
                isMarkedN=0
                for j in range(1, QToDel+1):
                    if NsToDel[j-1]==i:
                        isMarkedN=1
                    #
                #
                #
                if isMarkedN==0:
                    iniPart=iniparts[i-1]
                    finalParts.append(iniPart)
                #
            #
        #        
    #
    return finalParts
#



def digitOf(char, sysBase=10):
    y=-1
    if char=="0":
        y=0
    elif char=="1":
        y=1
    elif char=="2" and sysBase>2:
        y=2
    elif char=="3" and sysBase>3:
        y=3
    elif char=="4" and sysBase>4:
        y=4
    elif char=="5" and sysBase>5:
        y=5
    elif char=="6" and sysBase>6:
        y=6
    elif char=="7" and sysBase>7:
        y=7
    elif char=="8" and sysBase>8:
        y=8
    elif char=="9" and sysBase>9:
        y=9
    elif (char=="A" or char=="a") and sysBase>10:
        y=10
    elif (char=="B" or char=="b") and sysBase>11:
        y=11
    elif (char=="C" or char=="c") and sysBase>12:
        y=12
    elif (char=="D" or char=="d") and sysBase>13:
        y=13
    elif (char=="E" or char=="e") and sysBase>14:
        y=14
    elif (char=="F" or char=="f") and sysBase>15:
        y=15
    #
    return y
#

def parseNumber(numstr, sysBase=10):
    intPart=0
    fracPart=0
    fracPartDigit=0
    fracPartLen=0
    orderAbs=0
    negativeNum=0
    negativeOrder=0
    NowInt1Frac2Ord3=1
    errNs=[]
    number=0
    L=len(numstr)
    for i in range(1, L+1):
        char=numstr[i-1]
        if char=="+":
            if i==1:
                pass
            elif((numstr[i-1-1]=="E" or numstr[i-1-1]=="e")and sysBase<=10) or (numstr[i-1-1]=="@" and sysBase>10):
                pass
            else:
                 errNs.append(i)
            #
        elif char=="-":
            if i==1:
                negativeNum=1
            elif((numstr[i-1-1]=="E" or numstr[i-1-1]=="e")and sysBase<=10) or (numstr[i-1-1]=="@" and sysBase>10):
                negativeOrder=1
            else:
                errNs.append(i)
            #
        elif digitOf(char, sysBase)!=-1:
            digit=digitOf(char, sysBase)
            if NowInt1Frac2Ord3==1:
                intPart= intPart*sysBase+ digit
            elif NowInt1Frac2Ord3==2:
                fracPartLen+=1
                fracPartDigit=digit
                for j in range (1, fracPartLen+1):
                    fracPartDigit/=sysBase
                #
                fracPart+=fracPartDigit
            elif NowInt1Frac2Ord3==3:
                orderAbs=intPart*sysBase+digit
            #
        elif char=="." or char==",":
            if NowInt1Frac2Ord3<3:
                 NowInt1Frac2Ord3=3
            else:
                errNs.append(i)
            #
        #
    number=intPart+fracPart
    if orderAbs>0:
        if negativeOrder==0:
            for i in range(1, orderAbs+1):
                number*=sysBase
            #
        elif negativeOrder==1:
            for i in range(1, orderAbs+1):
                number/=sysBase
            #
        #
    #
    if negativeNum==1:
        number*=(-1)
    #
    return number, errNs
#

def StrToNum(numstr, sysBase=10):
    num=0
    errNs=[]
    num, errNs= parseNumber(numstr, sysBase)
    return num
#

def ErrsOfNum(numstr, sysBase=10):
    num=0
    errNs=[]
    num, errNs= parseNumber(numstr, sysBase)
    return errNs
#

#Const_BracketOpen_TypeN=1
#Const_BracketShut_TypeN=2
#Const_Number_TypeN=3
#Const_Variable_TypeN=31
#const_OperatorOf2Operands=4
#const_OperatorOf1Operand=5
#const_BooleanOperatorOf2OperandsConnectingParts=6
#const_BooleanOperatorOf2OperandsInternacCalc=7
#const_BooleanOperatorOf1Operand=8

def DefMathWordType(word, sysBase=10):
    typeN=0
    if ErrsOfNum(word, sysBase)==[]:
        typeN=Const_Number_TypeN
    elif word=="(":
        typeN=Const_BracketOpen_TypeN
    elif word==")":
        typeN=Const_BracketShut_TypeN
    elif arr1D_SeekValsFirstN(arr1D, BooleanOperatorOf2OperandsConnectingParts)!=0:
        typeN=const_BooleanOperatorOf2OperandsConnectingParts
    elif arr1D_SeekValsFirstN(arr1D, BooleanOperatorOf2OperandsInternalCalc)!=0:
        typeN=const_BooleanOperatorOf2OperandsInternacCalc
    elif arr1D_SeekValsFirstN(arr1D, BooleanOperatorOf1OperandOnly)!=0:
        typeN=const_BooleanOperatorOf1Operand
    else:
        typeN=Const_Variable_TypeN
    #
    return typeN
#

#(*/
# +-*/)
# )(
#xy
#++
#)x
#x(

const_ExprErr_BracketOpenAfterShut_TypeN=1
const_ExprErr_BracketOpenAfterShut_TypeName="Bracket Open After Shut"
const_ExprErr_BracketShutJustAfterOpen_TypeN=2
const_ExprErr_BracketShutJustAfterOpen_TypeName="Empty brackets"
const_ExprErr_VarOrConstJustBeforeBracketOpen_TypeN=3
const_ExprErr_VarOrConstJustBeforeBracketOpen_TypeName="Var Or Const Before Bracket Open"
const_ExprErr_VarOrConstJustAfterBracketShut_TypeN=4
const_ExprErr_VarOrConstJustAfterBracketShut_TypeName="Var Or Const Just After Bracket Shut"
const_ExprErr_VarOrConstJustOneAfterAnother_TypeN=5
const_ExprErr_VarOrConstJustOneAfterAnother_TypeName="Var Or Const Just One After Another"
const_ExprErr_OperatorsJustOneAfterAnother_TypeN=5
const_ExprErr_OperatorsJustOneAfterAnother_TypeName="Operators Just One After Another"
const_ExprErr_OperatorOf2OperandsJustAfterOpenBracket_TypeN=6
const_ExprErr_OperatorOf2OperandsJustAfterOpenBracket_TypeName="Operator Of 2 Operands Just After Open Bracket"
const_ExprErr_OperatorOf2OperandsJustBeforeShutBracket_TypeN=7
const_ExprErr_OperatorOf2OperandsJustBeforeShutBracket_TypeName="Operator Of 2 Operands Just Before Shut Bracket"


def ControlExpression(expr, sysBase=10):
    pair=[]
    exprErrs=[]
    countOpenBrackets=0
    countShutBrackets=0
    if isinstance(expr, list) and len(expr)>0:
        Qwords=len(expr)
        for  i in range(2, Qwords+1):
            Word1=expr[i-1-1]
            Word2=expr[i-1]
            Word1TypeN=DefMathWordType(Word1, sysBase)
            Word2TypeN=DefMathWordType(Word2, sysBase)
            if Word1TypeN==Const_BracketShut_TypeN and Word2TypeN==Const_BracketOpen_TypeN:
                pair=[]
                pair.append(i)
                pair.append(const_ExprErr_BracketOpenAfterShut_TypeN)
                exprErrs.append(pair)
            elif Word1TypeN==Const_BracketOpen_TypeN and Word2TypeN==Const_BracketShut_Type:
                pair=[]
                pair.append(i)
                pair.append(const_ExprErr_BracketShutJustAfterOpen_TypeN)
                exprErrs.append(pair)
            #if
        #for
    #if
    return exprErrs
#

#Const_BracketOpen_TypeN=1
#Const_BracketShut_TypeN=2
#Const_Number_TypeN=3
#Const_Variable_TypeN=31
#const_OperatorOf2Operands=4
#const_OperatorOf1Operand=5
#const_BooleanOperatorOf2OperandsConnectingParts=6
#const_BooleanOperatorOf2OperandsInternacCalc=7
#const_BooleanOperatorOf1Operand=8

            
#def ExpressionToListOfStrs(expr, stdWords=StandardWordsAll, sysBase=10):
#    wordsList=SplitExpr_CorrSignsMath(expr, stdWords)
#    element=AlgExprPart()
#    ExprPartslist=[]
#    QWords=len(wordsList)
#    if(QWords>0):
#        element.Operator=0
#        for i in range(1, QWords+1):
#            word=wordsList[i-1]
#            if DefMathWordType(word, sysBase)==Const_BracketOpen_TypeN:
#                element.
#    return ExprPartslist
#


