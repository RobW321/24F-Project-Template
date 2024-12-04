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