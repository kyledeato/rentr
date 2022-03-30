from flask import render_template, session, redirect, request, flash
from flask_app import app
from flask_app.models.rent import Rent
import os
# from werkzeug.utils import secure_filename

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
    if 'user_id' in session:
        logged_user = session['user_id']
        return render_template('rentboard.html', rents = rents, logged_user=logged_user)
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
    data1 = {
        "name": request.form["name"],
        "description": request.form["description"],
        "location": request.form["location"],
        "user_id" : request.form["user_id"],
        "image_name": Rent.no_space(request.form["image_name"])
    }
    if not Rent.is_valid(data1):
        return redirect ('/create')
    logged_user = session['user_id']
    image = request.files["image"]
    image_name = request.form["image_name"]
    if image:
        image_name = Rent.no_space(image_name)
        image.save(os.path.join(app.static_folder, f"img/{logged_user}-{image_name}.webp"))
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "location": request.form["location"],
        "user_id" : request.form["user_id"],
        "image_name": image_name
    }
    Rent.save(data)
    return redirect ('/rentboard')
