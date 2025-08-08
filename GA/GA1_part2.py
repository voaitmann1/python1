import random
import copy


def Array1DReverse(X):
    Y=[]
    L=len(X)
    for i in range(1, L+1):
        N=L-i+1
        x=X[N-1]
        Y.append(x)
    return Y

def PowNat(x, y):
    z=1
    for i in range(1, y+1):
        z*=x
    return z

def IntNumToDigitsAscendingOrder(x, baseDec=10, vsh=0):
    digits=[]
    if x<0:
        y=-x
    else:
        y=x
    order=0
    if vsh==1:
        print("IntNumToDigits starts working")
        print("Number given: "+str(x))
        print("Defining order")
    while y>=baseDec and not ( (PowNat(baseDec,order) <= y) and ( PowNat(baseDec,order+1) > y) ):
        if vsh==1:
            if not ((PowNat(baseDec,order) <= y) and ( PowNat(baseDec,order+1) > y)):
                print(str(baseDec)+"^"+str(order)+"="+str(PowNat(baseDec,order))+" < "+str(y)+" and  "+str(baseDec)+"^"+str(order+1)+"="+str(PowNat(baseDec,order+1))+" < "+str(y))
            else:
                print(str(baseDec)+"^"+str(order)+"="+str(PowNat(baseDec,order))+" <= "+str(y)+" and "+str(baseDec)+"^"+str(order+1)+"="+str(PowNat(baseDec,order+1))+" > "+str(y))
        order+=1
    if vsh==1:
        print(str(x)+" is number of order: "+str(order))
    for i in range(1, order+1+1):
        digits.append(0)
    z=y
    for i in range(1, order+1):
        N=order+1-i
        IntPart=z/baseDec
        rest=z-IntPart*baseDec
        digit=rest
        z=(z-rest)/baseDec
        digits[i-1]=digit
        if vsh==1:
            print(str(i)+") N= "+str(N)+" div.IntPart= "+str(IntPart)+" div.rest= "+str(rest)+" digit= "+str(digit)+" z= "+str(z))
    digits[order+1-1]=z
    if vsh==1:
        print("So digits (ascending order): "+str(digits))
        print("IntNumToDigits finishes working")
    return digits

def IntNumToDigitsUsualOrder(x, baseDec=10, vsh=0):
    digitsAscending=IntNumToDigitsAscendingOrder(x, baseDec, vsh)
    digits=Array1DReverse(digitsAscending)
    return digits

def IntNumOfDigitsAscendingOrder(digits, baseDec=10):
    y=0
    order=len(digits)-1
    for i in range(1, order+1+1):
        y=y+digits[i-1]*PowNat(baseDec, i-1)
    return y

def IntNumOfDigitsUsualOrder(digits, baseDec=10):
    X=Array1DReverse(digits)
    y=IntNumOfDigitsAscendingOrder(X, baseDec)
    return y

def DigitsToLength(digits, length):
    Y=[]
    L1=len(digits)
    if L1<length:
        for i in range(1, (length-L1+1)):
            Y.append(0)
        for i in range(1, L1+1):
            Y.append(digits[i-1])
    else:
        Y=copy.deepcopy(digits)
    return Y


def CreateRealRandomNumber(NegativeIfRealAllowed1Forbidden0=0, minimum=0, maximum=100, vsh=0):
    if(vsh==1):
        print("CreateRealRandomNumber starts working")
        print("Conditions: NegativeIfRealAllowed1Forbidden0="+str(NegativeIfRealAllowed1Forbidden0)+" min="+str(minimum)+" max="+str(maximum))
    intPart=random.randint(minimum, maximum)
    fracPart=random.random()
    if(vsh==1):
        print(" int part="+str(intPart)+" frac part="+str(fracPart))
    FracPartSignMinus0Plus1=random.randint(0, 1)
    if NegativeIfRealAllowed1Forbidden0==1:
        NumSignMinus0Plus1=random.randint(0, 1)
    else:
        NumSignMinus0Plus1=1
        if FracPartSignMinus0Plus1==0 and intPart==0:
            FracPartSignMinus0Plus1=1
    if NumSignMinus0Plus1==1 and intPart+fracPart>maximum:
        FracPartSignMinus0Plus1=0
    if(vsh==1):
        print("signs: NumSignMinus0Plus1="+str(NumSignMinus0Plus1)+" FracPartSignMinus0Plus1="+str(FracPartSignMinus0Plus1))
    if FracPartSignMinus0Plus1==0:
        fracPart*=(-1)
    if(vsh==1):
        print("now int part="+str(intPart)+" frac part="+str(fracPart))
    y=intPart+fracPart
    if NumSignMinus0Plus1==0:
        y*=(-1)
    if(vsh==1):
        print("parts generated and corrected:"+str(y))
        print("Answer:"+str(y))
        print("CreateRealRandomNumber finishes working")
    return y



