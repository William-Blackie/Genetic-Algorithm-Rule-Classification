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

        for temp_list in all_file_data:
            if temp_list[len(temp_list) - 1] == '1' and temp_list not in unique_file_data:  # and temp_list not in unique_file_data:
                unique_file_data.append(temp_list)  # Rule stored as string TODO maybe needed to think about something else

        print("Rules: %s" % (unique_file_data))
        return unique_file_data



