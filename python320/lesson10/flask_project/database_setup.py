from playhouse.dataset import DataSet

db = DataSet('sqlite:///chinook.db')

def create_tables(database):
    users = database["employees"]
    users.insert(EmployeeId='tmosby', FullName='Theodore Evelyn Mosby')
    users.insert(EmployeeId='bstinson', FullName='Barney Stinson')
    users.insert(EmployeeId='rscherbatsky', FullName='Robin Charles Scherbatsky, Jr.')
    users.insert(EmployeeId='laldrin', FullName='Lily Aldrin')
    users.insert(EmployeeId='meriksen', FullName='Marshall Eriksen')

    tracks = database["tracks"]
    tracks.insert(trackid='track01', name='Superdate', composer='Josh Radnor', unitprice='1.40')
    tracks.insert(trackid='track02', name="That Guy's Awesome", composer='Neil Patrick Harris', unitprice='2.00')
    tracks.insert(trackid='track03', name='Sandcastles in the Sand', composer='Cobie Smulders', unitprice='1.50')
    tracks.insert(trackid='track04', name='Marshal versus the Machines', composer='Jason Segel', unitprice='1.20')

if __name__ == "__main__":
    create_tables(db)