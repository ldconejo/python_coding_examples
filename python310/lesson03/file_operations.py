def process_csv_file(filename="random_facts.csv"):
    file = open(filename)
    lines_in_csv = file.readlines()

    for line in lines_in_csv:
        # Remove carriage return
        line = line.strip()

        # Separate the CSV line into its two columns
        # NOTE: This can be simpler by using the csv module in Python
        columns = line.split(",")
        #print(line)
        #print(columns)
        #print(f"Fact ID: {columns[0]}")
        #print(f"Description: {columns[1]}")
        #print("*"*20)

    return lines_in_csv
              
def make_it_all_caps(list_of_lines):
    # This one will keep the capitalized lines
    new_list = []

    for line in list_of_lines:
        new_list.append(line.upper().strip())

    return new_list

def save_new_file(list_of_lines, filename="output.csv"):
    target_file = open(filename, "w")

    # One way of doing it
    #for line in list_of_lines:
    #    target_file.write(line)

    # A quicker way:
    target_file.writelines(list_of_lines)

def save_new_file_adding_carriage_returns(list_of_lines, filename="output.csv"):
    target_file = open(filename, "a")
    # Add the carriage return back and save it to a file
    for line in list_of_lines:
        new_line = line + "\n"
        target_file.write(new_line)
    target_file.close()

def save_new_file_with_context_manager(list_of_lines, filename="output.csv"):
    with open(filename, "w") as target_file:
        for line in list_of_lines:
            new_line = line + "\n"
            target_file.write(new_line)

if __name__ == "__main__":
    list_of_lines = process_csv_file()
    list_of_lines = make_it_all_caps(list_of_lines)
    #save_new_file(list_of_lines)
    #save_new_file_adding_carriage_returns(list_of_lines)
    save_new_file_with_context_manager(list_of_lines)