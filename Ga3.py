import random
import copy

#Poulqation

def fMax(X, what_vals0Ns1=0):
    Q=len(X)
    maximum=0
    N=0
    R=0
    for i in range(1, Q+1):
        if i==1 or (i>1 and X[i-1]>maximum):
            maximum=X[i-1]
            N=i
    if what_vals0Ns1==1:
        R=N
    else:
        R=maximum
    return R

def fSort(X, how_Acs0Desc1=1, what_vals0Ns1=0, vsh=0):
    Y=[]
    Z=[]
    R=[]
    minimum=0
    Q=len(X)
    if vsh==1:
        print("fSort starts working")
        for i in range(1, Q+1):
            print(i, X[i-1])
    Z=copy.deepcopy(X)
    for i in range(1, Q+1):
        Y.append(i)
    if vsh==1:
        print("formed Y array: "+str(Y))
        if what_vals0Ns1==1:
            print("sort by Ns:")
        else:
            print("sort by vals:")

        if how_Acs0Desc1==1:
            print("sort descending:")
        else:
            print("sort ascending:")
    #
    if how_Acs0Desc1==1:
        for i in range(1, Q+1):
            for j in range(i+1, Q+1):
                if vsh==1:
                    print("Comparing X["+str(i)+"]="+str(X[i-1])+" with X["+str(j)+"]="+str(X[j-1]))
                if(Z[j-1]>Z[i-1]):
                    buf=copy.deepcopy(Z[i-1])
                    Z[i-1]=copy.deepcopy(Z[j-1])
                    Z[j-1]=copy.deepcopy(buf)
                    buf=copy.deepcopy(Y[i-1])
                    Y[i-1]=copy.deepcopy(Y[j-1])
                    Y[j-1]=copy.deepcopy(buf)
                    if vsh==1:
                        print("Now: Y["+str(i)+"]="+str(Y[i-1])+" and Y["+str(j)+"]="+str(Y[j-1]))
                else:
                    if vsh==1:
                        print("pass further")
    else:
        for i in range(1, Q+1):
            for j in range(i+1, Q+1):
                if vsh==1:
                    print("Comparing X["+str(i)+"]="+str(X[i-1])+" with X["+str(j)+"]="+str(X[j-1]))
                if(Z[j-1]<Z[i-1]):
                    buf=copy.deepcopy(Z[i-1])
                    Z[i-1]=copy.deepcopy(Z[j-1])
                    Z[j-1]=copy.deepcopy(buf)
                    buf=copy.deepcopy(Y[i-1])
                    Y[i-1]=copy.deepcopy(Y[j-1])
                    Y[j-1]=copy.deepcopy(buf)
                    if vsh==1:
                        print("Now: Y["+str(i)+"]="+str(Y[i-1])+" and Y["+str(j)+"]="+str(Y[j-1]))
                else:
                    if vsh==1:
                        print("pass further")
    if what_vals0Ns1==1:
        R=copy.deepcopy(Y)
    else:
        R=copy.deepcopy(X)
    if vsh==1:
        print("Now:")
        for i in range(1, Q+1):
            print(i, Y[i-1], X[Y[i-1]-1], Z[i-1])
        print("fSort finishes working")
    #
    return R

def PosInSucc(X, x, vsh=0):
    Q=len(X)
    R=[]
    R.append([0, "-IsLess"])#1-1
    R.append([0, "-IsGreater"])#2-1
    R.append([0, "-IsWithin"])#3-1
    R.append([0, "-EqualN"])#4-1
    R.append([0, "-LessN"])#5-1
    if(vsh==1):
        print("PosInSucc starts working")
    if x<X[1-1]:
        R[1-1][1-1]=1
        if(vsh==1):
            print("1-Less")
    elif x>X[Q-1]:
        R[2-1][1-1]=1
        if(vsh==1):
            print("2-greater")
    else:
        R[3-1][1-1]=1
        for i in range(1, Q+1):
            if x==X[i-1]:
                R[4-1][1-1]=i
                if(vsh==1):
                    print("3=1, 5=0, 4-eqN="+str(R[4-1][1-1]))
        if R[4-1][1-1]==0:
            for i in range(1, Q+1):
                if (x>X[i-1]) and (x<X[i+1-1]):
                    R[5-1][1-1]=i
                    if(vsh==1):
                        print("3=1, 4=0, 5-lessN="+str(R[5-1][1-1]))
    if(vsh==1):
        print("Answer: "+str(R))
        print("PosInSucc finishes working")
    return R

