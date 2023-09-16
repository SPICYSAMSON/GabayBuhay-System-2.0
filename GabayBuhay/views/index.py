import os
from flask import (Blueprint, current_app, render_template, request, redirect, url_for, session, jsonify, flash, make_response)
from werkzeug.utils import secure_filename
import db

home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/')
def index(): 
    roles = db.load_roles_from_db()
    return render_template('index/index.html', roles=roles)


@home_bp.route('/registration', methods=['POST'])
def registration():
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
                #Turn the user_data into a regular dictionary!! 
                user_data = {key: value[0] for key, value in user_data.items()}
                
                # Store user data in the session
                session['user_data'] = user_data
                
                #Redirects the user to his/her respective page based on their role (patient/clinician)
                if user_data['account_type'] == '1':
                    return redirect(url_for('patient_bp.patient_home'))
                elif user_data['account_type'] == '2':
                    return redirect(url_for('clinician_bp.clinician_home'))
                

@home_bp.route('/log_in', methods=['POST'])
def log_in():
    if request.method == 'POST':
        with current_app.app_context():
            bcrypt = current_app.config['BCRYPT']
            email = request.form['email']
            password = request.form['password']

            user_data = db.fetch_user(email)

            if user_data is None:
                # Invalid credentials
                error_message = 'You have not yet created an account. Please try again.'
                return jsonify({'error': error_message})

            elif not bcrypt.check_password_hash(user_data['password'], password):
                # Invalid credentials
                error_message = 'Invalid credentials. Please try entering the password again.'
                return jsonify({'error': error_message})

            # Successful login
            session['user_data'] = user_data

            if user_data['role_id'] == 1:
                return jsonify({'success': 'Patient login successful', 'redirect_url': url_for('patient_bp.patient_home')})
            elif user_data['role_id'] == 2:
                return jsonify({'success': 'Clinician login successful', 'redirect_url': url_for('clinician_bp.clinician_home')})
      
      
@home_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    # Remove session variables related to the user's login
    session.pop('user_data', None)  # Remove user ID or any other relevant session variables
    # Redirect the user to the login page or any other appropriate page
    return redirect(url_for('home_bp.index')) 