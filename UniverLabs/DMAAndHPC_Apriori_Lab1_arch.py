from MyLibs3 import *
import copy

transactionsList=[["bread", "milk", "cookie"],
                  ["milk", "sour cream"],
                  ["milk", "bread", "sour cream", "cookie"],
                  ["sausage", "sour cream"],
                  ["bread", "milk", "cookie", "sour cream"],
                  ["sweets"]]

def FormListOfUniqueItems(transactionsList):
    AllItemsList=[]
    for transaction in transactionsList:
        for item in transaction:
            if AllItemsList==[] or  PosInListFirst(AllItemsList, item)==0:
                AllItemsList.append(item)
    return AllItemsList
#
def fSupport(transactionsList, comb, vsh=0):
    QTransactions=len(transactionsList)
    if vsh==1:
        print("fSuppl starts working. Transactions: "+str(QTransactions)+" Comb: "+str(comb))
    countOccurances=0
    for i in range(1, QTransactions+1):
        transaction=transactionsList[i-1]
        if ArePrsentAllInAnySucc(transaction, comb)==1:
            countOccurances+=1
            if vsh==1:
                print("Comb "+str(comb)+" is  present in "+str(i)+" transaction "+str(transaction)+" - this is "+str(countOccurances)+"th case")
        else:
            if vsh==1:
                print("Comb "+str(comb)+" is not present in "+str(i)+" transaction "+str(transaction))
    sup=1.0*countOccurances/QTransactions*100
    if vsh==1:
        print("fSuppl finishes working with answer: "+str(sup))
    return sup
#
class Candidate:
    def __init__(self, ItemsList=[], memberN=0):
        self.LinkNsIncoming=[]
        self.LinkNsOutcoming=[]
        self.LinksIncoming=[]
        self.LinksOutcoming=[]
        self.ItemsList=ItemsList
        self.support=0
