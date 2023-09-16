from flask import Blueprint, render_template, jsonify, request, redirect, session

import db
clinician_bp = Blueprint('clinician_bp', __name__)

@clinician_bp.route('/clinician')
def clinician_home():
    # Retrieve user data from the session
    user_data = session.get('user_data', None)
    return render_template('clinician/clinician.html', clinician_data = user_data)