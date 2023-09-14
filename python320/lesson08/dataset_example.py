from playhouse.dataset import DataSet

ds = DataSet('sqlite:///socialnetwork.db')

Users = ds["UsersTable"]

Users.insert(user_id='test')
Users.create_index(['user_id'], unique=True)