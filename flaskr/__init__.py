from flaskr.controllers.UsersController import users
from flaskr.controllers.ChannelsController import channels
from flaskr.controllers.UserController import user
from flaskr.controllers.UserPostController import insertuser
from flaskr.controllers.UserDeleteController import deleteuser
from flaskr.controllers.SingleChannelController import singlechannel
from flaskr.controllers.ChannelPostController import insertchannel
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


if __name__ == '__main__':
    app.run()
