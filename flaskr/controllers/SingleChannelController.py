from flaskr.models.model import fetch_channel
from flask import Blueprint


singlechannel = Blueprint('singlechannel', __name__)


@singlechannel.route('/channels/<channel>')
def get(channel):
    return fetch_channel(channel)
