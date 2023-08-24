from sys import exit
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError, BulkWriteError

class MongoDBConnection():

    def __init__(self, host='127.0.0.1', port=27017):
        self.host = host
        self.port = port
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(self.host, self.port)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

def add_customer():
    name = input("Enter the customer's full name: ")
    customer_id = input("Enter the customer ID: ")

    new_customer = {
        'name': name,
        '_id': customer_id
    }

    try:
        customer_collection.insert_one(new_customer)
        print(f"Customer {name} has been added!")
    except DuplicateKeyError:
        print(f"ERROR: {customer_id} already exists!")

def list_customers():
    for customer in customer_collection.find():
        print(f"Customer ID: {customer['_id']} - Name: {customer['name']}")
    print("That's all customers!")

def update_customer():
    customer_id = input("Enter customer ID to modify: ")
    mongo_query = {"customer_id": customer_id}

    if customer_collection.count_documents(mongo_query) > 0:
        name = input('Enter customer full name: ')

        new_customer_data = {
            'name': name,
            '_id': customer_id
        }

        new_values = {"$set": new_customer_data}
        customer_collection.update_one(mongo_query, new_values)
        print(f"Customer {customer_id} updated")

def delete_customer():
    customer_id = input("Enter the customer ID to delete: ")
    mongo_query = {"_id": customer_id}
    customer_collection.delete_one(mongo_query)
    print(f"Customer {customer_id} deleted!")

def add_order():
    order_id = input("Enter order ID: ")
    customer_id = input('Enter customer ID: ')
    description = input('Describe the order: ')

    new_order = {
        '_id': order_id,
        'customer_id': customer_id,
        'description': description
    }

    order_collection.insert_one(new_order)
    print(f"Order {order_id} has been added!")

def list_orders():
    for order in order_collection.find():
        print(order)
    print("That's all orders")

def delete_order():
    order_id = input("Enter the order ID to delete: ")
    mongo_query = {"_id": order_id}
    order_collection.delete_one(mongo_query)
    print("Order deleted!!")

def find_false_orders():
    for order in order_collection.find():
        customer_id = order['customer_id']
        mongo_query = {"_id": customer_id}
        if not customer_collection.count_documents(mongo_query):
            print(f"Order {order['order_id']} corresponds to a non-existent user: {customer_id}")
    print("Search for false orders concluded")

def load_customer_list():
    filename = input('Enter the filename for the customer list: ')
    try:
        with open(filename) as file:
            list_of_customers = []
            for line in file:
                customer_id, name = line.strip('\n').split(',')
                new_entry = {
                    '_id': customer_id,
                    'name': name
                }
                list_of_customers.append(new_entry)
        customer_collection.insert_many(list_of_customers)
        print(f"All customers in {filename} have been added")
    except BulkWriteError:
        print(f"ERROR: Unable to add users from {filename}. Check for duplicates")
    except FileNotFoundError:
        print(f"ERROR: {filename} does not exist!")

def quit_program():
    drop = input("Drop database? [Y/N]: ")
    if drop.lower() == 'y':
        customer_collection.drop()
        order_collection.drop()
    exit()

if __name__ == "__main__":
    mongo = MongoDBConnection()
    with mongo:
        database = mongo.connection['FoodService']
        customer_collection = database['customers']
        order_collection = database['orders']

        menu_options = {
            'A': add_customer,
            'B': list_customers,
            'C': update_customer,
            'D': delete_customer,
            'E': add_order,
            'F': list_orders,
            'G': delete_order,
            'H': find_false_orders,
            'I': load_customer_list,
            'Q': quit_program
        }
        while True:
            user_selection = input("""
                                A: Add customer
                                B: List customers
                                C: Update customer
                                D: Delete customer
                                E: Add order
                                F: List orders
                                G: Delete order
                                H: Find false orders
                                I: Load customer list
                                Q: Quit
                                
                                Please enter your choice: """)
            if user_selection.upper() in menu_options:
                menu_options[user_selection.upper()]()
            else:
                print("Invalid option")
