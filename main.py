import populationUtils
import datautils

# values for change
populationNum = 50
geneNumber = 80

#Values for holding population info
current_population = []
new_population = []

old_fitness = 0
new_fitness = 0

epoch = 0
last_epoch_update = 0


class Main:
    #Setup population
    datautils = datautils.dataUtils()

    rule_list, rule_classifiers = datautils.read_from_file('/home/william/Projects/University/Genetic-Algorithm-Rule-Classification/data/data2.txt')
    popUtils = populationUtils.PopulationUtils()
    old_fitness, current_population = popUtils.create_population(current_population, populationNum, geneNumber, rule_list, rule_classifiers)

    while True:  # Begin stepping towards optimal solution
        new_population, new_fitness = popUtils.high_fitness_evaluation(current_population, rule_list, rule_classifiers)
        current_population = new_population

        print("New fitness: %s Old fitness: %s Epoch: %s" % (new_fitness, old_fitness, epoch))

        if new_fitness >= old_fitness: # Record the highest fitness seen
            old_fitness = new_fitness
            print("test: %s" % new_population[0].fitness)
            if new_population[0].fitness == 64:
                print("uh oh")

        genes = new_population[0].genes
        gene_list = []
        temp_gene_list = []
        fitness = 0
        total_fitness = 0

        # for gene in genes:  # Section genes based on length of rules
        #     temp_gene_list.append(gene)
        #     if len(temp_gene_list) == len(rule_list[0]):
        #         gene_list.append(temp_gene_list)
        #         temp_gene_list = []
        #
        # completed_rules = {}
        #
        # for index in range(0, len(rule_list)):
        #     completed_rules[index] = 0
        #
        # for index in range(0, len(rule_list)):  # Calculate fitness of genes
        #     current_rule = rule_list[index]
        #     for gene in gene_list:
        #         for gene_index in range(0, len(gene)):
        #             if gene[gene_index] != current_rule[gene_index] and gene[gene_index] != 2:
        #                 break
        #             if gene_index == len(current_rule) - 1 and gene[gene_index] != 2:
        #                 completed_rules[index] += 1
        #                 fitness += 1
        #         total_fitness += fitness
        #         wild_card_total = 0
        #         fitness = 0
        #
        # if 0 not in completed_rules.values():
        #     print("Total fitness: %s" % total_fitness)
        #     print(completed_rules)
        #     print(gene_list)
        #     break

        #print(completed_rules)

        epoch += 1



