import csv 

def interact_with_user():
    '''
    Implements a simple user interface (UI)
    '''
    print("Welcome to the Invoice Saver!!!")
    filename = input('Enter a filename: ')
    more_items = 'y'
    item_list = []

    while True:
        item_name = input('Enter an item: ')
        item_price = input('Enter a price: ')
        new_item = {
            'item_name': item_name,
            'item_price': item_price
        }
        item_list.append(new_item)
        while True:
            more_items = input('Add more items? ')
            if more_items.lower() in ('y', 'yes', 'yup', 'yeah', 'n', 'no', 'nah'):
                break
        if more_items.lower() in ('n', 'no', 'nah'):
            break
    return filename, item_list

def save_file(filename, item_list):
    '''
    Saves the data to a file
    '''
    with open(filename, mode='w') as csvfile:
        file_writer = csv.DictWriter(csvfile, fieldnames=['item_name', 'item_price'])
        file_writer.writeheader()
        for invoice_item in item_list:
            file_writer.writerow(invoice_item)
    return True

if __name__ == '__main__':
    filename, item_list = interact_with_user()
    save_file(filename, item_list)