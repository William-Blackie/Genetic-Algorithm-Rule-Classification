

class dataUtils():

    def read_from_file(self):
        unique_file_data = {}
        all_file_data = []
        file = open('/home/will/PycharmProjects/untitled/data/data1.tx', 'r')
        file.readline() # Remove header
        for line in file:
            line = line.strip() # Remove new line character
            all_file_data.append(line)
        file.close()

        rule = ""
        member = 0

        for x in all_file_data:
            temp_list = x
            if temp_list[0:4] not in unique_file_data:
                unique_file_data[temp_list[0:4]] = int(temp_list[6])  # Rule stored as string TODO maybe needed to think about something else
            else:
                print("element: %s already found" % (temp_list[0:4]))
        counter = 0
        for k, v in unique_file_data.items():
            if v == 1:
                print("Rule: %s Value: %s" % (k, v))
                counter += 1
        print(counter)

        print(unique_file_data)  # TODO remove this
        return unique_file_data



