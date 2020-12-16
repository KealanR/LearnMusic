from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class SignUpForm(FlaskForm):
    
    emailsu = StringField('Email',
                        validators=[DataRequired(), 
                        Email()])
                        
    usernamesu = StringField('Username',
                           validators=[DataRequired(), 
                           Length(min=5, max=15)])
                           
    passwordsu = PasswordField('Password', 
                            validators=[DataRequired(), Length(min=6)])
                            
    passwordchecksu = PasswordField('Confirm Password',
                            validators=[DataRequired(), 
                            EqualTo('passwordsu')])
                            
    signup = SubmitField('Sign Up')
    
    
class LoginForm(FlaskForm):
    email = StringField('Email', 
                        validators=[DataRequired(), 
                        Email()])
                        
    password = PasswordField('Password', 
                            validators=[DataRequired()])
                            
    remember = BooleanField('Stay logged in')
    
    submit = SubmitField('Login')
    