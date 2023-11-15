def remove_duplicates(target_list):
    new_list = []

    for number in sample_list:
        if number not in new_list:
            new_list.append(number)
    return new_list

if __name__ == "__main__":
    sample_list = [1,3,2,43,5,3,2,1,34,23,32,23,23,43,34]
    #result_list = remove_duplicates(sample_list)
    result_list = list(set(sample_list))
    print(result_list)
    sample_list[0] = 99
    print(sample_list)