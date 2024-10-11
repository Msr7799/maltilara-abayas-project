from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

# إنشاء مثيلات للامتدادات
db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_class=Config):
    # إنشاء وتكوين التطبيق
    app = Flask(__name__)
    app.config.from_object(config_class)

    # تهيئة الامتدادات
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # تسجيل البلوبرنتات
    from app.routes.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from app.routes.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from app.routes.admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    # إنشاء جميع الجداول في قاعدة البيانات
    with app.app_context():
        db.create_all()

    return app

# استيراد النماذج لضمان تعريفها قبل إنشاء الجداول
from app import models