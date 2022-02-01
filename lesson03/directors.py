from database_model import DirectorsTable
from peewee import IntegrityError, DoesNotExist

class DirectorsCollection():
    '''
    Contains a collection of Users objects
    '''
    def __init__(self, database):
        self.database = database

    def add_director(self, director_id, full_name):
        with self.database.transaction():
            try:
                new_director = DirectorsTable.create(
                    director_id = director_id,
                    full_name = full_name
                )
                new_director.save()
                return True
            except IntegrityError:
                return False

    def update_director(self, director_id, full_name):
        with self.database.transaction():
            try:
                modify_target = DirectorsTable.get(DirectorsTable.director_id == director_id)
                modify_target.full_name = full_name
                modify_target.save()
                return True
            except DoesNotExist:
                return False

    def delete_director(self, director_id):
        '''
        Deletes an existing user
        '''
        with self.database.transaction():
            try:
                delete_target = DirectorsTable.get(DirectorsTable.director_id == director_id)
                delete_target.delete_instance()
                return True
            except DoesNotExist:
                return False

    def search_director(self, director_id):
        '''
        Searches for user data
        '''
        with self.database.transaction():
            try:
                target = DirectorsTable.get(DirectorsTable.director_id == director_id)
            except DoesNotExist:
                target = None
            return target