from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, BooleanField, SubmitField)
from wtforms.validators import (
    DataRequired, ValidationError, Email, EqualTo)
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Имя пользоавтеля', validators=[DataRequired()])
    password= PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить')
    submit = SubmitField('Вход')


class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password2 = PasswordField(
        'Повторите ввод пароля', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('РЕгистрация')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Имя пользователя занято.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email занят.')