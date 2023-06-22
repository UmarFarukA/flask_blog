#!/usr/bin/env python

import os
from dotenv import load_dotenv
load_dotenv()

# Find the absolute file path to the top level project directory
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    
    FLASK_ENV = 'development'
    WTF_CSRF_ENABLED = True
    DEBUG = True
    TESTING = False

    # Settings applicable to all environment
    SECRET_KEY = os.environ.get('SECRET_KEY', default='a bad one')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', default='')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', default='')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_USERNAME', default='')
    MAIL_SUPPRESS_SEND = False

    
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    '''Defines Development related configurations'''
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}/{}".format(
        os.getenv('DB_USER'), os.getenv('DB_PWD'), 'localhost:5432', os.getenv('DB_NAME'))
    

class ProductionConfig(Config):
    '''Defines production related configurations.'''
    FLASK_ENV = 'production'
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_DB_PATH')

