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
    return render_template('patient/lichencheck.html', patient_data = user_data)