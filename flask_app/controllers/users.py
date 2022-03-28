from flask import render_template, session, redirect, request, flash
from flask_app import app


# LOGINS AND REGISTRATION
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

