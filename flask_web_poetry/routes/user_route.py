from flask import Blueprint, Response, render_template
from flask_login import current_user, login_required

from flask_web_poetry.forms.user.login_form import LoginForm
from flask_web_poetry.forms.user.profile_form import ProfileForm
from flask_web_poetry.forms.user.register_form import RegisterForm
from flask_web_poetry.services.user_service import UserService

user_blueprint = Blueprint('user_routes', __name__)


@user_blueprint.route('/register', methods=['GET', 'POST'])
def page_register():
    form: RegisterForm = RegisterForm()
    return UserService.create_user(form)


@user_blueprint.route('/login', methods=['GET', 'POST'])
def page_login():
    form: LoginForm = LoginForm()
    return UserService.signin_user(form)


@user_blueprint.route('/logout')
@login_required
def page_logout():
    return UserService.sing_out_user()


@user_blueprint.route('/profile', methods=['GET', 'POST'])
@login_required
def page_profile():
    form: ProfileForm = ProfileForm()
    form.avatar.data = current_user.avatar
    form.name.data = current_user.name
    form.email.data = current_user.email

    return render_template('/user/profile.html', form=form)


@user_blueprint.route('/profile/update', methods=['GET', 'POST'])
@login_required
def page_profile_update():
    form: ProfileForm = ProfileForm()
    return UserService.update_user(form)