def CreateRandomChromosome(config, vsh=0):
    y=[]
    if vsh==1:
        print("CreateRandomChromosome starts working")
    if config.typeN_bin0int1real2==0:
        y=[]
        if vsh==1:
            print("type:binary")
        #for i in range(minimum, maximum):
        x=random.randint(config.minimum, config.maximum)
        if vsh==1:
            print("x="+str(x))
        digits1=IntNumToDigitsUsualOrder(x, 2)
        digits2=DigitsToLength(digits1, config.length)
        if vsh==1:
            print("digits="+str(digits2))
        y=copy.deepcopy(digits2)
    elif config.typeN_bin0int1real2==1:
        pass
    elif config.typeN_bin0int1real2==2:
        if vsh==1:
            print("type:real")
        for i in range(1, length+1):
            x=CreateRealRandomNumber(config.NegativeIfRealAllowed1Forbidden0, config.minimum, config.maximum, vsh)
            if vsh==1:
                print("x["+str(i)+"]="+str(x))
            y.append(x)
    else:
        if vsh==1:
            print("type:unknown")
    if vsh==1:
        print("CreateRandomChromosome finishes working")
    return y

def fitness_fn1(x):
    return 5000-(x-10)*(x-10)

def fitness_fn2(X):
    x1=X[1-1]
    x2=X[2-1]
    x3=X[3-1]
    return(x1**3 + 3*x1*x2 - 5*x2*x3-x3**4)
    

class GAIndConfig:
    def __init__(self, length=8, typeN_bin0int1real2=2, minimum=0,  maximum=256, NegativeIfRealAllowed1Forbidden0=0):
        self.length=length
        self.typeN_bin0int1real2=typeN_bin0int1real2
        self.length=length
        self.minimum=minimum
        self.maximum=maximum
        self.NegativeIfRealAllowed1Forbidden0=NegativeIfRealAllowed1Forbidden0
    def __str__():
       s1=" length="+str(self.length)
       s2=" typeN: bin-0, int-1, real-2)="+str(typeN_bin0int1real2)
       s3=self.length=self.length
       s4= elf.minimum=self.minimum
       s5=self.maximum=self.maximum
       s6=self.NegativeIfRealAllowed1Forbidden0=self.NegativeIfRealAllowed1Forbidden0
       s="config: "+s1+s2+s3+s4+s5+s6
       return s

class Individual:
    def __init__(self, config, fitness, chromosome=[]):
        self.chromosome=[]
        if chromosome==[] or not isinstance(chromosome, list) or (isinstance(chromosome, list) and len(chromosome)!=config.length):
            self.chromosome=CreateRandomChromosome(config)
        else:
            self.chromosome=copy.deepcopy(chromosome)
        self.fitness=fitness
        self.config=config
                    
    def getFitness(self):
        y=0
        if self.config.typeN_bin0int1real2==0:
            x=IntNumOfDigitsUsualOrder(self.chromosome, 2)
            y=self.fitness(x)
        else:
            y=self.fitness(self.chromosome)
        return y

    def getGenome(self):
        return self.chromosome

    def __str__(self):
        return str(self.chromosome)

print("1..5 rev: "+str(Array1DReverse([1,2,3,4,5])))
print("Real number:")
NegativeIfRealAllowed1Forbidden0=0
minimum=0
maximum=100
vsh=0
length=8
typeN_bin0int1real2=2
x=CreateRealRandomNumber(NegativeIfRealAllowed1Forbidden0, minimum, maximum, vsh)
print(x)
print("Real numbers List:")
vsh=0
length=8
typeN_bin0int1real2=2
config=GAIndConfig(length, typeN_bin0int1real2, minimum, maximum, NegativeIfRealAllowed1Forbidden0)
rl=CreateRandomChromosome(config, vsh)
print(str(rl))
length=8
typeN_bin0int1real2=0
digits1=IntNumToDigitsUsualOrder(x, 2, vsh)
digits2=DigitsToLength(digits1, length)
#print("ini num="+str(x)+" bin digits="+str(digits)+" bin digits correct length="+str(DigitsToLength(digits, length))+" num to check="+str())
print("ini num="+str(x)+" bin digits="+str(digits1))
print(" bin digits correct length="+str(digits2)+" num to check="+str(IntNumOfDigitsUsualOrder(digits2, 2)))
print("List of digits of Binary number:")
vsh=0
length=8
typeN_bin0int1real2=0
config=GAIndConfig(length, typeN_bin0int1real2, minimum, maximum, NegativeIfRealAllowed1Forbidden0)
b=CreateRandomChromosome(config, vsh)
print("b="+str(b))
#
print("\n\nPopulation binary-v1")
N=15
length=8
typeN_bin0int1real2=0
length=8
minimum=0
maximum=255
NegativeIfRealAllowed1Forbidden0=0
config=GAIndConfig(length, typeN_bin0int1real2, minimum, maximum, NegativeIfRealAllowed1Forbidden0)
inds_bin=[]
fitnesses=[]
for i in range(1, N+1):
    chromosome=CreateRandomChromosome(config, vsh)
    individual=Individual(config, fitness_fn1, chromosome)
    inds_bin.append(individual)
