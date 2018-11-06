class dataUtils():

    def read_from_file(self, path):
        all_file_data = []
        file = open(path, 'r')
        file.readline()  # Remove header
        for line in file:
            line = line.strip()  # Remove new line character
            line = line.replace(" ", "")
            all_file_data.append(line)
        file.close()

        final_genes = self.convert_string_to_genes_list(all_file_data)
        return final_genes

    @staticmethod
    def convert_string_to_genes_list(all_file_data):
        final_genes = []
        gene = []
        for string in all_file_data:
            for x in string:
                gene.append(int(x))
            final_genes.append(gene)
            gene = []

        return final_genes



