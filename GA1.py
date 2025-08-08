#From book Virsansky Genetic algorythms

#import deap as ep
from deap import base#wa no in bog, ma afce ne ecri error
toolbox=base.Toolbox()#pg64


from deap import creator

creator.create("FitnessMax", base.Fitness, weights=(1.0,))


#possible analogs:
#creator.create("FitnessMin", base.Fitness, weights=(-1.0,))

#creator.create("FitnessCompound", base.Fitness, weights=(1.0, 0.2, -0.5))
creator.create("Individual", list, fitness=creator.FitnessMax)


from deap import tools
#from deap import toolbox#ecri: can't import tic name
#from deap import *#try ety so - et: toolbox name s'ne def'd

toolbox.register("select", tools.selTournament, tournsize=3) #ety es: selRoulette(),  selStochasticUniversalSampling() – стохастическая универсальная выборка 
toolbox.register("mate", tools.cxTwoPoint) #2-point crossover. Ety es:  cxOnePoint(), cxUniform()(), cxOrdered(),  cxPartialyMatched()(PMX) 
toolbox.register("mutate", tools.mutFlipBit, indpb=0.02)
#Ety es: mutGaussian()


def someFitnessCalculationFunction(individual):
    return _some_calculation_of_the_fitness

toolbox.register("evaluate",someFitnessCalculationFunction)


#sinmple bit invert mut gut work co binary

#================================================================

#1/3) prepartation

#1 linbs

from deap import base
from deap import creator
from deap import tools
import random
import matplotlib.pyplot as plt



#2 Consts

#tasks constants

ONE_MAX_LENGTH = 100    # длина подлежащей оптимизации битовой строки


#3 константы генетического алгоритма

POPULATION_SIZE = 200   # количество индивидуумов в популяции
P_CROSSOVER = 0.9       # вероятность скрещивания
P_MUTATION = 0.1        # вероятность мутации индивидуума
MAX_GENERATIONS = 50    # максимальное количество поколений



#3 efe val o'random nums gen'z ut results wu repeat'bl

RANDOM_SEED = 42
random.seed(RANDOM_SEED)


#4 ut wu random 0 or 1 et noid ady

toolbox = base.Toolbox()
toolbox.register("zeroOrOne", random.randint, 0, 1)



#5 Fitness: 1 aim tob 1 val of weights, aim s' maxf, tob val of weight >0

creator.create("FitnessMax", base.Fitness, weights=(1.0,))


#6 ut abfa individuals

creator.create("Individual", list, fitness=creator.FitnessMax)


#7 registering individual creator operator , filled by 0s et 1s.

toolbox.register("individualCreator", tools.initRepeat,
creator.Individual, toolbox.zeroOrOne, ONE_MAX_LENGTH)



#8 registering  populationCreator opwrator, ic abfa't inds list
#initRepeat val ne given hin tob um utf l'operator populationCreator V mus dat S

toolbox.register("populationCreator", tools.initRepeat, list, toolbox.individualCreator)



#9 fitness fn(items 10 et 11 co , pg 71):

def oneMaxFitness(individual):
    return sum(individual),#ce wi tuple, ob in deap fitness vals are returned as tuples

toolbox.register("evaluate", oneMaxFitness)


#10 def operatoe evaluate

toolbox.register("evaluate", oneMaxFitness)


#11

toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", tools.cxOnePoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=1.0/ONE_MAX_LENGTH)


# Solution Evolution - pg 72

# Gen alg s'real'd in
#main
#fn
#, below s' su steps
#1 Creo efe pop P..S

population = toolbox.populationCreator(n=POPULATION_SIZE)
generationCounter = 0


#2 ut calc fitness, V utf Py fn map, ic aPPL'T OPER EVAL AD JE ELT O'POP
#   ET TRA s ad liat o'tuples

fitnessValues = list(map(toolbox.evaluate, population))

#3 ob elts o' list fitnessVals we'y 1mean'y fit elts o'pop, V abl utf fn zip()
#ut unite em by pairs
# et fit je elt su fitness

for individual, fitnessValue in zip(population, fitnessValues):
    individual.fitness.values = fitnessValue


#4 V ha fitness co nur 1 aim

fitnessValues = [individual.fitness.values[0] for individual in population]


#5 uz statistik:

maxFitnessValues = []
meanFitnessValues = []


#6 main algs cycle:

while max(fitnessValues) < ONE_MAX_LENGTH and generationCounter< MAX_GENERATIONS:


#7 klar
    generationCounter = generationCounter + 1

#8 cor of alg - gen opers:

    offspring = toolbox.select(population, len(population))


#9 sel's inds clon'tc, ut appl a D l'gen opers, ne touching l'ini pop
    offspring = list(map(toolbox.clone, offspring))


#10 cvrossover
    #their code. Qid if Py2 ne cog it?
    #for child1, child2 in zip(offspring[::2], offspring[1::2]):
    #    if random.random() < P_CROSSOVER:
    #        toolbox.mate(child1, child2)
    #        del child1.fitness.values
    #        del child2.fitness.values
    #ud s'my alg. Ce >unal r'solv tic rebus
    QPairs=len(offspring)/2
    for i in range(1, QPairs+1):
        child1N=2*(i-1)
        child1=offspring[child1N-1]
        child2N=2*(i-1)+1
        child2=offspring[child2N-1]
        toolbox.mate(child1, child2)
        del child1.fitness.values
        del child2.fitness.values

# 11 muta
    for mutant in offspring:
        if random.random() < P_MUTATION:
            toolbox.mutate(mutant)
            del mutant.fitness.values

#12
    freshIndividuals = [ind for ind in offspring if not ind.fitness.valid]
    freshFitnessValues = list(map(toolbox.evaluate, freshIndividuals))
    for individual, fitnessValue in zip(freshIndividuals, freshFitnessValues):
        individual.fitness.values = fitnessValue

#13 WEPAS   old pop by new
    population[:] = offspring#so wa in book, ma it ecri error at af oper: invalid syntax
    #population=copy.deepcopy(offspring)#ce my new oper, ob mab py2 ne cog syntav ov


#14 print statistik
    maxFitness = max(fitnessValues)
    meanFitness = sum(fitnessValues) / len(population)
    maxFitnessValues.append(maxFitness)
    meanFitnessValues.append(meanFitness)
    print("- Поколение {}: Макс приспособ. = {}, Средняя приспособ. = {}".format(generationCounter, maxFitness, meanFitness))

#16 best ind N
    #t_index = fitnessValues.index(max(fitnessValues))              # wa in book, py 2 et I ne cog ce
    #print("Лучший индивидуум = ", *population[best_index], "\n")   # wa in book, py 2 et I ne cog ce
    best_index = fitnessValues.index(max(fitnessValues))               # ce my vrn o'id ov, ob py2 et I ne cog ce
    print("Лучший индивидуум = ", population[best_index], "\n")    # ce my vrn o'id ov, ob py2 et I ne cog ce
#17 graphs
    plt.plot(maxFitnessValues, color='red')
    plt.plot(meanFitnessValues, color='green')
    plt.xlabel('Поколение')
    plt.ylabel('Макс/средняя приспособленность')
    plt.title('Зависимость максимальной и средней приспособленности от поколения')
    plt.show()

#EW alles
        
        

    


