from flask import Blueprint, render_template

errors_blueprint = Blueprint('errors_routes', __name__, url_prefix='/error')


@errors_blueprint.app_errorhandler(404)
def error_404(error):
    return render_template('/errors/error_404.html')
