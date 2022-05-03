from distutils.log import debug
from flask import render_template, Flask, request, redirect, url_for

app = Flask(__name__)


@app.route('/dashboard')
def dashboard():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return "<h1>logout</h1>"



if __name__ == '__main__':
    app.run(debug=True)
     
     
