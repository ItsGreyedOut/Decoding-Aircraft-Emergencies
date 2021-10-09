# connection to Heroku
from airplane_emergencies.app import db

#db.drop_all()
db.create_all()