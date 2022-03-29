from flask import render_template, session, redirect, request, flash
from flask_app import app
from flask_app.models.rent import Rent
from flask_app.models.user import User

#DISPLAY ROUTES -----------------------
# dashboard
@app.route('/')
def index():
    return redirect('/rentboard')

@app.route('/dashboard')
def dashboard():
    # can only view dashboard if account true else go to login page
    if 'user_id' not in session:
        return redirect('/login')
    data = {"id": session['user_id']}
    rents = Rent.get_rents_by_id(data)
    return render_template('dashboard.html', rents = rents)

@app.route('/rentboard')
def rentboard():
    rents = Rent.get_all()
    # logged_in_user = User.get_by_email({"id": session['user_id']})
    return render_template('rentboard.html', rents = rents)

@app.route('/create')
def create():
    if 'user_id' not in session:
        return redirect('/login')
    return render_template('create.html')

#ACTION ROUTES -----------------------
@app.route('/create-post', methods=['POST'])
def create_post():
    if 'user_id' not in session:
        return redirect('/login')
    if not Rent.is_valid(request.form):
        return redirect ('/create')
    Rent.create(request.form)
    return redirect ('/rentboard')
