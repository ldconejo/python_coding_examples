import sys
from pymongo import MongoClient

class MongoDBConnection():
    '''MongoDB Connection'''

    def __init__(self, host='127.0.0.1', port=27017):
        """ be sure to use the ip address not name for local windows"""
        self.host = host
        self.port = port
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(self.host, self.port)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

def add_customer():
    name = input('Enter the customer full name: ')
    customer_id = input('Enter the customer ID: ')

    new_customer = {
        'name': name,
        'customer_id': customer_id
    }

    customer_collection.insert_one(new_customer)
    print(f"Customer {name} has been added!")

def list_customers():
    for customer in customer_collection.find():
        print(customer)
    print("That's all the customers")

def update_customer():
    customer_id = input("Enter the customer ID to modify: ") 
    mongo_query = {"customer_id": customer_id}
    if customer_collection.count_documents(mongo_query) > 0:
        name = input('Enter the customer full name: ')

        new_customer_data = {
            'name': name,
            'customer_id': customer_id
        }        

        new_values = {"$set": new_customer_data}
        customer_collection.update_one(mongo_query, new_values)
        print("Customer updated")

def delete_customer():
    customer_id = input("Enter the customer ID to delete: ")   
    mongo_query = {"customer_id": customer_id} 
    customer_collection.delete_one(mongo_query)
    print("Customer deleted!")

def add_order():
    order_id = input('Enter order ID: ')
    customer_id = input('Enter the customer ID: ')
    description = input('Describe the order: ')

    new_order = {
        'order_id': order_id,
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
    mongo_query = {"order_id": order_id} 
    order_collection.delete_one(mongo_query)
    print("Order deleted!")

def find_false_orders():
    for order in order_collection.find():
        customer_id = order['customer_id']
        mongo_query = {"customer_id": customer_id}
        if not customer_collection.count_documents(mongo_query):
            print(f"Order {order['order_id']} corresponds to a non-existent user {customer_id}!")
    print("Search for false orders concluded")

def quit_program():
    drop = input("Drop database? [Y/N]: ")
    if drop.lower() == 'y':
        customer_collection.drop()
        order_collection.drop()
    sys.exit()

if __name__ == "__main__":
    mongo = MongoDBConnection()
    with mongo:
        database = mongo.connection.FoodService
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
                                Q: Quit

                                Please enter your choice: """)
            if user_selection.upper() in menu_options:
                menu_options[user_selection.upper()]()
            else:
                print("Invalid option")