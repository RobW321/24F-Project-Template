from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

interviews = Blueprint('interviews', __name__)
@interviews.route('/interviews/<StudentNUID>', methods=['GET'])
def get_interviews(StudentNUID):
    current_app.logger.info('get /interviews/<StudentNUID> route')
    cursor = db.get_db().cursor()
    query = '''
            SELECT 
                I.InterviewID,
                I.InterviewType,
                I.Round,
                C.CompanyName,
                C.Location AS CompanyLocation,
                CONCAT(IV.FirstName, ' ', IV.LastName) AS InterviewerName,
                IV.Email AS InterviewerEmail
            FROM 
                Interview I
            JOIN 
                Company C ON I.CompanyID = C.CompanyID
            JOIN 
                Interviewer IV ON I.InterviewerID = IV.InterviewerID
            JOIN 
                Application A ON A.JobID = I.CompanyID
            WHERE 
                A.StudentNUID = {0}'''.format(StudentNUID)
    
    
    cursor.execute(query)
    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response







