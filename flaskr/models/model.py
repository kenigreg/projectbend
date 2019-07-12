from config import config
from pyrebase import pyrebase
from flask import request


firebase = pyrebase.initialize_app(config)
db = firebase.database()

# GET all Users
all_users = db.child("users").get()

# GET all Channels
all_channels = db.child("channels").get()

# GET User


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

# DELETE USER


def delete_user(username):
    remove_user = db.child("users/" + username).remove()
    return remove_user

# GET a Channel


def fetch_channel(channel):
    channel_info = db.child("channels/" + channel).get()
    return channel_info.val()

# POST Channel


def post_channel():
    req_data = request.get_json()

    channel_name = req_data['channel_name']
    description = req_data['description']
    channel_picture = req_data['channel_picture']

    data = {"channel_name": channel_name,
            "channel_picture": channel_picture, "description": description}
    send_channel = db.child("channels").child(data['channel_name']).set(data)
    return send_channel
