from flask import Flask
app = Flask(__name__)
app.secret_key = 'secret'

UPLOAD_PATH = 'static/img'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_PATH'] = UPLOAD_PATH