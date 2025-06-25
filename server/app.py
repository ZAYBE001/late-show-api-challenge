from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from server.extensions import db  
from server.config import Config
from server.controllers import guest_controller, episode_controller, appearance_controller

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)          
migrate = Migrate(app, db)
jwt = JWTManager(app)

app.register_blueprint(guest_controller.bp, url_prefix='/guests')
app.register_blueprint(episode_controller.bp, url_prefix='/episodes')
app.register_blueprint(appearance_controller.bp, url_prefix='/appearances')

from server.models import *  

if __name__ == '__main__':
    app.run(debug=True)
