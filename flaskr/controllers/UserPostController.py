from flaskr.models.model import query
from flask import Blueprint


insertuser = Blueprint('insertuser', __name__)


@insertuser.route('/users', methods=['POST'])
def post():
    return query()
