from flaskr.models.model import post_channel
from flask import Blueprint
from flask import request

insertchannel = Blueprint('insertchannel', __name__)


@insertchannel.route('/channels', methods=['POST'])
def newchannel():
    return post_channel()
