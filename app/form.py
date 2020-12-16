from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FileField
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
    emailli = StringField('Email', 
                        validators=[DataRequired(), 
                        Email()])
                        
    passwordli = PasswordField('Password', 
                            validators=[DataRequired()])
                            
    
    
    login = SubmitField('Login')
    
class QuestionForm(FlaskForm):
    
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    media = FileField('Want to attach a file?')
    uploadQuestion = SubmitField('Upload Question')