import decimal
import random
import individual
import copy


class PopulationUtils:

    def __init__(self):  # TODO maybe make this so main sets this.
        self.mutation_rate = 0.99
        self.crossover_rate = 0.3
        self.elite_population_number = 2

    @staticmethod
    def create_population(new_population, population_number, gene_number, rule_list, rule_classifiers, numRules):
        id_number = 0
        current_fitness = 0

        while id_number < population_number:
            new_individual = individual.Individual(id_number)
            new_individual.create_genes(gene_number, numRules)
            current_fitness += new_individual.data_classification_fitness(rule_list, rule_classifiers)
            new_population.append(new_individual)
            id_number += 1

        return current_fitness, new_population

    @staticmethod
    def tournament_selection(first_parent, second_parent, temp_individual):
        if first_parent.fitness >= second_parent.fitness:
            temp_genes = first_parent.genes
            temp_fitness = first_parent.fitness
            temp_individual.setup_individual(temp_genes, temp_fitness)
        else:
            temp_genes = second_parent.genes
            temp_fitness = second_parent.fitness
            temp_individual.setup_individual(temp_genes, temp_fitness)

        return temp_individual

    def high_fitness_evaluation(self, population, rules, rule_classifiers):
        new_pop = []
        new_fitness = 0
        id_number = 0
        elite_population = []

        population.sort(key=lambda x: x.fitness, reverse=True)  # Sort and save best fitness from last pop

        index = self.elite_population_number

        while index >= 0:
            elite_population.append(copy.deepcopy(population[index]))
            index -= 1

        while id_number < len(population):  # Tournament select new pop
            temp_individual = individual.Individual(id_number)
            temp_individual = self.tournament_selection(copy.deepcopy(population[random.randint(0, len(population) - 1)]),
                                                        copy.deepcopy(population[random.randint(0, len(population) - 1)]),
                                                        temp_individual)
            new_pop.append(temp_individual)
            id_number += 1

        id_number = 0

        while id_number < (len(population) - 1):  # Crossover and mutation
            temp_individual = copy.deepcopy(new_pop[id_number])
            temp_individual = self.single_point_mutation(temp_individual)
            temp_individual = self.single_point_crossover(temp_individual, new_pop[id_number + 1])
            new_pop[id_number] = copy.deepcopy(temp_individual)
            id_number += 1

        # Elite individuals added
        new_pop.sort(key=lambda x: x.fitness, reverse=True)

        for elite in elite_population:  # Remove least fit individuals
            new_pop.pop()

        for elite in elite_population:
            new_pop.append(copy.deepcopy(elite))  # Append fittest individuals from old pop

        for pop in new_pop:
            new_fitness += pop.data_classification_fitness(rules, rule_classifiers)  # Calculate fitness

        new_pop.sort(key=lambda x: x.fitness, reverse=True)

        return new_pop, new_fitness

    @staticmethod
    def roulette_selection(population):
        total_fitness = sum([f.fitness for f in population])
        pick = random.uniform(0, total_fitness)

        current = 0
        for pop in population:
            current += pop.fitness
            if current > pick:
                return pop

    def single_point_crossover(self, first_parent, second_parent):
        slice_start = 0
        slice_end = 0

        if random.uniform(0, 1) >= self.crossover_rate:
            while slice_start >= slice_end:
                slice_start = random.randint(0, len(first_parent.genes) - 1)
                slice_end = random.randint(0, len(first_parent.genes) - 1)  # TODO get value from main

            # Slice and insert the new genes into parent
            for index in range(slice_start, slice_end):  # TODO make more pythonic fix naming conventions
                first_parent.genes[index] = second_parent.genes[index]
        return first_parent

    def single_point_mutation(self, individual):  # TODO change name?
        for gene in range(len(individual.genes)):
            for gene_index in range(len(individual.genes[0])):
                mutation_chance = random.uniform(0, 1)
                if mutation_chance > self.mutation_rate:
                    if gene_index == 14:
                        individual.genes[gene][gene_index] = random.randint(0, 1)
                    else:
                        individual.genes[gene][gene_index] += random.uniform(-0.2, 0.2)
                        if individual.genes[gene][gene_index] > 1:
                            individual.genes[gene][gene_index] = 1.0
                        if individual.genes[gene][gene_index] < 0:
                            individual.genes[gene][gene_index] = 0.0
        return individual
