import os
from flask import Blueprint, render_template, jsonify, request, redirect, url_for, session, current_app
from werkzeug.utils import secure_filename
import db

home_bp = Blueprint('home_bp', __name__)



@home_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        with current_app.app_context():
            bcrypt = current_app.config['BCRYPT']  # Retrieve the bcrypt instance from the app config
            user_data = request.form.to_dict(flat=False)  # Convert to a regular dictionary
            password = user_data['password'][0]  # Get the raw password from the form
            repeat_password = user_data['repeat_password'][0]
            
            # Hash the password using Flask-Bcrypt 
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            hashed_repeat_password = bcrypt.generate_password_hash(repeat_password).decode('utf-8')
            # Replace the raw password with the hashed password in the user_data dictionary
            user_data['password'][0] = hashed_password
            user_data['repeat_password'][0] = hashed_repeat_password
            
            # Handle file upload
            if 'clinician_license' in request.files:
                file = request.files['clinician_license']
                if file.filename != '':
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
                    user_data['clinician_license'] = filename  # Save the filename to the database
                    
            db.register_user(user_data)
            
            # Store user data in the session
            session['user_data'] = user_data
            
            #Redirects the user to his/her respective page based on their role (patient/clinician)
            if user_data['account_type'][0] == '1':
                return redirect(url_for('patient_bp.patient_home'))
            elif user_data['account_type'][0] == '2':
                return redirect(url_for('clinician_bp.clinician_home'))
        
    roles = db.load_roles_from_db()
    return render_template('index/index.html', roles=roles)