for i in range(1, N+1):
    chromosome=inds_bin[i-1].getGenome()
    fvi=inds_bin[i-1].getFitness()
    genomeCode=IntNumOfDigitsUsualOrder(chromosome, 2)
    #fve=fitness_fn1(genomeCode)
    fitnesses.append(fvi)
    Ns=str(i)
    while len(Ns)<3:
        Ns="0"+Ns
    #print("Individual "+Ns+": "+str(chromosome)+" = "+str(genomeCode)+" fit.="+str(fvi)+"="+str(fve))
    print("Individual "+Ns+": "+str(chromosome)+" = "+str(genomeCode)+" fit.="+str(fvi))
print(str(fitnesses))
#2
print("\n\nPopulation binary-v2")
N=15
length=8
typeN_bin0int1real2=0
length=8
minimum=0
maximum=255
NegativeIfRealAllowed1Forbidden0=0
config=GAIndConfig(length, typeN_bin0int1real2, minimum, maximum, NegativeIfRealAllowed1Forbidden0)
inds_bin=[]
fitnesses=[]
for i in range(1, N+1):
    individual=Individual(config, fitness_fn1)
    inds_bin.append(individual)
for i in range(1, N+1):
    chromosome=inds_bin[i-1].getGenome()
    fvi=inds_bin[i-1].getFitness()
    genomeCode=IntNumOfDigitsUsualOrder(chromosome, 2)
    #fve=fitness_fn1(genomeCode)
    fitnesses.append(fvi)
    Ns=str(i)
    while len(Ns)<3:
        Ns="0"+Ns
    #print("Individual "+Ns+": "+str(chromosome)+" = "+str(genomeCode)+" fit.="+str(fvi)+"="+str(fve))
    print("Individual "+Ns+": "+str(chromosome)+" = "+str(genomeCode)+" fit.="+str(fvi))
print(str(fitnesses))
#
print("\n\nPopulation real-numbers-v1")
N=15
length=3
typeN_bin0int1real2=2
minimum=0
maximum=255
NegativeIfRealAllowed1Forbidden0=0
config=GAIndConfig(length, typeN_bin0int1real2, minimum, maximum, NegativeIfRealAllowed1Forbidden0)
inds_bin=[]
fitnesses=[]
for i in range(1, N+1):
    chromosome=CreateRandomChromosome(config, vsh)
    individual=Individual(config, fitness_fn2, chromosome)
    inds_bin.append(individual)
for i in range(1, N+1):
    chromosome=inds_bin[i-1].getGenome()
    fvi=inds_bin[i-1].getFitness()
    #genomeCode=IntNumOfDigitsUsualOrder(chromosome, 2)
    #fve=fitness_fn1(genomeCode)
    fitnesses.append(fvi)
    Ns=str(i)
    while len(Ns)<3:
        Ns="0"+Ns
    #print("Individual "+Ns+": "+str(chromosome)+" = "+str(genomeCode)+" fit.="+str(fvi)+"="+str(fve))
    print("Individual "+Ns+": "+str(chromosome)+" fit.="+str(fvi))
print(str(fitnesses))
#
print("\n\nPopulation real-numbers-v2")
N=15
length=3
typeN_bin0int1real2=2
minimum=0
maximum=255
NegativeIfRealAllowed1Forbidden0=0
config=GAIndConfig(length, typeN_bin0int1real2, minimum, maximum, NegativeIfRealAllowed1Forbidden0)
inds_bin=[]
fitnesses=[]
for i in range(1, N+1):
    individual=Individual(config, fitness_fn2)
    inds_bin.append(individual)
for i in range(1, N+1):
    chromosome=inds_bin[i-1].getGenome()
    fvi=round(inds_bin[i-1].getFitness(), 3)
    fitnesses.append(fvi)
    Ns=str(i)
    while len(Ns)<3:
        Ns="0"+Ns
    print("Individual "+Ns+": "+str(chromosome)+" fit.="+str(fvi))
print(str(fitnesses))
