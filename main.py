import populationUtils
import datautils

# values for change
populationNum = 50
geneNumber = 60
index = 10  # How many full runs for the average

crossover_rate = 0.7  # Starting rates
mutation_rate = 0.9

# Values for holding population info
current_population = []
new_population = []

old_fitness = 0
new_fitness = 0
epoch = 0
last_epoch_update = 0

test_values = []
temp_list = []
averaged_values = []
epoch_list = []

total_epoch = 0
avg_epoch = 0

class Main:
    #Setup population
    datautils = datautils.dataUtils()
    popUtils = populationUtils.PopulationUtils()

    #  Define Mutation and Crossover rate
    popUtils.mutation_rate = mutation_rate
    popUtils.crossover_rate = crossover_rate

    rule_list = datautils.read_from_file('/home/william/Projects/University/Genetic-Algorithm-Rule-Classification/data/data1.txt')
    old_fitness, current_population = popUtils.create_population(current_population, populationNum, geneNumber, rule_list)

    while crossover_rate < 1:
        # mutation_rate += 0.001
        crossover_rate += 0.1
        for x in range(index):
            current_population = []
            new_population = []

            old_fitness, current_population = popUtils.create_population(current_population, populationNum, geneNumber, rule_list)
            epoch = 0

            while True:  # Begin stepping towards optimal solution
                new_population, new_fitness = popUtils.high_fitness_evaluation(current_population, rule_list)
                current_population = new_population
                if new_fitness >= old_fitness:  # Record the highest fitness seen
                    old_fitness = new_fitness

                print("Average fitness: %s" % (new_fitness / populationNum))
                print(epoch, new_population[0])

                if new_population[0].fitness >= 10:
                    test_values.append(epoch)
                    break

                epoch += 1
        total_epoch = 0
        for x in test_values:
            total_epoch += x
        if total_epoch != 0:
            avg_epoch = total_epoch / index

        avg_fitness = new_fitness / populationNum
        temp_list = []
        temp_list.append(avg_fitness)
        temp_list.append(avg_epoch)
        temp_list.append(new_population[0].fitness)
        temp_list.append(crossover_rate)
        epoch_list.append(temp_list)
        datautils.copy_write_to_csv(
            "/home/william/Projects/University/Genetic-Algorithm-Rule-Classification/data/test/dataset1.csv",
            epoch_list)
        avg_epoch = 0
        total_epoch = 0
        epoch_list = []
    test_values = []



