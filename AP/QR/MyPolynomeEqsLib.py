import math

def MyComplex(re, im):
    re=re*(1+0j)
    im=im*(0+1j)
    return re+im

def polynomeEqOfPower2(a,b,c):
    ReX=[0, 0]
    ImX=[0, 0]
    d=b*b-4*a*c
    if d<0:
        ReX[1-1]=-b/(2*a)
        ReX[2-1]=ReX[1-1]
        ImX[1-1]=-math.sqrt(-d)/(2*a)
        ImX[2-1]=math.sqrt(-d)/(2*a)
    else:
        ReX[1-1]=(-b-math.sqrt(d))/(2*a)
        ReX[2-1]=(-b+math.sqrt(d))/(2*a)
    return[[ReX[1-1], ReX[2-1]], [ImX[1-1], ImX[2-1]]]

def polynomeEqOfPower3(c3, c2=0, c1=0, c0=0, vsh=0):
    ReX=[0, 0, 0]
    ImX=[0, 0, 0]
    ReY=[0, 0, 0]
    ImY=[0, 0, 0]
    if isinstance(c3, list):
        #c2=c3[2]
        #c1=c3[1]
        #c0=c3[0]
        #c3=c3[3]
        #
        c2=c3[2-1]
        c1=c3[3-1]
        c0=c3[4-1]
        c3=c3[1-1]
    if(vsh==1):
        print("polynomeEqOfPower3 starts working")
        print("Eq: c3="+str(c3)+" c2="+str(c2)+" c1="+str(c1)+" c0="+str(c0))
    a=1.0*c2/c3
    b=1.0*c1/c3
    c=1.0*c0/c3
    p=-a*a/3+b
    q=2*a*a*a/27-a*b/3+c
    Q=p*p*p/27+q*q/4
    if Q>=0:
        A=math.pow((-q/2+math.sqrt(Q)),1/3)
        B=math.pow((-q/2-math.sqrt(Q)),1/3)
        #cosalfa=0
    else:
        A=0
        B=0
        #cosalfa=-q/(2*math.sqrt(-p*p*p/27))
    if(vsh==1):
        print("Eq*: a="+str(a)+" b="+str(b)+" c="+str(c))
        #print("p="+str(p)+" q="+str(q)+" Q="+str(Q)+" A="+str(A)+" B="+str(B)+" cosalfa="+str(cosalfa)+" alfa="+str(alfa))
        print("p="+str(p)+" q="+str(q)+" Q="+str(Q)+" A="+str(A)+" B="+str(B))
    if Q<0:
        cosalfa=-q/(2*math.sqrt(-1.0*p*p*p/27))#else error!
    else:
        cosalfa=0
    print("cos(alfa)="+str(cosalfa))
    alfa=math.acos(cosalfa)
    if(vsh==1):
        #print("Eq*: a="+str(a)+" b="+str(b)+" c="+str(c))
        #print("p="+str(p)+" q="+str(q)+" Q="+str(Q)+" A="+str(A)+" B="+str(B)+" cosalfa="+str(cosalfa)+" alfa="+str(alfa))
        print(" cosalfa="+str(cosalfa)+" alfa="+str(alfa))
    if Q>=0:
        ReY[1-1]=A+B
        ImY[1-1]=0
        ReY[2-1]=-(A+B)/2
        ImY[2-1]=0
        ReY[3-1]=-(A+B)/2
        ImY[2-1]=0
    else:
        ReY[1-1]=2*math.sqrt(-p/3)*math.cos(alfa/3.0)
        ImY[1-1]=0
        ReY[2-1]=2*math.sqrt(-p/3)*math.cos(alfa/3.0+math.pi*2/3)
        ImY[2-1]=(A-B)*math.sqrt(3)/2
        ReY[3-1]=2*math.sqrt(-p/3)*math.cos(alfa/3.0-math.pi*2/3)
        ImY[2-1]=-(A-B)*math.sqrt(3)/2
    Y=[[ReY[1-1], ReY[2-1], ReY[3-1]], [ImY[1-1], ImY[2-1], ImY[3-1]]]
    for i in range(3):
        ReX[i]=ReY[i]-a/3
        ImX[i]=ImY[i]
    X=[[ReX[1-1], ReX[2-1], ReX[3-1]], [ImX[1-1], ImX[2-1], ImX[3-1]]]
    errs=[]
    for i in range(3):
        err=c3*MyComplex(ReX[i-1], ImX[i-1])*MyComplex(ReX[i-1], ImX[i-1])*MyComplex(ReX[i-1], ImX[i-1])+c2*MyComplex(ReX[i-1], ImX[i-1])*MyComplex(ReX[i-1], ImX[i-1])+c2*MyComplex(ReX[i-1], ImX[i-1])+c0
        errs.append(err)
    if vsh==1:
        print("Y="+str(Y))
        print("X="+str(X))
        print("errs="+str(errs))
        print("polynomeEqOfPower3 finishes working")
    return [[ReX[1-1], ReX[2-1], ReX[3-1]], [ImX[1-1], ImX[2-1], ImX[3-1]]]

