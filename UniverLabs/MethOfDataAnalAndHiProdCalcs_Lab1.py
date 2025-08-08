from MyLibs3 import *
import copy

#class TreeNode:
#    def __init__(self, left=0, right=0, root=0):
#        self.left=left
#        self.right=right
#
#    def GoToLeft(self):
#        return self.left
#
#    def GoToRight(self):
#        return self.right
#
#    def GoToRoot(self):
#        return self.root
#

class Candidate:
    def __init__(self, ItemsList=[], memberN=0):
        self.LinkNsIncoming=[]
        self.LinkNsOutcoming=[]
        self.LinksIncoming=[]
        self.LinksOutcoming=[]
        self.ItemsList=ItemsList
        #self.SupportIncoming=0
        #self.SupportCurrent=0
        #self.WorthElaborating=1
        #self.Charact=0
       # self.memberN=memberN
        

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

def FormAllCands(transactionsList, vsh=0):
    AllItemsList=[]
    for transaction in transactionsList:
        for item in transaction:
            if AllItemsList==[] or  PosInListFirst(AllItemsList, item)==0:
                AllItemsList.append(item)
    #AllItemsList=FormListOfUniqueItems(transactionsList)
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
        FirstLevelList.append(SingleMemberList)
    CandsOfLevel[1-1]=copy.deepcopy(FirstLevelList)
    if vsh==1:
        print("Level 1: "+str(CandsOfLevel[1-1]))
    for StepN in range(2, allL-1+1):
        #CandsOfLevel.append(EmptyList)#=>CandsOfLevel[StepN-1]=[]
        prevStepL=len(CandsOfLevel[StepN-1-1])
        PrevLevelList=copy.deepcopy(CandsOfLevel[StepN-1-1])
        if vsh==1:
            print("Level  "+str(StepN))
        CurLevelList=[]
        for NInPrevList in range (1, prevStepL+1):
            curToAddWhere=copy.deepcopy(PrevLevelList[NInPrevList-1])
            for N in range(1, allL+1):
                curToAddWhat=FirstLevelList[N-1]
                Content=ConcatLists(curToAddWhere, curToAddWhat)
                if vsh==1:
                    print("Content["+str(NInPrevList)+", "+str(N)+"]="+str(Content)+"("+str(curToAddWhere)+" + "+str(curToAddWhat)+")")
                if ArePrsentAllInAnySucc(curToAddWhere, curToAddWhat)==1:
                    if vsh==1:
                        print('No: '+str(curToAddWhat)+' is present in '+str(curToAddWhere))
                elif CurLevelList!=[] and ListIsPresentInListAsMember_AndSuccDoesNotMatter(CurLevelList, CurPossibleCandContent)==1:
                    if vsh==1:
                        print('No: '+str(CurPossibleCandContent)+' is present in '+str(CurLevelList))
                else:
                    CurLevelList.append(CurPossibleCandContent)
                    if vsh==1:
                        print('that member will do')
        CandsOfLevel.append(CurLevelList)
        if vsh==1:
            print("Level "+str(StepN)+" Members: "+str(CandsOfLevel[StepN-1]))
    if vsh==1:
        print("Candidates of all Levels are formed")
    for StepN in range(1, allL-1+1):
        if vsh==1:
            print('Level '+str(StepN))
            print(str(CandsOfLevel[StepN-1]))
    return CandsOfLevel

