from Utils import datautils, populationUtils

# values for change
populationNum = 50
geneNumber = 140

crossover_rate = 0.7
mutation_rate = 0.989

index = 5  # Number of runs to average across

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
    # Setup population
    datautils = datautils.dataUtils()
    popUtils = populationUtils.PopulationUtils()
    rule_list, rule_classifiers = datautils.read_from_file(
        '/home/william/Projects/University/Genetic-Algorithm-Rule-Classification/data/data2.txt')

    while populationNum < 100:
        populationNum += 1

        for x in range(index):
            current_population = []
            new_population = []

            old_fitness, current_population = popUtils.create_population(current_population, populationNum, geneNumber,
                                                                         rule_list, rule_classifiers)
            epoch = 0

            while True:  # Begin stepping towards optimal solution
                new_population, new_fitness = popUtils.high_fitness_evaluation(current_population, rule_list,
                                                                               rule_classifiers)
                current_population = new_population
                if new_fitness >= old_fitness:  # Record the highest fitness seen
                    old_fitness = new_fitness

                print("Average fitness: %s" % (new_fitness / populationNum))
                if new_population[0].fitness >= 64:
                    print(new_population[0])
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
        temp_list.append(populationNum)
        epoch_list.append(temp_list)
        datautils.copy_write_to_csv(
            "/home/william/Projects/University/Genetic-Algorithm-Rule-Classification/data/test/dataset2_wildcard.csv",
            epoch_list)
        avg_epoch = 0
        total_epoch = 0
        epoch_list = []
        test_values = []
