from flask import Blueprint, render_template, jsonify, request, redirect, session

import db
patient_bp = Blueprint('patient_bp', __name__)

@patient_bp.route('/patient/clinical_solutions')
def patient_home():
    # Retrieve user data from the session
    user_data = session.get('user_data', None)
    return render_template('patient/patient.html', patient_data = user_data)