def open_text_file():
    try:
        with open('no_file.txt') as data_file:
            contents = data_file.readlines()
            for line in contents:
                number_as_integer = int(line.strip())
                try:
                    result = (number_as_integer) / (number_as_integer - 523)
                    print(result)
                except ZeroDivisionError:
                    pass
    except (FileNotFoundError, 
            ValueError, TimeoutError):
        print("ERROR: Target file not found or data file corrupted")
    except Exception as exception_details:
        print(f"ERROR: {exception_details}")
        print("Notify Luis Conejo at IT Support right away!!!")
    else:
        print("Congratulations! Your code didn't trigger an exception!")
    finally:
        print("INFO: File processing concluded")

def validate_data_file(target="no_file.txt"):
    with open(target) as file:
        all_lines = file.readlines()
        for line in all_lines:
            if "523" in line:
                raise ValueError("523 found in data file!")
            print("End of the line!")
                
    
if __name__ == "__main__":
    #open_text_file()
    try:
        validate_data_file()
    except Exception as exception_details:
        print(f"ERROR: {exception_details}")
    print("End of code execution")