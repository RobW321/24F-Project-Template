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

@applications.route('/applications/<ApplicationID>', methods=['PUT'])
def update_application(ApplicationID):
    try:
        # Collect data from the request
        the_data = request.json
        current_app.logger.info(the_data)

        # Extract variables from request
        date_submitted = the_data.get('DateSubmitted')
        status = the_data.get('Status')
        priority = the_data.get('Priority')
        notes = the_data.get('Notes')

        # Construct the SQL query for updating the application
        query = f'''
            UPDATE Application
            SET 
                DateSubmitted = '{date_submitted}',
                Status = '{status}',
                Priority = {priority},
                Notes = '{notes}'
            WHERE ApplicationID = {ApplicationID}
        '''

        # Log query for debugging
        current_app.logger.info(f"Executing query: {query}")

        # Execute and commit the query
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()

        # Return a success response
        response = make_response(jsonify({"message": "Application updated successfully"}))
        response.status_code = 200
        return response

    except Exception as e:
        current_app.logger.error(f"Error updating application: {e}")
        return jsonify({"error": "Failed to update application"}), 500



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
    


@applications.route('/applications/<ApplicationID>', methods=['DELETE'])
def delete_application(ApplicationID):
    """
    Deletes a job application based on the ApplicationID.
    """
    try:
        # SQL query to delete the application
        query = f'''
            DELETE FROM Application
            WHERE ApplicationID = {ApplicationID}
        '''
        
        # Log the query for debugging
        current_app.logger.info(f"Executing query: {query}")

        # Execute and commit the query
        cursor = db.get_db().cursor()
        cursor.execute(query)
        db.get_db().commit()

        # Check if any row was deleted
        if cursor.rowcount == 0:
            return jsonify({"error": "Application not found"}), 404

        # Return success response
        response = make_response(jsonify({"message": "Application deleted successfully"}))
        response.status_code = 200
        return response

    except Exception as e:
        current_app.logger.error(f"Error deleting application: {e}")
        return jsonify({"error": "Failed to delete application"}), 500
    
@applications.route('/applications/priority/<int:priority>', methods=['GET'])
def get_applications_by_priority(priority):
    """
    Fetches all applications with the specified priority level.
    """
    try:
        # SQL query to fetch applications by priority
        query = f'''
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
            WHERE a.Priority = {priority}
        '''
        
        # Log the query for debugging
        current_app.logger.info(f"Executing query: {query}")

        # Execute the query
        cursor = db.get_db().cursor()
        cursor.execute(query)
        theData = cursor.fetchall()

        # Return the data
        response = make_response(jsonify(theData))
        response.status_code = 200
        return response

    except Exception as e:
        current_app.logger.error(f"Error fetching applications by priority: {e}")
        return jsonify({"error": "Failed to fetch applications"}), 500
    

@applications.route('/applications/status/<string:status>', methods=['GET'])
def get_applications_by_status(status):
    """
    Fetches all applications with the specified status.
    """
    try:
        # SQL query to fetch applications by status
        query = f'''
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
            WHERE a.Status = '{status}'
        '''
        
        # Log the query for debugging
        current_app.logger.info(f"Executing query: {query}")

        # Execute the query
        cursor = db.get_db().cursor()
        cursor.execute(query)
        theData = cursor.fetchall()

        # Return the data
        response = make_response(jsonify(theData))
        response.status_code = 200
        return response

    except Exception as e:
        current_app.logger.error(f"Error fetching applications by status: {e}")
        return jsonify({"error": "Failed to fetch applications"}), 500

    

@applications.route('/flowchart', methods=['GET'])
def get_flowchart_data():
    """
    Fetches all records from the FlowChart table in the database.
    """
    # SQL query to fetch all records from FlowChart table
    query = '''
        SELECT 
            FlowChartID,
            NumApplications,
            NumProgress,
            NumRejected,
            NumAccepted
        FROM FlowChart
    '''
    
    # Get a cursor object from the database
    cursor = db.get_db().cursor()
    cursor.execute(query)  # Execute the query
    data = cursor.fetchall()  # Fetch all results

    # Return the data as JSON response
    return jsonify(data)

@applications.route('/tickets', methods=['PUT'])
def add_ticket():
    """
    Adds a new ticket to the Ticket table in the database.
    """
    try:
        # Parse JSON request
        ticket_data = request.get_json()

        # Extract required fields
        description = ticket_data.get("Description")
        status = ticket_data.get("Status")
        priority = ticket_data.get("Priority")
        ticket_type = ticket_data.get("TicketType")
        employee_id = ticket_data.get("EmployeeID")
        student_nuid = ticket_data.get("StudentNUID")

        # Validate required fields
        if not all([description, status, priority, ticket_type, employee_id, student_nuid]):
            return jsonify({"error": "All fields are required."}), 400

        # SQL query to insert a new ticket
        query = '''
            INSERT INTO Ticket (Description, Status, Priority, TicketType, EmployeeID, StudentNUID)
            VALUES (%s, %s, %s, %s, %s, %s)
        '''
        values = (description, status, priority, ticket_type, employee_id, student_nuid)

        # Execute the query
        cursor = db.get_db().cursor()
        cursor.execute(query, values)
        db.get_db().commit()

        return jsonify({"message": "Ticket added successfully."}), 201

    except Exception as e:
        current_app.logger.error(f"Error adding ticket: {e}")
        return jsonify({"error": "Failed to add ticket."}), 500
    
    
    
    