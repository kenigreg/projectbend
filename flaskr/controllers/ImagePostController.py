from flaskr.models.model import post_image
from flask import Blueprint


insertimage = Blueprint('insertimage', __name__)


@insertimage.route('/images', methods=['POST'])
def newimage():
    return post_image()
