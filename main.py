import populationUtils
import datautils

# values for change
populationNum = 50
geneNumber = 60

#Values for holding population info
current_population = []
new_population = []

old_fitness = 0
new_fitness = 0

epoch = 0
last_epoch_update = 0


class Main:
    # Setup population
    popUtils = populationUtils.PopulationUtils()
    old_fitness, current_population = popUtils.create_population(current_population, populationNum, geneNumber)

    while True:  # Begin stepping towards optimal solution
        new_population, new_fitness = popUtils.high_fitness_evaluation(current_population)
        current_population = new_population

        print("New fitness: %s Old fitness: %s Epoch: %s" % (new_fitness, old_fitness, epoch))

        if new_fitness >= old_fitness: # Record the highest fitness seen
            old_fitness = new_fitness

        if new_fitness >= (populationNum * geneNumber / 4):
            print("Finished in %s epochs\n final fitness %s" % (epoch, new_fitness))
            break

        epoch += 1
    #datautils = datautils.dataUtils()

    #datautils.read_from_file()


