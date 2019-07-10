from flaskr.controllers.UsersController import users
from flask import Flask


app = Flask(__name__)


app.debug = True

app.register_blueprint(users)


if __name__ == '__main__':
    app.run()
