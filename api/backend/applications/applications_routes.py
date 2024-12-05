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
        # Collect data from the request
        the_data = request.json
        current_app.logger.info(the_data)

        # Extract variables from request
        student_nuid = the_data['StudentNUID']
        job_id = the_data['JobID']
        date_submitted = the_data['DateSubmitted']
        status = the_data['Status']
        priority = the_data['Priority']
        notes = the_data['Notes']

        # SQL query to insert the new application into the database
        query = f'''
            INSERT INTO Application (StudentNUID, JobID, DateSubmitted, Status, Priority, Notes)
            VALUES ({student_nuid}, {job_id}, '{date_submitted}', '{status}', {priority}, '{notes}')
        '''

        # Log query for debugging
        current_app.logger.info(f"Executing query: {query}")

        # Execute and commit the query
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()

        # Return a success response
        response = make_response(jsonify({"message": "Application added successfully"}))
        response.status_code = 201
        return response

    except Exception as e:
        current_app.logger.error(f"Error adding application: {e}")
        return jsonify({"error": "Failed to add application"}), 500