#
class GraphOfCands:
    def __init__(self, transactionsList, vsh=0):
        self.CandsOfLevel=self.FormAllCandsAndBuildQuasiTree(transactionsList, vsh)

    def FormAllCandsAndBuildQuasiTree(self, transactionsList, vsh=0):
        AllItemsList=FormListOfUniqueItems(transactionsList)
        if vsh==1:
            print('All:')
            print(AllItemsList)
            print('Candidates:')
        allL=len(AllItemsList)
        CandsOfLevel=[]
        EmptyList=[]
        CandsOfLevel.append(EmptyList)
        CandsOfLevel[1-1]=[]
        FirstLevelList=[]
        for i in range(1, allL+1):
            SingleMemberList=[]
            SingleMemberList.append(AllItemsList[i-1])
            CurPossibleCand=Candidate(SingleMemberList)
            FirstLevelList.append(CurPossibleCand)
        CandsOfLevel[1-1]=copy.deepcopy(FirstLevelList)
        if vsh==1:
            print("Level 1: "+str(CandsOfLevel[1-1]))
        for StepN in range(2, allL-1+1):
            if vsh==1:
                print("Level : "+str(StepN))
            prevStepL=len(CandsOfLevel[StepN-1-1])
            PrevLevelList=copy.deepcopy(CandsOfLevel[StepN-1-1])
            PrevLevelContentList=[]
            for i in range(1, prevStepL+1):
                PrevLevelContentList.append(PrevLevelList[i-1].ItemsList)
            if vsh==1:
                print("Prev level content: "+str(PrevLevelContentList))
                print("Level  "+str(StepN))
            #CurLevelList=[]
            CurLevelListContent=[]
            CurLevelListN=0
            EmptyList=[]#
            CandsOfLevel.append(EmptyList)#
            for NInPrevList in range (1, prevStepL+1):
                curToAddWhere=copy.deepcopy(PrevLevelList[NInPrevList-1].ItemsList)
                for N in range(1, allL+1):
                    curToAddWhat=FirstLevelList[N-1].ItemsList
                    CurPossibleCandContent=ConcatLists(curToAddWhere, curToAddWhat)
                    if vsh==1:
                        print("CurPossibleCandContent["+str(NInPrevList)+", "+str(N)+"]="+str(CurPossibleCandContent)+"("+str(curToAddWhere)+" + "+str(curToAddWhat)+")")
                    if ArePrsentAllInAnySucc(curToAddWhere, curToAddWhat)==1:
                        if vsh==1:
                            print('No: '+str(curToAddWhat)+' is present in '+str(curToAddWhere))
                    elif CurLevelListContent!=[] and ListIsPresentInListAsMember_AndSuccDoesNotMatter(CurLevelListContent, CurPossibleCandContent)==1:
                        if vsh==1:
                            print('No: '+str(CurPossibleCandContent)+' is present in '+str(CurLevelList))
                    else:
                        CurLevelListN+=1
                        #
                        CurLevelListContent.append(CurPossibleCandContent)
                        #
                        CurPossibleCand=Candidate(CurPossibleCandContent)
                        #
                        if vsh==1:
                            print("Candidate: Level: "+str(StepN)+" N "+str(CurLevelListN)+" Content: "+str(CurPossibleCandContent))
                            print("Checking connections with prev (Level "+str(StepN-1)+"): ")
                        for prvN in range(1, prevStepL+1):
                            prvCurItemContentList=PrevLevelList[prvN-1].ItemsList
                            if vsh==1:
                                print("Candidate: Level: "+str(StepN-1)+" N "+str(prvN)+" Content: "+str(prvCurItemContentList))
                            if ArePrsentAllInAnySucc(CurPossibleCandContent, prvCurItemContentList)==1:
                                CurPossibleCand.LinkNsIncoming.append(prvN)
                                CurPossibleCand.LinksIncoming.append(CandsOfLevel[StepN-1-1][prvN-1])
                                CandsOfLevel[StepN-1-1][prvN-1].LinkNsOutcoming.append(CurLevelListN)
                                if vsh==1:
                                    print("Connected!")
                            else:
                                if vsh==1:
                                    print("Not connected")
                        #
                        CandsOfLevel[StepN-1].append(CurPossibleCand)
                        #
                        for inN in CurPossibleCand.LinkNsIncoming:
                            CandsOfLevel[StepN-1-1][inN-1].LinksOutcoming.append(CandsOfLevel[StepN-1][CurLevelListN-1])
                        #
                        if vsh==1:
                            print('that member will do')
            #
            for prvN in range(1, prevStepL+1):
                outList=CandsOfLevel[StepN-1-1][prvN-1].LinkNsOutcoming
                outL=len(outList)
            if vsh==1:
                print("Level "+str(StepN)+" Members: "+str(self.CandsOfLevel[StepN-1]))
        #
        if vsh==1:
            print("Candidates of automatical Levels are formed")
        if vsh==1:
            print("Forming last level and connections")
        StepN+=1
        PrevLevelList=copy.deepcopy(CandsOfLevel[StepN-1-1])
        CurLevelList=[]
        CurPossibleCandContent=AllItemsList
        CurPossibleCand=Candidate(CurPossibleCandContent)
        if vsh==1:
            print("Candidate: (he will win): "+str(CurPossibleCand.ItemsList))
        CurLevelListN=1
        prevStepL=len(PrevLevelList)
        if vsh==1:
            print("prevStepL= "+str(prevStepL))
        for prvN in range(1, prevStepL+1):
            prvCurItemContentList=PrevLevelList[prvN-1].ItemsList
            if vsh==1:
                print("Candidate: Level: "+str(StepN-1)+" N "+str(prvN)+" Content: "+str(prvCurItemContentList))
            if ArePrsentAllInAnySucc(CurPossibleCandContent, prvCurItemContentList)==1:
                CurPossibleCand.LinkNsIncoming.append(prvN)
                CandsOfLevel[StepN-1-1][prvN-1].LinkNsOutcoming.append(CurLevelListN)
                if vsh==1:
                    print("Connected!")
            else:
                if vsh==1:
                    print("Not connected")
        CurLevelList.append(CurPossibleCand)#ce ne help't
        CandsOfLevel.append(CurLevelList)
        if vsh==1:
            print("Candidates of all Levels are formed")
        #
        for StepN in range(1, allL+1):
            if vsh==1:
                print('Level '+str(StepN))
                print(str(CandsOfLevel[StepN-1]))
        return CandsOfLevel

    def getQlevels(self):
        return len(self.CandsOfLevel)

    def getAllChildrenGenerationsList(self, LevelN, ItemN, listExt=[], vsh=0):
        if vsh==1:
            print("getAllChildrenGenerationsList starts working")
            print("Level "+str(LevelN)+" N "+str(ItemN)+" list came: "+str(listExt))
        QLevels=len(self.CandsOfLevel)
        listIne=copy.deepcopy(listExt)
        QMembersAtLevel=len(self.CandsOfLevel[LevelN-1])
        ChildrenLevelN=LevelN+1  
        if LevelN>=1 and LevelN<QLevels and ItemN>=1 and ItemN<=QMembersAtLevel:
            QOutcomingConns=len(self.CandsOfLevel[LevelN-1][ItemN-1].LinkNsOutcoming)
            for N in range(1, QOutcomingConns+1):
                ChildrenItem=[]
                ChildrenItem.append(ChildrenLevelN)
                ChildrenItem.append(self.CandsOfLevel[LevelN-1][ItemN-1].LinkNsOutcoming[N-1])
                listIne.append(ChildrenItem)
                if vsh==1:
                    print("Child: Level "+str(ChildrenLevelN)+" N "+str(N)+" or "+str(ChildrenItem))
                    print("Starting Recursion. From: Level "+str(LevelN)+" N "+str(ItemN)+" To: Level "+str(ChildrenLevelN)+" N "+str(N))
                listIne=self.getAllChildrenGenerationsList(ChildrenLevelN, N, listIne, vsh)
                if vsh==1:
                    print("Returning from Recursion. From: Level "+str(ChildrenLevelN)+" N "+str(N)+" To: Level: "+str(LevelN)+" N "+str(ItemN))
                    print("Now List: "+str(listIne))
        if vsh==1:
            print("list before elab:")
        #listIne=CandsOfLevel.getAllChildrenGenerationsList(1, 1)
        #if vsh==1:
            print(listIne)
            print("list after del same:")
        listIne=ClearListFromNotUniqueVals(listIne)
        if vsh==1:
            print(listIne)
            print("list after sort acscending:")
        listIne_1=SortListOfPairsOfFirstThenSecondAscending(listIne)
        if vsh==1:
            print(listIne_1)
            print("list after sort descending:")
        listIne=SortListOfPairsOfFirstThenSecondDescending(listIne)
        if vsh==1:
            print(listIne)
            print("Answer: List: "+str(listIne))
            print("getAllChildrenGenerationsList finishes working")
        return listIne

    def getElementPosByContent(self, content):
        Qlevels=len(self.CandsOfLevel)
        R=[]
        for i in range (1, Qlevels+1):
            L=len(CandsOfLevel[i-1])
            for j in range (1, L+1):
                if CandsOfLevel[i-1][j-1].ItemsList==content:
                    R.append(i)
                    R.append(j)
        return R

    def DelElement(self, LevelN, memberN, vsh=0):
        if vsh==1:
            print("DelElement sterts working: LevelN="+str(LevelN)+" memberN="+str(memberN)+" Level length="+str(len(self.CandsOfLevel[LevelN-1])))
        if LevelN>=1 and LevelN<=self.getQlevels() and memberN>=1 and memberN<=len(self.CandsOfLevel[LevelN-1]):
            QWithMates=len(self.CandsOfLevel[LevelN-1])
            if LevelN>1:
                if vsh==1:
                    print("Del and change outcoming links from prev level:")
                QOther=len(self.CandsOfLevel[LevelN-1-1])
                for i in range(1, QOther+1):
                    if vsh==1:
                        print("Element "+str(i)+":")
                    #Deleting link to this element
                    ConnListL=len(self.CandsOfLevel[LevelN-1-1][i-1].LinksOutcoming)
                    for j in range(1, ConnListL+1):
                        if self.CandsOfLevel[LevelN-1-1][i-1].LinksOutcoming[j-1]==self.CandsOfLevel[LevelN-1][memberN-1]:
                            del(self.CandsOfLevel[LevelN-1-1][i-1].LinksOutcoming[j-1:j+1-1])
                    #Deleting link to N of this element
                    if vsh==1:
                        print("List of outcoming list Previously: "+str(self.CandsOfLevel[LevelN-1-1][i-1].LinkNsOutcoming))
                    ConnListL=len(self.CandsOfLevel[LevelN-1-1][i-1].LinkNsOutcoming)
                    for j in range(1, ConnListL+1):
                        linkToN=self.CandsOfLevel[LevelN-1-1][i-1].LinkNsOutcoming[j-1]
                        if linkToN==memberN:
                            del(self.CandsOfLevel[LevelN-1-1][i-1].LinkNsOutcoming[j-1:j+1-1])
                    if vsh==1:
                        print("List of outcoming list After deleting: "+str(self.CandsOfLevel[LevelN-1-1][i-1].LinkNsOutcoming))
                    #Decreasing links to N of next elements
                    ConnListL=len(self.CandsOfLevel[LevelN-1-1][i-1].LinkNsOutcoming)
                    for j in range(1, ConnListL+1):
                        if linkToN>memberN:
                            self.CandsOfLevel[LevelN-1-1][i-1].LinkNsOutcoming[j-1]-=1
                    if vsh==1:
                        print("List of outcoming list After changing: "+str(self.CandsOfLevel[LevelN-1-1][i-1].LinkNsOutcoming))
            if LevelN<self.getQlevels():
                if vsh==1:
                    print("Del and change incoming links from next level :")
                QOther=len(self.CandsOfLevel[LevelN+1-1])
                for i in range(1, QOther+1):
                    if vsh==1:
                        print("Element "+str(i)+":")
                    #Deleting link to this element
                    ConnListL=len(self.CandsOfLevel[LevelN+1-1][i-1].LinksIncoming)
                    for j in range(1, ConnListL+1):
                        if self.CandsOfLevel[LevelN+1-1][i-1].LinksIncoming[j-1]==CandsOfLevel[LevelN-1][memberN-1]:
                            del(self.CandsOfLevel[LevelN+1-1][i-1].LinksIncoming[j-1:j+1-1])
                    if vsh==1:
                        print("List of incoming list Previously: "+str(self.CandsOfLevel[LevelN-1-1][i-1].LinkNsIncoming))
                    #Deleting link to N of this element
                    if vsh==1:
                        print("Element "+str(i)+":")
                    ConnListL=len(self.CandsOfLevel[LevelN+1-1][i-1].LinkNsIncoming)
                    for j in range(1, ConnListL+1):
                        linkToN=self.CandsOfLevel[LevelN+1-1][i-1].LinkNsIntcoming[j-1]
                        if linkToN==memberN:
                            del(self.CandsOfLevel[LevelN+1-1][i-1].LinkNsIncoming[j-1:j+1-1])
                    if vsh==1:
                        print("List of incoming list After deleting: "+str(self.CandsOfLevel[LevelN-1-1][i-1].LinkNsIncoming))
                    #Decreasing links to N of next elements
                    ConnListL=len(self.CandsOfLevel[LevelN+1-1][i-1].LinkNsIncoming)
                    for j in range(1, ConnListL+1):
                        if linkToN>memberN:
                            self.CandsOfLevel[LevelN+1-1][i-1].LinkNsIncoming[j-1]-=1
                    if vsh==1:
                        print("List of incoming list After changing: "+str(self.CandsOfLevel[LevelN-1-1][i-1].LinkNsIncoming))
                #}for
            del(self.CandsOfLevel[LevelN-1][memberN-1:memberN+1-1])
        #}//if need to do
        if vsh==1:
            print("Now Level length="+str(len(self.CandsOfLevel[LevelN-1])))
            print("DelElement finishes working")

    def ElaborateFirst(self, transactionsList, minsupport, vsh=0):
        if vsh==1:
            print("ElaborateFirst starts working")
        continLevels=1
        LevelN=0
        Qlevels=self.getQlevels()
        #listToDel=[]
        while continLevels==1:
            LevelN+=1
            if LevelN==Qlevels:
                continLevels=0
            LevelL=len(self.CandsOfLevel[LevelN-1])
            if vsh==1:
                print("Level "+str(LevelN)+" items quantity: "+str(LevelL))
            for i in range(1, LevelL+1):
                content=self.CandsOfLevel[LevelL-1][i-1].ItemsList
                support=fSupport(transactionsList, content, vsh)
                if vsh==1:
                    print("Element "+str(i)+" Content: "+str(content)+" support="+str(support))
                if support<minsupport:
                    listToDel=[]
                    listToDel=self.getAllChildrenGenerationsList(LevelN, i, listToDel, vsh)
                    if vsh==1:
                        print("support="+str(support)+" < min="+str(minsupport))
                    #sort it!
                    QToDelNow=len(listToDel)
                    if vsh==1:
                        print("List of ("+str(QToDelNow)+") connected \"children\" to del:")
                        print(str(QToDelNow))
                    for itemToDelN in range (1, QToDelNow+1):
                        levelToDelN=listToDel[itemToDelN-1][1-1]
                        memberlToDelN=listToDel[itemToDelN-1][2-1]
                        levelOfDelL=len(self.CandsOfLevel[levelToDelN-1])
                        if vsh==1:
                            #print("\n")
                            print("Deleting element: Level "+str(levelToDelN)+" N "+str(memberlToDelN)+" Level length: "+str(levelOfDelL))
                        self.DelElement(levelToDelN, memberlToDelN, vsh)
                        #
                        levelOfDelL=len(self.CandsOfLevel[levelToDelN-1])
                        if vsh==1:
                            print("Level length after Deleting element: "+str(levelOfDelL))
                            #print("Now graph:")
                            #self.ShowToConsole()
                            print("\n")
                else:
                    self.CandsOfLevel[LevelN-1][i-1].support=support
            if vsh==1:
                print("Some elements were deleted. Deleting empty levels")
            if LevelN<Qlevels and (CandsOfLevel[LevelL+1-1]==[]):
                continLevels=0
                for i in range(LevelN, Qlevels+1):
                    N=Qlevels-i+1
                    del(self.CandsOfLevel[N-1:N+1-1])
                    QLevelsNew=len(self.CandsOfLevel)
                    if vsh==1:
                        print("Q Levels now="+str(QLevelsNew))
        if vsh==1:
            print("\n")
            print("Q Levels now="+str(QLevelsNew))
            print("ElaborateFirst finishes working")
            print("\n")
                        
    def ShowToConsole(self, Sup_HideoShow1=0):
        QLevels=len(self.CandsOfLevel)
        if Sup_HideoShow1==0:
            for LvlN in range(1, QLevels+1):
                LevelL=len(self.CandsOfLevel[LvlN-1])
                print("Level "+str(LvlN))
                for itmN in range(1, LevelL+1):
                    print(str(itmN)+") "+str(self.CandsOfLevel[LvlN-1][itmN-1].ItemsList)+" In: "+str(self.CandsOfLevel[LvlN-1][itmN-1].LinkNsIncoming)+" Out: "+str(self.CandsOfLevel[LvlN-1][itmN-1].LinkNsOutcoming))
                #for
            #for
        else:
            for LvlN in range(1, QLevels+1):
               LevelL=len(self.CandsOfLevel[LvlN-1])
               print("Level "+str(LvlN))
               for itmN in range(1, LevelL+1):
                   print(str(itmN)+") "+str(self.CandsOfLevel[LvlN-1][itmN-1].ItemsList)+" sup="+str(self.CandsOfLevel[LvlN-1][itmN-1].suport)+"% In: "+str(self.CandsOfLevel[LvlN-1][itmN-1].LinkNsIncoming)+" Out: "+str(self.CandsOfLevel[LvlN-1][itmN-1].LinkNsOutcoming))
               #for
           #for
        #end if
    #end of last function

vsh=0
minsupport=50
minconfidence=60
#
print("\nTransaction list:")
print(str(transactionsList))
print("\nList of unique items:")
AllItemsList=FormListOfUniqueItems(transactionsList)
print(str(AllItemsList))
graphOfCands=GraphOfCands(transactionsList, vsh)
print("\nGraph of Candidates:")
graphOfCands.ShowToConsole()    
#
print("\nFirst Graph elaboration: Deleting nodes and calc supports\n")
vsh=1
graphOfCands.ElaborateFirst(transactionsList, minsupport, vsh)
print("Graph became smaller after deleting elements:")
graphOfCands.ShowToConsole(1)
#
print("\n\nRecursive Connected with [1, 1] at Sub-levels:")
items=graphOfCands.getAllChildrenGenerationsList(1, 1)
print(items)
print("that list sorted ascending:")
items_1=SortListOfPairsOfFirstThenSecondAscending(items)
print(items_1)
print("list after sort descending:")

        


                    
         
           
        

    