def FormAllCandsAndBuildQuasiTree(transactionsList, vsh=0):
    AllItemsList=FormListOfUniqueItems(transactionsList)
    if vsh==1:
        print('All:')
        print(AllItemsList)
        print('Candidates:')
    allL=len(AllItemsList)
    CandsOfLevel=[]
    EmptyList=[]
    #ConnsInOfLevel=[]
    #ConnsOutOfLevel=[]
    CandsOfLevel.append(EmptyList)
    CandsOfLevel[1-1]=[]
    FirstLevelList=[]
    for i in range(1, allL+1):
        SingleMemberList=[]
        SingleMemberList.append(AllItemsList[i-1])
        CurPossibleCand=Candidate(SingleMemberList)
        #FirstLevelContentList.append(SingleMemberList)#alr not needed
        FirstLevelList.append(CurPossibleCand)
    CandsOfLevel[1-1]=copy.deepcopy(FirstLevelList)
    if vsh==1:
        print("Level 1: "+str(CandsOfLevel[1-1]))
    for StepN in range(2, allL-1+1):
        #CandsOfLevel.append(EmptyList)#=>CandsOfLevel[StepN-1]=[]
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
        CurLevelList=[]
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
                    #CurPossibleCand.LinkNsIncoming.append(NInPrevList)
                    #CurPossibleCand.LinkNsIncoming.append(N)
                    #
                    if vsh==1:
                        print("Candidate: Level: "+str(StepN)+" N "+str(CurLevelListN)+" Content: "+str(CurPossibleCandContent))
                        print("Checking connections with prev (Level "+str(StepN-1)+"): ")
                    for prvN in range(1, prevStepL+1):
                        prvCurItemContentList=PrevLevelList[prvN-1].ItemsList
                        if vsh==1:
                            print("Candidate: Level: "+str(StepN-1)+" N "+str(prvN)+" Content: "+str(prvCurItemContentList))
                        if ArePrsentAllInAnySucc(CurPossibleCandContent, prvCurItemContentList)==1:
                            #CurPossibleCand.memberN=CurLevelListN
                            CurPossibleCand.LinkNsIncoming.append(prvN)
                            CurPossibleCand.LinksIncoming.append(CandsOfLevel[StepN-1-1][prvN-1])
                            #PrevLevelList[prvN-1].LinkNsOutcoming.append(CurLevelListN)
                            CandsOfLevel[StepN-1-1][prvN-1].LinkNsOutcoming.append(CurLevelListN)
                            #CandsOfLevel[StepN-1-1][prvN-1].LinksOutcoming.append(CandsOfLevel[StepN-1][CurLevelListN-1])
                            if vsh==1:
                                print("Connected!")
                        else:
                            if vsh==1:
                                print("Not connected")
                    #
                    #PrevLevelList[NInPrevList-1].LinkNsOutcoming.append(CurLevelListN)
                    #
                    #CurLevelList.append(CurPossibleCand)#so sabl, ce work. Nu altf
                    #
                    CandsOfLevel[StepN-1].append(CurPossibleCand)
                    #
                    for inN in CurPossibleCand.LinkNsIncoming:
                        CandsOfLevel[StepN-1-1][inN-1].LinksOutcoming.append(CandsOfLevel[StepN-1][CurLevelListN-1])
                    #
                    #CandsOfLevel[StepN-1-1][prvN-1].LinksOutcoming.append(CandsOfLevel[StepN-1][CurLevelListN-1])
                    if vsh==1:
                        print('that member will do')
        #CandsOfLevel.append(CurLevelList)#so sabl, ce work. Nu altf
        #
        for prvN in range(1, prevStepL+1):
            outList=CandsOfLevel[StepN-1-1][prvN-1].LinkNsOutcoming
            outL=len(outList)
            #for outN in outList:
            #    if outN==CurLevelListN:
            #        CandsOfLevel[StepN-1-1][prvN-1].LinksOutcoming.append(CandsOfLevel[StepN-1][outN-1])
            print("cur level "+str(StepN)+" N "+str(CurLevelListN)+"prev level "+str(StepN-1)+" N "+str(prvN)+" out list: "+str(outList))
        #
        if vsh==1:
            print("Level "+str(StepN)+" Members: "+str(CandsOfLevel[StepN-1]))
    #
    if vsh==1:
        print("Candidates of automatical Levels are formed")
        print("Forming last level and connections")
    StepN+=1
    PrevLevelList=copy.deepcopy(CurLevelList)
    CurLevelList=[]
    CurPossibleCandContent=AllItemsList
    CurPossibleCand=Candidate(CurPossibleCandContent)
    CurLevelList.append(CurPossibleCand)
    CandsOfLevel.append(CurLevelList)
    CurLevelListN=1
    prevStepL=len(PrevLevelList)
    for prvN in range(1, prevStepL+1):
        prvCurItemContentList=PrevLevelList[prvN-1].ItemsList
        if vsh==1:
            print("Candidate: Level: "+str(StepN-1)+" N "+str(prvN)+" Content: "+str(prvCurItemContentList))
        if ArePrsentAllInAnySucc(CurPossibleCandContent, prvCurItemContentList)==1:
            CurPossibleCand.LinkNsIncoming.append(prvN)
            #PrevLevelList[prvN-1].LinkNsOutcoming.append(CurLevelListN)
            CandsOfLevel[StepN-1-1][prvN-1].LinkNsOutcoming.append(CurLevelListN)
            if vsh==1:
                print("Connected!")
        else:
            if vsh==1:
                print("Not connected")
    if vsh==1:
        print("Candidates of all Levels are formed")
    #
    #for StepN in range(1, allL-1+1)
    for StepN in range(1, allL+1):
        if vsh==1:
            print('Level '+str(StepN))
            print(str(CandsOfLevel[StepN-1]))
    return CandsOfLevel
