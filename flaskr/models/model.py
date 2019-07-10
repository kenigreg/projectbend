from config import config
from pyrebase import pyrebase


firebase = pyrebase.initialize_app(config)


db = firebase.database()

all_users = db.child("users").get()
