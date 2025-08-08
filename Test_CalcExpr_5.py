from expressions5 import *

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

#-----------------------------------------------------------
#trstr=CalcExprStrToTransmit()
#trstr.N=1
#trstr.dataPart=data[1-1]
#
##rstr=AlgExprPart()
#rstr=data[1-1]
##trstr.PrevOperationN=0
#
##y, N=CalcQuery_ConsiderOrder_NoBrackets(data, 1)#work't ety tak, ac y,n=...
##y, N=CalcExpr(data, 1)#work't ety tak, ac y,n=... # n'int isinstance #works somehow
#rstr=CalcExpr(data, trstr)#work't ety tak, ac y,n=... # n'int isinstance
#y=rstr.dataPart.getVal()
#N=rstr.N
#print("Answer: y="+str(y)+" (last N="+str(N)+")")
#---------------------------------------------------------

#===============================================================================================================

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
a.QOpenBrackets=1#if ce (et to af) comment, arb ver
data.append(a)

a= AlgExprPart()
a.Operator="*"
a.val=2
a.QShutBrackets=1#if ce (et to ef) comment, arb ver
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
#y, N=CalcExpr(data, 1)#work't ety tak, ac y,n=... # n'int isinstance #works somehow
rstr=CalcExpr(data, trstr)#work't ety tak, ac y,n=... # n'int isinstance
y=rstr.dataPart.getVal()
N=rstr.N
print("Answer: y="+str(y)+" (last N="+str(N)+")")