#
def fSupport(transactionsList, comb, vsh=0):
    QTransactions=len(transactionsList)
    if vsh==1:
        print("fSuppl starts working. Transactions: "+str(QTransactions)+" Comb: "+str(comb))
    countOccurances=0
    #if vsh==0:
    #    for transaction in transactionsList:
    #        if ArePrsentAllInAnySucc(transaction, comb, vsh)==1:
    #            countOccurances+=1
    #else:
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

#def getChildrenList(tree, LevelN, ItemN, listExt=[]):
#    QLevels=len(tree)
#    listIne=copy.deepcopy(listExt)
#    QMembersAtLevel=len(tree[LevelN-1])
#    ChildrenLevelN=LevelN+1  
#    if LevelN>=1 and LevelN<QLevels and ItemN>=1 and ItemN<=QMembersAtLevel:
#        QOutcomingConns=len(tree[LevelN-1][ItemN-1].LinkNsOutcoming)
#        for N in range(1, QOutcomingConns+1):
#            ChildrenItem=[]
#            ChildrenItem.append(ChildrenLevelN)
#            ChildrenItem.append(tree[ChildrenLevelN-1][ItemN-1].LinkNsOutcoming[N-1])
#            listIne.append(ChildrenItem)
#    return listIne

def getAllChildrenGenerationsList(tree, LevelN, ItemN, listExt=[], vsh=0):
    if vsh==1:
        print("getAllChildrenGenerationsList starts working")
        print("Level "+str(LevelN)+" N "+str(ItemN)+" list came: "+str(listExt))
    QLevels=len(tree)
    listIne=copy.deepcopy(listExt)
    QMembersAtLevel=len(tree[LevelN-1])
    ChildrenLevelN=LevelN+1  
    if LevelN>=1 and LevelN<QLevels and ItemN>=1 and ItemN<=QMembersAtLevel:
        QOutcomingConns=len(tree[LevelN-1][ItemN-1].LinkNsOutcoming)
        for N in range(1, QOutcomingConns+1):
            ChildrenItem=[]
            ChildrenItem.append(ChildrenLevelN)
            #ChildrenItem.append(tree[ChildrenLevelN-1][ItemN-1].LinkNsOutcoming[N-1])
            ChildrenItem.append(tree[LevelN-1][ItemN-1].LinkNsOutcoming[N-1])
            listIne.append(ChildrenItem)
            if vsh==1:
                print("Child: Level "+str(ChildrenLevelN)+" N "+str(N)+" or "+str(ChildrenItem))
                print("Starting Recursion. From: Level "+str(LevelN)+" N "+str(ItemN)+" To: Level "+str(ChildrenLevelN)+" N "+str(N))
            listIne=getAllChildrenGenerationsList(tree, ChildrenLevelN, N, listIne, vsh)
            if vsh==1:
                print("Returning from Recursion. From: Level "+str(ChildrenLevelN)+" N "+str(N)+" To: Level: "+str(LevelN)+" N "+str(ItemN))
                print("Now List: "+str(listIne))
    listIne=ClearListFromNotUniqueVals(listIne)
    if vsh==1:
        print("Answer: List: "+str(listIne))
        print("getAllChildrenGenerationsList finishes working")
    return listIne

