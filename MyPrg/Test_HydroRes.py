from  HydroRes import *

X=[4,1,3,2,6,4,8,7,4]
print("Ha row")
print(X)
print("Sort descending")
X=Sort(X,1)
print(X)
print("Ha row")
X=[4,1,3,2,6,4,8,7,4]
print(X)
print("Sort ascending")
X=Sort(X)
print(X)
print("ins 5")
X=InsToSucc(5,X)
print(X)
print("ins 0")
X=InsToSucc(0,X)
print(X)
print("ins 10")
X=InsToSucc(10,X)
print(X)
print("ins 6")
X=InsToSucc(6,X)
print(X)
print("\n\n")
X=[4,1,3,2,6,4,8,7,4]
X=Sort(X)
x=5
pos=DefPositionInSuccession(x, X, 1)
print("pos 1: ",pos)
print("pos 2: ",pos.__str__())
print("\n\n")
#
R1=HResSimple(1)
R11=HResSimple(11,0)
R12=HResSimple(12,1)
R121=HResSimple(2)
R122=HResSimple(5)
R12.Add(R121)
R12.Add(R122)
R1.Add(R11)
R1.Add(R12)
vsh=0#vsh=1
k=R1.Calc(vsh)
print("ANSWER: k="+str(k))
#
#
print("\nStartRec")
data=RecStr(QVals, QNumerats)
data.N=1
print(data)
data=RecSearch(data, 1)
print(data)
Q=len(data.lst)
if(Q>0):
    print("answer:")
    for i in range(1,Q+1):
        Sum=0
        st=str(i)+") "
        for j in range(1, data.QVals+1):
            el=data.lst[i-1]
            c=el[j-1]
            Sum=Sum+c
            st=st+str(c)
            if j<data.QVals:
                st=st+" + "
            #print( 
        st=st+" = "+str(Sum)
        print(st)
print("FinishRec") 
