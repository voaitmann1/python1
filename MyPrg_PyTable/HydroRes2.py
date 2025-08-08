import copy
import math

class HResSimple:
    def __init__(self, k=0, curN=0, Conn_Suc0Par1=0, upper=0, Ress=[], outerN=0, vsh=0):
        if vsh==1:
            print('RConstr HResSimple starts working ')
            print("Given params: k="+str(k)+" curN="+str(curN)+" Conn_Suc0Par1="+str(Conn_Suc0Par1)+ " outerN="+str(outerN))
        self.SetDefault()#uz self.Elements=[]
        self.Conn_Suc0Par1=Conn_Suc0Par1
        self.k=k
        Q=0
        if isinstance(Ress, list):
            Q=len(Ress)
        if  vsh==1:
            print("Sub-Elts given : Q="+str(Q))
        for i in range(1, Q+1):
            Element=copy.deepcopy(Ress[i-1])
            self.Elements.append(Element)
        self.curN=curN
        self.outerN=outerN
        self.upper=upper
        if(vsh==1):
            print('RConstr HResSimple  finishes working '+self.__str__())

#def __init__(self, k=0, curN=0, Conn_Suc0Par1=0, upper=0, Ress=[], outerN=0, vsh=0):
    def Set(self, k=0, curN=0, Conn_Suc0Par1=0, upper=0, Ress=[], outerN=0, vsh=0):
        self.Conn_Suc0Par1=Conn_Suc0Par1
        self.k=k
        Q=0
        if isinstance(Ress, list):
            Q=len(Ress)
        for i in range(1, Q+1):
            Element=copy.deepcopy(Ress[i-1])
            self.Elements.append(Element)
        self.curN=curN
        self.outerN=outerN
        self.upper=upper

    def QSubElts(self):
        Q=0
        if isinstance(self.Elements, list) and len(self.Elements)>0:
            Q=len(self.Elements)
        return Q
            
    def SetDefault(self):
        self.Elements=[]
        self.Conn_Suc0Par1=0
        

    def Calc(self, vsh=0):
        S=0
        C=0
        if(vsh==1):
            print('Calc starts working '+self.__str__())
            print(self.__str__())
        R=self.k
        if(vsh==1):
            print('R='+str(R))
        L=len(self.Elements)
        if(vsh==1):
            print('L='+str(L))
        #if(L>0):#abl ac ce
        if self.Conn_Suc0Par1==0:
            if(vsh==1):
                print('succ conn')
            S=0
            for i in range(1, L+1):
                C=self.Elements[i-1].Calc()
                if(vsh==1):
                    print("prev Calc finished, external one continueing")
                C=C*C
                S=S+C
                if(vsh==1):
                    print("RN"+str(i)+" k="+str(self.Elements[1-1].k)+" C="+str(C)+" S="+str(S))
            R=R+math.sqrt(S)
        elif self.Conn_Suc0Par1==1:
            S=0
            if(vsh==1):
                print('parallel conn')
            for i in range(1, L+1):
                C=1/self.Elements[i-1].Calc()
                if(vsh==1):
                    print("prev Calc finished, external one continueing")
                S=S+C
                if(vsh==1):
                    print("RN"+str(i)+" k="+str(self.Elements[1-1].k)+" C="+str(C)+" S="+str(S))
            if(S!=0):
                R=R+1/S
        if(vsh==1):
            print('R='+str(R))
            print('Calc finishes working '+self.__str__())
        return R

    def AddInner(self, ElementExt, vsh=0):
        if(vsh==1):
            print('AddInner starts working '+self.__str__())
        Element=copy.deepcopy(ElementExt)
        Q=0
        if isinstance(self.Elements, list):
            Q=len(self.Elements)
        Element.outerN=Q+1
        Element.upper=self
        if(vsh==1):
            print('trying to add: '+Element.__str__())
        self.Elements.append(Element)
        if(vsh==1):
            Q=len(self.Elements)
            print('trying to add: '+self.Elements[Q-1].__str__())
        if(vsh==1):
            print('AddInner finishes working '+self.__str__())

    def DelInner(self, N):
        row=[]
        Q=len(self.Elements)
        if N>=1 and N<=len(self.Elements):
            for i in range(1, N-1+1):
                row.append(self.Elements[i-1])
            for i in range(N+1, Q+1):
                Element=self.Elements[i-1]
                Element.outerN=Element.outerN-1
                Element.upper=self
                row.append(Element)
            self.Elements=row

    def InsInnerN(self, ElementExt, N):
        row=[]
        ElementToIns=copy.deepcopy(ElementExt)
        Q=len(self.Elements)
        if N>=1 and N<=Q:
            for i in range(1, N-1+1):
                Element=self.Elements[i-1]
                #Element.outerN=Element.outerN
                Element.upper=self
                row.append(Element)
            ElementToIns.outerN=N
            row.append(ElementToIns)
            for i in range(N, Q+1):
                Element=self.Elements[i-1]
                Element.outerN=Element.outerN+1
                Element.upper=self
                row.append(Element)
            self.Elements=row

    def LinkToTopR(self, vsh=0):
        if vsh==1:
            print("LinkToTopR starts working")
        ptr=self.upper
        if vsh==1:
            print("At Start: self="+self.__str__())
        if ptr!=0:
            print("At Start:  upper= R"+str(self.upper.curN))
            while ptr.upper!=0:
                ptr=ptr.upper
                if vsh==1:
                    print("now ptr=R"+str(ptr.curN))
        else:
            ptr=self
            if vsh==1:
                print("upper="+str(self.upper))
        if vsh==1:
            print("LinkToTopR finishes working. ptr=R"+str(ptr.curN))
        return ptr

    def CurPresentNsList(self, Ns=[], vsh=0):
        Ns.append(self.curN)
        Q=0
        if isinstance(self.Elements, list) and len(self.Elements)>0:
            Q=len(self.Elements)
        for i in range(1, Q+1):
            self.Elements[i-1].CurPresentNsList(Ns)

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
    #    #def __init__(self, k=0, curN=0, Conn_Suc0Par1=0, upper=0, Ress=[], outerN=0, vsh=0):
    #    if self.upper==0:
    #        ElementInstead=HResSimple(self.k, newN, self.Conn_Suc0Par1, self, self.Elements, vsh)
    #        #
    #        self.k=k_new
    #        self.Conn_Suc0Par1=0
    #        self.AddInner(ElementInstead)
    #        self.AddInner(ElementToAdd)
    #    elif isinstance(self.upper, HResSimple):#so!, not else, S cog S int et ecri: int ne ha flds 
    #        QUpperSubElts=self.upper.QSubElts()
    #        if self.upper.Conn_Suc0Par1==0:
    #            if self.outerN==QUpperSubElts:
    #                self.upper.AddInner(ElementToAdd)
    #            else:
    #                self.upper.InsInnerN(ElementToAdd, self.outerN+1)
    #        else:#self.upper.Conn_Suc0Par1==1
    #            ##def __init__(self, k=0, curN=0, Conn_Suc0Par1=0, upper=0, Ress=[], outerN=0, vsh=0):
    #            ElementInstead=HResSimple(self.k, newN, self.Conn_Suc0Par1, self, self.Elements, vsh)
    #            #
    #            #ElementUpper.AddInner(ElementInstead)
    #            #ElementUpper.AddInner(ElementToAdd)
    #            if self.outerN==QUpperSubElts:
    #                self.upper.AddInner(ElementToAdd)
    #            else:
    #                self.upper.InsInnerN(ElementToAdd, self.outerN+1)
    #            self.k=k_new
    #            self.Conn_Suc0Par1=0

    def AddSucSmart(self, ElementExt, smartAdd=0, k_new=0, vsh=0):
        if vsh==1:
            print("AddSucSmart starts working")
        newN=self.FirsrAbsentN()#;#ne sees tic exnot char!
        ElementToAdd=copy.deepcopy(ElementExt)
        if vsh==1:
            print("Adding to: "+self.__str__())
            print("Adding what: "+ElementToAdd.__str__())
            print("new N = "+str(newN))
        ##def __init__(self, k=0, curN=0, Conn_Suc0Par1=0, upper=0, Ress=[], outerN=0, vsh=0):
        if self.upper==0 or ( isinstance(self.upper, HResSimple) and self.upper.Conn_Suc0Par1==1):
            if vsh==1:
                if self.upper==0:
                    print("No upper Rs. This will be first added, param - second")
                if isinstance(self.upper, HResSimple) and self.upper.Conn_Suc0Par1==1:
                     print("Trying conn -- to || con'd R")
                print("R, to which we try to conn, will be container of self's copy and connected R")
            ##def __init__(self, k=0, curN=0, Conn_Suc0Par1=0, upper=0, Ress=[], outerN=0, vsh=0):
            ElementInstead=HResSimple(self.k, newN, self.Conn_Suc0Par1, self, self.Elements, vsh)
            if vsh==1:
                print("Copy: "+ElementInstead.__str__())
            #
            self.k=k_new
            self.Conn_Suc0Par1=0
            if vsh==1:
                print("Self ef adding: "+self.__str__())
                print("Adding copy:")
            self.AddInner(ElementInstead)
            if vsh==1:
                print("Self ef adding copy:")
                self.Show_WithSubElts()
                print("Adding R to Add:")
            self.AddInner(ElementToAdd)
            if vsh==1:
                print("Finally: ")
                self.Show_WithSubElts()
        else:
            QUpperSubElts=self.upper.QSubElts()
            if self.outerN==QUpperSubElts:
                if vsh==1:
                    print("This is sub-element, one ("+str(self.outerN)+") of "+str(QUpperSubElts)+", inited par, last, will be added")
                self.upper.AddInner(ElementToAdd)
            else:
                if vsh==1:
                    print("This is sub-element, one ("+str(self.outerN)+") of "+str(QUpperSubElts)+", inited par,  not last, will be ins'd")
                self.upper.InsInnerN(ElementToAdd, self.outerN+1)
            if vsh==1:
                print("Finally: ")
                self.Show_WithSubElts()
        if vsh==1:
            print("AddSucSmart finishes working") 

   
        

    #def AddParSmart(self, ElementExt, smartAdd=0, k_new=0, vsh=0):
    #    if vsh==1:
    #        print("AddParSmart starts working")
    #    newN=self.FirsrAbsentN();
    #    ElementToAdd=copy.deepcopy(ElementExt)
    #    if vsh==1:
    #        print("Adding to: "+self.__str__())
    #        print("Adding what: "+self.__str__())
    #        print("new N = "+str(newN))
    #    #def __init__(self, k=0, curN=0, upper=0, Conn_Suc0Par1=0, Ress=[], outerN=0, vsh=0):
    #    if self.upper==0:
    #        if vsh==1:
    #            print("No upper Rs. This will be first added, param - second")
    #        ElementInstead=HResSimple(self.k, newN, self, self.Conn_Suc0Par1, self.Elements, vsh)
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
    #            if self.outerN==QUpperSubElts:
    #                if vsh==1:
    #                    print("This is sub-element, one of "+str(QUpperSubElts)+", inited par, last, will be added")
    #                self.upper.AddInner(ElementToAdd)
    #            else:
    #                self.upper.InsInnerN(ElementToAdd, self.outerN+1)
    #                if vsh==1:
    #                    print("This is sub-element, one of "+str(QUpperSubElts)+", inited par, last, not last, will be ins'd")
    #                self.upper.AddInner(ElementToAdd)
    # 
    #        else:#self.upper.Conn_Suc0Par1==0
    #            if vsh==1:
    #                print("This is sub-element, one of "+str(QUpperSubElts)+", inited suc")
    #            self.Conn_Suc0Par1=1
    #            #
    #            ElementInstead=HResSimple(self.k, newN, self, self.Conn_Suc0Par1, self.Elements, vsh)
    #            if vsh==1:
    #                print("Adding copy of this R: "+ElementInstead.__str__())
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
        newN=self.FirsrAbsentN()#;#ne sees tic exnot char!
        ElementToAdd=copy.deepcopy(ElementExt)
        if vsh==1:
            print("Adding to: "+self.__str__())
            print("Adding what: "+ElementToAdd.__str__())
            print("new N = "+str(newN))
        ##def __init__(self, k=0, curN=0, Conn_Suc0Par1=0, upper=0, Ress=[], outerN=0, vsh=0):
        if self.upper==0 or ( isinstance(self.upper, HResSimple) and self.upper.Conn_Suc0Par1==0):
            if vsh==1:
                if self.upper==0:
                    print("No upper Rs. This will be first added, param - second")
                if isinstance(self.upper, HResSimple) and self.upper.Conn_Suc0Par1==0:
                     print("Trying conn || to -- con'd R")
                print("R, to which we try to conn, will be container of self's copy and connected R")
            ##def __init__(self, k=0, curN=0, Conn_Suc0Par1=0, upper=0, Ress=[], outerN=0, vsh=0):
            ElementInstead=HResSimple(self.k, newN, self.Conn_Suc0Par1, self, self.Elements, vsh)
            if vsh==1:
                print("Copy: "+ElementInstead.__str__())
            #
            self.k=k_new
            self.Conn_Suc0Par1=1
            if vsh==1:
                print("Self ef adding: "+self.__str__())
                print("Adding copy:")
            self.AddInner(ElementInstead)
            if vsh==1:
                print("Self ef adding copy:")
                self.Show_WithSubElts()
                print("Adding R to Add:")
            self.AddInner(ElementToAdd)
            if vsh==1:
                print("Finally: ")
                self.Show_WithSubElts()
        else:
            QUpperSubElts=self.upper.QSubElts()
            if self.outerN==QUpperSubElts:
                if vsh==1:
                    print("This is sub-element, one ("+str(self.outerN)+") of "+str(QUpperSubElts)+", inited par, last, will be added")
                self.upper.AddInner(ElementToAdd)
            else:
                if vsh==1:
                    print("This is sub-element, one ("+str(self.outerN)+") of "+str(QUpperSubElts)+", inited par,  not last, will be ins'd")
                self.upper.InsInnerN(ElementToAdd, self.outerN+1)
            if vsh==1:
                print("Finally: ")
                self.Show_WithSubElts()
        if vsh==1:
            print("AddParSmart finishes working")            
                
                
            

    def vis_L(self, vsh=0):
        L=1
        if(vsh==1):
            print("vis_L starts working "+self.__str__())
        if self.upper==0:
            L=L+1
            if(vsh==1):
                print("Ext: now L=2="+str(L)+" (left: connector and wall or itself)")
        if isinstance(self.Elements,list) and len(self.Elements)>0:
            Q=len(self.Elements)
            if self.Conn_Suc0Par1==0:
                for i in range(1, Q-1+1):
                    Lcur=self.Elements[i-1].vis_L(vsh)#i
                    if(vsh==1):
                         print("returning to prev") 
                    L=L+Lcur
                    L=L+1
                    if(vsh==1):
                        print(str(i)+") Now L=L(R"+str(self.Elements[i-1].curN)+")="+str(Lcur)+"+1 connector So L="+str(L))
                Lcur=self.Elements[Q-1].vis_L(vsh)#q
                L=L+Lcur
                if(vsh==1):
                    print(str(Q)+") Now L=L(R"+str(self.Elements[Q-1].curN)+")="+str(Lcur)+" So L="+str(L))
            else:
                Lmax=0
                for i in range(1, Q+1):
                    Lcur=self.Elements[i-1].vis_L(vsh)
                    if i==1 or (i>1 and Lcur<Lmax):
                        Lmax=Lcur
                L=L+Lmax+2
                if(vsh==1):
                    print("L=Lmax+2 connectors="+str(L)+"+"+str(Lmax)+"+2="+str(L))
            L=L+1
            if(vsh==1):
                print("L=L+1 right wall="+str(L))
        else:
            if(vsh==1):
                print("Nil to add. L="+str(L))
        if self.upper==0:
            L=L+1
            if(vsh==1):
                print("Ext: now L=L+1="+str(L)+" (right connector)")
        if(vsh==1):
            print("vis_L finishes working "+self.__str__()+" L="+str(L))
        return L

    def vis_yUpper(self, vsh=0):
        yUpper=0
        if(vsh==1):
            print("vis_yUpper starts working. "+self.__str__()+" yUpper="+str(yUpper))
        if isinstance(self.Elements, list) and len(self.Elements)>0:
            yUpper=yUpper+1
            if(vsh==1):
                print("complex: 1 upper wall. yUpper="+str(yUpper))
            Q=len(self.Elements)
            if self.Conn_Suc0Par1==0:
                if(vsh==1):
                    print("[--] finding max")
                yUpperMax=0
                for i in range(1, Q+1):
                    yUpperCur=self.Elements[i-1].vis_yUpper(vsh)
                    if i==1 or (i>1 and yUpperMax<yUpperCur):
                        yUpperMax=yUpperCur
                    if(vsh==1):
                        print("-element"+str(i)+" R"+str(self.Elements[i-1].curN)+": yUpperCur="+str(yUpperCur)+" yUpperMax="+str(yUpperMax))
                yUpper=yUpper+yUpperMax
                if(vsh==1):
                    print("yUpper = yUpper+ yUpperMax: ="+str(yUpper)+" (yUpperMax = "+str(yUpper)+")")
            else:
                if(vsh==1):
                    print("[||] yUpper = first")
                yUpperCur=self.Elements[1-1].vis_yUpper(vsh)
                yUpper=yUpper+yUpperCur
                if(vsh==1):
                    print("Return to prev. yUpper=yUpperCur+1="+str(yUpperCur))
            #yUpper=yUpper+1
            #if(vsh==1):
            #    print("complex: 1 lower wall. yUpper="+str(yUpper))
        else:
            if(vsh==1):
                print("simple - nil to add")
        if(vsh==1):
            print("vis_yUpper finishes working. "+self.__str__()+" yUpper="+str(yUpper))
        return yUpper

    def vis_yLower(self, vsh=0):
        yLower=0
        if(vsh==1):
            print("vis_yLower starts working. "+self.__str__()+" yLower="+str(yLower))
        if isinstance(self.Elements, list) and len(self.Elements)>0:
            yLower=yLower+1
            if(vsh==1):
                print("complex: 1 upper wall. yUpper="+str(yLower))
            Q=len(self.Elements)
            if self.Conn_Suc0Par1==0:
                if(vsh==1):
                    print("[--] finding max")
                yLowerMax=0
                for i in range(1, Q+1):
                    yLowerCur=self.Elements[i-1].vis_yLower(vsh)
                    if i==1 or (i>1 and yLowerMax<yLowerCur):
                        yLowerMax=yLowerCur
                    if(vsh==1):
                        print("-element"+str(i)+" R"+str(self.Elements[i-1].curN)+": yUpperCur="+str(yLowerCur)+" yUpperMax="+str(yLowerMax))
                yLower=yLower+yLowerMax
                if(vsh==1):
                    print("yLower = yLower+ yLowerMax: ="+str(yLower)+" (yLowerMax = "+str(yLower)+")")
            else:
                yLowerCur=yLower+self.Elements[1-1].vis_yLower(vsh)
                yLower=yLower+yLowerCur
                if(vsh==1):
                    print("yLower = yLower+ yLowerCur[1]: ="+str(yLower)+" (yLowerCur[1] = "+str(yLowerCur)+")")
                for i in  range(2, Q-1+1):
                    yUpperCur=self.Elements[i-1].vis_yLower(vsh)
                    yLowerCur=self.Elements[i-1].vis_yLower(vsh)
                    yLower=yLower+yUpperCur+yLowerCur+1
                    if(vsh==1):
                        print("yLower = yLower+ yUpperCur+ yLowerCur: ="+str(yLower)+" (yUpperCur = "+str(yUpperCur)+" yLowerCur = "+str(yLowerCur)+")")
                yUpperCur=self.Elements[Q-1].vis_yLower(vsh)
                yLowerCur=self.Elements[Q-1].vis_yLower(vsh)
                yLower=yLower+yUpperCur+yLowerCur+1
                if(vsh==1):
                    print("Return to prev. yLower="+str(yLower))
            #yUpper=yUpper+1
            #if(vsh==1):
            #    print("complex: 1 lower wall. yUpper="+str(yUpper))
        else:
            if(vsh==1):
                print("simple - nil to add")
        if(vsh==1):
            print("vis_yLower finishes working. "+self.__str__()+" yLower="+str(yLower))
        return yLower

    def vis_x(self, vsh=0):
        if(vsh==1):
            print("vis_x starts working. "+self.__str__())
        x=2
        if self.upper==0:
            #
            if(vsh==1):
                print("Ext.: nil to add. x="+str(x))
        elif isinstance(self.upper, int):
            print("Error upper of: "+self.__str__())
        elif isinstance(self.upper, HResSimple):
            xUpper=self.upper.vis_x(vsh)
            x=xUpper
            if(vsh==1):
                print("Part of: "+self.upper.__str__()+" xUpper="+str(xUpper)+" = x ="+str(x))
            if(self.upper.Conn_Suc0Par1==0):
                x=x+1
                if(vsh==1):
                    print("[--] x=x+1: left wall x ="+str(x))
                LCur=0
                if self.outerN>1:
                    for i in range(1, self.outerN-1+1):
                        LCur=self.upper.Elements[i-1].vis_L(vsh)
                        x=x+LCur
                        x=x+1
                        if(vsh==1):
                            print("Elt"+str(i)+" R"+str(self.upper.Elements[i-1].curN)+" +1 connector="+str(LCur)+" cur x="+str(x))
                if(vsh==1):
                    print("x= "+str(x))
            else:
                x=xUpper+2
                if(vsh==1):
                    print(" || part of "+self.upper.__str__()+"x=xUpper+2 (wall and connector)="+str(x)+" (xUpper="+str(xUpper)+")")
        #else:
        #    print(self.__str__()+" upper error: upper="+str(self.upper))
        if(vsh==1):
            print("vis_x finishes working. "+self.__str__()+" x="+str(x))
        return x
        #if isinstance(self.Elements and len(self.Elements)>0):

    def vis_y(self, vsh=0):
        y=0#vikt!: S'formality, not'd, ob aso S ecri y s'ref'd ef assign
        if(vsh==1):
            print("vis_y starts working. "+self.__str__())
        if self.upper==0:
            yMyUpper=self.vis_yUpper(vsh)
            y=yMyUpper
            if(vsh==1):
                if self.upper==0:
                    print("Ext. y=yUpper="+str(yMyUpper)+"="+str(y))
                #elif self.upper.Conn_Suc0Par1==0:
                #    print("united [--]. y=yUpper="+str(yMyUpper)+"="+str(y))
        elif isinstance(self.upper, HResSimple):
            yUpper=self.upper.vis_y(vsh)
            if self.upper.Conn_Suc0Par1==1:
                if self.outerN>=1:
                    y=yUpper
                    if(vsh==1):
                        print("Ce part of "+self.upper.__str__()+" ["+str(self.outerN)+"]>=1 => y=y(upper)="+str(yUpper)+"="+str(y))
                if self.outerN>=2:
                    yLower1=self.upper.Elements[1-1].vis_yLower(vsh)
                    y=y+yLower1+1
                    if(vsh==1):
                        print("Ce part of "+self.upper.__str__()+" ["+str(self.outerN)+"]>=2 y=y(upper)+yLower[1]+1= "+str(y)+" (y(upper)="+str(yUpper)+" yLower[1]="+str(yLower1)+")")
                if self.outerN>2:
                    for i in range (3, self.outerN-1+1):
                        yUpperCur=self.upper.Elements[i-1].vis_yUpper(vsh)
                        yLowerCur=self.upper.Elements[i-1].vis_yLower(vsh)
                        y=y+yUpperCur+yLowerCur+1
                        if(vsh==1):
                            print(str(i)+")  y=y+yUpperCur[i]+yLower[i]+1= "+str(y)+" (yUpperCur[i]="+str(yUpperCur)+" yLowerCur[i]"+str(yUpperCur)+")")
                    yMyUpper=self.vis_yUpper(vsh)
                    y=y+yMyUpper
                    if(vsh==1):
                        print(" y=y+yMyUpper = "+str(y)+" (yMyUpper="+str(yMyUpper)+")")
                if self.outerN>1:
                    y=y+1
                if(vsh==1):
                    print("finally: y="+str(y))
            else:
                y=yUpper
                if vsh==1:
                    print("united [--]. y=y(upper)="+str(yUpper)+"="+str(y))
        if(vsh==1):
            print("vis_y finishes working. "+self.__str__()+" y="+str(y))
        return y

    def vis_connectorLeft_x(self, vsh=0):
        x=-1
        xSelf=self.vis_x(vsh) 
        if self.upper==0:
            x=xSelf-1
        elif isinstance(self.upper, HResSimple) and self.upper.Conn_Suc0Par1==1:
            x=xSelf-1
        elif isinstance(self.upper, HResSimple) and self.upper.Conn_Suc0Par1==0:
            if self.outerN>1:
                x=xSelf-1
            else:
                pass
        return x
            

    def vis_connectorLeft_y(self, vsh=0):
        return self.vis_y(vsh)

    def vis_connectorRight_x(self, vsh=0):
        xSelf=self.vis_x(vsh)
        L=self.vis_L(vsh)
        x=xSelf+L
        return x

    def vis_connectorRight_y(self, vsh=0):
        return self.vis_y(vsh)

    def vis_caption_x(self, vsh=0):
        x=-1
        xSelf=self.vis_x(vsh)
        if isinstance(self.Elements, list) and len(self.Elements)>0:
            x=xSelf+1
        else:
            x=xSelf
        return x

    def vis_caption_y(self, vsh=0):
        y=-1
        ySelf=self.vis_y(vsh)
        if isinstance(self.Elements, list) and len(self.Elements)>0:
            y=ySelf-1
        else:
            y=ySelf
        return y

    def vis_cornersLeft_x(self, vsh=0):
        return self.vis_x()

    def vis_cornersRight_x(self, vsh=0):
        xSelf=self.vis_x()
        L=self.vis_L()
        return xSelf+L-1

    def vis_cornersUpper_y(self, vsh=0):
        y=-1
        ySelf=self.vis_y(vsh)
        yUpper=self.vis_yUpper(vsh)
        if isinstance(self.Elements, list) and len(self.Elements)>0:
            y=ySelf-yUpper
        else:
            y=ySelf
        return y
 
    def vis_cornersLower_y(self, vsh=0):
        y=-1
        ySelf=self.vis_y(vsh)
        yLower=self.vis_yLower(vsh)
        if isinstance(self.Elements, list) and len(self.Elements)>0:
            y=ySelf+yLower
        else:
            y=ySelf
        return y

    def __str__(self):
        s="R"+str(self.curN)+" k="+str(self.k)+" Sub-Elts: "
        s=s+" (self.Conn_Suc0Par1="+str(self.Conn_Suc0Par1)+") "
        if self.Conn_Suc0Par1==0:
            s=s+" [--] "
        else:
            s=s+" [||] "  
        if isinstance (self.Elements, list):
            s=s+str(len(self.Elements))
        else:
            s=s+"0"
        if self.upper==0:
            s=s+" (Ext.) "
        elif isinstance(self.upper, int):
            s=s+" Upper: "+str(self.upper)+" ["+str(self.outerN)+"]"
        else:#vikt! ce faiz! ac ce ne works, ecri: int ne ha field curN
            s=s+" Of: R"+str(self.upper.curN)+" ["+str(self.outerN)+"]"
        x=self.vis_x()
        y=self.vis_y()
        s=s+" Coords:("+str(x)+", "+str(y)+");"
        x=self.vis_cornersLeft_x()
        y=self.vis_cornersUpper_y()
        s=s+" crnrLU("+str(x)+", "+str(y)+"); "
        x=self.vis_cornersLeft_x()
        y=self.vis_cornersLower_y()
        s=s+" crnrLL("+str(x)+", "+str(y)+"); "
        x=self.vis_cornersRight_x()
        y=self.vis_cornersUpper_y()
        s=s+" crnrRU("+str(x)+", "+str(y)+"); "
        x=self.vis_cornersRight_x()
        y=self.vis_cornersLower_y()
        s=s+" crnrRL("+str(x)+", "+str(y)+"); "
        x=self.vis_connectorLeft_x()
        y=self.vis_connectorLeft_y()
        s=s+" cnctL("+str(x)+", "+str(y)+"); "
        x=self.vis_connectorRight_x()
        y=self.vis_connectorRight_y()
        s=s+" cnctRL("+str(x)+", "+str(y)+"); "
        x=self.vis_caption_x()
        y=self.vis_caption_y()
        s=s+" cpt("+str(x)+", "+str(y)+") "
        return s

    def Show_WithSubElts(self):
        print(self.__str__())#vikt! faiz! S work ac (), ma writes method name
        Q=self.QSubElts()
        for i in range(1, Q+1):
            self.Elements[i-1].Show_WithSubElts()
            


