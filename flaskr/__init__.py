from flaskr.controllers.UsersController import users
from flaskr.controllers.ChannelsController import channels
from flaskr.controllers.UserController import user
from flaskr.controllers.UserPostController import insertuser
from flaskr.controllers.UserDeleteController import deleteuser
from flaskr.controllers.SingleChannelController import singlechannel
from flaskr.controllers.ChannelPostController import insertchannel
from flaskr.controllers.ImagesController import images
from flaskr.controllers.ImageController import image
from flaskr.controllers.ImagePostController import insertimage
from flask import Flask


app = Flask(__name__)


app.debug = True

app.register_blueprint(users)
app.register_blueprint(channels)
app.register_blueprint(user)
app.register_blueprint(insertuser)
app.register_blueprint(deleteuser)
app.register_blueprint(singlechannel)
app.register_blueprint(insertchannel)
app.register_blueprint(images)
app.register_blueprint(image)
app.register_blueprint(insertimage)


if __name__ == '__main__':
    app.run()
