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

def PosInList(X, x, vsh=0):
    Ns=[]
    if isinstance(X, list) and len(X)>0:
        Q=len(X)
        for i in range(1, Q+1):
            #N=Q+1-i
            if(X[i-1]==x):
                Ns.append(i)
    return Ns

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
        pos=PosInList(SNs, ii, vsh_hlp)
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
            #pos=PosInList(LB, val, vsh_hlp)
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
                posInWinners=PosInList(winners, N, vsh_hlp)
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

