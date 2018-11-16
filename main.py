from Utils import datautils, populationUtils

# values for change
populationNum = 50
geneNumber = 40

#Values for holding population info
current_population = []
new_population = []

old_fitness = 0
new_fitness = 0

epoch = 0
last_epoch_update = 0

test_values = []

class Main:
    #Setup population
    datautils = datautils.dataUtils()

    rule_list, rule_classifiers = datautils.read_from_file('/home/william/Projects/University/Genetic-Algorithm-Rule-Classification/data/data2.txt')
    popUtils = populationUtils.PopulationUtils()
    old_fitness, current_population = popUtils.create_population(current_population, populationNum, geneNumber, rule_list, rule_classifiers)

    while True:  # Begin stepping towards optimal solution
        new_population, new_fitness = popUtils.high_fitness_evaluation(current_population, rule_list, rule_classifiers)
        current_population = new_population



        temp_list = []
        temp_list.append((new_fitness/populationNum))
        temp_list.append(epoch)
        test_values.append(temp_list)

        if new_fitness >= old_fitness: # Record the highest fitness seen
            old_fitness = new_fitness

        print("Average fitness: %s" % (new_fitness/populationNum))
        if new_fitness / populationNum >= 64:
            print(new_population[0])
            datautils.copy_write_to_csv("/home/william/Projects/University/Genetic-Algorithm-Rule-Classification/data/test/dataset2_wildcard.csv",test_values)
            break

        epoch += 1



