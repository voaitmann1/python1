QVals=4
QNumerats=4
Denomin=QVals*QNumerats
Show1Hide0=1
#
p_st=[]
dp=Denomin/(QNumerats-0)
#print("dp=",dp)
for i in range(0, QNumerats+1):
    if i==0:
        p_st.append(i)
        #print(i,"->",p_st[i])
        p_prev=p_st[i-1]
    else:
        p_st.append(p_st[i-1]+dp)
        #print(i,"->",p_st[i]," p prev=",p_st[i-1],"=",p_prev," dp=",dp,"p_prev+dp=",p_st[i-1]+dp)
        p_prev=p_st[i-1]
    #print(i,") ->",p_st[i-1])

p_st=[]
#print("\n\n QVals=",QVals," QNumerats=",QNumerats," Denomin=",Denomin)
dp=Denomin/(QNumerats-1)
#print("dp=",dp)
dp=Denomin/(QNumerats-1)*1.0
#print("dp=",dp)
dp=1.0*Denomin/(QNumerats-1)
#print("dp=",dp)
for i in range(1, QNumerats+1):
    p_st.append((i-1)*dp)
   # print(i,") ->",p_st[i-1]))

from random import randint
for i in range(1, QNumerats+1):
    p_rand=randint(p_st[0], p_st[len(p_st)-1])
    print(p_rand)


class PosInSucc:
    def __init__(self):
        self.EgalN=0
        self.LessN=0
        self.BoundsLess1More2Within3=0
    def __str__(self):
         st="EgalN="+str(self.EgalN)+" LessN="+str(self.LessN)+" BoundsLess1More2Within3="+str(self.BoundsLess1More2Within3)
         return st

def DefPosInSucc(x, X):
    pos=PosInSucc()
    if x<X[1-1]:
        pos.BoundsLess1More2Within3=1
    elif x>X[len(X)-1]:
        pos.BoundsLess1More2Within3=2
    else:
        pos.BoundsLess1More2Within3=3
        for i in range(1, len(X)+1):
            if x==X[i-1]:
                pos.EgalN=i
        if pos.EgalN==0:
            LastIndex=len(X)-1
            for i in range(1, LastIndex-1+1):
               if x>X[i-1] and x<X[i+1-1]:
                   pos.LessN=i
    return pos

def InsertToSucc1(x,X):
    Y=[]
    print("InsertToSucc1 starts working")
    pos=DefPosInSucc(x, X)
    print("x=",x)
    print("X:")
    print("X")
    print("Pos:")
    print(pos)
    if pos.BoundsLess1More2Within3==1:
        Y.append(x)
        for i in range(1, len(X)+1):
            Y.append(X[i-1])
    elif pos.BoundsLess1More2Within3==2:
        for i in range(1, len(X)+1):
            Y.append(X[i-1])
        Y.append(x)
    else:
        if pos.LessN>0:
            for i in range(1, pos.LessN+1):
                Y.append(X[i-1])
            Y.append(x)
            for i in range(pos.LessN+1, len(X)+1):
                Y.append(X[i-1])
        else:
            Y=X
    print("InsertToSucc1 finishes working")
    return Y

p_st1=InsertToSucc1(p_rand,p_st)
print("Result: p_rand in p_st:")
print(p_st1)
