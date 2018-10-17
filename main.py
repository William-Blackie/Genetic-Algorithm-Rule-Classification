import individual
import populationUtils

# values for change
populationNum = 50
geneNumber = 50

#Values for holding population info
current_population = []
new_population = []

old_fitness = 0
new_fitness = 0

epoch = 0


class Main():
    # setup population
    popnUtils = populationUtils.PopulationUtils()
    old_fitness, current_population = popnUtils.create_population(current_population, populationNum, geneNumber)

    while True:
        #begin stepping towards optima
        new_population, new_fitness = popnUtils.high_fitness_evaluation(current_population)
        print("New pop: %s Old pop: %s" , new_fitness, old_fitness)
        if(new_fitness > old_fitness): #Prevent fitness reduction
            print(old_fitness, new_fitness)
            old_fitness = new_fitness
            current_population = new_population
        if(new_fitness == populationNum * geneNumber):
            print ("Finished in %s epochs\n final fitness %s",epoch, new_fitness)

        epoch += 1


