from model import db, SavedTotal

db.connect()
db.create_tables([SavedTotal])