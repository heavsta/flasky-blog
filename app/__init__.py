from app.config import Config
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_ckeditor import CKEditor
from flask_login import LoginManager, login_manager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
ckeditor = CKEditor()
mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    # Extensions Initialization
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    ckeditor.init_app(app)
    mail.init_app(app)

    # Blueprints
    from app.articles.routes import articles
    from app.categories.routes import categories
    from app.main.routes import main
    from app.users.routes import users
    from app.errors.handlers import errors
    app.register_blueprint(articles)
    app.register_blueprint(categories)
    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(errors)

    return app