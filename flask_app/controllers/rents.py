from flask import render_template, session, redirect, request, flash
from flask_app import app
# from flask_app.models.user import User

# DASHBOARD
@app.route('/')
def index():
    return redirect('/rentboard')

@app.route('/dashboard')
def dashboard():
    # can only view dashboard if account true else go to login page
    if 'user_id' not in session:
        return redirect('/login')
    return render_template('dashboard.html')

@app.route('/rentboard')
def rentboard():
    return render_template('rentboard.html')