QVals=4
QNumerats=4

DenRes=10

class RecStr:
    def __init__(self, QVals=0, QNumerats=0):
        self.QVals=0
        self.QNumerats=0
        self.Denomin=0
        self.p=[]
        self.lst=[]
        self.N=0
        self.countAll=0
        self.countGut=0
        if(QVals>0 and QNumerats>0):
            self.Set(QVals, QNumerats)
            self.N=1
        #print("RecStr created: QVals="+str(QVals)+"="+str(self.QVals)+" QNumerats="+str(QNumerats)+"="+str(self.QNumerats))
            
    def Set(self, QVals, QNumerats):
        self.QVals=QVals
        self.QNumerats=QNumerats
        self.Denomin=self.QVals*self.QVals*self.QNumerats
        #self.MaxNumerat=self.QVals*self.QNumerats
        self.N=1
        for i in range (1, self.QVals+1):
            #self.p[i-1]=i
            self.p.append(0)

    #def SetN(self, N):
    #    self.N=N

    def __str__(self):#works gut. Ma full idem fn o'alt class ne works in Py2
        #st=" QVals="+str(self.QVals)+" QNumerats="+str(self.QVals)+"; Denomin="+str(self.Denomin)+" Sum="+str(self.Sum)+" N="+str(self.N)+" size(p)="+str(len(self.p))
        st=" QVals="+str(self.QVals)+" QNumerats="+str(self.QVals)+" N="+str(self.N)+" size(p)="+str(len(self.p))
        return st



