from database_model import MoviesTable
from peewee import IntegrityError, DoesNotExist

class MoviesCollection():
    '''
    Contains a collection of Users objects
    '''
    def __init__(self, database):
        self.database = database

    def add_movie(self, movie_id, director_id, movie_title):
        with self.database.transaction():
            try:
                new_movie = MoviesTable.create(
                    movie_id = movie_id,
                    director_id = director_id,
                    movie_title = movie_title
                )
                new_movie.save()
                return True
            except IntegrityError:
                return False

    def update_movie(self, movie_id, director_id, movie_title):
        with self.database.transaction():
            try:
                modify_target = MoviesTable.get(MoviesTable.movie_id == movie_id)
                modify_target.director_id = director_id
                modify_target.movie_title = movie_title
                modify_target.save()
                return True
            except DoesNotExist:
                return False

    def delete_movie(self, movie_id):
        '''
        Deletes an existing user
        '''
        with self.database.transaction():
            try:
                delete_target = MoviesTable.get(MoviesTable.movie_id == movie_id)
                delete_target.delete_instance()
                return True
            except DoesNotExist:
                return False

    def search_movie(self, movie_id):
        '''
        Searches for user data
        '''
        with self.database.transaction():
            try:
                target = MoviesTable.get(MoviesTable.movie_id == movie_id)
            except DoesNotExist:
                target = None
            return target