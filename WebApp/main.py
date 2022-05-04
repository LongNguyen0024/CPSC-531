import os
from distutils.log import debug
from flask_login import login_user, login_required, logout_user, current_user
from flask import render_template, Flask, request, redirect, url_for, flash
from .models import User
from . import db
from flask import RegistrationForm
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)


@app.route('/dashboard')
def dashboard():
    return render_template('index.html')

@app.route('/signup', methods = ['POST','GET'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        
        newUser = User(email=email, password=password, username=username)
        db.session.add(newUser)
        db.session.commit()
        login_user(newUser, remember=True)
        flash('Account created!', category='success')
        return redirect(url_for('views.home'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return "<h1>logout</h1>"



if __name__ == '__main__':
    app.run(debug=True)
     
     
     
