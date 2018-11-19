from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError
from wtforms.validators import Required,Email,EqualTo
from ..models import User



class RegistrationForm(FlaskForm):
    email = StringField("Your Email Address",validators=[Required(),Email()])
    username = Stringfield("Enter your username",validators=[Required()])
    password = PasswordField("Password",validators=[Required(),EqualTo('password_confirm',message='Passwords must match')])
    password_confirm = PasswordField('Confirm passwords',validators=[Required()])
    submit = SubmitField("Sign Up")


    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('There is an account with that email.')

    def validate_username(self,data_field):
        if User.query.filter_by(usernsme = data_field.data).first():
            raise ValidationError('That username is taken.')