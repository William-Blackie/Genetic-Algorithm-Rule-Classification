import csv
import os

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

    def write_to_csv(self, file_path, list):
        with open(file_path, 'w') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=',',
                       quotechar=',', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(['Average fitness', 'Epoch'])
            for x in list:
                csv_writer.writerow([x[0], x[1]])


    def copy_write_to_csv(self, file_path, list):
        if os.stat(file_path).st_size != 0:
            with open(file_path, newline='') as csvfile:
                row_number = 0
                csv_reader = csv.reader(csvfile, delimiter=',', quotechar=',')
                for row in csv_reader:
                    temp_list = []
                    if row_number != 0:
                        temp_list = [float(row[0]), int(row[1])]
                        list.append(temp_list)
                    row_number += 1
            self.write_to_csv(file_path, list)
        else:
            self.write_to_csv(file_path, list)



