from  HydroRes1w import *

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
R1=HResSimple(1, 1)
R11=HResSimple(11,11,0)
R12=HResSimple(12,12,1)
R121=HResSimple(2,121)
R122=HResSimple(5,121)
R12.AddInner(R121,1)
R12.AddInner(R122,1)
R1.AddInner(R11,1)
R1.AddInner(R12,1)
vsh=0#vsh=1
print("pipeline:")
R1.Show_WithSubElts()
print("calc k sum:")
k=R1.Calc(vsh)
print("ANSWER: k="+str(k)+"\n")
#
print("\nPipeline idem, alt build method:")
#R1=HResSimple(1, 1)
R1=HResSimple(11,1,0)
R12=HResSimple(12,12,1)
print("trying to add R12 to R1 suc")
R1.AddSucSmart(R12)
R1.k=1
print("must be added R12 to R1 suc")
print("now pipeline:")
R1.Show_WithSubElts()
R121=HResSimple(2,121)
R122=HResSimple(5,121)
R1.Elements[1-1].k=11
print("trying to add R121 to R12 par")
R12.AddParSmart(R121)
print("must be  added R121 to R12 par")
R12.Show_WithSubElts()
R1.Elements[2-1].k=12
print("trying to add R122 to R121 par")
R121.AddParSmart(R122)
R1.Show_WithSubElts()
R1.Elements[2-1].k=12
vsh=0#vsh=1
print("pipeline:")
R1.Show_WithSubElts()
print("calc k sum:")
k=R1.Calc(vsh)
print("ANSWER: k="+str(k))
#
print("\nLength:")
L=R1.vis_L(1)
print("Answer: L="+str(L)+"\n")
#
print("\nNs:")
Ns=R121.FullPresentNsList(1)
print("Ns(121): Ns=",Ns)
Ns=R11.FullPresentNsList(1)
print("Ns(11): Ns=",Ns)
Ns=R1.FullPresentNsList(1)
print("Ns(1): Ns=",Ns)
print("Ns(11): Ns=",Ns)
Ns=R1.Elements[1-1].FullPresentNsList(1)
print("Ns(1): Ns=",Ns)
print("Ns(121): Ns=",Ns)
Ns=(R1.Elements[2-1]).Elements[1-1].FullPresentNsList(1)
print("Ns(121): Ns=",Ns)
print("\n")
#
print("\nFirst absent N:")
N=(R1.Elements[2-1]).Elements[1-1].FirsrAbsentN()
print("N1(121)=",N)
print("\n")
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
