import config
import secrets
from PIL import Image
from flask import Flask

from App.models.auth import login_manager
from App.extensions import db, bcrypt, csrf, migrate, cors


login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'


def create_app(config=config.DevelopmentConfig):

    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    bcrypt.init_app(app)
    csrf.init_app(app)
    migrate.init_app(app)
    cors.init_app(app)
    login_manager.init_app(app)

    from App.auth.routes import auth_bp
    app.register_blueprint(auth_bp)

    from App.main.routes import main_bp
    app.register_blueprint(main_bp)

    from App.posts.routes import posts_bp 
    app.register_blueprint(posts_bp)

    return app