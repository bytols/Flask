from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField , BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo



class RegistrationForm(FlaskForm):

    username = StringField("username" , validators=[DataRequired() , Length(min=2 , max=20)])

    Email = StringField("email" , validators=[DataRequired() , Email()])

    password = PasswordField("password" , validators=[DataRequired()])
    confirm_password = PasswordField("password" , validators=[DataRequired() , EqualTo("password")])

    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):

    Email = StringField("email" , validators=[DataRequired() , Email()])

    password = PasswordField("password" , validators=[DataRequired()])
    remember = BooleanField("remember me")

    submit = SubmitField("Login")