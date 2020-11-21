from flask import Flask, jsonify, g
from flask_cors import CORS
from flask_mail import Mail, Message
from resources.pets import pet
from resources.users import user
from flask_login import LoginManager

import models

DEBUG = True
PORT = 8000


app = Flask(__name__)
app.secret_key = "Dust Bunnies Snuggle best with Dirty Dogs"


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'thatguyfromcodingcamp@gmail.com'
app.config['MAIL_PASSWORD'] = 'campcamp'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    try:
        print(f"Loading")
        user = models.User.get_by_id(user_id)
        return user
    except models.DoesNotExist:
        return None


CORS(pet, origins=['http://localhost:3000'], supports_credentals=True)
CORS(user, origins=['http://localhost:3000'], supports_credentals=True)


app.register_blueprint(pet, url_prefix='/api/v1/pets')
app.register_blueprint(user, url_prefix='/api/v1/users')


mail = Mail(app)


@app.route("/send")
def index():
    msg = Message("Found your Pet!!",  sender = "thatguyfromcodingcamp@gmail.com",
        recipients=['joemalatesta@msn.com'])
    msg.body = "WOOT WOOT!!! With Help from Paresh, We got an email API working!!!  THIS WAS SENT FROM THE APP!!!!!!  Come to our sight and find out where your pet is!!"
    mail.send(msg)
    return jsonify(data={}, status={"code": 201, "message": "success"})


@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    g.db.close()
    return response


if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)


# end