def PossInList(X, x, vsh=0):
    Ns=[]
    count=0
    if(vsh==1):
        print("PosInSucc finishes working")
        print("Seeking pos of "+str(x)+" in "+str(X))
    if isinstance(X, list) and len(X)>0:
        Q=len(X)
        if(vsh==1):
            print("X is not empty (Length="+str(Q)+"), starting search")
        for i in range(1, Q+1):
            #N=Q+1-i
            if(vsh==1):
                print("X["+str(i)+"]="+str(X[i-1]))
            if(X[i-1]==x):
                Ns.append(i)
                count=count+1
                if(vsh==1):
                    print("found "+str(count)+": X["+str(i)+"]="+str(X[i-1])+" = "+str(x)+" Now poss: "+str(Ns))
    else:
        if(vsh==1):
            print("X is  empty, no set to seek in")
    if(vsh==1):
        print("Answer: pos(s) of "+str(x)+" in "+str(X)+" is "+str(Ns))
        print("PosInSucc finishes working")
    return Ns

def PosInListFirst(X, x, vsh=0):
    Ns=PossInList(X, x, vsh)
    R=0
    if Ns!=[]:
        R=Ns[1-1]
    return R

def DelN(X, N):
    del(X[N-1:(N+1-1)])


def CalcRanges(X, vsh=0):
    pass


