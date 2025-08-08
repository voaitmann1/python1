def f1(x, y):
    return x + y

def f2(x, y):
    return x * y

def fof(fl, x, y, z):
    D=fl(x,y)
    return 10*D+z

x=4

y=2

z=1

print("10+:",fof(f1, x, y, z))
print("10*:",fof(f2, x, y, z))

class CalcConfigPrec1D:
    def __init__():
        self.eps=0.001
        self.QIters=50
        self.SectsQuantityCharact=50
        self_Prec1QIters2PrecAndQIters3PrecOrQIters4=4
        self.QSects1QBounds2=1

    def GetQSects():
        y=self.SectsQuantityCharact
        if self.QSects1QBounds2==2:
            y=self.SectsQuantityCharact-1
        return y

     def GetQBnds():
        y=self.SectsQuantityCharact+1
        if self.QSects1QBounds2==1:
            y=self.SectsQuantityCharact+1
        return y

    def SetQSects(n):
        self.QSects1QBounds2=1
        self.SectsQuantityCharact=n

    def SetQBnds(n):
        self.QSects1QBounds2=2
        self.SectsQuantityCharact=n

class HalfDivResult:
    def __init__():
        self.QSects=1
        self.x=0
        self.y=0
        self.found=0
        self.epsX=0
        self.epsY=0
        self.CountIters=0
    
            

def HalfDiv(fl, a, b, cfg, X=0):# not tested
    R=[]
    LBnd=a
    HBnd=b
    SectLen=(HBnd-LBnd)/QSects
    QSects=cfg.GetQSects()
    for SectN in range(1,QSects+1): 
        CurSect=HalfDivResult()
        #
        SectLBnd=LBnd+(i-1)*SectLen
        SectHBnd=SectLBnd+SectLen
        #
        contin=1
        found=0
        calculated=0
        #
        a=SectLBnd
        b=SectHBnd
        fa=f1(a)
        fb=f1(a)
        if(fa*fb<=cfg.epsY):
            found=1
        contin=found
        if found==0:
            R.append(CurSect)
        CurSect.found=found
        c=(a+b)/2
        fa=f1(a)
        fb=f1(b)
        fc=f1(c)
        #
        if abs(fa)<cfg.epsY and SectN==1:
            CurSect.x=a
            CurSect.y=fa
        elif abs(fb)<cfg.epsY:
            CurSect.x=b
            CurSect.y=fb
        elif abs(fc)<cfg.epsY:
            CurSect.x=c
            CurSect.y=fc
        else:
            contin=found
            while contin==1:
                CurSect.CountIters +=1
                if(fa*fc<0):
                    b=c
                if(fc*fb<0):
                    a=c
                fa=f1(a)
                fb=f1(b)
                c=(a+b)/2
                fc=f1(c)
                #
                if abs(fa)<cfg.epsY and SectN==1:
                    CurSect.x=a
                    CurSect.y=fa
                    contin=0
                elif abs(fb)<cfg.epsY:
                    CurSect.x=b
                    CurSect.y=fb
                    contin=0
                elif abs(fc)<cfg.epsY:
                    CurSect.x=c
                    CurSect.y=fc
                    contin=0
                elif b-a<epsX:
                    CurSect.x=c
                    CurSect.y=fc
                    contin=0
                elif CurSect.CountIters>=cfg.QIters and (cfg.self_Prec1QIters2PrecAndQIters3PrecOrQIters4==2  or cfg.self_Prec1QIters2PrecAndQIters3PrecOrQIters4==4):
                    CurSect.x=c
                    CurSect.y=fc
                    contin=0
                if contin==0:
                    R.append(CurSect)
    return R
            
                
                
        
        
