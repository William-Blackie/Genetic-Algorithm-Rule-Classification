import decimal
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
        fitness = 0

        for rule_index in range(0, len(rule_list)):  # Calculate fitness of genes
            current_rule = rule_list[rule_index]
            for gene_index in range(len(genes)):
                current_gene = genes[gene_index]
                if self.match_cond(current_rule, current_gene):
                    if float(rule_classifiers[rule_index]) == float(current_gene[14]):
                        fitness += 1
                    break
        self.fitness = fitness
        return fitness

    @staticmethod
    def match_cond(current_rule, current_gene):
        gene_index = 0
        for x in range(0, len(current_rule)):
            gene1 = current_gene[gene_index]
            gene2 = current_gene[gene_index + 1]
            rule = current_rule[x]
            if gene1 >= rule or rule >= gene2:
                return False
            gene_index + 2
        return True

    def create_genes(self, gene_length, num_rules):
        temp_genes = []
        current_gene = 0
        full_genes = []
        for x in range(num_rules):
            while current_gene < gene_length:
                temp1 = 0
                temp2 = 0
                while temp1 >= temp2:
                    temp1 = float(decimal.Decimal(random.randrange(100000, 900000)) / 1000000)
                    temp2 = float(decimal.Decimal(random.randrange(100000, 900000)) / 1000000)

                temp_genes.append(temp1)
                temp_genes.append(temp2)
                current_gene += 2

            current_gene = 0
            temp_genes.append(random.randint(0, 1))
            full_genes.append(temp_genes)
            temp_genes = []
        self.genes = full_genes

    def setup_individual(self, genes, fitness):
        self.genes = genes
        self.fitness = fitness
