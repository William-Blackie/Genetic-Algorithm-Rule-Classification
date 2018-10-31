import random


class Individual:
    genes = []
    fitness = None
    ID = None

    def __init__(self, id):
        self.genes
        self.fitness
        self.ID = id

    def __str__(self):
        return "ID: %s Fitness:  %s Genes: %s" % (self.ID, self.fitness, self.genes)

    def calculate_fitness(self):
        total_fitness = 0

        for value in self.genes:
            total_fitness += value

        self.fitness = total_fitness
        return total_fitness

    def create_genes(self, gene_length):
        temp_genes = []
        current_gene = 0

        while current_gene < gene_length:
            temp_genes.append(random.randint(0, 1))
            current_gene += 1
        self.genes = temp_genes

    def setup_individual(self, genes, fitness):
        self.genes = genes
        self.fitness = fitness




