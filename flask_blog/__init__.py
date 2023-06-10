import config
import secrets
from PIL import Image
from flask import Flask, render_template, url_for, redirect, request, flash, abort
from flask_cors import CORS
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt
from auth.models import login_manager

bcrypt = Bcrypt()
csrf = CSRFProtect()

login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'


def create_app(config=config):

    app = Flask(__name__)
    app.config.from_object(config.DevelopmentConfig)
    bcrypt.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)

    from auth.routes import auth
    from main.routes import main
    from posts.routes import posts

    app.register_blueprint(auth)
    app.register_blueprint(main)
    app.register_blueprint(posts)

    return app