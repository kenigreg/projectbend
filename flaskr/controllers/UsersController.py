from flaskr.models.model import all_users
from flask import Blueprint


users = Blueprint('users', __name__)


@users.route('/users')
def get():
    return (all_users.val())