def RecSearch(dataExt, Show1Hide0=0):
    data=copy.deepcopy(dataExt)
    st=""
    Sum=0
    data.countAll=data.countAll+1
    countAll=data.countAll
    N=data.N
    if Show1Hide0==1:
        print("RecSearch Starts working. countAll=",countAll, " N=",data.N)
    for i in range(1, data.QNumerats+1):
        data.p[N-1]=i#vikt! so ob af recurs data.N wi alt, so nur ine N!
        st="countAll="+str(countAll)+" N="+str(N)+" i="+str(i)+" p["+str(N)+"]="+str(data.p[N-1])+" : " 
        if Show1Hide0==1 and N<data.QVals:
            print(st)
        #if data.N==data.QVals:#NLim
        if N==data.QVals:#vikt! so ob af recurs data.N wi alt, so nur ine N!
            Sum=0
            for j in range(1, data.QVals+1):
                Sum=Sum+data.p[j-1]
                st=st+str(data.p[j-1])
                if(j<data.QVals):
                    st=st+" + "
                #Elt=[]
                
            st=st+" = "+str(Sum)+" "
            if Show1Hide0==1:
                print(st)
            if Sum==DenRes:#get out rec
                data.countGut=data.countGut+1
                #Elt.append(
                pc=copy.deepcopy(data.p)
                data.lst.append(pc)
                if Show1Hide0==1:
                    print("Required Sum! ="+str(Sum)+" = "+str(DenRes))
            #if countAll<data.QVals*data.QNumerats:# no nod
            data.N=1
        else:
            if Show1Hide0==1:
                print("So, N="+str(N)+" data.N="+str(data.N))
            data.N=N+1 #vikt! so ob af recurs data.N wi alt, so nur ine N!
            if Show1Hide0==1:
                print("And now N="+str(N)+" data.N="+str(data.N))
            data=RecSearch(data, Show1Hide0)
            if Show1Hide0==1:
                print("Return to prev. CountAll="+str(countAll)+" N="+str(N))
    if Show1Hide0==1:
        print("RecSearch Finishes working. countAll=",countAll, " N=",data.N)  
    return data

