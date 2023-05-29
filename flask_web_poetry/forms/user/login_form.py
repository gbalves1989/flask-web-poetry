from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
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

    submit = SubmitField(label='Entrar')
