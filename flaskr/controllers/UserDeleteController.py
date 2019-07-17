from flaskr.models.model import delete_user
from flask import Blueprint
from flask import request

deleteuser = Blueprint('deleteuser', __name__)


@deleteuser.route('/users/<username>', methods=['DELETE'])
def delete(username):

    if request.method == 'DELETE':
        delete_user(username)
    pass
