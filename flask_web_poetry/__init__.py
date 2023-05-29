from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config.from_object('config')

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)

login_manager.login_view = 'user_routes.page_login'
login_manager.login_message = 'Por favor, realize o login'
login_manager.login_message_category = 'info'

from flask_web_poetry.models import category_model, product_model, user_model
from flask_web_poetry.routes.category_route import category_blueprint
from flask_web_poetry.routes.errors_route import errors_blueprint
from flask_web_poetry.routes.home_route import home_blueprint
from flask_web_poetry.routes.product_route import product_blueprint
from flask_web_poetry.routes.user_route import user_blueprint

app.register_blueprint(user_blueprint)
app.register_blueprint(home_blueprint)
app.register_blueprint(category_blueprint)
app.register_blueprint(product_blueprint)
app.register_blueprint(errors_blueprint)
