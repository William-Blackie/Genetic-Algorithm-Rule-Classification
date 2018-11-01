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

    def data_classification_fitness(self):
        genes = self.genes
        rule_length = 4
        counter = 0
        gene_list = []

        for x in genes:
            counter += 1
            gene = x
            if counter == rule_length:
                gene_list.append(str(gene))
                counter = 0

        total_fitness = 0

        for gene in gene_list:
            if gene == "0011":
                total_fitness += 1
            elif gene == "0101":
                total_fitness += 1
            elif gene == "0110":
                total_fitness += 1
            elif gene == "1001":
                total_fitness += 1
            elif gene == "1010":
                total_fitness += 1
            elif gene == "1100":
                total_fitness += 1
            elif gene == "1111":
                total_fitness += 1

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




