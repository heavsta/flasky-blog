from app.models import Category
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    ValidationError
)
from wtforms.validators import DataRequired


class CategoryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Create')

    def validate_name(self, name):
        category = Category.query.filter_by(name=name.data).first()
        if category:
            raise ValidationError('It seems this category already exists!')