def fTournament(pop, k, n, vsh=0):               
    group=[]
    winners=[]
    rest=[]
    Ns=[]
    N=len(pop)
    global vsh_hlp
    for i in range(1, N+1):
        Ns.append(i)
    rest=copy.deepcopy(Ns)
    if(vsh==1):
        print("fTournament starts working")
        print("Population:")
        for i in range(1, N+1):
            print(i, pop[i-1])
    SNs=fSort(pop, 1, 1, vsh_hlp)
    popRanges=[]
    if(vsh==1):
        print("Sorted by ranges:")
        print("N in pop; Quasi-Range; Val")
        for i in range(1, N+1):
            print(i, SNs[i-1], pop[SNs[i-1]-1])
        print("Forming ranges:")
    for ii in range(1, N+1):
        #for jj in range(1, N+1):
        #pos=PosInSucc(SNs, ii, vsh_hlp)
        pos=PossInList(SNs, ii, vsh_hlp)
        #if pos[4-1][1-1]>0:
        #popRanges.append(pos[4-1][1-1])
        popRanges.append(pos[1-1])
    if(vsh==1):
        print("Ranges:")
        print("N in pop; Val; Quasi-Range")
        for ii in range(1, N+1):
            print(ii, pop[ii-1], popRanges[ii-1])
        #Quasi-Range - quasi - ob 2 obes: 1) ne work if vals s' ne unique; 2) S ms'b sorted VV
    if(vsh==1):
        print("Group forming :")
    for i in range(1, n+1):
        group=[]
        restL=len(rest)
        if(vsh==1):
            print("Group "+str(i))
            print(" is being formed from: ")
            print("N in rest; N in pop; Val")
            for ii in range(1, restL+1):
                print(ii, rest[ii-1], pop[rest[ii-1]-1])
        for j in range(1, k+1):
            contin=1
            while contin==1:
                xr=random.randint(1, restL)#N in rest
                x=rest[xr-1]# N in pop
                if(vsh==1):
                    print("N= "+str(x))
                if winners!=[]:
                    winnersSorted=fSort(winners)
                    posInWinners=PosInSucc(winnersSorted, x, vsh_hlp)
                if winners==[] or posInWinners[4-1][1-1]==0:
                    if (group==[]):
                        contin=0
                        if(vsh==1):
                            print("group is empty - this is the first participant")
                    else:
                        groupSorted=fSort(group, 1, 0)
                        pos=PosInSucc(groupSorted, x, vsh_hlp)
                        if pos[4-1][1-1]==0:
                            contin=0
                            if(vsh==1):
                                print("this is the "+str(j)+"th participant") 
                        else:
                            if(vsh==1):
                                print("Incorrect: this is "+str(pos[4-1][1-1])+"th participant - trying again")
                else:
                    if(vsh==1):
                        print("Incorrect: this is "+str(posInWinners[4-1][1-1])+"th winner - trying again")
                if contin==0:
                    if(vsh==1):
                        print("seek in rest:")
                        restL=len(rest)
                        print("rest before considering Val:")
                        print("N in rest; N in pop; Val")
                        for ii in range(1, restL+1):
                            print(ii, rest[ii-1], pop[rest[ii-1]-1])
                    group.append(x)        
                    pos=PosInSucc(rest, x, vsh_hlp)
                    DelN(rest, pos[4-1][1-1])
                    if(vsh==1):
                        restL=len(rest)
                        print("rest after considering (deleting) Val:")
                        print("N in rest; N in pop; Val")
                        for ii in range(1, restL+1):
                            print(ii, rest[ii-1], pop[rest[ii-1]-1])
        #group ready
        if(vsh==1):
            print("Group "+str(i)+" is formed: ")#+str(group))
            print("N in group; N in pop; Val")
            for ii in range(1, k+1):
                print(ii, group[ii-1], pop[group[ii-1]-1])
            print("Tournament starts!")
        TurnGroup=[]
        for ii in range(1, k+1):
            TurnGroup.append(pop[group[ii-1]-1])
        x=fMax(TurnGroup, 1)
        if(vsh==1):
            print("Winner is known! This is : N in group: "+str(x)+" N in pop: "+str(group[x-1])+" val:"+str(pop[group[x-1]-1]))
            print("In group : "+str(group))
        winners.append(group[x-1])
        #zu irrational
        #for ii in range(1, k+1):
        #    DelN(rest, group[ii-1])
        #DelN(group, x)
        #groupL=len(group)
        winnersL=len(winners)
        restL=len(rest)
        if restL>=k:
            if(vsh==1):
                print("Left part of population is more than group size - part of population "+"\n"+" to participate remains")
        else:
            if(vsh==1):
                print("Left part of population is less than group size - allow previous "+"\n"+" tournaments participants to participate again:")
            rest=copy.deepcopy(Ns)
            for ii in range (1, winnersL+1):
                pos=PosInSucc(rest, winners[ii-1], vsh_hlp)
                x=pos[4-1][1-1]
                DelN(rest, x)
            restL=len(rest)
        if(vsh==1):
            print("Now: Winners:")
            print("N in winners group; N in pop; Val")
            for ii in range(1, winnersL+1):
                print(ii, winners[ii-1], pop[winners[ii-1]-1])
            print("Now: Rest:")
            print("N in rest group; N in pop; Val")
            for ii in range(1, restL+1):
                print(ii, rest[ii-1], pop[rest[ii-1]-1])
    if(vsh==1):
        print("Answer:")
        print("Loosers:")
        print("N in rest group; N in pop; Val")
        for ii in range(1, restL+1):
            print(ii, rest[ii-1], pop[rest[ii-1]-1])
        print("Winners:")
        print("N in winners group; N in pop; Val")
        for ii in range(1, winnersL+1):
            print(ii, winners[ii-1], pop[winners[ii-1]-1])
        print("fTournament finishes working")
    return winners

#def fRoulette(LBs, HBs, val, vsh=0):
#    if isinstance(LBs, list) and isinstance(HBs, list) and len(LBs)>-0 and len(HBs)=len(LBs):
#        Q=len(LBs)
#        pos=

