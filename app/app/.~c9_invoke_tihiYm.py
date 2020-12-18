from app import application, bcrypt
from flask import Flask, render_template, url_for, request, redirect, flash, session
from app.form import SignUpForm, LoginForm, QuestionForm
import app.dynamodb_connection as db
import app.s3_connection as s3
from flask_wtf import FlaskForm
from flask_uploads import configure_uploads, IMAGES, UploadSet
#from werkzeug.utils import secure_filename

images = UploadSet('images', IMAGES)
configure_uploads(application, images)

#can assign multiple routes to same function
@application.route('/', methods=["GET", "POST"])
@application.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    message =""
    if request.method == 'POST':
        if form.validate_on_submit():
            user = db.checkIfExistsLogin(form.emailli.data, form.passwordli.data)
            
            # if (user.signedIn):
            if(user != None):
                
                message = (f"Welcome back ", user.username)
                flash(message, "success")
                # print("THIS IS THE USERNAME ", user.username)
                # print("THIS IS THE EMAIL     ", user.email)
                session_user = {"username": user.username, "email": user.email}
                session["session_user"] = session_user
                print(session_user['username'])
                
                return redirect(url_for("home"))
            else:
                message = ("incorrect details")
                flash(message, "warning")    
                
           
    return render_template('login.html', form=form, message=message)
    
@application.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            if(db.checkIfExistsSignUp(form.emailsu.data)):
                passwordBcrypt = bcrypt.generate_password_hash(form.passwordsu.data).decode('utf-8')
                db.signupDB(form.emailsu.data, form.usernamesu.data, passwordBcrypt)
                flash(f"Welcome {form.usernamesu.data}", "success")
                session_user = {"username": form.usernamesu.data, "email": form.emailsu.data}
                session["session_user"] = session_user
                print(session_user["username"])
                #print("SIGNED IN")
                return redirect(url_for("home"))
        
            else:
                flash(f"Something went wrong", "danger")
    return render_template('signup.html', form=form)

@application.route('/home')
def home():
    if "session_user" in session:
        session_user = session["session_user"]
        #get list of questions from dydb to list on homepage
        questions = db.questionList()
    
        return render_template('index.html', questions=questions) 
        
    else:
        return redirect(url_for("login"))
  

@application.route('/question')
def question():
    if "session_user" in session:
        session_user = session["session_user"]
        return render_template('question.html')
    else:
        return redirect(url_for("login"))
        
@application.route('/questionform', methods=["GET", "POST"])
def questionForm():
    if "session_user" in session:
        session_user = session["session_user"]
        print(session_user['username'])
        form = QuestionForm()
        if request.method == 'POST':
            if form.validate_on_submit():
                #try:
                if not form.questionMedia.data:
                    db.postQuestionWithoutFile(session_user['username'], form.questionTitle.data, 
                                    form.questionDescription.data)
                    print("UPLOADING NO FILE")
                    return redirect(url_for("question"))
                else:
                    print(form.questionMedia.data)
                    filename = images.save(form.questionMedia.data)
                    
                    
                    s3.upload_to_S3(f"{filename}")
                    print(session_user.username)
                    db.postQuestionWithFile(session_user['username'], form.questionTitle.data, 
                                      form.questionDescription.data, filename)
        
                    return redirect(url_for("question"))
                
        return render_template('question_form.html', form=form)
    else:
        return redirect(url_for("login"))
        
@application.route('/logout')
def logout():
    session.pop("session_user", None)
    return redirect(url_for("login"))