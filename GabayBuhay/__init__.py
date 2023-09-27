import os

from flask import Flask
from flask_bcrypt import Bcrypt
# Create and configure the app
app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'DERMA4LYF'

# Initialize Flask-Bcrypt
bcrypt = Bcrypt(app)
app.config['BCRYPT'] = bcrypt

#BLUEPRINTS
from views.guest import guest_bp
app.register_blueprint(guest_bp, bcrypt = bcrypt)

from views.patient import patient_bp  
app.register_blueprint(patient_bp)


if __name__ == '__main__':
    app.run(debug=True)