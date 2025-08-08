import math


def polynomeEqOfPower2(a,b,c):
    ReX=[0, 0]
    ImX=[0, 0]
    d=b*b-4*a*c
    if d<0:
        ReX[1-1]=-1.0*b/(2*a)
        ReX[2-1]=ReX[1-1]
        ImX[1-1]=-1.0*math.sqrt(-d)/(2*a)
        ImX[2-1]=1.0*math.sqrt(-d)/(2*a)
    else:
        ReX[1-1]=1.0*(-b-math.sqrt(d))/(2*a)
        ReX[2-1]=1.0*(-b+math.sqrt(d))/(2*a)
        
    return[[ReX[1-1], ReX[2-1]], [ImX[1-1], ImX[2-1]]]

def polynomeEqOfPower3(c3, c2, c1, c0, vsh=0):
    if vsh==1:
        print("polynomeEqOfPower3 starts working")
        print(str(c3)+"*x^3+"+str(c2)+"*x^2+"+str(c1)+"*x"+str(c0)+"=0")
    ReX=[0, 0, 0]
    ImX=[0, 0, 0]
    ReY=[0, 0, 0]
    ImY=[0, 0, 0]
    a=1.0*c2/c3
    b=1.0*c1/c3
    c=1.0*c0/c3
    if vsh==1:
        print("a="+str(a)+" b="+str(b)+" c="+str(c))
    p=-1.0*a*a/3+b
    q=2.0*a*a*a/27-a*b/3+c
    Q=1.0*p*p*p/27+q*q/4
    if Q>=0:
        A=math.pow((-1.0*q/2+math.sqrt(Q)),1.0/3)
        B=math.pow((-1.0*q/2-math.sqrt(Q)),1.0/3)
        cosalfa=0
    else:
        A=0
        B=0
        cosalfa=-1.0*q/(2*math.sqrt(-p*p*p/27))
    alfa=math.acos(cosalfa)
    if Q>=0:
        ReY[1-1]=A+B
        ImY[1-1]=0
        ReY[2-1]=-(A+B)/2
        ImY[2-1]=0
        ReY[3-1]=-(A+B)/2
        ImY[2-1]=0
    else:
        ReY[1-1]=2*math.sqrt(-1.0*p/3)*math.cos(alfa/3)
        ImY[1-1]=0
        ReY[2-1]=2*math.sqrt(-1.0*p/3)*math.cos(1.0*alfa/3+2.0/3*math.pi)
        ImY[2-1]=(A-B)*math.sqrt(3)/2
        ReY[3-1]=2*math.sqrt(-1.0*p/3)*math.cos(1.0*alfa/3-2.0/3*math.pi)
        ImY[2-1]=-(A-B)*math.sqrt(3)/2
    for i in range(3):
        ReX[i]=ReY[i]-a/3
        ImX[i]=ImY[i]
    if vsh==1:
        #print("polynomeEqOfPower3 starts working")
        #print("p="+str(p)+" q="+str(q)+" Q="+str(Q)+" cos(alfa)="+str(cosalfa)+" alfa="+str(alfa)+" A="+str(A)+" B="+str(B))
        print("p="+str(p)+" q="+str(q)+" Q="+str(Q))
        print("cos(alfa)="+str(cosalfa)+" alfa="+str(alfa)+" A="+str(A)+" B="+str(B))
        print("polynomeEqOfPower3 finishes working")
    return [[ReX[1-1], ReX[2-1], ReX[3-1]], [ImX[1-1], ImX[2-1], ImX[3-1]]]

