from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

applications = Blueprint('applications', __name__)
@applications.route('/applications/<StudentNUID>', methods=['GET'])
def get_user_applications(StudentNUID):
    current_app.logger.info('get /applications/<StudentNUID> route')
    cursor = db.get_db().cursor()
    """
    Fetches all applications for a specific user (NUID) from the database.
    """

        # SQL query to fetch applications for the given NUID
    query = '''
            SELECT 
                a.ApplicationID,
                a.DateSubmitted,
                a.Status,
                a.Priority,
                a.Notes,
                j.JobDescription,
                c.CompanyName
            FROM Application a
            JOIN Job j ON a.JobID = j.JobID
            JOIN Company c ON j.CompanyID = c.CompanyID
            WHERE a.StudentNUID = {0}'''.format(StudentNUID)
    
   

        # Execute query
    
    cursor.execute(query)
    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response


@applications.route('/applications', methods=['POST'])
def add_application():
    try:
        # Get data from the request
        data = request.json
        nuid = data['StudentNUID']
        job_id = data['JobID']
        date_submitted = data['DateSubmitted']
        status = data['Status']
        priority = data['Priority']
        notes = data.get('Notes', '')  # Optional notes field

        # SQL query to insert a new application
        query = f'''
            INSERT INTO Application (StudentNUID, JobID, DateSubmitted, Status, Priority, Notes)
            VALUES (%s, %s, %s, %s, %s, %s)
        '''

        # Execute the query
        cursor = db.get_db().cursor()
        cursor.execute(query, (nuid, job_id, date_submitted, status, priority, notes))
        db.get_db().commit()

        current_app.logger.info(f"New application added for NUID {nuid}.")
        return jsonify({"message": "Application added successfully"}), 201

    except Exception as e:
        current_app.logger.error(f"Error adding application: {e}")
        return jsonify({"error": "Could not add application"}), 500