#def getParentsList(tree, LevelN, ItemN, listExt=[]):
#    QLevels=len(tree)
#    listIne=copy.deepcopy(listExt)
#    QMembersAtLevel=len(tree[LevelN-1])
#    ParentLevelN=LevelN+1
#    if LevelN>1 and LevelN<=QLevels and ItemN>=1 and ItemN<=QMembersAtLevel:
#        QIncomingConns=len(tree[LevelN-1][ItemN-1].LinkNsIntcoming)
#        for N in range(1, QIncomingConns+1):
#            ParentItem=[]
#            ParentItem.append(ParentLevelN)
#            ParentItem.append(tree[ParentLevelN-1][ItemN-1].LinkNsOutcoming[N-1])
#            listIne.append(ParentItem)
#    return listIne
#
class GraphOfCands:
    def __init__(self, transactionsList, vsh=0):
        self.CandsOfLevel=FormAllCandsAndBuildQuasiTree(transactionsList, vsh)

    def FormAllCandsAndBuildQuasiTree(self, transactionsList, vsh=0):
        AllItemsList=FormListOfUniqueItems(transactionsList)
        if vsh==1:
            print('All:')
            print(AllItemsList)
            print('Candidates:')
        allL=len(AllItemsList)
        CandsOfLevel=[]
        EmptyList=[]
        #ConnsInOfLevel=[]
        #ConnsOutOfLevel=[]
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
            CurLevelList=[]
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
                #
                print("cur level "+str(StepN)+" N "+str(CurLevelListN)+"prev level "+str(StepN-1)+" N "+str(prvN)+" out list: "+str(outList))
            #
            if vsh==1:
                print("Level "+str(StepN)+" Members: "+str(CandsOfLevel[StepN-1]))
        #
        if vsh==1:
            print("Candidates of automatical Levels are formed")
            print("Forming last level and connections")
        StepN+=1
        PrevLevelList=copy.deepcopy(CurLevelList)
        CurLevelList=[]
        CurPossibleCandContent=AllItemsList
        CurPossibleCand=Candidate(CurPossibleCandContent)
        CurLevelList.append(CurPossibleCand)
        CandsOfLevel.append(CurLevelList)
        CurLevelListN=1
        prevStepL=len(PrevLevelList)
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
                listIne=getAllChildrenGenerationsList(tree, ChildrenLevelN, N, listIne, vsh)
                if vsh==1:
                    print("Returning from Recursion. From: Level "+str(ChildrenLevelN)+" N "+str(N)+" To: Level: "+str(LevelN)+" N "+str(ItemN))
                    print("Now List: "+str(listIne))
        listIne=ClearListFromNotUniqueVals(listIne)
        if vsh==1:
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
            print("DelElement sterts working: LevelN="+str(LevelN)+" memberN="+str(memberN)+" Level length="+str(len(self.CandsOflevel[LevelN-1])))
        if LevelN>=1 and LevelN<=self.getQlevels() and memberN>=1 and memberN<=len(self.CandsOflevel[LevelN-1]):
            QWithMates=len(self.CandsOflevel[LevelN-1])
            if LevelN>1:
                if vsh==1:
                    print("Del and change outcoming links from prev level:")
                QOther=len(self.CandsOflevel[LevelN-1-1])
                if vsh==1:
                    print("Element "+str(i)+":")
                for i in range(1, QOther+1):
                    #Deleting link to this element
                    ConnListL=len(self.CandsOflevel[LevelN-1-1][i-1].LinksOutcoming)
                    for j in range(1, ConnListL+1):
                        if self.CandsOflevel[LevelN-1-1][i-1].LinksOutcoming[j-1]==CandsOflevel[LevelN-1][memberN-1]:
                            del(self.CandsOflevel[LevelN-1-1][i-1].LinksOutcoming[j-1:j+1-1])
                    #Deleting link to N of this element
                    if vsh==1:
                        print("List of outcoming list Previously: "+str(self.CandsOflevel[LevelN-1-1][i-1].LinkNsOutcoming))
                    ConnListL=len(self.CandsOflevel[LevelN-1-1][i-1].LinkNsOutcoming)
                    for j in range(1, ConnListL+1):
                        linkToN=self.CandsOflevel[LevelN-1-1][i-1].LinkNsOutcoming[j-1]
                        if linkToN==memberN:
                            del(self.CandsOflevel[LevelN-1-1][i-1].LinkNsOutcoming[j-1:j+1-1])
                    if vsh==1:
                        print("List of outcoming list After deleting: "+str(self.CandsOflevel[LevelN-1-1][i-1].LinkNsOutcoming))
                    #Decreasing links to N of next elements
                    ConnListL=len(self.CandsOflevel[LevelN-1-1][i-1].LinkNsOutcoming)
                    for j in range(1, ConnListL+1):
                        if linkToN>memberN:
                            self.CandsOflevel[LevelN-1-1][i-1].LinkNsOutcoming[j-1]-=1
                    if vsh==1:
                        print("List of outcoming list After changing: "+str(self.CandsOflevel[LevelN-1-1][i-1].LinkNsOutcoming))
            if LevelN<self.getQlevels():
                if vsh==1:
                    print("Del and change incoming links from next level :")
                QOther=len(self.CandsOflevel[LevelN+1-1])
                for i in range(1, QOther+1):
                    if vsh==1:
                        print("Element "+str(i)+":")
                    #Deleting link to this element
                    ConnListL=len(self.CandsOflevel[LevelN+1-1][i-1].LinksIncoming)
                    for j in range(1, ConnListL+1):
                        if self.CandsOflevel[LevelN+1-1][i-1].LinksIncoming[j-1]==CandsOflevel[LevelN-1][memberN-1]:
                            del(self.CandsOflevel[LevelN+1-1][i-1].LinksIncoming[j-1:j+1-1])
                    if vsh==1:
                        print("List of incoming list Previously: "+str(self.CandsOflevel[LevelN-1-1][i-1].LinkNsIncoming))
                    #Deleting link to N of this element
                    if vsh==1:
                        print("Element "+str(i)+":")
                    ConnListL=len(self.CandsOflevel[LevelN+1-1][i-1].LinkNsIncoming)
                    for j in range(1, ConnListL+1):
                        linkToN=self.CandsOflevel[LevelN+1-1][i-1].LinkNsIntcoming[j-1]
                        if linkToN==memberN:
                            del(self.CandsOflevel[LevelN+1-1][i-1].LinkNsIncoming[j-1:j+1-1])
                    if vsh==1:
                        print("List of incoming list After deleting: "+str(self.CandsOflevel[LevelN-1-1][i-1].LinkNsIncoming))
                    #Decreasing links to N of next elements
                    ConnListL=len(self.CandsOflevel[LevelN+1-1][i-1].LinkNsIncoming)
                    for j in range(1, ConnListL+1):
                        if linkToN>memberN:
                            self.CandsOflevel[LevelN+1-1][i-1].LinkNsIncoming[j-1]-=1
                    if vsh==1:
                        print("List of incoming list After changing: "+str(self.CandsOflevel[LevelN-1-1][i-1].LinkNsIncoming))
            del(self.CandsOflevel[LevelN-1][memberN-1:memberN+1-1])
            if vsh==1:
                print("Now Level length="+str(len(self.CandsOflevel[LevelN-1])))
                print("DelElement finishes working")

    
        

    def Elaborate(self, transactionsList, minsupport):
        continLevels=1
        LevelN=0
        while continLevels==1:
            LevelN+=1
            
                
        

