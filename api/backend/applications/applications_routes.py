from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

student_applications = Blueprint('student_applications', __name__)

# ------------------------------------------------------------
# User Story 1: Add a position to the list of applications
@student_applications.route('/applications', methods=['POST'])
def add_application():
    data = request.json
    current_app.logger.info(data)

    # Extract fields from request
    student_id = data['student_id']
    job_id = data['job_id']
    date_submitted = data['date_submitted']
    status = data['status']
    priority = data['priority']
    notes = data.get('notes', '')

    query = f'''
        INSERT INTO Application (DateSubmitted, Status, Priority, StudentNUID, JobID, Notes)
        VALUES ('{date_submitted}', '{status}', {priority}, {student_id}, {job_id}, '{notes}')
    '''
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Application added successfully")
    response.status_code = 201
    return response