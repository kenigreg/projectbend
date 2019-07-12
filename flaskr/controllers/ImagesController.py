from flaskr.models.model import all_images
from flask import Blueprint


images = Blueprint('images', __name__)


@images.route('/images')
def get():
    return (all_images.val())
