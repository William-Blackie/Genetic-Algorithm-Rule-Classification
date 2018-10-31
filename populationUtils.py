import random
import individual
import copy


class PopulationUtils:

    # Population rates
    mutation_rate = 0.99
    crossover_rate = 0.30


    @staticmethod
    def create_population(new_population, population_number, gene_number):
        id = 0
        current_fitness = 0

        while id < population_number:
            new_individual = individual.Individual(id)
            new_individual.create_genes(gene_number)
            current_fitness += new_individual.calculate_fitness()
            new_population.append(new_individual)
            id += 1

        return current_fitness, new_population

    def evaluate_population(self, old_population):
        ID = 0
        new_fitness = 0
        new_population = []

        while ID < 50:
            
            first_parent = old_population[random.randint(0, 49)]
            second_parent = old_population[random.randint(0, 49)]
            temp_individual = individual.Individual(ID)

            temp_individual = self.tournament_selection(first_parent, second_parent, temp_individual)

            temp_individual = self.single_bit_corssover(temp_individual)
            temp_individual = self.single_point_mutation(temp_individual)

            new_fitness += temp_individual.calculate_fitness()
            new_population.append(temp_individual)
            ID += 1

        return new_population, new_fitness


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

    def high_fitness_evaluation(self, population):
        new_pop = []
        new_fitness = 0
        id_number = 0

        population.sort(key=lambda x: x.fitness, reverse=True)  # Sort and save best fitness from last pop
        best_individual = population[0]

        while id_number < len(population):  # Tournament select new pop
            temp_individual = individual.Individual(id_number)
            temp_individual = self.tournament_selection(copy.deepcopy(population[random.randint(0, 49)]), copy.deepcopy(population[random.randint(0, 49)]), temp_individual)
            new_pop.append(temp_individual)
            id_number += 1

        id_number = 0

        while id_number < (len(population) - 1):  # Crossover and mutation
            temp_individual = copy.deepcopy(new_pop[id_number])
            temp_individual = self.single_point_mutation(temp_individual)
            temp_individual = self.single_point_crossover(temp_individual, new_pop[id_number + 1])

            new_fitness += temp_individual.calculate_fitness()
            new_pop[id_number] = temp_individual
            id_number += 1

        #population.sort(key=lambda x: x.fitness, reverse=True)
        new_pop.sort(key=lambda x: x.fitness, reverse=True)
        new_pop.pop(49)
        new_pop.append(best_individual)
        #new_pop[49] = best_individual  # Swap best candidate from last gen for worst of new.
        new_pop.sort(key=lambda x: x.fitness, reverse=True)
        new_fitness += best_individual.calculate_fitness()
        return new_pop, new_fitness

    @staticmethod
    def roulete_selection(population):
        total_fitness = sum([f.fitness for f in population])
        pick = random.uniform(0, total_fitness)

        current = 0
        for pop in population:
            current += pop.fitness
            if current > pick:
                return pop

    @staticmethod
    def single_point_crossover(first_parent, second_parent):
        slice_start = 0
        slice_end = 0

        while slice_start >= slice_end:
            slice_start = random.randint(0, 49)
            slice_end = random.randint(0, 49)

        # Slice and insert the new genes into parent
        for index in range(slice_start, slice_end):  # TODO make more pythonic fix naming conventions
            first_parent.genes[index] = second_parent.genes[index]
        return first_parent

    @staticmethod
    def single_point_mutation(individual):
        index = 0

        while index < len(individual.genes):  # Mutate at each gene
            mutation_chance = random.uniform(0, 1)

            if mutation_chance > 0.99:
                if individual.genes[index] == 1:
                    individual.genes[index] = 0
                else:
                    individual.genes[index] = 1
            index += 1
        return individual






