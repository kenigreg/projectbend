from config import config
from pyrebase import pyrebase
from flask import request, jsonify


firebase = pyrebase.initialize_app(config)
db = firebase.database()

# GET all Users
all_users = db.child("users").get()

# GET all Channels
all_channels = db.child("channels").get()

# GET a User


def fetch_user(username):
    user_info = db.child("users/" + username).get()
    return user_info.val()


# POST User
def query():
    req_data = request.get_json()

    name = req_data['name']
    email = req_data['email']
    username = req_data['username']
    password = req_data['password']

    data = {"email": email, "username": username,
            "password": password, "name": name}
    send_user = db.child("users").child(data['username']).set(data)
    return send_user