vsh=0
minsupport=50
minconfidence=60
#
print("\nTransaction list:")
print(str(transactionsList))
print("\nList of unique items:")
AllItemsList=FormListOfUniqueItems(transactionsList)
Q=len(AllItemsList)
print(str(AllItemsList))
CandsOfLevel=FormAllCandsAndBuildQuasiTree(transactionsList, vsh)
print("\nCandidates:")
QLevels=len(CandsOfLevel)
for LvlN in range(1, QLevels+1):
    LevelL=len(CandsOfLevel[LvlN-1])
    print("Level "+str(LvlN))
    for itmN in range(1, LevelL+1):
        print(str(itmN)+") "+str(CandsOfLevel[LvlN-1][itmN-1].ItemsList)+" In: "+str(CandsOfLevel[LvlN-1][itmN-1].LinkNsIncoming)+" Out: "+str(CandsOfLevel[LvlN-1][itmN-1].LinkNsOutcoming))
    
#
print("\n\nCalc support smart")
ContinCheckLevels=1
StepN=0
LastLevelToElab=0
while ContinCheckLevels==1:
    StepN+=1
    for StepN in range(1, Q-1+1):
        CountLevelSuitableSupportVals=0
        CurLevelLength=len(CandsOfLevel[StepN-1])
        LevelMemberLength=len(CandsOfLevel[StepN-1][1-1].ItemsList)
        #
        NextStepN=StepN+1
        NextLevelLength=len(CandsOfLevel[NextStepN-1])
        #
        for memberN in range(1, CurLevelLength+1):
            pass
#
print("\n\nElaborating quasi-tree and searching for rules:\n")


print("\n\nRecursive Cojnnected at Sub-levels:")
items=getAllChildrenGenerationsList(CandsOfLevel, 1, 1)
print(items)
        


                    
         
           
        

    
