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


@interviews.route('/interviews/<int:InterviewID>', methods=['PUT'])
def update_interview(InterviewID):
    current_app.logger.info('PUT /interviews/<InterviewID> route')

    # Get data from the request body
    data = request.get_json()

    # Extract the details for the interview that need to be updated
    interview_type = data.get('InterviewType')
    round_ = data.get('Round')
    company_id = data.get('CompanyID')
    interviewer_id = data.get('InterviewerID')
    date = data.get('Date')
    location = data.get('Location')

    if not all([interview_type, round_, company_id, interviewer_id, date]):
        return make_response(jsonify({"error": "Missing required fields"}), 400)

    # Create the update query
    query = '''
        UPDATE Interview
        SET InterviewType = %s,
            Round = %s,
            CompanyID = %s,
            InterviewerID = %s,
            Dates = %s,
            Locations = %s
        WHERE InterviewID = %s
    '''
    
    try:
        # Execute the update query
        cursor = db.get_db().cursor()
        cursor.execute(query, (interview_type, round_, company_id, interviewer_id, date, location, InterviewID))
        db.get_db().commit()

        # Check if any row was updated
        if cursor.rowcount == 0:
            return make_response(jsonify({"error": "Interview not found"}), 404)

        return make_response(jsonify({"message": "Interview updated successfully"}), 200)

    except Exception as e:
        current_app.logger.error(f"Error updating interview: {e}")
        return make_response(jsonify({"error": "Internal server error"}), 500)





