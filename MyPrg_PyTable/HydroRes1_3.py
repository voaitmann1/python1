import copy
import math

class HResSimple:
    def __init__(self, k=0, curN=0, Conn_Suc0Par1=0, upper=0, Ress=[], NinUpper=0, vsh=0):
        if vsh==1:
            print('RConstr HResSimple starts working ')
            print("Given params: k="+str(k)+" curN="+str(curN)+" Conn_Suc0Par1="+str(Conn_Suc0Par1)+ " NinUpper="+str(NinUpper))
        self.SetDefault()#uz self.elems=[]
        self.Conn_Suc0Par1=Conn_Suc0Par1
        self.k=k
        self.curSubElementN=0
        Q=0
        if isinstance(Ress, list):
            Q=len(Ress)
        if  vsh==1:
            print("Sub-Elts given : Q="+str(Q))
        for i in range(1, Q+1):
            Element=copy.deepcopy(Ress[i-1])
            self.elems.append(Element)
        self.curN=curN
        self.NinUpper=NinUpper
        self.upper=upper
        if(vsh==1):
            print('RConstr HResSimple  finishes working '+self.ToStringShort())

#def __init__(self, k=0, curN=0, Conn_Suc0Par1=0, upper=0, Ress=[], NinUpper=0, vsh=0):
    def Set(self, k=0, curN=0, Conn_Suc0Par1=0, upper=0, Ress=[], NinUpper=0, vsh=0):
        self.Conn_Suc0Par1=Conn_Suc0Par1
        self.k=k
        Q=0
        if isinstance(Ress, list):
            Q=len(Ress)
        for i in range(1, Q+1):
            Element=copy.deepcopy(Ress[i-1])
            self.elems.append(Element)
        self.curN=curN
        self.NinUpper=NinUpper
        self.upper=upper


    def GetQSubElts(self):
        Q=0
        if isinstance(self.elems, list) and len(self.elems)>0:
            Q=len(self.elems)
        return Q

    def SetN(self, N):
        self.curN=N
        
    def GetN(self):
        return self.curN

    def GetNInUpper(self):
        return self.NinUpper

    def get_uper(self):
        return self.upper
    
    def get_k(self):
        return self.k

            
    def SetDefault(self):
        self.elems=[]
        self.Conn_Suc0Par1=0

    def GetIfIsSimple(self):
        R=1
        if isinstance(self.elems, list) and len(self.elems)>0:
            R=0
        return R

    def FindByN(N):
    #{
        ptr = 0
        #bool contin;
        #int CurSN;
        if (self.GetN() == N):
        #{
            ptr = self
        #}
        else:
        #{
            if (self.GetIfIsSimple()):
            #{
                CurSN = 0
                contin = 1
                while(contin==1):
                #{
                    CurSN=CurSN+1
                    ptr = self.elems[CurSN - 1].FindByN(N)
                    if (ptr != 0):
                    #{
                        contin = 0
                    #}
                    if (CurSN == len(self.elems)):
                    #{
                        contin = 0
                    #}
                #}
            #}
        #}
        return ptr
    #}
    def FirstAbsentN(self, vsh=0):#{
        #//if vsh==1:
        #//    print("FirsrAbsentNt starts working. R"+str(ptr.curN))
        #int[] Ns = null;// this.FullPresentNsList(vsh);
        Ns=[]
        #//vikt! below s' gut examples for test et debug; in py Z s' verf'd, amda Z s'peresent ut be verf'd
        #//Ns=[1, 2, 3, 4, 5]
        #//Ns=[2, 3, 4, 5, 6]
        #//Ns=[1, 3, 4, 5, 6]
        #//Ns=[1, 2, 4, 5, 6]
        #//Ns=[1, 2, 3, 4, 7]
        #//Ns=[]#ja, N=1
        if vsh==1:
            print("FirstAbsentN starts working")
            print("Call from R: "+self.ToStringShort())
        Ns = self.FullPresentNsList(vsh)
        if vsh==1:
            print("Present Ns: ",Ns)
        #//MyLib.writeln(vsh, "Checking:");
        Q=len(Ns)
        contin=1
        count=0
        N=0
        #cur;
        #countPrev;
        while(contin==1):#{
            N=N+1#;
            if (N == Q + 1):
            #{
                contin = 0
            #}
            count=0
            countPrev = 0
            for i in range(1, Q+1):#{
                cur=Ns[i-1]
                countPrev = count
                if(N==cur):
                #{
                    count=count+1
                #}
            #}
            if(count==0):#{
                contin=0
            #}
            if (countPrev == count):
            #{
                print(str(N) + ": already present")
            #}
            else:
            #{
                if vsh!=0:
                    print(str(N) + ": found!")
            #}
        #}
        return N 
    #}
        

    def Calc(self, vsh=0):
        S=0
        C=0
        if(vsh==1):
            print('Calc starts working '+self.ToStringShort())
            print(self.ToStringShort())
        R=self.k
        if(vsh==1):
            print('R='+str(R))
        L=len(self.elems)
        if(vsh==1):
            print('L='+str(L))
        #if(L>0):#abl ac ce
        if self.Conn_Suc0Par1==0:
            if(vsh==1):
                print('succ conn')
            S=0
            for i in range(1, L+1):
                C=self.elems[i-1].Calc()
                if(vsh==1):
                    print("prev Calc finished, external one continueing")
                C=C*C
                S=S+C
                if(vsh==1):
                    print("RN"+str(i)+" k="+str(self.elems[1-1].k)+" C="+str(C)+" S="+str(S))
            R=R+math.sqrt(S)
        elif self.Conn_Suc0Par1==1:
            S=0
            if(vsh==1):
                print('parallel conn')
            for i in range(1, L+1):
                C=1/self.elems[i-1].Calc()
                if(vsh==1):
                    print("prev Calc finished, external one continueing")
                S=S+C
                if(vsh==1):
                    print("RN"+str(i)+" k="+str(self.elems[1-1].k)+" C="+str(C)+" S="+str(S))
            if(S!=0):
                R=R+1/S
        if(vsh==1):
            print('R='+str(R))
            print('Calc finishes working '+self.ToStringShort())
        return R

    def AddInner(self, ElementExt, vsh=0):
        if(vsh==1):
            print('AddInner starts working '+self.ToStringShort())
        Element=copy.deepcopy(ElementExt)
        Q=0
        if isinstance(self.elems, list):
            Q=len(self.elems)
        Element.NinUpper=Q+1
        Element.upper=self
        if(vsh==1):
            print('trying to add: '+Element.ToStringShort())
        self.elems.append(Element)
        if(vsh==1):
            Q=len(self.elems)
            print('trying to add: '+self.elems[Q-1].ToStringShort())
        self.curSubElementN=Q
        if(vsh==1):
            print('now habemus:')
            self.ShowText()
            print(self.ToStringShort()+' curSubElementN='+str(self.curSubElementN))
            print('AddInner finishes working '+self.ToStringShort())
                

    def DelInner(self, N):
        row=[]
        Q=len(self.elems)
        if N>=1 and N<=len(self.elems):
            for i in range(1, N-1+1):
                row.append(self.elems[i-1])
            for i in range(N+1, Q+1):
                Element=self.elems[i-1]
                Element.NinUpper=Element.NinUpper-1
                Element.upper=self
                row.append(Element)
            QI=self.elems[N-1].GetQSubElts()
            for i in range(1, QI+1):
                self.elems[N-1].DelInner(i)
            self.elems=row
            self.curSubElementN=N

    def InsInnerN(self, ElementExt, N, vsh=0):
        row=[]
        ElementToIns=copy.deepcopy(ElementExt)
        if vsh==1:
            print('InsInnerN starts working')
        Q=len(self.elems)
        if N>=1 and N<=Q:
            for i in range(1, N-1+1):
                Element=self.elems[i-1]
                #Element.NinUpper=Element.NinUpper
                Element.upper=self
                row.append(Element)
            ElementToIns.NinUpper=N
            row.append(ElementToIns)
            for i in range(N, Q+1):
                Element=self.elems[i-1]
                Element.NinUpper=Element.NinUpper+1
                Element.upper=self
                row.append(Element)
            self.elems=row
            self.curSubElementN=N
        if vsh==1:
            print('now habemus:')
            self.ShowText()
            print(self.ToStringShort()+' curSubElementN='+str(self.curSubElementN))
            print('InsInnerN finishes working')

    def LinkToTopR(self, vsh=0):
        if vsh==1:
            print("LinkToTopR starts working")
        ptr=self.upper
        if vsh==1:
            #print("At Start: self="+self.ToStringShort())
            print("At Start: self="+self.ToStringShort())
        if ptr!=0:
            print("At Start:  upper= R"+str(self.upper.curN))
            while ptr.upper!=0:
                ptr=ptr.upper
                if vsh==1:
                    print("now ptr=R"+str(ptr.curN))
        else:
            ptr=self
            if vsh==1:
                #print("upper="+str(self.upper))
                #print("This is top: "+str(self.ToStringShort()))
                print("This is top: "+str(self.ToStringShort()))
        if vsh==1:
            print("LinkToTopR finishes working. ptr=R"+str(ptr.curN))
        return ptr

    def CurPresentNsList(self, Ns=[], vsh=0):
        Ns.append(self.curN)
        Q=0
        if isinstance(self.elems, list) and len(self.elems)>0:
            Q=len(self.elems)
        for i in range(1, Q+1):
            self.elems[i-1].CurPresentNsList(Ns)

    def FullPresentNsList(self, vsh=0):
        Ns=[]
        ptr=self.LinkToTopR(vsh)
        if vsh==1:
            print("FullPresentNsList starts working. ptr=R"+str(ptr.curN))
        ptr.CurPresentNsList(Ns, vsh)
        if vsh==1:
            print("FullPresentNsList finishes working. ptr=R"+str(ptr.curN))
        return Ns

    def FirsrAbsentN(self, vsh=0):
        #if vsh==1:
        #    print("FirsrAbsentNt starts working. R"+str(ptr.curN))
        Ns=self.FullPresentNsList(vsh)
        #vikt! below s' gut examples for test et debug
        #Ns=[1, 2, 3, 4, 5]#ja, N=6
        #Ns=[2, 3, 4, 5, 6]#ja, N=1#
        #Ns=[1, 3, 4, 5, 6]#ja, N=2
        #Ns=[1, 2, 4, 5, 6]#ja, N=3
        #Ns=[1, 2, 3, 4, 7]#ja, N=5
        #Ns=[]#ja, N=1
        Q=len(Ns)
        contin=1
        count=0
        N=0
        while contin==1:
            N=N+1
            if N==Q+1:
                contin=0
            count=0
            for i in range(1, Q+1):
                cur=Ns[i-1]
                if N==cur:
                    count=count+1
            if count==0:
                contin=0
        #if vsh==1:
        #    print("FirsrAbsentNt finishes working. R"+str(ptr.curN))
        return N 
            
        

    #def AddSucSmart(self, ElementExt, smartAdd=0, k_new=0, vsh=0):
    #   newN=self.FirsrAbsentN();
    #    ElementToAdd=copy.deepcopy(ElementExt)
    #    #QUpperSubElts=self.upper.QSubElts()
    #    #def __init__(self, k=0, curN=0, Conn_Suc0Par1=0, upper=0, Ress=[], NinUpper=0, vsh=0):
    #    if self.upper==0:
    #        ElementInstead=HResSimple(self.k, newN, self.Conn_Suc0Par1, self, self.elems, vsh)
    #        #
    #        self.k=k_new
    #        self.Conn_Suc0Par1=0
    #        self.AddInner(ElementInstead)
    #        self.AddInner(ElementToAdd)
    #    elif isinstance(self.upper, HResSimple):#so!, not else, S cog S int et ecri: int ne ha flds 
    #        QUpperSubElts=self.upper.QSubElts()
    #        if self.upper.Conn_Suc0Par1==0:
    #            if self.NinUpper==QUpperSubElts:
    #                self.upper.AddInner(ElementToAdd)
    #            else:
    #                self.upper.InsInnerN(ElementToAdd, self.NinUpper+1)
    #        else:#self.upper.Conn_Suc0Par1==1
    #            ##def __init__(self, k=0, curN=0, Conn_Suc0Par1=0, upper=0, Ress=[], NinUpper=0, vsh=0):
    #            ElementInstead=HResSimple(self.k, newN, self.Conn_Suc0Par1, self, self.elems, vsh)
    #            #
    #            #ElementUpper.AddInner(ElementInstead)
    #            #ElementUpper.AddInner(ElementToAdd)
    #            if self.NinUpper==QUpperSubElts:
    #                self.upper.AddInner(ElementToAdd)
    #            else:
    #                self.upper.InsInnerN(ElementToAdd, self.NinUpper+1)
    #            self.k=k_new
    #            self.Conn_Suc0Par1=0

    def AddSucSmart(self, ElementExt, smartAdd=0, k_new=0, vsh=0):
        if vsh==1:
            print("AddSucSmart starts working")
        newN=self.FirsrAbsentN(vsh)#;#ne sees tic exnot char!
        ElementToAdd=copy.deepcopy(ElementExt)
        if vsh==1:
            print("Adding to: "+self.ToStringShort())
            print("Adding what: "+ElementToAdd.ToStringShort())
            print("new N = "+str(newN))
        ##def __init__(self, k=0, curN=0, Conn_Suc0Par1=0, upper=0, Ress=[], NinUpper=0, vsh=0):
        if self.upper==0 or ( isinstance(self.upper, HResSimple) and self.upper.Conn_Suc0Par1==1):
            if vsh==1:
                if self.upper==0:
                    print("No upper Rs. This will be first added, param - second")
                if isinstance(self.upper, HResSimple) and self.upper.Conn_Suc0Par1==1:
                     print("Trying conn -- to || con'd R")
                print("R, to which we try to conn, will be container of self's copy and connected R")
            ##def __init__(self, k=0, curN=0, Conn_Suc0Par1=0, upper=0, Ress=[], NinUpper=0, vsh=0):
            ElementInstead=HResSimple(self.k, newN, self.Conn_Suc0Par1, self, self.elems, vsh)
            if vsh==1:
                print("Copy: "+ElementInstead.ToStringShort())
            #
            self.k=k_new
            self.Conn_Suc0Par1=0
            if vsh==1:
                print("Self ef adding: "+self.ToStringShort())
                print("Adding copy:")
            self.AddInner(ElementInstead, vsh)
            if vsh==1:
                print("Self ef adding copy:")
                #self.Show_WithSubElts()
                self.ShowText()
                print("Adding R to Add:")
            #
            if(ElementToAdd.GetN() == 0):
            #{
                newNForNew = self.FirstAbsentN(0)#;//vsh
                if vsh==1:
                    print("N for new: " + str(newNForNew))
                ElementToAdd.SetN(newNForNew)#;
            #}
            self.AddInner(ElementToAdd, vsh)
            if vsh==1:
                print("Finally: ")
                #self.Show_WithSubElts()
                self.ShowText()
        else:
            QUpperSubElts=self.upper.QSubElts()
            if self.NinUpper==QUpperSubElts:
                if vsh==1:
                    print("This is sub-element, one ("+str(self.NinUpper)+") of "+str(QUpperSubElts)+", inited par, last, will be added")
                self.upper.AddInner(ElementToAdd, vsh)
            else:
                if vsh==1:
                    print("This is sub-element, one ("+str(self.NinUpper)+") of "+str(QUpperSubElts)+", inited par,  not last, will be ins'd")
                self.upper.InsInnerN(ElementToAdd, self.NinUpper+1, vsh)
            if vsh==1:
                print("Finally: ")
                #self.Show_WithSubElts()
                self.ShowText()
        if vsh==1:
            print("Now habemus:")
            self.ShowText()
            print(self.ToStringShort()+" CurSubEltN="+str(self.curSubElementN)+" of "+str(len(self.elems)))
            print("AddSucSmart finishes working") 

   
        

    #def AddParSmart(self, ElementExt, smartAdd=0, k_new=0, vsh=0):
    #    if vsh==1:
    #        print("AddParSmart starts working")
    #    newN=self.FirsrAbsentN();
    #    ElementToAdd=copy.deepcopy(ElementExt)
    #    if vsh==1:
    #        print("Adding to: "+self.ToStringShort())
    #        print("Adding what: "+self.ToStringShort())
    #        print("new N = "+str(newN))
    #    #def __init__(self, k=0, curN=0, upper=0, Conn_Suc0Par1=0, Ress=[], NinUpper=0, vsh=0):
    #    if self.upper==0:
    #        if vsh==1:
    #            print("No upper Rs. This will be first added, param - second")
    #        ElementInstead=HResSimple(self.k, newN, self, self.Conn_Suc0Par1, self.elems, vsh)
    #        #
    #        self.k=k_new
    #        self.Conn_Suc0Par1=1
    #        self.AddInner(ElementInstead)
    #        self.AddInner(ElementToAdd)
    #        if vsh==1:
    #            print("Now element, to which added, is: ")
    #            self.Show_WithSubElts()
    #    elif isinstance(self.upper, HResSimple):#so!, not else, S cog S int et ecri: int ne ha flds 
    #        QUpperSubElts=self.upper.QSubElts()
    #        if self.upper.Conn_Suc0Par1==1:
    #            if self.NinUpper==QUpperSubElts:
    #                if vsh==1:
    #                    print("This is sub-element, one of "+str(QUpperSubElts)+", inited par, last, will be added")
    #                self.upper.AddInner(ElementToAdd)
    #            else:
    #                self.upper.InsInnerN(ElementToAdd, self.NinUpper+1)
    #                if vsh==1:
    #                    print("This is sub-element, one of "+str(QUpperSubElts)+", inited par, last, not last, will be ins'd")
    #                self.upper.AddInner(ElementToAdd)
    # 
    #        else:#self.upper.Conn_Suc0Par1==0
    #            if vsh==1:
    #                print("This is sub-element, one of "+str(QUpperSubElts)+", inited suc")
    #            self.Conn_Suc0Par1=1
    #            #
    #            ElementInstead=HResSimple(self.k, newN, self, self.Conn_Suc0Par1, self.elems, vsh)
    #            if vsh==1:
    #                print("Adding copy of this R: "+ElementInstead.ToStringShort())
    #            #
    #            self.AddInner(ElementInstead)
    #            if vsh==1:
    #                print("Adding element from param")
    #            self.AddInner(ElementToAdd)
    #            self.k=k_new
    #            if vsh==1:
    #                 if vsh==1:
    #                    print("Now element, to which added, is: ")
    #                    self.Show_WithSubElts()
    #    if vsh==1:
    #        print("AddParSmart finishes working")
                
    def AddParSmart(self, ElementExt, smartAdd=0, k_new=0, vsh=0):
        if vsh==1:
            print("AddParSmart starts working")
        newN=self.FirsrAbsentN(vsh)#;#ne sees tic exnot char!
        ElementToAdd=copy.deepcopy(ElementExt)
        if vsh==1:
            print("Adding to: "+self.ToStringShort())
            #print("Adding what: "+ElementToAdd.ToStringShort())
            print("Adding what: "+ElementToAdd.ToStringShort())
            print("new N = "+str(newN))
        ##def __init__(self, k=0, curN=0, Conn_Suc0Par1=0, upper=0, Ress=[], NinUpper=0, vsh=0):
        if self.upper==0 or ( isinstance(self.upper, HResSimple) and self.upper.Conn_Suc0Par1==0):
            if vsh==1:
                if self.upper==0:
                    print("No upper Rs. This will be first added, param - second")
                if isinstance(self.upper, HResSimple) and self.upper.Conn_Suc0Par1==0:
                     print("Trying conn || to -- con'd R")
                print("R, to which we try to conn, will be container of self's copy and connected R")
            ##def __init__(self, k=0, curN=0, Conn_Suc0Par1=0, upper=0, Ress=[], NinUpper=0, vsh=0):
            ElementInstead=HResSimple(self.k, newN, self.Conn_Suc0Par1, self, self.elems, vsh)
            if vsh==1:
                print("Copy: "+ElementInstead.ToStringShort())
            #
            self.k=k_new
            self.Conn_Suc0Par1=1
            if vsh==1:
                print("Self ef adding: "+self.ToStringShort())
                print("Adding copy:")
            self.AddInner(ElementInstead, vsh)
            if vsh==1:
                print("Self ef adding copy:")
                #self.Show_WithSubElts()
                self.ShowText()
                print("Adding R to Add:")
            if(ElementToAdd.GetN() == 0):
            #{
                newNForNew = self.FirstAbsentN(0)#;//vsh
                if vsh==1:
                    print("N for new: " + str(newNForNew))
                ElementToAdd.SetN(newNForNew)#;
            #}
            self.AddInner(ElementToAdd, vsh)
            if vsh==1:
                print("Finally: ")
                #self.Show_WithSubElts()
                self.ShowText()
        else:
            QUpperSubElts=self.upper.QSubElts()
            if self.NinUpper==QUpperSubElts:
                if vsh==1:
                    print("This is sub-element, one ("+str(self.NinUpper)+") of "+str(QUpperSubElts)+", inited par, last, will be added")
                self.upper.AddInner(ElementToAdd, vsh)
            else:
                if vsh==1:
                    print("This is sub-element, one ("+str(self.NinUpper)+") of "+str(QUpperSubElts)+", inited par,  not last, will be ins'd")
                self.upper.InsInnerN(ElementToAdd, self.NinUpper+1, vsh)
            if vsh==1:
                print("Finally: ")
                #self.Show_WithSubElts()
                self.ShowText()
        if vsh==1:
            print("Now habemus:")
            self.ShowText()
            print(self.ToStringShort()+" CurSubEltN="+str(self.curSubElementN)+" of "+str(len(self.elems)))
            print("AddParSmart finishes working")            
                
    def GetIfConnectionTypeIsSucc(self):
        v=0
        if self.Conn_Suc0Par1==0:
            v=1
        return v
    
    def GetIfConnectionTypeIsPrl(self):
        v=0
        if self.Conn_Suc0Par1==1:
            v=1
        return v
    #
    #
    def GetCoodsAsStr(self, vsh=0):
        x=self.vis_x(vsh)
        y=self.vis_y(vsh)
        s="[x="+str(x)+"; y= "+str(y)+"]"
        return s
        
    def ToStringShort(self):
        R="R"+str(self.curN)
        return R
    def ToStringShortLonger(self):
        R="R"+str(self.curN)
        return R
                  
    def ToStringLong(self, vsh=0):
        R=self.ToStringShort()
        if self.upper==0:
            R= R+" (top element) "
        else:
            #upr=self.upper.ToStringLong()
            #R=R+" ("+str(self.NinUpper)+" of: ["+upr+"]) "
            upr=self.upper.ToStringShort()
            R=R+" ("+str(self.NinUpper)+" of "+upr+") "
        R=R+" Path: "+self.GetPathString()+" "
        R=R+" Coords: "+self.GetCoodsAsStr(vsh)
        R=R+" SubElts"
        if self.Conn_Suc0Par1==0:
            R=R+" [--]"
        else:
            R=R+" [//]"
        R=R+": "+str(len(self.elems))
        return R
            
    def ShowText(self, vsh=0):
        #print(self.ToStringLong())
        slf=self.ToStringLong(vsh)
        if len(self.elems)>0:
            slf=slf+":"
        print(slf)
        for i in range(1, len(self.elems)+1):
            #print(self.elems[i-1].ToStringLong())
            print("SubElement "+str(i)+": "+self.elems[i-1].ToStringShort()) 
            self.elems[i-1].ShowText(vsh)
    #
    #
    #vis
    #
    #
    def vis_L(self, vsh):
        if(vsh!=0):
            print("vis_L starts working. R: " + self.ToStringShort())
        L = 1
        Lmax = 0
        Lcur = 0 #simple or left wall
        QElements=len(self.elems)
        if(vsh!=0):
            print(" L=1=" + str(L) + " If it's simple, so it is, if it's complex - left wall")
        if self.upper == 0:
            if(vsh!=0):
                print( "Ext: now L=1")
            if (QElements > 0):
                if (self.Conn_Suc0Par1 == 0):
                    if(vsh!=0):
                        print("It's complex. First-level sub-elements s'united in succession")
                    #for (int i = 1; i <= self.QElements - 1; i++)
                    for i in range(1, QElements - 1+1):
                        Lcur = self.elems[i - 1].vis_L(vsh)
                        L = L + Lcur
                        L = L + 1#connector
                        if(vsh!=0):
                            print("( returning to R" + str(self.curN) + ")")
                            print(str(i) + ") Lcur=" + str(Lcur) + "+1 connector. now L=" + str(L))
                    Lcur = self.elems[QElements - 1].vis_L(vsh)
                    L = L + Lcur
                    if(vsh!=0):
                        print("( returning to R" + str(self.curN) + ")")
                        print(str(QElements) + ") Lcur=" + str(Lcur) + " L=" + str(L))
                else: #parallel
                    if(vsh!=0):
                        print("It's complex. First-level sub-elements s'united parallelly. Finding max")
                    L = L + 1#connector left
                    if(vsh!=0):
                        print("Connector left: L=" + L.ToStringShort())
                    #for (int i = 1; i <= self.QElements; i++)
                    for i in range (1, QElements+1):
                        Lcur = self.elems[i - 1].vis_L(vsh)
                        if (i == 1 or (i > 1 and Lmax < Lcur)):
                            Lmax = Lcur
                            #print( "( returning to R) " + i.ToString() + ") Lcur=" + Lcur.ToString() + " Lmax=" + Lmax.ToString() );
                        if(vsh!=0):
                            print("( returning to R" + str(self.curN) + ")")
                            print(str(i) + ") Lcur=" + str(Lcur) + " Lmax=" + str(Lmax))
                    #Lmax=self.vis_
                    L = L + Lmax
                    L = L + 1#connector right
                    if(vsh!=0):
                        print( " Lmax=" + str(Lmax) + "+2 connectors. so L=" + str(L))
                L = L + 1#right wall
                if(vsh!=0):
                    print("+1 right wall. so L=" + str(L))
            else:
                if(vsh!=0):
                    print("Simple: nil to add. L=" + str(L))
            #if (self.upper == null)
            ##{
            #    L = L + 1;#L2=
            #    print( "Ext: L=L+1= " + L.ToString() + " - right connector + right wall");
            ##}
        if(vsh!=0):
            print("vis_L finishes working. R" + str(self.curN) + " L=" + str(L))
        return L

    def vis_L_WithConnectors(self, vsh):
        if(vsh!=0):
            print("vis_L starts working. R: " + self.ToStringShort())
        L = 1
        Lmax = 0
        Lcur = 0#simple or left wall
        QElements=0
        if isinstance(self.elems, list) and len(self.elems)>0:
            QElements=len(self.elems)
        if(vsh!=0):
            print( " L=1=" + str(L) + " If it's simple, so it is, if it's complex - left wall");
        if self.upper == 0:
            L = L + 1;#L2=
            if(vsh!=0):
                rint( "Ext: now L=2=" + str(L) + " it's most external - left connector + left wall");
        if (QElements > 0):
            if (self.Conn_Suc0Par1 == 0):
                if(vsh!=0):
                    print( "It's complex. First-level sub-elements s'united in succession");
                #for (int i = 1; i <= self.QElements - 1; i++)#{
                for  i in range(1, QElements - 1+1):
                    Lcur = self.elems[i - 1].vis_L(vsh)
                    L = L + Lcur
                    L = L + 1#connector
                    if(vsh!=0):
                        print( "( returning to R" + str(self.curN) + ")");
                        print( str(i) + ") Lcur=" + str(Lcur) + "+1 connector. now L=" + str(L))
                #}
                Lcur = self.elems[QElements - 1].vis_L(vsh)
                L = L + Lcur
                if(vsh!=0):
                    print( "( returning to R" + str(self.curN) + ")")
                    print( str(QElements) + ") Lcur=" + str(Lcur) + " L=" + str(L))
            else: #parallel
                if(vsh!=0):
                    print( "It's complex. First-level sub-elements s'united parallelly. Finding max");
                L = L + 1#connector left
                if(vsh!=0):
                    print( "Connector left: L=" + str(L))
                #for (int i = 1; i <= self.QElements; i++)
                for i in range(1, QElements+1):
                    Lcur = self.elems[i - 1].vis_L(vsh)
                    if (i == 1 or (i > 1 and Lmax < Lcur)):
                        Lmax = Lcur
                        #print( "( returning to R) " + i.ToString() + ") Lcur=" + Lcur.ToString() + " Lmax=" + Lmax.ToString() );
                    if(vsh!=0):
                        print( "( returning to R" + str(self.curN) + ")");
                        print( str(i) + ") Lcur=" + str(Lcur) + " Lmax=" + str(Lmax))
                #Lmax=self.vis_
                L = L + Lmax
                L = L + 1#connector right
                if(vsh!=0):
                    print( " Lmax=" + str(Lmax) + "+2 connectors. so L=" + str(L))
            L = L + 1#right wall
            if(vsh!=0):
                print( "+1 right wall. so L=" + str(L))
        else:
            if(vsh!=0):
                print( "Simple: nil to add. L=" + str(L))
        if (self.upper == 0):
            L = L + 1#L2=
            if(vsh!=0):
                print( "Ext: L=L+1= " + str(L) + " - right connector + right wall");
        if(vsh!=0):
            print( "vis_L finishes working. R" + str(self.curN) + " L=" + str(L))
        return L
    
    def vis_yUpper(self, vsh):
        yUpper = 0
        #yUpperMax, yUpperCur;
        QElements=0
        if (isinstance(self.elems, list) and len(self.elems)>0):
            QElements=len(self.elems)
        if(vsh!=0):
            print( "vis_yUpper starts working. " + self.ToStringShort() + " yUpper=" + str(yUpper))
        if (QElements>0):
            yUpper = yUpper + 1
            if(vsh!=0):
                print( "complex: 1 upper wall. yUpper=" + str(yUpper))
            if (self.Conn_Suc0Par1 == 0):
                if(vsh!=0):
                    print( "[--] finding max");
                yUpperMax = 0
                #for (int i = 1; i <= self.QElements; i++)
                for i in range(1, QElements+1):
                    yUpperCur = self.elems[i - 1].vis_yUpper(vsh)
                    if (i == 1 or (i > 1 and yUpperMax < yUpperCur)):
                        yUpperMax = yUpperCur
                    if(vsh!=0):
                        print( "-element" + str(i) + " R" + str(self.elems[i - 1].curN) + ": yUpperCur=" + str(yUpper) + " yUpperMax=" + str(yUpperMax))
                yUpper = yUpper + yUpperMax
                if(vsh!=0):
                    print( "yUpper = yUpper+ yUpperMax: =" + str(yUpper) + " (yUpperMax = " + str(yUpper))
            else:
                if(vsh!=0):
                    print( "[||] yUpper = first")
                yUpperCur = self.elems[1 - 1].vis_yUpper(vsh)
                yUpper = yUpper + yUpperCur
                if(vsh!=0):
                    print( "Return to prev. yUpper=yUpperCur+1=" + str(yUpperCur))
            ##}
        ##}
        else:
        ##{
            if(vsh!=0):
                print( "simple - nil to add");
        if(vsh!=0):
            print( "vis_yUpper finishes working. " + self.ToStringShort() + " yUpper=" + str(yUpper))
        ##}
        return yUpper
    ##}
    def vis_yLower(self, vsh):
    #{
        yLower = 0
        #yLowerCur, yUpperCur, yLowerMax;
        QElements=0
        if(isinstance(self.elems, list) and len(self.elems) > 0):
            QElements=len(self.elems)
        if(vsh!=0):
            print( "vis_yLower starts working. " + self.ToStringShort() + " yLower=" + str(yLower))
        if (QElements > 0):
        #{
            if (self.Conn_Suc0Par1 == 0):
            #{
                if(vsh!=0):
                    print( "[--] finding max")
                yLowerMax = 0
                #for (int i = 1; i <= self.QElements; i++)
                for i in range(1, QElements+1):
                #{
                    yLowerCur = self.elems[i - 1].vis_yLower(vsh)
                    if (i == 1 or (i > 1 and yLowerMax < yLowerCur)):
                    #{
                        yLowerMax = yLowerCur
                    #}
                    if(vsh!=0):
                        print( "-element" + str(i) + " R" + str(self.elems[i - 1].curN) + ": yLowerCur=" + str(yLowerCur) + " yLowerMax=" + str(yLowerMax))
                #}
                yLower = yLower + yLowerMax
                if(vsh!=0):
                    print( "yLower = yLower+ yLowerMax: =" + str(yLower) + " (yLowerMax = " + str(yLowerMax) + ")");
            #}
            else:#if (self.Conn_Suc0Par1 == 1)
            #{
                yLowerCur =  self.elems[1 - 1].vis_yLower(vsh)
                yLower = yLower + yLowerCur;
                if(vsh!=0):
                    print( "yLower = yLower+ yLowerCur[1]: =" + str(yLower) + " (yLowerCur[1] = " + str(yLowerCur) + ")");
                #for (int i = 2; i <= self.QElements; i++)
                for i in range(2, QElements+1):
                #{
                    yUpperCur = self.elems[i - 1].vis_yLower(vsh)#yUpperCur = self.elems[i - 1].vis_yLower(vsh);
                    yLowerCur = self.elems[i - 1].vis_yLower(vsh)
                    yLower = yLower + yUpperCur + yLowerCur + 2
                    if(vsh!=0):
                        print( "yLower = yLower+ yUpperCur+ yLowerCur+2: =" + str(yLower) + " (yUpperCur = " + str(yUpperCur) + " yLowerCur = " + str(yLowerCur) + "):2=1ipse+1space");
                #}
            #}
            yLower = yLower + 1
            if(vsh!=0):
                print( " yLower=yLower+1wall=" + str(yLower))
                print( "Return to prev. yLower=" + str(yLower))
        #}
        else:
        #{
            if(vsh!=0):
                print( "simple - nil to add");
        #}
        if(vsh!=0):
            print( "vis_yLower finishes working. " + self.ToStringShort() + " yLower=" + str(yLower))
        return yLower
    #}
    def vis_H(self, vsh):
    #{
        return self.vis_yUpper(vsh) + 1+self.vis_yLower(vsh)
    #}
    def vis_x(self, vsh):
    #{
        if(vsh!=0):
            print( "vis_x starts working. " + self.ToStringShort())
        x = 2
        #xUpper, LCur;
        #if (self.upper == null)
        if (self.upper == 0):
        #{
            if(vsh!=0):
                print( "Ext.: nil to add. x=" + str(x))
            ##}else if (self.upper is int)#{
            #    print("Error upper of: "+self.ToString());
        #}
        elif (self.upper != 0):
        #{
            xUpper = self.upper.vis_x(vsh)
            x = xUpper
            if(vsh!=0):
                print( "Part of: " + self.upper.ToStringShort() + " xUpper=" + str(xUpper) + " = x =" + str(x))
            if (self.upper.Conn_Suc0Par1 == 0):
            #{
                x = x + 1
                if(vsh!=0):
                    print( "[--] x=x+1: left wall x =" + str(x))
                LCur = 0
                if (self.NinUpper > 1):
                #{
                    #for (int i = 1; i <= self.NinUpper - 1; i++)
                    for i in range(1, self.NinUpper - 1+1):
                    #{
                        LCur = self.upper.elems[i - 1].vis_L(vsh)
                        x = x + LCur
                        x = x + 1
                        if(vsh!=0):
                            print( "Elt" + str(i) + " R" + str(self.upper.elems[i - 1].curN) + " +1 connector=" + str(LCur) + " cur x=" + str(x))
                    #}
                #}
                if(vsh!=0):
                    print( "x= " + str(x))
            #}
            else:
            #{
                x = xUpper + 2
                if(vsh!=0):
                    print( " || part of " + self.upper.ToStringShort() + "x=xUpper+2 (wall and connector)=" + str(x) + " (xUpper=" + str(xUpper) + ")")
            #}
        #}
        if(vsh!=0):
            print( "vis_x finishes working. " + self.ToStringShort() + " x=" + str(x))
        return x
    #}
    def vis_y(self, vsh):
    #{
        y = 0
        #yMyUpper, yOfUpper, yLower1, yUpperCur, yLowerCur;
        if(vsh!=0):
            print( "vis_y starts working. " + self.ToStringShort())
        #if (self.upper == null)
        if (self.upper == 0):
        #{
            yMyUpper = self.vis_yUpper(vsh)
            y = yMyUpper + 1
            #if (vsh != null)
            if (vsh != 0):
            #{
                #if (self.upper == null)
                if (self.upper == 0):
                #{
                    if(vsh!=0):
                        print( "Ext. y=yUpper+1=" + str(yMyUpper) + "+1=" + str(y))
                #}
            #}
        #}
        #else if (self.upper != null)
        elif (self.upper != 0):
        #{
            yOfUpper = self.upper.vis_y(vsh)
            #yUpper1=self.upper.elems[1-1].vis_yUpper(vsh);
            if (self.upper.Conn_Suc0Par1 == 1):
            #{
                #if (self.NinUpper >= 1)
                ##{
                #    y = yUpper;
                #    print( "Ce part of " + self.upper.ToString() + " [" + self.NinUpper.ToString() + "]>=1 => y=y(upper)=" + yUpper.ToString() + "=" + y.ToString());
                ##}
                #if (self.NinUpper >= 2)
                ##{
                #    yLower1 = self.upper.elems[1 - 1].vis_yLower(vsh);
                #    y = y + yLower1 + 1;
                #    print( "Ce part of " + self.upper.ToString() + " [" + self.NinUpper.ToString() + "]>=2 y=y(upper)+yLower[1]+1= " + y.ToString() + " (y(upper)=" + yUpper.ToString() + " yLower[1]=" + yLower1.ToString() + ")");
                ##}
                #if (self.NinUpper > 2)
                ##{
                #    for (int i = 2; i <= self.NinUpper - 1; i++)
                #    #{
                #        yUpperCur = self.upper.elems[i - 1].vis_yUpper(vsh);
                #        yLowerCur = self.upper.elems[i - 1].vis_yLower(vsh);
                #        y = y + yUpperCur + 1 + yLowerCur + 1;
                #        print( i.ToString() + ")  y=y+yUpperCur[i]+yLower[i]+1= " + y.ToString() + " (yUpperCur[i]=" + yUpperCur.ToString() + " yLowerCur[i]" + yUpperCur.ToString() + ")");
                #    #}
                #    yMyUpper = self.vis_yUpper(vsh);
                #    y = y + yMyUpper;
                #    print( " y=y+yMyUpper = " + y.ToString() + " (yMyUpper=" + yMyUpper.ToString() + ")");
                ##}
                #
                y = yOfUpper
                if(vsh!=0):
                    print( "Ce part of " + self.upper.ToStringShort() + " [" + str(self.NinUpper) + "]>=1 => y=y(upper)=" + str(yOfUpper) + "=" + str(y))
                #
                if (self.NinUpper > 1):
                #{
                    yLower1 = self.upper.elems[1 - 1].vis_yLower(vsh)
                    y = y + yLower1 + 1
                    if(vsh!=0):
                        print( "Ce part of " + self.upper.ToStringShort() + " [" + str(self.NinUpper) + "]>1 y=y(upper)+yLower[1]+1(space lower)= " + str(y) + " (y(upper)=" + str(yOfUpper) + " yLower[1]=" + str(yLower1) + ")")
                #}
                #for (int i = 2; i <= self.NinUpper - 1; i++)
                for i in range(2, self.NinUpper - 1+1):
                #{
                    yUpperCur = self.upper.elems[i - 1].vis_yUpper(vsh)
                    yLowerCur = self.upper.elems[i - 1].vis_yLower(vsh)
                    y = y + yUpperCur + 1 + yLowerCur + 1
                    if(vsh!=0):
                        print( str(i) + ")  y=y+yUpperCur[i]+1(ipse)+yLower[i]+1(space lower)= " + str(y) + " (yUpperCur[i]=" + str(yUpperCur) + " yLowerCur[i]" + str(yLowerCur) + ")")
                #}
                #
                if (self.NinUpper > 1):
                #{
                    yMyUpper = self.vis_yUpper(vsh)
                    y = y + yMyUpper
                    if(vsh!=0):
                        print( " y=y+yMyUpper = " + str(y) + " (yMyUpper=" + str(yMyUpper) + ")")
                    y = y + 1;
                    if(vsh!=0):
                        print( " N>1=" + str(self.NinUpper)+ " => y=y+1 = " + str(y))
                #}
                if(vsh!=0):
                    print( "finally: y=" + str(y))
            #}
            else:
            #{
                y = yOfUpper;
                if(vsh!=0):
                    print( "united [--]. y=y(upper)=" + str(yOfUpper) + "=" + str(y))
            #}
        #}
        if(vsh!=0):
            print( "vis_y finishes working. " + self.ToStringShort() + " y=" + str(y))
        return y
    #}
    #
    def vis_x_cornerLeft(self, vsh = 0):
    #{
        x = 0
        x = self.vis_x(vsh)
        return x
    #}
    def vis_x_cornerRight(self, vsh = 0):
    #{
        x = self.vis_x(vsh)+self.vis_L(vsh)-1
        return x
    #}
    def vis_y_cornerUpper(self, vsh = 0):
    #{
        y = self.vis_y(vsh)
        QElements=0
        if isinstance(self.elems, list) and len(self.elems)>0:
            QElements=len(self.elems)
        if (QElements > 0):
        #{
            y = y - self.vis_yUpper(vsh)
        #}
        return y
    #}
    def vis_y_cornerLower(self,  vsh = 0):
    #{
        y =  self.vis_y(vsh)
        QElements=0
        if isinstance(self.elems, list) and len(self.elems)>0:
            QElements=len(self.elems)
        if (QElements > 0):
        #{
            y = y + self.vis_yLower(vsh)
        #}
        return y
    #}
    def vis_x_Caption(self, vsh = 0):
    #{
        x = self.vis_x(vsh)
        QElements=0
        if isinstance(self.elems, list) and len(self.elems)>0:
            QElements=len(self.elems)
        if (QElements > 0):
        #{
            x = x+1
        #}
        return x
    #}
    def vis_y_Caption(self, vsh = 0):
    #{
        curN = self.curN;
        y = self.vis_y(vsh)
        QElements=0
        if isinstance(self.elems, list) and len(self.elems)>0:
            QElements=len(self.elems)
        if (QElements > 0):
        #{
            y = y - self.vis_yUpper(vsh)
        #}
        return y
    #}
    def vis_x_LeftConnection(self, vsh = 0):
    #{
        x = 0
        if (self.upper == 0 or not(self.upper.GetIfConnectionTypeIsSucc() == 1 and self.NinUpper == 1)):
        #{
            x = self.vis_x(vsh) - 1
        #}
        return x
    #}
    def vis_y_LeftConnection(self, vsh = 0):
    #{
        y = 0
        if (self.upper == 0 or not(self.upper.GetIfConnectionTypeIsSucc() == 1 and self.NinUpper == 1)):
        #{
           y = self.vis_y(vsh)
        #}
        return y
    #}
    def vis_x_RightConnection(self, vsh = 0):
    #{
        x = 0
        #xOwnCur, xOwnMax=0, xOwn, dL, QMates,  CurMateN
        CurN=self.curN
        #if (self.upper == null || !(self.upper.GetIfConnectionTypeIsSucc() == true && self.NinUpper == self.upper.GetQSubElts()))
        if (self.upper == 0 or not(self.upper.GetIfConnectionTypeIsSucc() == 1 and self.NinUpper == self.upper.GetQSubElts())):
        #{
            xOwn = self.vis_x(vsh) + self.vis_L(vsh)
            x = xOwn
            if (self.upper != 0 and self.upper.GetIfConnectionTypeIsPrl() == 1):
            #{
                QMates=self.upper.GetQSubElts()
                #for (int i = 1; i <= QMates; i++)
                for i in range(1, QMates+1):
                #{
                    CurMateN = self.upper.elems[i - 1].GetN()
                    xOwnCur = self.upper.elems[i - 1].vis_x(vsh) + self.upper.elems[i - 1].vis_L(vsh)
                    if (i == 1 or (i > 1 and xOwnMax<xOwnCur)):
                        xOwnMax=xOwnCur;
                #}
                x = xOwnMax
            #}
        #}
        return x
    #}
    def vis_y_RightConnection(self, vsh = 0):
    #{
        y = 0
        if (self.upper == 0 or not(self.upper.GetIfConnectionTypeIsSucc() == 1 and self.NinUpper == self.upper.GetQSubElts())):
        #{
            y = self.vis_y(vsh)
        #}
        return y
    #}
    #
    #public int vis_x_SE_NInSucc(int SubEltN, TValsShowHide vsh=null)
    ##{
    #    int x = 0;
    #    if (SubEltN >= 1 && SubEltN <= self.QElements)
    #    #{
    #        x = self.elems[SubEltN - 1].vis_x(vsh);
    #    #}
    #    return x;
    ##}
    #public int vis_y_SE_NInSucc(int SubEltN, TValsShowHide vsh = null)
    ##{
    #    int y = 0;
    #    if (SubEltN >= 1 && SubEltN <= self.QElements)
    #    #{
    #        y = self.elems[SubEltN - 1].vis_y(vsh);
    #    #}
    #    return y;
    ##}
    #public int vis_yLower_SE_NInSucc(int SubEltN, TValsShowHide vsh = null)
    ##{
    #    int yLower = 0;
    #    if (SubEltN >= 1 && SubEltN <= self.QElements)
    #    #{
    #        yLower = self.elems[SubEltN - 1].vis_yLower(vsh);
    #    #}
    #    return yLower;
    ##}
    #public int vis_yUpper_SE_NInSucc(int SubEltN, TValsShowHide vsh = null)
    ##{
    #    int yUpper = 0;
    #    if (SubEltN >= 1 && SubEltN <= self.QElements)
    #    #{
    #        yUpper = self.elems[SubEltN - 1].vis_yUpper(vsh);
    #    #}
    #    return yUpper;
    ##}
    #public int vis_L_SE_NInSucc(int SubEltN, TValsShowHide vsh = null)
    ##{
    #    int L = 0;
    #    if (SubEltN >= 1 && SubEltN <= self.QElements)
    #    #{
    #        L = self.elems[SubEltN - 1].vis_L(vsh);
    #    #}
    #    return L;
    ##}
    #public int vis_H_SE_NInSucc(int SubEltN, TValsShowHide vsh = null)
    ##{
    #    int H = 0;
    #    if (SubEltN >= 1 && SubEltN <= self.QElements)
    #    #{
    #        H = self.elems[SubEltN - 1].vis_H(vsh);
    #    #}
    #    return H;
    ##}
    ##
    #public int vis_x_Mate_NInSucc(int SubEltN, TValsShowHide vsh = null)
    ##{
    #    int x = 0;
    #    if (self.upper!=null && SubEltN >= 1 && SubEltN <= self.upper.GetQSubElts())
    #    #{
    #        x = self.upper.elems[SubEltN - 1].vis_x(vsh);
    #    #}
    #    return x;
    ##}
    #public int vis_y_Mate_NInSucc(int SubEltN, TValsShowHide vsh = null)
    ##{
    #    int y = 0;
    #    if (self.upper != null && SubEltN >= 1 && SubEltN <= self.upper.GetQSubElts())
    #    #{
    #        y = self.upper.elems[SubEltN - 1].vis_y(vsh);
    #    #}
    #    return y;
    ##}
    #public int vis_yLower_Mate_NInSucc(int SubEltN, TValsShowHide vsh = null)
    ##{
    #    int yLower = 0;
    #    if (self.upper != null && SubEltN >= 1 && SubEltN <= self.upper.GetQSubElts())
    #    #{
    #        yLower = self.upper.elems[SubEltN - 1].vis_yLower(vsh);
    #    #}
    #    return yLower;
    ##}
    #public int vis_yUpper_Mate_NInSucc(int SubEltN, TValsShowHide vsh = null)
    ##{
    #    int yUpper = 0;
    #    if (self.upper != null && SubEltN >= 1 && SubEltN <= self.upper.GetQSubElts())
    #    #{
    #        yUpper = self.upper.elems[SubEltN - 1].vis_yUpper(vsh);
    #    #}
    #    return yUpper;
    ##}
    #public int vis_L_Mate_NInSucc(int SubEltN, TValsShowHide vsh = null)
    ##{
    #    int L = 0;
    #    if (self.upper != null && SubEltN >= 1 && SubEltN <= self.upper.GetQSubElts())
    #    #{
    #        L = self.upper.elems[SubEltN - 1].vis_L(vsh);
    #    #}
    #    return L;
    ##}
    #public int vis_H_Mate_NInSucc(int SubEltN, TValsShowHide vsh = null)
    ##{
    #    int H = 0;
    #    if (self.upper != null && SubEltN >= 1 && SubEltN <= self.upper.GetQSubElts())
    #    #{
    #        H = self.upper.elems[SubEltN - 1].vis_H(vsh);
    #    #}
    #    return H;
    ##}
    ##
    #public int vis_x_UpperElement( TValsShowHide vsh = null)
    ##{
    #    int x = 0;
    #    if (self.upper != null )
    #    #{
    #        x = self.upper.vis_x(vsh);
    #    #}
    #    return x;
    ##}
    #public int vis_y_UpperElement(TValsShowHide vsh = null)
    ##{
    #    int y = 0;
    #    if (self.upper != null )
    #    #{
    #        y = self.upper.vis_y(vsh);
    #    #}
    #    return y;
    ##}
    #public int vis_yLower_UpperElement(TValsShowHide vsh = null)
    ##{
    #    int yLower = 0;
    #    if (self.upper != null )
    #    #{
    #        yLower = self.upper.vis_yLower(vsh);
    #    #}
    #    return yLower;
    ##}
    #public int vis_yUpper_UpperElement(TValsShowHide vsh = null)
    ##{
    #    int yUpper = 0;
    #    if (self.upper != null )
    #    #{
    #        yUpper = self.upper.vis_yUpper(vsh);
    #    #}
    #    return yUpper;
    ##}
    #public int vis_L_UpperElement(TValsShowHide vsh = null)
    ##{
    #    int L = 0;
    #    if (self.upper != null )
    #    #{
    #        L = self.upper.vis_L(vsh);
    #    #}
    #    return L;
    ##}
    #public int vis_H_UpperElement(TValsShowHide vsh = null)
    ##{
    #    int H = 0;
    #    if (self.upper != null )
    #    #{
    #        H = self.upper.vis_H(vsh);
    #    #}
    #    return H;
    ##}
    #
    def CoordsToStr(self, vsh):
    #{
        s="R"+str(self.curN)+": "
        #int x, y;
        x=self.vis_x(vsh)
        y=self.vis_y(vsh)
        s = s + " Coords: "
        s = s + "(" + str(x) + "; " + str(y) + ") "
        x = self.vis_L(vsh)
        y = self.vis_H(vsh)
        s = s + " Size: "
        s = s + "(" + str(x) + " x " + str(y) + ") "
        x = self.vis_x_Caption(vsh)
        y = self.vis_y_Caption(vsh)
        s = s + " Cap: "
        s = s + "(" + str(x) + "; " + str(y) + ") "
        x = self.vis_x_cornerLeft(vsh)
        s = s + " Corners: "
        x = self.vis_x_cornerLeft(vsh)
        s = s + " xL=" + str(x) + "; "
        x = self.vis_x_cornerRight(vsh)
        s = s + " xR="+str(x)+"; "
        y = self.vis_y_cornerLower(vsh)
        s = s + " yL=" + str(y) + "; ";
        y = self.vis_y_cornerUpper(vsh)
        s = s + " yU=" + str(y) + "; ";
        s = s + " Connectors: ";
        s = s + " Left: ";
        x = self.vis_x_LeftConnection(vsh)
        y = self.vis_y_LeftConnection(vsh)
        s = s + "(" + str(x) + "; " + str(y) + ") "
        s = s + " Right: ";
        x = self.vis_x_RightConnection(vsh);
        y = self.vis_y_RightConnection(vsh);
        s = s + "(" + str(x) + "; " + str(y) + ") "
        return s
    #}
    def ShowCoords_IpseAndSub(self, vsh):
    #{
        s = self.CoordsToStr(vsh);
        print( s)
        QElements=0
        if isinstance(self.elems, list) and len(self.elems)>0:
            QElements=len(self.elems)
            #for (int i = 1; i <= self.QElements; i++)
            for i in range(1, QElements+1):
        #{
                self.elems[i - 1].ShowCoords_IpseAndSub(vsh)
        #}
    #}
            
    def vis_Display_WithSubElts(self, canvas, vsh = 0):
    #{
        #int x, y, x1, y1;
        if(vsh!=0):
            print( "");
            print( "vis_Display_WithSubElts starts working. R" + str(self.curN))
        #
        QElements = 0
        if isinstance(self.elems, list) and len(self.elems)>0:
            QElements =len(self.elems)
        #
        top = self.nav_GoToTop()
        #canvas.SetSize(top.vis_L_WithConnectors(null), top.vis_H(null));
        if (self.upper == 0):
        #{
            canvas.SetSize(top.vis_L_WithConnectors(0), top.vis_H(0))
            canvas.Clear()
        #}
        #
        if (self.upper == 0):
        #{
            #canvas.SetSize(self.vis_L_WithConnectors(null), self.vis_H(null));
            #
            x = self.vis_x_LeftConnection(vsh)
            y = self.vis_y_LeftConnection(vsh)
            canvas.Draw_ConnectorCentral(x, y)
            x = self.vis_x_RightConnection(vsh)
            y = self.vis_y_RightConnection(vsh)
            canvas.Draw_ConnectorCentral(x, y)
        #}
        if (QElements == 0):
        #{
            x = self.vis_x(vsh)
            y = self.vis_y(vsh)
            canvas.Draw_ResistanceElementar(x, y, self.curN)
        #}
        else:
        #{
            #Draw_FrameName
            x = self.vis_x_Caption()
            y = self.vis_y_Caption()
            canvas.Draw_FrameName(x, y, self.curN)
            #LineFrameIntersection left
            x = self.vis_x(vsh)
            y = self.vis_y(vsh)
            canvas.Draw_LineFrameIntersection(x, y)
            #LineFrameIntersection right
            x = self.vis_x_cornerRight(vsh)
            y = self.vis_y(vsh)
            canvas.Draw_LineFrameIntersection(x, y)
            #hor frame
            x1 = self.vis_x_cornerRight(vsh)-1
            #upper frame
            x = self.vis_x_Caption(vsh)+1
            y = self.vis_y_cornerUpper(vsh)
            #for (int CurX = x; CurX <= x1; CurX++)
            for CurX in range(x, x1+1):
            #{
                canvas.Draw_FrameElementHorisontal(CurX, y)
            #}
            #lower frame
            x = self.vis_x(vsh)+1
            y = self.vis_y_cornerLower(vsh)
            #for (int CurX = x; CurX <= x1; CurX++)
            for CurX in range(x, x1+1):
            #{
                canvas.Draw_FrameElementHorisontal(CurX, y)
            #}
            #vert frame
            y = self.vis_y_cornerUpper(vsh)+1
            y1 = self.vis_y(vsh)-1 
            x = self.vis_x_cornerLeft(vsh)
            x1 = self.vis_x_cornerRight(vsh)
            #for (int CurY = y; CurY <= y1; CurY++)
            for CurY in range(y, y1+1):
            #{
                canvas.Draw_FrameElementVertical(x, CurY)
                canvas.Draw_FrameElementVertical(x1, CurY)
            #}
            y = self.vis_y(vsh) + 1;
            y1 = self.vis_y_cornerLower(vsh) - 1;
            x = self.vis_x_cornerLeft(vsh);
            x1 = self.vis_x_cornerRight(vsh);
            #for (int CurY = y; CurY <= y1; CurY++)
            for CurY in range(y, y1+1):
            #{
                canvas.Draw_FrameElementVertical(x, CurY)
                canvas.Draw_FrameElementVertical(x1, CurY)
            #}
            #Corners
            #Left 
            x = self.vis_x_cornerLeft(vsh)
            #Left upper
            y = self.vis_y_cornerUpper(vsh)
            #canvas.Draw_ResistanceLeftSide(x, y);#vikt! ecri right corner alt left! qob?
            canvas.Draw_FrameElementLeft(x, y)
            #Left lower
            y = self.vis_y_cornerLower(vsh)
            #canvas.Draw_ResistanceLeftSide(x, y);
            canvas.Draw_FrameElementLeft(x, y)
            #Right
            x = self.vis_x_cornerRight(vsh)#vikt! ecri right corner alt left! qob?
            #Right upper
            y = self.vis_y_cornerUpper(vsh)
            #canvas.Draw_ResistanceRightSide(x, y);
            canvas.Draw_FrameElementRight(x, y)
            #Right lower
            y = self.vis_y_cornerLower(vsh)
            #canvas.Draw_ResistanceRightSide(x, y);#vikt! ecri right corner alt left! qob?
            canvas.Draw_FrameElementRight(x, y)
            #Sub-elements
            #for (int i = 1; i <= self.QElements; i++)
            for  i in range(1, QElements+1):
            #{
                self.elems[i - 1].vis_Display_WithSubElts(canvas, vsh)
            #}
            #self.elems[self.QElements - 1].vis_Display_WithSubElts(canvas, vsh);
            if (self.Conn_Suc0Par1 == 0):
            #{
                #
                #for (int i = 2; i <= self.QElements; i++)
                for  i in range(2, QElements+1):
                #{
                    x = self.elems[i - 1].vis_x_LeftConnection(vsh)
                    y = self.elems[i - 1].vis_y_LeftConnection(vsh)
                    canvas.Draw_ConnectorCentral(x, y)
                #}
            #}
            else: #self.Conn_Suc0Par1 == 1
            #{
                #connectors
                #for (int i = 1; i <= self.QElements; i++)
                for  i in range(1, QElements+1):
                #{
                    x = self.elems[i - 1].vis_x_LeftConnection(vsh)
                    y = self.elems[i - 1].vis_y_LeftConnection(vsh)
                    if (i == 1):
                    #{
                        canvas.Draw_ConnectorCentral(x, y)
                    #}
                    elif (i == QElements):
                    #{
                        canvas.Draw_ConnectorLeft(x, y)
                    #}
                    else:
                    #{
                        canvas.Draw_ConnectorLeft(x, y)
                    #}
                    #
                    x = self.elems[i - 1].vis_x_RightConnection(vsh)
                    y = self.elems[i - 1].vis_y_RightConnection(vsh)
                    if (i == 1):
                    #{
                        canvas.Draw_ConnectorCentral(x, y)
                    #}
                    elif (i == QElements):
                    #{
                        canvas.Draw_ConnectorRight(x, y)
                    #}
                    else:
                    #{
                        canvas.Draw_ConnectorRight(x, y)
                    #}
                #}#for conectors
                #Lines
                #vertical lines
                #for (int i = 2; i <= self.QElements; i++)
                for  i in range(2, Elements+1):
                #{
                    x = self.elems[i - 1 - 1].vis_x_LeftConnection(vsh)
                    x1 = self.elems[i - 1 ].vis_x_RightConnection(vsh)
                    y = self.elems[i - 1 - 1].vis_y_LeftConnection(vsh)
                    y1 = self.elems[i - 1].vis_y_LeftConnection(vsh)
                    #for (int curY = y + 1; curY <= y1 - 1; curY++)
                    for curY in range(y + 1, curY <= y1 - 1+1):
                    #{
                        canvas.Draw_LineVertical(x, curY)
                        canvas.Draw_LineVertical(x1, curY)
                    #}
                #}
                #hor lines
                #for (int i = 1; i <= self.QElements; i++)
                for  i in range(1, Elements+1):
                #{
                    x = self.elems[i - 1].vis_x_RightConnection(vsh)-1
                    x1 = self.elems[i - 1].vis_x(vsh) + self.elems[i - 1].vis_L(vsh)
                    y = self.elems[i - 1].vis_y(vsh)
                    #for (int curX = x1; curX <= x; curX++)
                    for curX in range(x1, x+1):
                    #{
                        canvas.Draw_LineHorisontal(curX, y)
                    #}
                #}
            #}
        #}
        if(vsh!=0):
            print( "vis_Display_WithSubElts finishes working. R" + str(self.curN))
    #}#fn draw all, ma name'd aso: vis_Display_WithSubElts
    def DisplaySchem(self, canvas, vsh = 0):
    #{
        top = self.nav_GoToTop()
        canvas.SetSize(top.vis_L_WithConnectors(vsh), top.vis_H(vsh))
        top.vis_Display_WithSubElts(canvas, vsh)
    #}
    #nav
    def  nav_GoToTop(self):
    #{
        ptr = self
        while (ptr.upper != 0):
        #{
            ptr = ptr.upper
        #}
        return ptr
    #}
    def nav_GoToUpper(self):
    #{
        return self.upper
    #}
    def nav_Enter(self):
    #{
        subElt = self#in C# wa null
        if isinstance(self.elems, list) and len(self.elems)>0:
        #{
            subElt = self.elems[1 - 1]
        #}
        return subElt
    #}
    def nav_SubEltN(self, N):
    #{
        subElt = 0
        if ( isinstance(self.elems, list) and len(self.elems)>0 and N >= 1 and N <= len(self.elems)):
        #{
            subElt = self.elems[N - 1]
        #}
        return subElt
    #}
    def nav_Prev(self):
    #{
        R = 0# subElt = null;
        #
        #if (self.upper != null && self.NinUpper > 1 && self.NinUpper <= self.upper.QElements)
        if (self.upper != 0 and self.NinUpper > 1 and isinstance(self.upper.elems, list) and  self.NinUpper <= len(self.upper.elems)):
        #{
            #subElt 
            R= self.upper.elems[self.NinUpper - 1 - 1]
        #}
        return R# subElt;
    #}
    def nav_Next(self):
    #{
        R =0# subElt = null;
        #
        #if (self.upper != null && self.NinUpper >= 1 && self.NinUpper < self.upper.QElements)
        if (self.upper != 0 and self.NinUpper >= 1 and isinstance(self.upper.elems, list) and  self.NinUpper < len(self.upper.elems)):
        #{
            #subElt = self.upper.elems[self.NinUpper + 1 - 1];
            R = self.upper.elems[self.NinUpper + 1 - 1]
        #}
        return R# subElt;
    #}
    def nav_First(self):
    #{
        R = self#in C# was null;# subElt = null;
        if (self.upper != 0):
        #{
            #subElt = self.elems[1 - 1];
            R = self.upper.elems[1 - 1]
        #}
        return R# subElt;
    #}
    def nav_Last(self):
    #{
        R = self#in C# null;# subElt = null;
        if (self.upper != 0):
        #{
            #subElt = self.elems[self.upper.QElements - 1];
            #if isinstance(self.upper.elems, list) and len(self.upper.elems)>0:
               R = self.upper.elems[len(self.upper.elems) - 1]
        #}    
        return R# subElt;
    #}
    #
    #
    def CheckRIf_CoordsBelongToThisR(self, x, y, vsh = 0):
    #{
        b = 0
        #int xL, xR, yL, yU;
        if(vsh!=0):
            print( "CheckRIf_CoordsBelongToThisR starts working");
        xL = self.vis_x_cornerLeft()
        xR = self.vis_x_cornerRight()
        yU = self.vis_y_cornerUpper()
        yL = self.vis_y_cornerLower()
        if(vsh!=0):
            print( "Must be: L=" + str(y) + " E [" + str(xL) + "; " + str(xR) + "], C=" + styr(y) + " E [" + str(yU) + "; " + str(yL) + "]");
        if (x >= xL and x <= xR and y >= yU and y <= yL):
        #{
            b = 1
        #}
        if(vsh!=0):
            print( "CheckRIf_CoordsBelongToThisR finishes working. Answer: " + str(b))
        return b
    #}
    def CheckRIf_CoordsBelongToThisR(self, x, y):
    #{
        b=0
        #int xL, xR, yL, yU;
        xL=self.vis_x_cornerLeft()
        xR=self.vis_x_cornerRight()
        yU=self.vis_y_cornerUpper()
        yL=self.vis_y_cornerLower()
        if (x >= xL and x <= xR and y >= yU and y <= yL):
        #{
            b=1
        #}
        return b
    #}
    def CheckRIf_CoordsAreOfThisR(self, x, y):
    #{
        #return ( x == self.vis_x(0) && y == self.vis_y(0) )
        verdict=0
        if x == self.vis_x(0) and y == self.vis_y(0):
            verdict=1
        return verdict
    #}
    def CheckRIf_CapIsOfThisR(self, x, y):
    #{
        #return (x == self.vis_x_Caption(null) && y == self.vis_y_Caption(null));
        verdict=0
        if x == self.vis_x_Caption(0) and y == self.vis_y_Caption(0):
            verdict=1
        return verdict
    #}
    def CheckRIf_NisOfThisElement(self, N,  i = 0):# ab hin !!!!!!!!!!!!!!!!!!
    #{
        R=0
        if self.curN==N:
            R=1
        return R
    #}
    #private delegate bool SearchCondition(int p1, int p2);
    def  SeekElementByNPrimitive(self, N, vsh = 0):
    #{
        if(vsh!=0):
            print( "Recursive search fn SeekElementByNPrimitive starts working, for: " + self.ToStringShort())
        cur = self
        QElements=0
        R = 0# = self.nav_GoToTop();#no: if fn s'recursive, so S ms'abdo ab cur
        #bool found = false, contin;
        found = 0
        SE_N = 0
        #found = (cur.GetN() == N)
        found=0
        if cur.GetN() == N:
            found=1
        if (found==1):
        #{
            R = cur
            if(vsh!=0):
                print( "Found at: " + R.ToStringShort())
        #}
        else:
        #{
            if(vsh!=0):
                print( "Not Found at: " + self.ToStringShort())
        #}
        #contin = !found;
        if found==0:
            contin=1
        elif found==1:
            contin=0
        if (contin==1):
        #{
            #contin = (self.QElements > 0);
            if isinstance(self.elems, list) and len(self.elems)>0:
                contin=1
            else:
                contin=0
            if (contin==1):
            #{
                if(vsh!=0):
                    print( "Trying to seek in Sub-Elts");
            #}
            else:
            #{
                if(vsh!=0):
                    print( "Search is over. Not found.");
            #}
        #}
        while (contin==1):
        #{
            SE_N=SE_N+1
            cur = self.elems[SE_N - 1]#cur = cur.elems[SE_N - 1];
            if(vsh!=0):
                print( "Sub-elt N " + str(SE_N) + " - " + cur.ToStringShort())
            R = cur.SeekElementByNPrimitive(N, vsh)
            found = (R != null);
            if R==0:
                found=0
            else :
                found=1
            #contin = !found;
            if found==0:
                contin=1
            elif found==1:
                contin=0
            if(vsh!=0):
                print( "found=" + str(found) + " contin=" + str(contin))
            if (contin==1):
            #{
                #contin = (SE_N < self.QElements);
                if isinstance(self.elems, list) and len(self.elems)>0 and SE_N <len(self.elems):
                    contin=1
                    QElements=len(self.elems)
                else:
                    contin=0
            #}
            if(vsh!=0):
                print( "SE_N=" + str(SE_N) + " Q=" + str(QElements) + " contin=" + str(contin))
        #}
        if (found==1):
        #{
            #R = cur;#!
            if(vsh!=0):
                print( "Finally: Found at: " + R.ToStringShort())
        #}
        else:
        #{
            if(vsh!=0):
                print( "Finally: Not found");
        #}
        if(vsh!=0):
            print( "Recursive search fn SeekElementByNPrimitive finishes working, for: " + self.ToStringShort());
        return R
    #}
    def SeekElementByCoordsPrimitive(self, x, y, vsh = 0):
    #{
        if(vsh!=0):
            print( "Recursive search fn SeekElementByCoordsPrimitive starts working, for: " + self.ToStringShort());
        cur=self
        R=0# = self.nav_GoToTop();#no: if fn s'recursive, so S ms'abdo ab cur
        #found = 0
        #contin;
        SE_N = 0
        #found = (cur.vis_x(vsh) == x && y==cur.vis_y(vsh));
        if cur.vis_x(vsh) == x and y==cur.vis_y(vsh):
            found=1
        else:
            found=0
        if (found==1):
        #{
            R = cur
            if(vsh!=0):
                print( "Found at: " + R.ToStringShort())
        #}
        else:
        #{
            if(vsh!=0):
                print( "Not Found at: " + self.ToStringShort())
        #}
        #contin = !found;
        if found==1:
            contin=0
        elif found==0:
            contin=1
        #
        if (contin==1):
        #{
            #contin = (self.QElements > 0);
            if (self.QsubElts() > 0):
                contin=1
            else:
                contin=0
            if (contin==1):
            #{
                if(vsh!=0):
                    print( "Trying to seek in Sub-Elts");
            #}
            else:
            #{
                if(vsh!=0):
                    print( "Search is over. Not found.");
            #}
        #}
        while (contin==1):
        #{
            SE_N=SE_N+1
            cur = self.elems[SE_N - 1]#cur = cur.elems[SE_N - 1];
            if(vsh!=0):
                print( "Sub-elt N " + str(SE_N)+" - "+cur.ToStringShort())
            R = cur.SeekElementByCoordsPrimitive(x, y, vsh)
            #found = (R != null);
            if R==0:
                found=0
            else:
                found=1
            #contin = !found;
            if found==0:
                contin=1
            else:
                contin=0
            if(vsh!=0):
                print( "found=" + str(found) + " contin=" + str(contin))
            if (contin==1):
            #{
                #contin = (SE_N < self.QElements);
                if SE_N < self.QSubElts():
                    contin=1
                else:
                    contin=0
            #}
            #print( "SE_N=" + SE_N.ToString() + " Q=" + self.QElements.ToString() + " contin=" + (MyLib.BoolToInt(contin)).ToString());
            if(vsh!=0):
                print( "SE_N=" + str(SE_N) + " Q=" + str(self.QSubElts()) + " contin=" + str(contin))
        #}
        if (found==1):
        #{
            #R = cur;#!
            if(vsh!=0):
                print( "Finally: Found at: " + R.ToStringShort())
        #}
        else:
        #{
            if(vsh!=0):
                print( "Finally: Not found");
        #}
        if(vsh!=0):
            print( "Recursive search fn SeekElementByCoordsPrimitive finishes working, for: " + self.ToStringShort())
        return R
    #}
    def GetPathString(self, vsh=0):
    #{
        R = "R" + str(self.curN)
        if(vsh!=0):
            print(R)
        cur = self
        while (cur.upper != 0):
        #{
            #
            R = "/<N[" + str(cur.NinUpper) + "]>/" + R
            R = "R" + str(cur.upper.GetN()) + R
            if(vsh!=0):
                print(R)
            cur=cur.get_uper()
        #}
        return R
    #}
    def SeekElementByCoordsBelongingPrimitive(self, x, y, vsh = 0):
    #{
        print( "Recursive search fn SeekElementByCoordsBelongingPrimitive starts working, for: " + self.ToStringShort())
        #HydroPipelineElement
        cur = self
        R = 0#null;# = self.nav_GoToTop();#no: if fn s'recursive, so S ms'abdo ab cur
        found = 0
        #bool contin, caught;
        SE_N = 0;
        xL = self.vis_x_cornerLeft(0)
        xR = self.vis_x_cornerRight(0)
        yL = self.vis_y_cornerLower(0)
        yU = self.vis_y_cornerUpper(0)
        caught = CheckRIf_CoordsBelongToThisR(x, y, vsh)
        if caught:
        #{
            if(vsh!=0):
                print( "Caught at: " + self.ToStringShort());
            if (QElements == 0 or ((x == xL or x == xR) and (y <= yL and y >= yU)) or ((y == yL or y == yU) and (x <= xR and x >= xL))):
            #{
                found = 1
                contin = 0
                R = self;
                if (QElements == 0):
                #{
                    if(vsh!=0):
                        print( "Found (Q=0) at: " + R.ToStringShort())
                #}
                if ((x == xL or x == xR) and (y <= yL and y >= yU)):
                #{
                   if(vsh!=0):
                       print( "Found (contour vert) at: " + R.ToStringShort())
                #}
                if ((y == yL or y == yU) and (x <= xR and x >= xL)):
                #{
                    if(vsh!=0):
                        print( "Found (contour hor) at: " + R.ToStringShort())
                #}
            #}else#{
                if(vsh!=0):
                    print( "Seek in sub-Elts: ")
                contin = 1
                while(contin==1):#{
                    SE_N=SE_N+1;
                    cur = self.elems[SE_N - 1];
                    if(vsh!=0):
                        print( "Checking element:" + SE_N.ToStringShort() + ") " + cur.ToStringShort())
                    R=cur.SeekElementByCoordsBelongingPrimitive(x, y, vsh)
                    if(R!=0):#{
                        contin=0;
                        found = 1;
                    #}
                    if(contin):#{
                        contin=(SE_N<QElements)
                    #}
                #}
            #}#seek in hin or in Sub-Elts
            if (found==0):
            #{
                R = self
                found = 1
            #}
        #}#if caught or not    
        if (found==1):
        #{
            if(vsh!=0):
                print( "Finally: Found at: " + R.ToStringShort())
        #}
        else:
        #{
            if(vsh!=0):
                print( "Finally: Not found")
        #}
        if(vsh!=0):
            print( "Recursive search fn SeekElementByCoordsBelongingPrimitive finishes working, for: " + self.ToStringShort())
        return R
    #}
     
    def SeekElementByDelegate(self, typeN_, p1, p2, vsh=0):
    #{
        #SearchCondition dlgt = self.CheckRIf_NisOfThisElement;
        #switch (typeN_)
        ##{
        #    case 1:
        #        dlgt = self.CheckRIf_CoordsBelongToThisR;
        #        break;
        #    case 2:
        #        dlgt = self.CheckRIf_CoordsAreOfThisR;
        #        break;
        #    case 3:
        #        dlgt = self.CheckRIf_CapIsOfThisR;
        #        break;
        #    case 4:
        #        dlgt = self.CheckRIf_NisOfThisElement;
        #        break;
        #}
        #copy
        if(vsh!=0):
            print( "Recursive search fn SeekElementByDelegate starts working, for: " + self.ToStringShort());
        #HydroPipelineElement
        cur = self
        R = 0# = self.nav_GoToTop();#no: if fn s'recursive, so S ms'abdo ab cur
        found = 0
        #contin;
        SE_N = 0
        QElements=0
        if isinstance(self.elems, list) and len(self.elems>0):
            QElements=len(self.elems)
        #
        #found = dlgt(p1, p2);
        #
        if typeN_==1:
            found=self.CheckRIf_CoordsBelongToThisR(p1, p2)
        elif typeN_==2:
            found=self.CheckRIf_CoordsAreOfThisR(p1, p2)
        elif typeN_==3:
            found=self.CheckRIf_CapIsOfThisR(p1, p2)
        elif typeN_==4:
            found=self.CheckRIf_NisOfThisElement(p1, p2)
        #
        if (found==1):
        #{
            R = cur;
            if(vsh!=0):
                print( "Found at: " + R.ToStringShort());
        #}
        else:
        #{
            if(vsh!=0):
                print( "Not Found at: " + self.ToStringShort());
        #}
        #contin = !found;
        if contin==1:
            found=0
        elif contin==0:
            found=1
        if (contin==1):
        #{
            #contin = (QElements > 0);
            if QElements > 0:
                contin=1
            else:
                contin=0
            if (contin==1):
            #{
                if(vsh!=0):
                    print( "Trying to seek in Sub-Elts");
            #}
            else:
            #{
                if(vsh!=0):
                    print( "Search is over. Not found.");
            #}
        #}
        while (contin==1):
        #{
            SE_N=+SE_N+1;
            cur = self.elems[SE_N - 1]#;#cur = cur.elems[SE_N - 1];
            if(vsh!=0):
                print( "Sub-elt N " + str(SE_N) + " - " + cur.ToStringShort())
            R = cur.SeekElementByDelegate( typeN_,  p1,  p2,  vsh)
            #found = (R != null);
            if isinstance(R, HResSimple):#R!=0:
                found=1
            else:
                found=0
            #contin = !found;
            if contin==1:
                found=0
            elif contin==0:
                found=1
            if(vsh!=0):
                print( "found=" + str(found) + " contin=" + str(contin))
            if (contin==1):
            #{
                contin = (SE_N < QElements);
                if SE_N < QElements:
                    contin=1
                else:
                    contin=0
             #}
            if(vsh!=0):
                print( "SE_N=" + str(SE_N) + " Q=" + str(QElements) + " contin=" + str(contin))
        #}
        if (found==1):
        #{
            #R = cur;#!
            if(vsh!=0):
                print( "Finally: Found at: " + R.ToStringShort())
        #}
        else:
        #{
            if(vsh!=0):
                print( "Finally: Not found");
        #}
        if(vsh!=0):
            print( "Recursive search fn SeekElementByDelegate finishes working, for: " + self.ToStringShort())
        return R
    #}#fn
    #
    # 
    #public TTable hydroResistance_IniDataAdvanced_GetAsTable()
    ##{
    #    TTable tbl= self.HydroRData.IniData.GetAsTable();
    #    DataCell cell = new DataCell(new string[] #{ "--", "#" #}, 2);
    #    if (self.GetIfConnectionTypeIsSucc())
    #    #{
    #        cell.SetActiveN(1);
    #    #}
    #    else
    #    #{
    #        cell.SetActiveN(2);
    #    #}
    #    DataCellRowCoHeader row = new DataCellRowCoHeader(new DataCell("Conn.Type"), new DataCellRow(new DataCell[] #{ cell #}, 1));
    #    tbl.InsLine(1, row);
    #    return tbl;
    ##}
    #public void hydroResistance_IniDataAdvanced_SetFromTable(TTable tbl)
    ##{
    #    self.Conn_Suc0Par1 = tbl.GetIntVal(1, 1) - 1;
    #    self.HydroRData.IniData.SetFromTable(tbl, 1);
    ##}
    ##
    #public TTable hydroResistance_IniData_GetAsTable()
    ##{
    #    return self.HydroRData.IniData.GetAsTable();
    ##}
    #public void hydroResistance_IniData_SetFromtTable(TTable tbl)
    ##{
    #    self.HydroRData.IniData.SetFromTable(tbl);
    ##}
    ##    



        
