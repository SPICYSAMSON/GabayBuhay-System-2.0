import os
from flask import (Blueprint, current_app, render_template, request, redirect, url_for, session, jsonify, flash, make_response)
from werkzeug.utils import secure_filename
import db

guest_bp = Blueprint('guest_bp', __name__)

@guest_bp.route('/')
def index(): 
    return render_template('guest/index.html')


@guest_bp.route('/registration', methods=['POST'])
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
            
            db.register_user(user_data)
            #Turn the user_data into a regular dictionary!! 
            user_data = {key: value[0] for key, value in user_data.items()}
            
            # Store user data in the session
            session['user_data'] = user_data
            
            #Redirects the user to his/her respective page based on their role (patient/clinician)
            return redirect(url_for('patient_bp.patient_home'))
            

@guest_bp.route('/log_in', methods=['POST'])
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
            
            return jsonify({'success': 'Patient login successful', 'redirect_url': url_for('patient_bp.patient_home')})
      

@guest_bp.route('/about_us')
def about_us():
    return render_template('guest/about_us.html')