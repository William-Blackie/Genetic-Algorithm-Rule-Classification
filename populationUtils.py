import random
import individual


class PopulationUtils:

    @staticmethod
    def create_population(new_population, population_number, gene_number):
        id = 0
        current_fitness = 0

        while id < population_number:
            new_individual = individual.Individual(id)
            new_individual.CreateGenes(gene_number)
            current_fitness += new_individual.CalcFitness()
            new_population.append(new_individual)
            id += 1

        return current_fitness, new_population

    def evaluate_population(self, old_population):
        ID = 0
        new_fitness = 0
        new_population = []

        while ID < 50:
            selector = random.randint(0, 2)
            
            first_parent = old_population[random.randint(0, 49)]
            second_parent = old_population[random.randint(0, 49)]
            temp_individual = individual.Individual(ID)

            temp_individual = self.generic_evaluation(first_parent, second_parent, temp_individual)
            temp_individual = self.single_bit_corssover(temp_individual)
            temp_individual = self.single_point_mutation(temp_individual)

            new_fitness += temp_individual.CalcFitness()
            new_population.append(temp_individual)
            ID += 1

        # if old_fitness > new_fitness: #Recursively call until new population is more fit than the old
        #     new_population = self.evaluate_population(old_fitness, old_population)
        return new_population, new_fitness


    @staticmethod
    def generic_evaluation(first_parent, second_parent, temp_individual):
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

        population.sort(key=lambda x: x.genes, reverse=True)
        index = 0

        while index < 50:
            iterator = 0.2 * len(population)
            while iterator > 0:
                if len(new_pop) >= len(population): #Prevent over population
                    break
                temp_individual = individual.Individual(index)

                if random.randint(0, 100) > 90:
                    temp_individual = self.single_point_crossover(temp_individual, population[index + 1])
                    print("corssover")
                elif random.randint(0, 100) > 70:
                    temp_individual = self.single_point_mutation(temp_individual)
                    print("mutation")
                else:
                    temp_individual = self.generic_evaluation(population[index], population[index + 1], temp_individual)

                index += 1
                iterator -= 1

                new_fitness += temp_individual.CalcFitness()
                new_pop.append(temp_individual)
        index = 0
        return new_pop, new_fitness



    @staticmethod
    def find_individual( population, id):
        for pop in population:
            if pop.ID == id:
                return pop

    @staticmethod
    def single_point_crossover(first_parent, second_parent):
        slice_start = random.randint(0, 25)
        slice_end = random.randint(26, 50)
        # Slice and insert the new genes into parent
        for i in range(slice_start, slice_end):
            first_parent.genes[i] = second_parent.genes[i]

        return first_parent

    @staticmethod
    def single_bit_corssover(first_parent):
        gene_index = random.randint(0, 49)
        print(gene_index)
        if first_parent.genes[gene_index] == 1:
            first_parent.genes[gene_index] = 0
        else:
            first_parent.genes[gene_index] = 1

        return first_parent

    @staticmethod
    def single_point_mutation(individual):
        index = random.randint(0, 49)
        print(index)

        if individual.genes[index] == 1:
            individual.genes[index] = 0
        else:
            individual.genes[index] = 1

        return individual