def CalcEqualBounds(a, b, QSects):
    Y=[]
    dx=(b-a)/QSects
    for i in range(1, QSects+1):
        c=(i-1)*dx
        Y.append(c)
    return Y

class PositionInSuccession:
    def __init__(self, IsLess=0, IsGreater=0, EqualN=0, LessN=0):
        #self.LessN=LessN#.LessN=0
        #self.EqualN=EqualN#self.EqualN=0
        #self.IsLess=IsLess#self.IsLess=0
        #self.IsGreater=IsGreater#self.IsGreater=0
        self.SetIni()

    def SetIni(self):
        self.LessN=0
        self.EqualN=0
        self.IsLess=0
        self.IsGreater=0

    def __str__(self):#ne works in Py2. Ma full idem fn o'alt class  works in Py2 gut
        st=" IsLess="+str(self.IsLess)+" IsGreater="+str(self.IsGreater)+" EqualN="+str(self.EqualN)+" LessN="+str(self.LessN)
        print("Info:  "+st)
        return st########
   #def __str__(self):

    #def Show(self):
    #    st=" IsLess="+str(self.IsLess)+" IsGreater="+str(self.IsGreater)+" EqualN="+str(self.EqualN)+" LessN="+str(self.LessN)
    #    print("Info:  "+st)
        


