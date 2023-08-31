import csv
import time
from pymongo import MongoClient

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        total_time = (te - ts)*1000
        print(f"Total time for {method.__name__} was {total_time:.2f} ms")

        return result
    return timed

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

mongo = MongoDBConnection()

@timeit
def example_one():
    with mongo:
        database = mongo.connection.Sample_Database
        customer_collection = database['customers']

        with open("accounts.csv", "r") as file:
            reader = csv.DictReader(file)
            dict_of_customers = list(reader)

        for record in dict_of_customers:
            customer_collection.insert_one(record)
        customer_collection.drop()

@timeit
def example_two():
    with mongo:
        database = mongo.connection.Sample_Database
        customer_collection = database['customers']

        with open("accounts.csv", "r") as file:
            reader = csv.DictReader(file)
            dict_of_customers = list(reader)

        customer_collection.insert_many(dict_of_customers)
        customer_collection.drop()

@timeit
def example_three():
    with open("accounts.csv", "r") as file:
        reader = csv.DictReader(file)
        dict_of_customers = list(reader)

        for record in dict_of_customers:
            with mongo:
                database = mongo.connection.Sample_Database
                customer_collection = database['customers']
                customer_collection.insert_one(record)
        with mongo:
            database = mongo.connection.Sample_Database
            customer_collection = database['customers']
            customer_collection.drop()

if __name__ == "__main__":
    example_two()
    example_one()
    example_three()