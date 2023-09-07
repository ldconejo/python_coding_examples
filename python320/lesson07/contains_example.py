from pymongo import MongoClient

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

def example():
    with mongo:
        database = mongo.connection.Sample_Database
        customer_collection = database['customers']

        record = {
            'status_id': 'ldconejo01',
            'status_text': 'Just a simple test'
        }

        customer_collection.insert_one(record)

        record = {
            'status_id': 'ldconejo02',
            'status_text': 'That food sampler was simply amazing'
        }

        customer_collection.insert_one(record)

        record = {
            'status_id': 'ldconejo03',
            'status_text': 'Well, that movie was not good all'
        }

        customer_collection.insert_one(record)

        keyword = input("Enter the search string: ")

        mongo_query = {'status_text': {'$regex':keyword}}
        results = customer_collection.find(mongo_query)

        for result in results:
            print(result)

        customer_collection.drop()

if __name__ == "__main__":
    example()