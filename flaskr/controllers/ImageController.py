from flaskr.models.model import fetch_image
from flask import Blueprint


image = Blueprint('image', __name__)


@image.route('/images/<id>')
def get(id):
    return fetch_image(id)
