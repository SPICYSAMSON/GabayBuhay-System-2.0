from flask import (Blueprint, render_template, jsonify, request, redirect, make_response,session, url_for)

import db
clinician_bp = Blueprint('clinician_bp', __name__)

@clinician_bp.route('/clinician')
def clinician_home():
    # Your code to render the user's profile page
    user_data = session.get('user_data', None)
    if not user_data:
        return redirect(url_for('guest_bp.index'))  # Redirect to the index if not logged in
    
    # Create the response and set Cache-Control to prevent caching
    response = make_response(render_template('clinician/clinician.html', clinician_data = user_data))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    return response