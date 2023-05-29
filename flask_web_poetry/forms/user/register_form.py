from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegisterForm(FlaskForm):
    name = StringField(
        label='Nome de Usuário:',
        validators=[
            Length(
                min=3, max=120, message='Nome deve ter de 3 a 120 caracteres'
            ),
            DataRequired(),
        ],
    )

    email = StringField(
        label='E-mail do Usuário:',
        validators=[Email(message='E-mail inválido'), DataRequired()],
    )

    password = PasswordField(
        label='Senha do Usuário:',
        validators=[
            Length(
                min=5, max=20, message='Senha deve ter de 5 a 20 caracteres'
            ),
            DataRequired(),
        ],
    )

    password_confirm = PasswordField(
        label='Confirmação de Senha:',
        validators=[
            Length(
                min=5, max=20, message='Senha deve ter de 5 a 20 caracteres'
            ),
            EqualTo('password', message='Senhas não conferem'),
            DataRequired(),
        ],
    )

    submit = SubmitField(label='Cadastrar-se')