def polynomeEqOfPower4(c4, c3, c2, c1, c0, vsh=0):
    if vsh==1:
        print("polynomeEqOfPower4 starts working")
        print(str(c4)+"*x^4+"+str(c3)+"*x^3+"+str(c2)+"*x^2+"+str(c1)+"*x"+str(c0)+"=0")
    a=1.0*c3/c4
    b=1.0*c2/c4
    c=1.0*c1/c4
    d=1.0*c0/c4
    p=1.0*b-3.0*a*a/8
    q=1.0*a*a*a/8.0-1.0*a*b/2+c
    r=-3.0*a*a*a*a/256+1.0*a*a*b/16-1.0*c*a/4+d
    ResolvC3=2
    ResolvC2=-p
    ResolvC1=-2.0*r
    ResolvC0=r*p-q*q/4.0
    if vsh==1:
        print("polynomeEqOfPower4 starts working")
        print("a="+str(a)+" b="+str(b)+" c="+str(c)+" d="+str(d))
        print("p="+str(p)+" q="+str(q)+" r="+str(r))
        print("ResolvC3="+str(ResolvC3)+" ResolvC2="+str(ResolvC2)+" ResolvC1="+str(ResolvC1)+" ResolvC0="+str(ResolvC0))
    ResolvX=polynomeEqOfPower3(ResolvC3, ResolvC2, ResolvC1, ResolvC0)
    ResolvRel=ResolvX[0][0]
    if vsh==1:
        print("ResolvX="+str(ResolvX))
        print("ResolvRe1="+str(ResolvRel))
    Eq1C2=1
    Eq1C1=-math.sqrt(2*ResolvRel-p)
    Eq1C0=1.0*q/2/math.sqrt(2*ResolvRel-p)+ResolvRel
    Eq2C2=Eq1C2
    Eq2C1=-Eq1C1
    Eq2C0=-1.0*q/2/math.sqrt(2*ResolvRel-p)+ResolvRel
    if vsh==1:
        print("Quadratic Eq1:")
        print(str(Eq1C2)+"*x^2+"+str(Eq1C1)+"*x+"+str(Eq1C0)+"=0")
        print("Quadratic Eq2:")
        print(str(Eq2C2)+"*x^2+"+str(Eq2C1)+"*x+"+str(Eq2C0)+"=0")
    RootSqEq1=polynomeEqOfPower2(Eq1C2, Eq1C1, Eq1C0)
    RootSqEq2=polynomeEqOfPower2(Eq2C2, Eq2C1, Eq2C0)
    if vsh==1:
        print("Quadratic Eq1:")
        print(str(RootSqEq1))
        print("Quadratic Eq2:")
        print(str(RootSqEq2))
    XR=[]
    XI=[]
    X=[]
    YR=[]
    YI=[]
    Y=[]
    XR.append(RootSqEq1[1-1][1-1])
    XR.append(RootSqEq1[1-1][2-1])
    XR.append(RootSqEq2[1-1][1-1])
    XR.append(RootSqEq2[1-1][2-1])
    #
    XI.append(RootSqEq1[2-1][1-1])
    XI.append(RootSqEq1[2-1][2-1])
    XI.append(RootSqEq2[2-1][1-1])
    XI.append(RootSqEq2[2-1][2-1])
    #
    for i in range(4):
        YR.append(XR[i]-a/4)
        YI.append(XI[i])
    if vsh==1:
        print("polynomeEqOfPower4 finishes working")
    #return[[RootSqEq1[1-1][1-1], RootSqEq1[2-1][1-1], RootSqEq2[1-1][1-1], RootSqEq2[2-1][1-1]],
    #       [RootSqEq1[1-1][2-1], RootSqEq1[2-1][2-1], RootSqEq2[1-1][2-1], RootSqEq2[2-1][2-1]]]
    return [YR, YI]

def polynomeEqGenerator(R):#arr - list of roots
    Ord=len(R)
    c=[]
    for i in range(Ord):
        cl=[]
        for j in range(Ord):
            cl[j]=0
        c.append(cl)
    for n in range(0, Ord+1):
        for i in range(0, Ord+1):
            if n==0 or i>n:
                c[n][i]=0
            else:
                if n==2:
                    if i==2:
                        c[n][i]=1
                    else:
                        if i>0:
                            c[n][i]=-(R[1-1]+R[2-1])
                        else:
                            c[n][i]=1
                            for j in range(1, n+1):
                                c[n][i]*=R[j-1]
                else:
                    if i==n:
                        c[n][i]=c[n-1][i-1]
                    else:
                        if i==0:
                            c[n][i]=-R[n-1]*c[n-1][i]
                        else:
                            c[n][i]=c[n-1][i-1]-R[n-1]*c[n-1][i]
    #
    C=[]
    for i in range(Ord):
        C.append(c[Ord][i])
    return C

def polynomeEqGeneratorAllRecur(R, vsh=0):
    Ord=len(R)
    c=[]
    for n in range(0, Ord+1):
        cr=[]
        for i in range(0, n+1):#(0, Ord+1):
            cr.append(0)
        c.append(cr)
    for n in range(0, Ord+1):
        s=""
        for i in range(0, n+1):#(0, Ord+1):
            
            if n==0 or i>n:
                c[n][i]=0
            else:
                if n==1:
                    if i==1:
                        c[n][i]=1
                    else:
                        c[n][i]=R[1-1]
                elif n==2:
                    if i==2:
                        c[n][i]=1
                    else:
                        if i==0:
                            m=1
                            for j in range(1, n+1):
                                m*=R[j-1]
                            c[n][i]=m
                        else:
                            c[n][i]=-(R[1-1]+R[2-1])
                else:
                    if i==n:
                        c[n][i]=c[n-1][i-1]#exnot
                    else:
                        if i==0:
                            c[n][i]=-R[n-1]*c[n-1][i]
                        else:
                            c[n][i]=c[n-1][i-1]-R[n-1]*c[n-1][i]
            s+=str(c[n][i])+" "
            #print("->:"+str(c[n]))
        if vsh==1:
            print(s)
            print(".")
    if vsh==1:
        print("answer: ")
        printListAsPolynome(polynomeCoefs, 0)
    return c
                            
def polynomeEqGenerator(X):
    C1=polynomeEqGeneratorAllRecur(X)
    Ord=len(C1)
    C2=C1[Ord-1]
    return C2
