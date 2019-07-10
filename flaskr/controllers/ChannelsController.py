from flaskr.models.model import all_channels
from flask import Blueprint

channels = Blueprint('channels', __name__)


@channels.route('/channels')
def get():
    return (all_channels.val())
