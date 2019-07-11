from flaskr.models.model import fetch_user
from flask import Blueprint


user = Blueprint('user', __name__)


@user.route('/users/<username>')
def get(username):
    return fetch_user(username)
