from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

bcrypt = Bcrypt()
csrf = CSRFProtect()
migrate = Migrate()
cors = CORS()
db = SQLAlchemy()
login_manager = LoginManager()