def polynomeEqOfPower4(c4, c3=0, c2=0, c1=0, c0=0, vsh=1):
    if isinstance(c4, list):
        #c3=c4[3]
        #c2=c4[2]
        #c1=c4[1]
        #c0=c4[0]
        #c4=c4[4]
        #
        c3=c4[2-1]
        c2=c4[3-1]
        c1=c4[4-1]
        c0=c4[5-1]
        c4=c4[1-1]
    if vsh==1:
        print("polynomeEqOfPower4 starts working")
        print("Solving Eq: "+str(c4)+"*x^4+"+str(c3)+"*x^3+"+str(c2)+"*x^2+"+str(c1)+"*x^1+"+str(c0)+"=0")
    a=1.0*c3/c4
    b=1.0*c2/c4
    c=1.0*c1/c4
    d=1.0*c0/c4
    if vsh==1:
        print("Solving Eq*: "+"*x^4+"+str(a)+"*x^3+"+str(b)+"*x^2+"+str(c)+"*x^1+"+str(d)+"=0")
    p=b-3*a*a/8
    q=a*a*a/8-a*b/2+c
    r=-3*a*a*a*a/256+a*a*b/16-c*a/4+d
    ResolvC3=2.0
    ResolvC2=-p
    ResolvC1=-2*r
    ResolvC0=r*p-q*q/4
    if vsh==1:
        print(" p="+str(p)+" q="+str(q)+" r="+str(r)+" ResolvC3="+str(ResolvC3)+" ResolvC2="+str(ResolvC2)+" ResolvC1="+str(ResolvC1)+" ResolvC0="+str(ResolvC0))
    ResolvX=polynomeEqOfPower3(ResolvC3, ResolvC2, ResolvC1, ResolvC0, vsh)
    if vsh==1:
        print("ResolvX="+str(ResolvX)) 
    ResolvRel=ResolvX[0][0]
    Eq1C2=1
    Eq1C1=-math.sqrt(2*ResolvRel-p)
    Eq1C0=q/2/math.sqrt(2*ResolvRel-p)+ResolvRel
    Eq2C2=Eq1C2
    Eq2C1=-Eq1C1
    Eq2C0=-q/2/math.sqrt(2*ResolvRel-p)+ResolvRel
    if(vsh==1):
        print("2 quadratic eqs:")
        print("Eq1: "+str(Eq1C2)+"*x^2+"+str(Eq1C1)+"*x+"+str(Eq1C0)+"=0")
        print("Eq2: "+str(Eq2C2)+"*x^2+"+str(Eq2C1)+"*x+"+str(Eq2C0)+"=0")
    RootSqEq1=polynomeEqOfPower2(Eq1C2, Eq1C1, Eq1C0)
    RootSqEq2=polynomeEqOfPower2(Eq2C2, Eq2C1, Eq2C0)
    if(vsh==1):
        print("and 2 Solutions:")
        print("Eq1: "+str(RootSqEq1))
        print("Eq2: "+str(RootSqEq2))
    SqEq1Root1Re=RootSqEq1[1-1][1-1]
    SqEq1Root2Re=RootSqEq1[1-1][2-1]
    SqEq1Root1Im=RootSqEq1[2-1][1-1]
    SqEq1Root2Im=RootSqEq1[2-1][2-1]
    SqEq2Root1Re=RootSqEq2[1-1][1-1]
    SqEq2Root2Re=RootSqEq2[1-1][2-1]
    SqEq2Root1Im=RootSqEq2[2-1][1-1]
    SqEq2Root2Im=RootSqEq2[2-1][2-1]
    Y=[[SqEq1Root1Re, SqEq1Root2Re, SqEq2Root1Re, SqEq2Root2Re],
       [SqEq1Root1Im, SqEq1Root2Im, SqEq2Root1Im, SqEq2Root2Im]]
    if(vsh==1):
        print("For solutions:"+str(Y))
    X=[[0,0,0,0],[0,0,0,0]]
    for i in range(4):
        X[1-1][i-1]=Y[1-1][i-1]-a/4
        X[2-1][i-1]=Y[2-1][i-1]
    if(vsh==1):
        print("Solution:"+str(X))
        print("polynomeEqOfPower4 finishes working")
    return X

def polynomeEqGenerator(R):
    Ord=len(R)
    c=[]
    for i in range(Ord+1):
        cl=[]
        for j in range(Ord+1):
            cl.append(0)
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
    for i in range(Ord+1):
        C.append(c[Ord][i])
    return C


                            
                            
                            
