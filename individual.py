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

    def data_classification_fitness(self, rule_list, rule_classifiers):
        genes = self.genes
        gene_list = []
        temp_temp_gene_list =[]
        gene_classifier = []
        temp_gene_list = []
        fitness = 0

        gene_index = 0
        for gene in range(0, len(genes)):  # Section genes based on length of rules
            if gene_index < len(rule_list[0]):
                temp_gene_list.append(genes[gene])
                gene_index += 1
            else:
                gene_index == len(rule_list[0])
                gene_classifier.append(genes[gene])
                temp_temp_gene_list.append(temp_gene_list)
                temp_gene_list = []
                gene_index = 0

        for rule_index in range(0, len(rule_list)):  # Calculate fitness of genes
            current_rule = rule_list[rule_index]
            for gene_index in range(0, len(temp_temp_gene_list)):
                current_gene = temp_temp_gene_list[gene_index]
                if self.match_cond(current_rule, current_gene):
                    if rule_classifiers[rule_index] == gene_classifier[gene_index]:
                        fitness += 1
                    break
        self.fitness = fitness
        return fitness

    @staticmethod
    def match_cond(current_rule, current_gene):
        for x in range(0, len(current_rule)):
            if current_rule[x] != current_gene[x] and current_gene[x] != 2:
                return False

        return True

    def create_genes(self, gene_length):
        temp_genes = []
        current_gene = 0

        while current_gene < gene_length:
            temp_genes.append(random.randint(0, 2))
            current_gene += 1
        self.genes = temp_genes

    def setup_individual(self, genes, fitness):
        self.genes = genes
        self.fitness = fitness