def DefPositionInSuccession(x, Xe, ValsShow1Hide0=0):
    pos=PositionInSuccession()
    X=copy.deepcopy(Xe)
    if ValsShow1Hide0==1:
        print("DefPositionInSuccession starts working. Before work:")
        print("pos: ", pos)
        print("pos: ", pos.__str__())
        print("X: ", X)
        if isinstance(X, list):
            print("X is List, Length="+str(len(X)))
        else:
            print("X: ", X)
            print("X is NOT List")
    if(isinstance(X, list) and len(X)>0):
        Q=len(X)
        if ValsShow1Hide0==1:
            print("Q=", Q)
        if x<X[1-1]:
            pos.IsLess=1
            if ValsShow1Hide0==1:
                print("x IsLess: "+str(x)+"<"+str(X[1-1]))
        elif x>X[Q-1]:
            pos.IsGreater=1
            if ValsShow1Hide0==1:
                print("x is IsGreater: "+str(x)+">"+str(X[Q-1]))
        else:
            for i in range(1, Q+1):
                if x==X[i-1]:
                    pos.EqualN=i
                    if ValsShow1Hide0==1:
                        print("x="+str(x)+"=X["+str(i)+"]="+str(X[i-1]))
            #if pos.EqualN>0:
            #    Y=X
            #else:
            if pos.EqualN==0:
                for i in range(1, Q-1+1):
                    if x>X[i-1] and x<X[i+1-1]:
                        pos.LessN=i
                        if ValsShow1Hide0==1:
                            print("X["+str(i)+"]="+str(X[i-1])+"<x="+str(x)+"<X["+str(i+1)+"]="+str(X[i+1-1]))
        if pos.EqualN==0 and pos.LessN==0 and pos.IsLess==0 and pos.IsGreater==0 and ValsShow1Hide0==1:
            print("unknown vrn")
    else:
        if ValsShow1Hide0==1:
            print("X is not a list or is an empty list")
    if ValsShow1Hide0==1:
        print("So Pos: ", pos.__str__())
        print("DefPositionInSuccession finishes working")
    return pos
            
