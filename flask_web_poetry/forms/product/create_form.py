from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Length


class CreateForm(FlaskForm):
    name = StringField(
        label='Nome do Produto:',
        validators=[
            Length(
                min=5, max=20, message='Nome deve ter de 5 a 120 caracteres'
            ),
            DataRequired(),
        ],
    )

    category = SelectField(label='Categoria do Produto')

    submit = SubmitField(label='Salvar')
