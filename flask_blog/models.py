# from sqlalchemy import Column, String, Text, ForeignKey, Integer
# from sqlalchemy.orm import relationship
# from datetime import datetime
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager, UserMixin


# from flask_cors import CORS
# from flask_migrate import Migrate

# db_name = 'flask_blog'
# db_path = 'postgresql://{}@{}/{}'.format(
#     "postgres:ufazbng", 'localhost:5432', db_name)

# Instance of SQLAlchemy
# db = SQLAlchemy()
# migrate = Migrate()

# login_manager = LoginManager()


# def setup_db(app):
    # """
    # setup_db(app):
    #     bind flask application and SQLAlchemy serve
    # app: flask instance
    # database_path: string - path to db
    # """
    # app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # app.config.from_object('config.DevelopmentConfig')
    # db.app = app
    # db.init_app(app)
    # migrate.init_app(app, db)



