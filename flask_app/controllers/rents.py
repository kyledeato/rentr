from flask import render_template, session, redirect, request, flash
from flask_app import app
from flask_app.models.rent import Rent
from flask_app.models.user import User
import os
# from flask_mail import Mail, Message

# mail= Mail(app)
# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'yourId@gmail.com'
# app.config['MAIL_PASSWORD'] = '*****'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True
# mail = Mail(app)


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
    user = User.get_by_id(data)
    logged_user = session['user_id']
    return render_template('dashboard.html', rents = rents,logged_user=logged_user, user=user)

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


@app.route('/delete/<int:id>')
def delete(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {"id": id}
    Rent.delete(data)
    return redirect('/dashboard')

@app.route('/show/<int:id>')
def show(id):
    if 'user_id' not in session:
        return redirect('/')
    rent = Rent.get_one({"id": id})
    logged_user = session['user_id']
    return render_template('show.html', rent = rent, logged_user=logged_user)

@app.route('/edit/<int:id>')
def edit_recipe(id):
    if not 'user_id' in session:
        return redirect('/')
    rent = Rent.get_one({"id": id})
    logged_user = session['user_id']
    return render_template('edit.html', rent = rent, logged_user=logged_user)

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
    image = request.files["image"]
    image_name = request.form["image_name"]
    if image:
        image_name = Rent.no_space(image_name)
        print(image_name)
        image.save(os.path.join(app.static_folder, f"img/{image_name}.webp"))
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "location": request.form["location"],
        "user_id" : request.form["user_id"],
        "image_name": image_name
    }
    Rent.save(data)
    return redirect ('/rentboard')

@app.route('/update-post', methods=['POST'])
def update_post():
    if 'user_id' not in session:
        return redirect('/login')
    print('here')
    data1 = {
        "name": request.form["name"],
        "description": request.form["description"],
        "location": request.form["location"],
        "user_id" : request.form["user_id"],
        "image_name": Rent.no_space(request.form["image_name"])
    }
    if not Rent.is_valid(data1):
        return redirect ('/edit/<int:id>')
    image = request.files["image"]
    image_name = request.form["image_name"]
    if image:
        image_name = Rent.no_space(image_name)
        image.save(os.path.join(app.static_folder, f"img/{image_name}.webp"))
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "location": request.form["location"],
        "user_id" : request.form["user_id"],
        "image_name": image_name
    }
    Rent.update(data)
    return redirect('/dashboard')

# @app.route('/send', methods=['POST'])
# def send():
#     user_id = session['user_id']
#     rents = Rent.get_rents_by_id(user_id)

#     app.config['MAIL_SERVER']='smtp.gmail.com'
#     app.config['MAIL_PORT'] = 465
#     app.config['MAIL_USERNAME'] = f"{rents}"
#     app.config['MAIL_PASSWORD'] = '*****'
#     app.config['MAIL_USE_TLS'] = False
#     app.config['MAIL_USE_SSL'] = True
#     mail = Mail(app)
    