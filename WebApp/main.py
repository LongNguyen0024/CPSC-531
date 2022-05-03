from distutils.log import debug
from flask import render_template, Flask, request

app = Flask(__name__)


@app.route('/dashboard')
def dashboard():
    return render_template('index.html')
    # return "<p>hehe</p>"

@app.route('/signup')
def signup():
    return "<h1>signup</h1>"

@app.route('/login')
def login():
    return "<h1>login</h1>"

@app.route('/logout')
def logout():
    return "<h1>logout</h1>"



if __name__ == '__main__':
    app.run(debug=True)
     