from flask import Blueprint
from flask_login import login_required

from flask_web_poetry.services.home_service import HomeService

home_blueprint = Blueprint('home_routes', __name__)


@home_blueprint.route('/')
@login_required
def page_home():
    return HomeService.list_home()