def Sort(Xe, SortDir_Asc0Desc1=0):
    X=copy.deepcopy(Xe)
    Q=len(X)
    if SortDir_Asc0Desc1==0:
        for i in range (1, Q+1):
            for j in range (i, Q+1):
                if X[j-1]<X[i-1]:
                    buf=X[j-1]
                    X[j-1]=X[i-1]
                    X[i-1]=buf
    else:
        for i in range (1, Q+1):
            for j in range (i, Q+1):
                if X[j-1]>X[i-1]:
                    buf=X[j-1]
                    X[j-1]=X[i-1]
                    X[i-1]=buf
    return X        

def InsToSucc(x, Xe):
    X=copy.deepcopy(Xe)
    Y=[]
    Q=len(X)
    pos=DefPositionInSuccession(x, X)
    #print("pos: ",x," ",pos)
    if(pos.IsLess==1):
        Y.append(x)
        for i in range(1, Q+1):
            Y.append(X[i-1])
    elif(pos.IsGreater==1):
        for i in range(1, Q+1):
            Y.append(X[i-1])
        Y.append(x)
    elif pos.LessN>0:
        for i in range(1, pos.LessN+1):
            Y.append(X[i-1])
        Y.append(x)
        for i in range(pos.LessN+1, Q+1):
            Y.append(X[i-1])
    else:#EqualN>0
        #Y=X
        Y=copy.deepcopy(X)
    return Y
    



        
