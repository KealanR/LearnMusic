from flask import Flask, render_template, url_for, request
from form import SignUpForm, LoginForm
import dynamodb_connection as db

#import keys


application = Flask(__name__)


#can assign multiple routes to same function
@application.route('/')
@application.route('/login')
def login():
    form = LoginForm()
    #no need to specify template folder - it knows to look in templates
    return render_template('login.html', form=form)
    
@application.route('/signup')
def signup():
    form = SignUpForm()
    return render_template('signup.html', form=form)
     
@application.route('/home')
def home():
    #get list of questions from dydb to list on homepage
    questions = db.questionList()
    
    return render_template('index.html', questions=questions)
    
@application.route('/question')
def question():
    return render_template('question.html')
    
@application.route('/questionform')
def questionForm():
    return render_template('question_form.html')
    
@application.route('/test')
def testHtml():
    return render_template('test.html')
    
#wont be able to run on c9 without this
if __name__ == '__main__':
     application.run(host='0.0.0.0', port=8080, debug=True)