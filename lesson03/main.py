import directors
import movies

def init_director_collection(database):
    return directors.DirectorsCollection(database)

def init_movie_collection(database):
    return movies.MoviesCollection(database)

def add_director(director_collection, director_id, full_name):
    return director_collection.add_director(director_id, full_name)

def update_director(director_collection, director_id, full_name):
    return director_collection.update_director(director_id, full_name)

def search_director(director_collection, director_id):
    return director_collection.search_director(director_id)

def delete_director(director_collection, director_id):
    return director_collection.delete_director(director_id)

def add_movie(movie_collection, movie_id, director_id, movie_title):
    return movie_collection.add_movie(movie_id, director_id, movie_title)

def update_movie(movie_collection, movie_id, director_id, movie_title):
    return movie_collection.update_movie(movie_id, director_id, movie_title)

def search_movie(movie_collection, movie_id):
    return movie_collection.search_movie(movie_id)

def delete_movie(movie_collection, movie_id):
    return movie_collection.delete_movie(movie_id)