from flask import Flask, jsonify, g
from flask_cors import flask_cors
from resources.pets import pet
from resources.users import user
from flask_login import LoginManager


import models


DEBUG = True
PORT = 8000


app = Flask(__name__)
app.secret_key = "Dust Bunnies Snuggle best with Dirty Dogs"


login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    try:
        print(f"Loading {user_id}")
        user = models.User.get_by_id(user_id)
        return users
    except models.DoesNotExist:
        return None


CORS(pet, origins=['http://localhost:3000'], supports_credentals=True)
CORS(user, origins=['http://localhost:3000'], supports_credentals=True)


@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    g.db.close()
    return response


if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)
    

# end
