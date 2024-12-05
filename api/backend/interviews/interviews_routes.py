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
                I.Dates,
                I.Locations,
                I.InterviewType,
                I.Round,
                C.CompanyName,
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


@interviews.route('/interviews/<InterviewID>', methods=['PUT'])
def update_interview(InterviewID):
    try:
        data = request.json
        current_app.logger.info(data)

        # Extract the details for the interview that need to be updated
        interview_type = data.get('InterviewType')
        round = data.get('Round')
        interview_date = data.get('Dates')
        location = data.get('Locations')

        # Create the update query
        query = f'''
            UPDATE Interview
            SET 
                InterviewType = '{interview_type}',
                Round = '{round}',
                Dates = '{interview_date}',
                Locations = '{location}'
            WHERE InterviewID = '{InterviewID}'
        '''
    
    
        # Execute the update query
        current_app.logger.info(f"Executing query: {query}")

        # Execute and commit the query
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()

        # Return a success response
        response = make_response(jsonify({"message": "Interview updated successfully"}))
        response.status_code = 200
        return response

    except Exception as e:
        current_app.logger.error(f"Error updating interview: {e}")
        return make_response(jsonify({"error": "Internal server error"}), 500)


@interviews.route('/interviews', methods=['POST'])
def add_interview():
    try:
        data = request.json
        current_app.logger.info(data)

        # Extract interview details from the request
        interview_id = data['InterviewID']
        interview_date = data['Dates']
        location = data['Locations']
        interview_type = data['InterviewType']
        round = data['Round']
        company_id = data['CompanyID']
        interviewer_id = data['InterviewerID']

        # SQL Insert query
        query = f'''
            INSERT INTO Interview (InterviewID, Dates, Locations, InterviewType, Round, CompanyID, InterviewerID)
            VALUES ({interview_id}, '{interview_date}', '{location}', '{interview_type}', '{round}', {company_id}, {interviewer_id}) 
        '''

        current_app.logger.info(f"Executing query: {query}")

        # Execute the insert query
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()

        # Return a success response
        response = make_response(jsonify({"message": "Interview added successfully!"}))
        response.status_code = 201
        return response

    except Exception as e:
        current_app.logger.error(f"Error adding interview: {e}")
        return make_response(jsonify({"error": "Internal server error"}), 500)
    

@interviews.route('/delete/<interview_id>', methods=['DELETE'])
def delete_interview(interview_id):
    try:
        # SQL query to delete the interview from the database
        query = '''
            DELETE FROM Interview
            WHERE InterviewID = %s
        '''

        current_app.logger.info(f"Executing query: {query}")
        
        cursor = db.get_db().cursor()
        cursor.execute(query, (interview_id,))
        db.get_db().commit()

        if cursor.rowcount == 0:
            return jsonify({"error": "Interview not found"}), 404
        
        # Return success response
        response = make_response(jsonify({"message": "Interview deleted successfully"}))
        response.status_code = 200
        return response
    
    except Exception as e:
        current_app.logger.error(f"Error deleting interview with ID {interview_id}: {e}")
        return make_response(jsonify({"error": "Internal server error"}), 500)


