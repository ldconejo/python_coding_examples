import sys
from peewee import SqliteDatabase
import main

def add_director():
    director_id = input("Enter director ID: ")
    full_name = input("Enter director's full name: ")
    if main.add_director(director_collection, director_id, full_name):
        print(f"{full_name} added to director's table")
    else:
        print(f"There was an error adding {full_name} to director's database")

def update_director():
    director_id = input("Enter director ID: ")
    full_name = input("Enter updated director's full name: ")
    if main.update_director(director_collection, director_id, full_name):
        print(f"{director_id}'s information updated")
    else:
        print(f"There was an error modifying {director_id}")

def search_director():
    director_id = input("Enter director ID: ")
    result = main.search_director(director_collection, director_id)
    if result:
        print(f"Director ID: {result.director_id}")
        print(f"Director's name: {result.full_name}")
    else:
        print(f"No record found for {director_id}")

def delete_director():
    director_id = input("Enter director ID: ")   
    if main.delete_director(director_collection, director_id):
        print(f"{director_id} has been deleted")
    else:
        print(f"There was an error deleting {director_id}")

def add_movie():
    movie_id = input("Enter movie ID: ")
    director_id = input("Enter movie's director ID: ")
    movie_title = input("Enter movie title: ")
    if main.add_movie(movie_collection, movie_id, director_id, movie_title):
        print(f"{movie_title} added to the Movies table")
    else:
        print(f"There was an error adding {movie_title}")

def update_movie():
    movie_id = input("Enter movie ID: ")
    director_id = input("Enter movie's director ID: ")
    movie_title = input("Enter movie title: ")
    if main.update_movie(movie_collection, movie_id, director_id, movie_title):
        print(f"{movie_id} successfully updated")
    else:
        print(f"There was an error updating {movie_id}")

def search_movie():
    movie_id = input("Enter movie ID: ")
    result = main.search_movie(movie_collection, movie_id)
    if result:
        print(f"Movie ID: {result.movie_id}")
        print(f"Movie title: {result.movie_title}")
        print(f"Movie director: {result.director_id}")
    else:
        print(f"No results for {movie_id}")

def delete_movie():
    movie_id = input("Enter movie ID: ")
    if main.delete_movie(movie_collection, movie_id):
        print(f"{movie_id} was successfully deleted")
    else:
        print(f"There was an error deleting {movie_id}")

def quit_program():
    '''
    Quits program
    '''
    sys.exit()

if __name__ == '__main__':
    database = SqliteDatabase('database_model.db')
    database.connect()
    director_collection = main.init_director_collection(database)
    movie_collection = main.init_movie_collection(database)
    menu_options = {
        'A': add_director,
        'B': update_director,
        'C': search_director,
        'D': delete_director,
        'E': add_movie,
        'F': update_movie,
        'G': search_movie,
        'H': delete_movie,
        'Q': quit_program
    }
    while True:
        user_selection = input("""
                            A: Add director
                            B: Update director
                            C: Search director
                            D: Delete director
                            E: Add movie
                            F: Update movie
                            G: Search movie
                            H: Delete movie
                            Q: Quit

                            Please enter your choice: """)
        if user_selection.upper() in menu_options:
            menu_options[user_selection.upper()]()
        else:
            print("Invalid option")
