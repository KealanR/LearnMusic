from flask import Flask, render_template, url_for, request, redirect, flash
from form import SignUpForm, LoginForm, QuestionForm
import dynamodb_connection as db

application = Flask(__name__)
#secret key for authentication
application.config["SECRET_KEY"] = "69f0386d3078f92207ba280c371bb2ae7c321c2b9192f1626a"


#can assign multiple routes to same function
@application.route('/', methods=["GET", "POST"])
@application.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    message =""
    if request.method == 'POST':
        if form.validate_on_submit():
            if(db.checkIfExistsLogin(form.emailli.data, form.passwordli.data)):
                message = "welcome back"
                flash(message, "success")
                return redirect(url_for("home"))
            else:
                message = ("incorrect details")
                flash(message)
    return render_template('login.html', form=form, message=message)
    
@application.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            if(db.checkIfExistsSignUp(form.emailsu.data)):
                db.signupDB(form.emailsu.data, form.usernamesu.data, form.passwordsu.data)
                flash(f"Welcome {form.usernamesu.data}", "success")
                #signedIn = True
                username = form.usernamesu.data
               
                return redirect(url_for("home"))
        #     #
            #Talk about issues with the page getting stuck in a loop without the if == post
        # else:
        #     flash("Email already exists", "warning")
        #     return redirect(url_for("signup"))
        
    return render_template('signup.html', form=form)
     
@application.route('/home')
def home():
    # print(signedIn)
    # if signedIn == False:
    #     return redirect(url_for('signup'))
    #get list of questions from dydb to list on homepage
    questions = db.questionList()
    
    return render_template('index.html', questions=questions)
    
@application.route('/question')
def question():
    return render_template('question.html')
    
@application.route('/questionform', methods=["GET", "POST"])
def questionForm():
    form = QuestionForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            print("YEAO")
            
    return render_template('question_form.html', form=form)
    

    
#wont be able to run on c9 without this
if __name__ == '__main__':
     application.run(host='0.0.0.0', port=8080, debug=True)
     