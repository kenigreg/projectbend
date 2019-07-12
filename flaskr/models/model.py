from config import config
from pyrebase import pyrebase
from flask import request


firebase = pyrebase.initialize_app(config)
db = firebase.database()

# GET all Users
all_users = db.child("users").get()

# GET all Channels
all_channels = db.child("channels").get()

# GET all Images
all_images = db.child("images").get()

# GET User


def fetch_user(username):
    user_info = db.child("users/" + username).get()
    return user_info.val()

# GET Image


def fetch_image(id):
    image_info = db.child("images/" + id).get()
    return image_info.val()


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

# POST Image


def post_image():
    req_data = request.get_json()

    caption = req_data['caption']
    id = req_data['id']
    created_at = req_data['created_at']
    event_img = req_data['event_img']
    geolocation = req_data['geolocation']
    relevant_channels = req_data['relevant_channels']
    username = req_data['username']

    data = {"caption": caption, "created_at": created_at, "event_img": event_img,
            "geolocation": geolocation, "relevant_channels": relevant_channels, "username": username, "id": id}
    send_image = db.child("images").child(data['id']).set(data)
    return send_image
