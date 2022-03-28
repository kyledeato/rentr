from flask import render_template, session, redirect, request
from flask_app import app
from flask_app.models.user import User

# LOGINS AND REGISTRATION
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/dashboard')

    # action routes
@app.route('/register-account',methods=['POST'])
def register_account():
    if not User.reg_is_valid(request.form):
        return redirect('/register')
    session['user_id'] = User.create(request.form)
    return redirect('/dashboard')

@app.route('/login-account', methods=['POST'])
def login_account():
    if not User.log_valid(request.form):
        return redirect('/login')
    user = User.get_by_email(request.form)
    session['user_id'] = user.id
    print(f"logged in as id:{session['user_id']}")
    return redirect('/dashboard')