def fRouletteChoice(X, n, vsh=0):
    global vsh_hlp
    winners=[]
    parts=[]
    rest=[]
    LB=[]
    HB=[]
    Ns=[]
    N=len(X)
    if vsh==1:
        print("fRouletteChoice starts working")
        print("Population:")
        for j in range(1, N+1):
            print(j, X[j-1])
    #
    for i in range(1, N+1):
        Ns.append(i)
    rest=copy.deepcopy(Ns)
    #
    if vsh==1:
        print("Preparing for Marking roulette's sectors:")
    summa=0
    for i in range(1, N+1):
        summa=summa+X[i-1]
    if vsh==1:
        print("summa="+str(summa))
    for i in range(1, N+1):
        parts.append(1.0*X[i-1]/summa)
        if vsh==1:
            print("part["+str(i)+"]="+str(parts[i-1]))
    if vsh==1:
        print("Marking roulette's sectors:")
    LB.append(0)
    #HB.append(parts[1-1])
    HB.append(LB[1-1]+parts[1-1])
    if vsh==1:
        print(str(1)+") "+str(LB[1-1])+" ... "+str(HB[1-1])+"  (dL="+str(parts[1-1])+")")
    for i in range(2, N+1):
        LB.append (HB[i-1-1])
        HB.append(LB[i-1]+parts[i-1])
        if vsh==1:
            print(str(i)+") "+str(LB[i-1])+" ... "+str(HB[i-1])+"  (dL="+str(parts[i-1])+")")
    #
    if vsh==1:
        print("Turning roulette!")
    for i in range(1, n+1):
        contin=1
        N=0
        while contin==1:
            val=random.random()
            if vsh==1:
                print("We have val:"+str(val))
            pos=PosInSucc(LB, val, vsh_hlp)
            if pos[4-1][1-1]>0:
                N=pos[4-1][1-1]
            elif pos[5-1][1-1]>0:
                N=pos[5-1][1-1]
            #pos=PossInList(LB, val, vsh_hlp)
            #if pos[1-1]>0:
            #    N=pos[1-1]
            if vsh==1:
                print("This is "+str(N)+"th range: "+str(LB[N-1])+" < "+str(val)+" < "+str(HB[N-1]))
            if winners==[]:
                contin=0
                if vsh==1:
                    print("There were no winners before- so "+str(N)+" is first winner!")
            else:
                #posInWinners=PosInSucc(winners, N, vsh_hlp)
                #if posInWinners[4-1][1-1]==0:
                posInWinners=PossInList(winners, N, vsh_hlp)
                if posInWinners==[]:
                    contin=0
                    if vsh==1:
                        print("This is new participant - so "+str(N)+" is new winner!")
                else:
                    if vsh==1:
                        print("Oh, "+str(N)+" already wone - Turning our roulette once more!")
        if N>0:
            winners.append(N)
            #
            DelN(rest, N)
            winnersL=len(winners)
            #
            if vsh==1:
                print("Now:")
                print("winners:")
                print("N winners group; N in pop; Val")
                for j in range(1, winnersL+1):
                    print(j, winners[j-1], pop[winners[j-1]-1])
                restL=len(rest)
                print("rest:")
                print("N rest group; N in pop; Val")
                for j in range(1, restL+1):
                    print(j, rest[j-1], pop[rest[j-1]-1])
    if vsh==1:
        print("answer:")
        print("Now:")
        print("winners:")
        print("N winners group; N in pop; Val")
        for j in range(1, winnersL):
            print(j, winners[j-1], pop[winners[j-1]-1])
        restL=len(rest)
        print("rest:")
        print("N rest group; N in pop; Val")
        for j in range(1, restL):
            print(j, rest[j-1], pop[rest[j-1]-1])
        print("fRouletteChoice finishes working")
    return winners


