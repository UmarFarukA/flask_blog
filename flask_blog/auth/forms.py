from flask_wtf import Form
from wtforms import StringField, EmailField, FileField, PasswordField, TextAreaField, SubmitField, validators, ValidationError
from flask_login import current_user
from models import User

class RegistratioinForm(Form):
    username = StringField("Username", [validators.InputRequired(
        message="Username is required"), validators.Length(min=2, max=25, message="Username must be above 2 & not more than 25")])
    email = EmailField(
        "Email", [validators.InputRequired(message="Email field cannot be empty")])
    password = PasswordField("Password", validators=[validators.DataRequired(message="Password field cannot be empty"), validators.EqualTo(
        'confirm_password', message="Passwords must match")])
    confirm_password = PasswordField("Confirm Password")
    submit = SubmitField("Sign up")

    def validate_username(self, username):
        """Function that validate existance of username"""
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                "Username already exists, kindly use another username")

    def validate_email(self, email):
        """Function that validates the existance of email"""
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError("Email already in use, kindly login")


class LoginForm(Form):
    email = EmailField("Email", [validators.DataRequired(
        message="Email is required")])
    password = PasswordField(
        "Password", [validators.DataRequired(message="Password is required")])
    login = SubmitField("Login")
