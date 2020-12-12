from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    #no need to specify template folder - it knows to look in templates
    return render_template('base.html')
    
@app.route('/question')
def question():
    return render_template('question.html')
    
@app.route('/questionform')
def questionForm():
    return render_template('question_form.html')
    
@app.route('/test')
def testHtml():
    return render_template('test.html')
    
#wont be able to run on c9 without this
if __name__ == '__main__':
     app.run(host='0.0.0.0', port=8080, debug=True)