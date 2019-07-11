from flaskr.controllers.UsersController import users
from flaskr.controllers.ChannelsController import channels
from flaskr.controllers.UserController import user
from flaskr.controllers.UserPostController import insertuser
from flask import Flask


app = Flask(__name__)


app.debug = True

app.register_blueprint(users)
app.register_blueprint(channels)
app.register_blueprint(user)
app.register_blueprint(insertuser)

if __name__ == '__main__':
    app.run()