def FormParentsPairsPanMixio(potentialParents, QPairs=0, NoSame=0, NoWithSelf=0, vsh=0):
    pairs=[]
    seld=[]
    pair=[]
    rest=[]
    QParents=len(potentialParents)
    if QPairs==0 or (QPairs>QParents/2 and NoSame==1):
        QPairs=QParents/2
    if(vsh==1):
        print("FormParentsPairsPanMixio starts working")
        print("Potential parents: "+str(QParents)+" Pairs needed: "+str(QPairs)+" Same more than in 1 pair:(0-allowed,1-forbidden): "+str(NoSame)+" Pair with self:(0-allowed,1-forbidden): "+str(NoWithSelf))
        s=""
        for i in range(1, QParents+1):
           #s=s+str(i)+") "+str(potentialParents[i-1])+"(fit.="+str(pop[potentialParents[i-1]-1])+"); "
           print(str(i)+") "+str(potentialParents[i-1])+"(fit.="+str(pop[potentialParents[i-1]-1])+"); ")
        #print("Potential parents: "+s)
    #for i in range(1, QParents+1):
    #    #rest.append(potentialParents[i-1])#! no! so copies last!
    #    rest.append(copy.deepcopy(potentialParents[i-1]))
    #if(vsh==1):
    #    print("Potential parents (copy):")
    #    print(str(rest))
    #if(vsh==1):
    #    s=""
    #    for i in range(1, QParents+1):
    #       s=s+str(i)+") "+str (rest[i-1])+"; "
    #    print("Choose from: "+s)
    for i in range(1, QPairs+1):
        if(vsh==1):
            print("Forming "+str(i)+"st pair:")
           #print("Choosing from "+str(len(rest))+" individuals: "+str(rest))
        pair=[]
        contin=1
        QRest=len(rest)
        while contin:
            N1=random.randint(1, QParents)
            if(vsh==1):
                print("Trying N1 ["+str(i)+"]= in list of potential parents"+str(N1)+" = ind "+str(potentialParents[N1-1])+" (fit.="+str(pop[potentialParents[N1-1]-1])+")")
                if NoSame==1 and isinstance(seld, list) and len(seld)>0 and PosInListFirst(seld, N1)!=0:
                    if(vsh==1):
                        print("already present, this is forbidden, seeking again")
                else:
                    contin=0
                    if(vsh==1):
                        print("Chosen N1 ["+str(i)+"]= in list of potential parents"+str(N1)+" = ind "+str(potentialParents[N1-1])+" (fit.="+str(pop[potentialParents[N1-1]-1])+")")
        inN=PosInListFirst(seld, N1)
        if inN==0:
            seld.append(N1)
        pair.append(N1)
        #if NoSame==1:
        #    DelN(rest, N1)
        #    if(vsh==1):
        #        print("Now choosing from: "+str(rest))
        #No need this is checked if chosen is in selected
        contin=1
        QRest=len(rest)
        while contin:
            N2=random.randint(1, QParents)
            if(vsh==1):
                print("Trying N2 ["+str(i)+"]= in list of potential parents"+str(N2)+" = ind "+str(potentialParents[N2-1])+" (fit.="+str(pop[potentialParents[N2-1]-1])+")")
            if NoSame==1 and isinstance(seld, list) and len(seld)>0 and PosInSucc(seld, N1)>0:
                if vsh==1:
                     print("already present, this is forbidden, seeking again")
            elif NoWithSelf==1 and N1==N2:
                if vsh==1:
                     print("It is first parent in pair, pair with self is forbidden, seeking again")
            else:
                contin=0
                if(vsh==1):
                    print("Chosen N2 ["+str(i)+"]= in list of potential parents"+str(N2)+" = ind "+str(potentialParents[N2-1])+" (fit.="+str(pop[potentialParents[N2-1]-1])+")")
        #
        inN=PosInListFirst(seld, N2)
        if inN==0:
            seld.append(N2)
        pair.append(N2)  #N2=random.randint(1, QParents)  pair.append(N2)
        #if NoSame==1:
        #    DelN(rest, N2)
        #pair.append(N2)
        pairs.append(pair)
        if(vsh==1):
            print("pair: "+str(pair))
            print("Now all selected: ")#+str(seld))
            s=""
            QSeld=len(seld)
            for j in range(1, QSeld+1):
                s=s+str(j)+") parent "+str(seld[j-1])+" ind "+str(potentialParents[seld[j-1]-1])+"; "
            print(s)
    #
    if vsh==1:
        print("Exception method - forming list of those who didn't become parent:")
    #rest=copy.deepcopy(potentialParents)#no need to use
    if vsh==1:
        #print("Potential parents were_:")#+str(rest))
        #QRest=len(rest)
        #s=""
        #for j in range(1, QRest+1):
        #    print("potential parent "+str(j)+" ind "+str(rest[j-1])+"(fit.="+str(pop[rest[j-1]-1])+") ")
        #print(s)
        print("Now (1st vrn):")
    QSeld=len(seld)
    rest=copy.deepcopy(potentialParents)#no need to use
    if vsh==1:
        print("All (inds Ns): "+str(rest))
        print("Paired (parents Ns): "+str(seld)+" Inds Ns:")# in seld were written parents Ns
        s=""
        for j in range(1, QSeld+1):
            #inN=PosInListFirst(potentialParents, seld[j-1])
            #if inN>0:
            #    #    s=s+str(potentialParents[inN-1])+"; "
            #    print(str(potentialParents[inN-1]))
            #else:
            #    print("error: "+str(seld[j-1])+" doesn't belong to parents")
            s=s+str(potentialParents[seld[j-1]-1])+"; "
        print(s)
    for i in range(1,QSeld+1):#seld s'Ns of parents, rest s'Ns of inds
        #inN=PosInListFirst(rest, seld[i-1])
        indN=potentialParents[seld[i-1]-1]
        inN=PosInListFirst(rest, indN)
        if inN>0:
            DelN(rest, inN)
    if vsh==1:
        print("Unhappy Rest (Inds Ns): "+str(rest))
        #QRest=len(rest)
        #s=""
        #for j in range(1, QRest+1):
        #    inN=PosInListFirst(potentialParents, rest[j-1])
        #    if inN>0:
        #        s=s+str(potentialParents[inN-1])+"; "
        #print(s)
        print("Now (2nd vrn):")
    rest=copy.deepcopy(potentialParents)#no need to use
    for i in range(1, QPairs+1):
        for j in range(1, 2+1):
            #indN=pairs[i-1][j-1] #N2=random.randint(1, QParents)  pair.append(N2) => indN s'parentN
            parentN=pairs[i-1][j-1]
            indN=potentialParents[parentN-1]
            #inN=PosInListFirst(rest, indN) # in rest are inds Ns, ob os copy => so ne work
            inN=PosInListFirst(rest, indN)
            #if vsh==1:
            #    print("pair "+str(i)+" participant:"+str(j))
            #if i==1 or j==1:
            #    inN=PosInListFirst(rest, indN, 1)
            #else:
            #    inN=PosInListFirst(rest, indN, 0)
            if vsh==1:
                print("pair "+str(i)+" participant:"+str(j)+" parent: "+str(parentN)+" ind: "+str(indN)+" in list of rest of parents: "+str(inN))
            if inN>0:
                DelN(rest, inN)
                QRest=len(rest)
           # if vsh==1:
           #     print("Now list is: ")#+str(rest))
           #     s=""
           #     for k in range(1, QRest+1):
           #         inN=PosInListFirst(potentialParents, rest[k-1])
           #         s1=str(k)+") parent "+str(inN)+" ind "+str(potentialParents[inN-1])+"); "
           #         s=s+s1
           #     print(s)
    if vsh==1:
        #QRest=len(rest)
        print("Potential parents, who didn't become actual ones:")
        #print(str(rest))
        #QRest=len(rest)
        #s=""
        for k in range(1, QRest+1):
            inN=PosInListFirst(potentialParents, rest[k-1])
            s1=str(k)+") parent "+str(inN)+" ind "+str(potentialParents[inN-1])+"); "
            #s=s+s1
            print(s1)
       # print(s)
    #
    if(vsh==1):#here ecri'te err: invalid syntax: ma ce wa ob above in print missed 2nd bracket
        print("Choice results - pairs formed:")
        s=""
        for i in range(1, QPairs+1):
            #print("pair "+str(i)+": "+str(pairs[i-1][1-1])+" (fitness= "+str(pop[pairs[i-1][1-1]-1])+") & "+str(pairs[i-1][2-1])+" (fitness= "+str(pop[pairs[i-1][2-1]-1])+"); ")
            print("pair "+str(i)+": ind_in_potent_parents= "+str(pairs[i-1][1-1])+" ind_in pop= "+str(potentialParents[pairs[i-1][1-1]-1])+" (fitness= "+str(pop[potentialParents[pairs[i-1][1-1]-1]-1])+") & ind_in_potent_parents="+str(pairs[i-1][2-1])+" ind_in_pop= "+str(potentialParents[pairs[i-1][2-1]-1])+" (fitness= "+str(pop[potentialParents[pairs[i-1][2-1]-1]-1])+"); ")
        print("FormParentsPairsPanMixio finishes working")
    pair=[]
    pairsR=[]
    for i in range(1, QPairs+1):
        pair=[]
        parentN=pairs[i-1][1-1]
        indN=potentialParents[parentN-1]
        pair.append(indN)
        parentN=pairs[i-1][2-1]
        indN=potentialParents[parentN-1]
        pair.append(indN)
        pairsR.append(pair)
    #return pairs
    return pairsR
        
                    
    


