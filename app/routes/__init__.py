from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_talisman import Talisman
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    Talisman(app, content_security_policy=None)

    from app.routes import main, admin, auth
    app.register_blueprint(main.bp)
    app.register_blueprint(admin.bp)
    app.register_blueprint(auth.bp)

    return app