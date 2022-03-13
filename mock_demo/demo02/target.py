import csv
from sys import argv

def display_user_data(filename):
    '''
    Gets a CSV file, validates the data in the file
    and prints it
    '''
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Check for empty values
                for value in list(row.values()):
                    if not value or value.isspace():
                        print(f"ERROR: Row with empty fields {row}")
                        return False
                print(row['name'], row['last_name'], row['position'])
        return True
    except FileNotFoundError:
        print("ERROR: File not found")
        return False
    except OSError:
        print("ERROR: OS error")
        return False

#if __name__ == "__main__":
#    display_user_data(argv[1])