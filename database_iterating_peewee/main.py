'''
ldconejo - Demonstrates searching a SQL database table,
by querying the table and by treating it as an iterable.
'''
import sys
from peewee import SqliteDatabase, IntegrityError, DoesNotExist, Model, CharField

database = SqliteDatabase('test.db')
database.connect()
database.pragma('foreign_keys', 1, permanent=True)

class BaseModel(Model):
    """
        BaseModel class
    """
    class Meta:
        """
            Meta class
        """
        database = database

class UsersTable(BaseModel):
    """
        Table for user accounts.
    """
    user_id = CharField(primary_key=True, max_length=30)
    user_name = CharField(max_length=30)
    user_last_name = CharField(max_length=100)
    user_email = CharField(max_length=100)

database.create_tables([
        UsersTable,
    ])

database.close()

def add_user(user_id, user_email, user_name, user_last_name):
    '''
    Adds a new user to the collection
    '''
    with database.transaction():
        try:
            new_user = UsersTable.create(
                user_id=user_id,
                user_name=user_name,
                user_last_name=user_last_name,
                user_email=user_email
            )
            new_user.save()
            return True
        except IntegrityError:
            return False

def add_user_ui():
    '''
    Adds a new user into the database
    '''
    user_id = input('User ID: ')
    email = input('User email: ')
    user_name = input('User name: ')
    user_last_name = input('User last name: ')
    if not add_user(user_id, email, user_name, user_last_name):
        print("An error occurred while trying to add new user")
    else:
        print("User was successfully added")

def search_user_iterable_ui():
    '''
    Searches a user in the database
    '''
    user_id = input('Enter user ID to search: ')
    result = search_user_iterable(user_id)
    if not result:
        print("ERROR: User does not exist")
    else:
        print(f"User ID: {result.user_id}")
        print(f"Email: {result.user_email}")
        print(f"Name: {result.user_name}")
        print(f"Last name: {result.user_last_name}")

def search_user_ui():
    '''
    Searches a user in the database
    '''
    user_id = input('Enter user ID to search: ')
    result = search_user_iterable(user_id)
    if not result:
        print("ERROR: User does not exist")
    else:
        print(f"User ID: {result.user_id}")
        print(f"Email: {result.user_email}")
        print(f"Name: {result.user_name}")
        print(f"Last name: {result.user_last_name}")

def search_user(user_id):
    '''
    Searches for user data
    '''
    with database.transaction():
        try:
            target = UsersTable.get(UsersTable.user_id == user_id)
        except DoesNotExist:
            target = None
        return target

def search_user_iterable(user_id):
    '''
    Searches for user data, treating the
    SQLite table as an iterable (which I thought should not work
    but then stood correct by one of our students, thank you Hwai-Jiang Jong!)
    Note that this is highlighted as an error by Pylint, but it works
    E1135: Value 'UsersTable' doesn't support membership test (unsupported-membership-test)
    '''
    if user_id in UsersTable:
        target = UsersTable.get(UsersTable.user_id == user_id)
    else:
        target = None
    return target

def quit_program():
    '''
    Quits program
    '''
    sys.exit()

if __name__ == "__main__":
    menu_options = {
        'A': add_user_ui,
        'B': search_user_ui,
        'C': search_user_iterable_ui,
        'Q': quit_program
    }
    while True:
        user_selection = input("""
                            A: Add user
                            B: Search user
                            C: Search iterable
                            Q: Quit

                            Please enter your choice: """)
        if user_selection.upper() in menu_options:
            menu_options[user_selection.upper()]()
        else:
            print("Invalid option")
