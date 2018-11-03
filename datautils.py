class dataUtils():

    def read_from_file(self, path):
        unique_file_data = []
        all_file_data = []
        file = open(path, 'r')
        file.readline()  # Remove header
        for line in file:
            line = line.strip()  # Remove new line character
            line = line.replace(" ", "")
            all_file_data.append(line)
        file.close()

        print("Rules: %s" % (all_file_data))
        return all_file_data



