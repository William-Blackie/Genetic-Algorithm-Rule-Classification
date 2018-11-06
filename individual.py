import random


class Individual:
    genes = []
    fitness = None
    ID = None

    def __init__(self, id):
        self.ID = id

    def __str__(self):
        return "ID: %s Fitness:  %s Genes: %s" % (self.ID, self.fitness, self.genes)

    def calculate_fitness(self):
        total_fitness = 0

        for value in self.genes:
            total_fitness += value

        self.fitness = total_fitness
        return total_fitness

    def data_classification_fitness(self, rule_list):
        genes = self.genes
        gene_list = []
        temp_gene_list = []
        fitness = 0
        total_fitness = 0

        for gene in genes:
            temp_gene_list.append(gene)
            if len(temp_gene_list) == len(rule_list[0]):
                gene_list.append(temp_gene_list)
                temp_gene_list = []

        for index in range(0, len(rule_list)):  # TODO this is trashed
            current_rule = rule_list[index]
            for gene in gene_list:
                for gene_index in range(0, len(gene)):
                    if gene[gene_index] != current_rule[gene_index] or gene[gene_index] == 2:
                        break
                    if gene_index == len(current_rule) - 1:
                        fitness += 1
                total_fitness += fitness
                fitness = 0

        if total_fitness == 10:
            print("foob")

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
