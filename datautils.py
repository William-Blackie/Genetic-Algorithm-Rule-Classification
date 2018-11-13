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

        genes, classifiers = self.convert_string_to_genes_list(all_file_data)
        return genes, classifiers

    @staticmethod
    def convert_string_to_genes_list(all_file_data):
        final_rules = []
        rule = []
        rule_classifier = []
        index = 0
        for string in all_file_data:
            for x in string:
                if index < len(string) - 1:
                    index += 1
                    rule.append(int(x))
                else:
                    rule_classifier.append(int(x))
                    index = 0
            final_rules.append(rule)
            rule = []

        return final_rules, rule_classifier



