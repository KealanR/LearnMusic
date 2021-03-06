from flask_wtf import FlaskForm
from flask_uploads import UploadSet, configure_uploads
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField, FileField, FieldList, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange

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

class GeneratePasswordForm(FlaskForm):
    pwordAmount = IntegerField('How long do you want it? 6-50', validators=[DataRequired(), NumberRange(min=6, max=50)])
    pwordStrength = IntegerField('How Strong? 1-4', validators=[DataRequired(), NumberRange(min=1, max=4)])
    pwordSubmit = SubmitField("GenerateQuestion")
    
class QuestionForm(FlaskForm):
    
    questionTitle = StringField('Title', validators=[DataRequired()])
    questionDescription = TextAreaField('Description', render_kw={"rows": 4}, validators=[DataRequired()])
    questionMedia = FileField('Want to attach a file?')
    questionTag = StringField('Please add a tag', validators=[DataRequired()])
    questionUpload = SubmitField('Upload Question')
    
class CommentForm(FlaskForm):
    
    commentTextArea = TextAreaField('Add a comment', render_kw={"rows": 6}, validators=[DataRequired()])
    commentSubmit = SubmitField('Upload Comment')