def FormParentsPairs(winners, Which_Nearest0Furthest1=0):#not finished
    pairs=[]
    rest=[]
    QParents=len(winners)
    QPairs=QParents/2
    for i in range(1, QPairs+1):
        pairs.append(winners[i-1])
    for i in range(QPairs+1, QParents+1):
        pairs.append(winners[i-1])
    #
    pass
    
N=15#40
k=6
p=0.7
n=int(round(p*N))
if n%2!=0:
    n-=1
pop=[]
vsh_hlp=0
for i in range(1, N+1):
    #x=random.random()
    x=random.randint(1, 100)
    pop.append(x)
print("Population: ")
for i in range(1, N+1):
    print(i, pop[i-1])
print(" N="+str(N)+" k="+str(k)+" p="+str(p)+" n"+str(n))
#
#winners=fTournament(pop, k, n, 1)
#print("Winners: ", str(winners))
#
winners=fRouletteChoice(pop, n, 1)
print("Winners: ", str(winners))
print("\n\n\n")
pairs=FormParentsPairsPanMixio(winners, len(winners)/2, NoSame=0, NoWithSelf=0, vsh=1)                              
print("\nPairs formed:")
print(str(pairs))
#---------------------------------------------------------
#print("\n")
#QWinners=len(winners)
#PairedWinners=[]
#restAll=copy.deepcopy(pop)
#for i in range(1, QWinners+1):
#    indN=winners[i-1]
#    inN=PosInListFirst(restAll, indN)
#    DelN(restAll, inN)
#    if len(PairedWinners)==0 or PosInListFirst(PairedWinners, indN)==0:
#        PairedWinners.append(indN)
#loosersAfterFirstSelection=copy.deepcopy(restAll)
#print('Loosers after 1st selection: '+str(loosersAfterFirstSelection))
#print('Paired winners: '+str(PairedWinners))
#restWinners=copy.deepcopy(winners)
#restAll=copy.deepcopy(pop)
#QPairs=len(pairs)
#for i in range(1, QPairs+1):
#    for j in range(1, 2+1):
#        indN=pairs[i-1][j-1]
#        NinAll=PosInListFirst(restAll, indN)
#        NinWin=PosInListFirst(restWinners, indN)
#        if NinAll>0:
#            DelN(restAll, NinAll)
#        if NinWin>0:
#            DelN(restWinners, NinWin)
#print('Loosers after 2nd selection: '+str(restWinners))
#print('All loosers: '+str(restAll))        
