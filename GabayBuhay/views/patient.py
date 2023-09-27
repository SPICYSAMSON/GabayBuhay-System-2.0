from flask import (Blueprint, render_template, jsonify, request, redirect, session, make_response, url_for)

import db
patient_bp = Blueprint('patient_bp', __name__)

@patient_bp.route('/patient_home')
def patient_home():
    # Your code to render the user's profile page
    user_data = session.get('user_data', None)
    if not user_data:
        return redirect(url_for('guest_bp.index'))  # Redirect to the index if not logged in
    
    # Create the response and set Cache-Control to prevent caching
    response = make_response(render_template('patient/patient_home.html', patient_data = user_data))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    return response


@patient_bp.route('/patient/lichencheck')
def lichencheck():
    # Your code to render the user's profile page
    user_data = session.get('user_data', None)
    if not user_data:
        return redirect(url_for('guest_bp.index'))  # Redirect to the index if not logged in
    
    # Create the response and set Cache-Control to prevent caching
    response = make_response(render_template('patient/lichencheck.html', patient_data = user_data))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    return response


@patient_bp.route('/patient/lichenhub')
def lichenhub():
    # Your code to render the user's profile page
    user_data = session.get('user_data', None)
    if not user_data:
        return redirect(url_for('guest_bp.index'))  # Redirect to the index if not logged in
    
    # Create the response and set Cache-Control to prevent caching
    response = make_response(render_template('patient/lichenhub.html', patient_data = user_data))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    return response


@patient_bp.route('/patient/licheknow')
def licheknow():
    # Your code to render the user's profile page
    user_data = session.get('user_data', None)
    if not user_data:
        return redirect(url_for('guest_bp.index'))  # Redirect to the index if not logged in
    
    # Create the response and set Cache-Control to prevent caching
    response = make_response(render_template('patient/licheknow.html', patient_data = user_data))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    return response

@patient_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    # Remove session variables related to the user's login
    session.pop('user_data', None)  # Remove user ID or any other relevant session variables
    # Redirect the user to the login page or any other appropriate page
    return redirect(url_for('guest_bp.index')) 