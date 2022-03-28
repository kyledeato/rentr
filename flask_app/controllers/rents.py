from flask import render_template, session, redirect, request, flash
from flask_app import app
# from flask_app.models.user import User

# DASHBOARD
@app.route('/')
def index():
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/rent-board')

