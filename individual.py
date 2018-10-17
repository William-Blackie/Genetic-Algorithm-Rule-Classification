import random


class Individual:
    genes = []
    fitness = None
    ID = None

    def __init__(self, ID):
        self.genes
        self.fitness
        self.ID = ID

    def __str__(self):
        return "ID: %s\nFitness:  %s\nGenes: %s" % (self.ID, self.fitness, self.genes)

    def CalcFitness(self):
        totalFitness = 0

        for value in self.genes:
            totalFitness += value
            self.fitness = totalFitness
        return totalFitness

    def CreateGenes(self, geneLength):
        tempGenes = []
        currentGene = 0


        while currentGene < geneLength:
            tempGenes.append(random.randint(0,1))
            currentGene += 1
        self.genes = tempGenes

    def setup_individual(self, genes, fitness):
        self.genes = genes
        self.fitness = fitness




