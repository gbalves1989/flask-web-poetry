from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import FileField, StringField, SubmitField
from wtforms.validators import DataRequired, Length


class ProfileForm(FlaskForm):
    avatar = FileField(
        label='Avatar do Usuário',
        validators=[FileAllowed(['png', 'jpg', 'jpeg'], 'Image only!')],
    )

    name = StringField(
        label='Nome de Usuário:',
        validators=[
            Length(
                min=3, max=120, message='Nome deve ter de 3 a 120 caracteres'
            ),
            DataRequired(),
        ],
    )

    email = StringField(label='E-mail do Usuário:')

    submit = SubmitField(label='Atualizar')
