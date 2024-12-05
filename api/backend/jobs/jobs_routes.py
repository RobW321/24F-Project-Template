from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

jobs = Blueprint('jobs', __name__)

# ------------------------------------------------------------
# Route to view all jobs
@jobs.route('/jobs', methods=['GET'])
def get_jobs():
    query = '''
        SELECT 
            *
        FROM Job
    '''
    # Get a cursor object from the database
    cursor = db.get_db().cursor()

    # Use cursor to query the database for a list of jobs
    cursor.execute(query)

    # Fetch all the data from the cursor
    theData = cursor.fetchall()

    # Create an HTTP Response object and add results of the query to it
    response = make_response(jsonify(theData))
    # Set the proper HTTP status code of 200 (meaning all good)
    response.status_code = 200
    # Send the response back to the client
    return response


# ------------------------------------------------------------
# Route to edit a job
@jobs.route('/edit', methods=['PUT'])
def update_jobs():
    the_data = request.json
    current_app.logger.info(the_data)

    # Extract and validate fields
    job_description = the_data.get('job_description')
    sponsorship_required = the_data.get('sponsorship_required')
    deadline = the_data.get('deadline')
    company_id = the_data.get('company_id')
    job_id = the_data.get('job_id')

    if not all([job_description, sponsorship_required, deadline, company_id, job_id]):
        return jsonify({"error": "All fields are required"}), 400

    query = '''
        UPDATE Job
        SET JobDescription = %s, SponsorshipRequired = %s, Deadline = %s, CompanyID = %s
        WHERE JobID = %s
    '''
    data = (job_description, sponsorship_required, deadline, company_id, job_id)

    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, data)
        db.get_db().commit()
        response = jsonify({"message": "Successfully edited Job"})
        response.status_code = 200
    except Exception as e:
        current_app.logger.error(f"Error updating job: {e}")
        response = jsonify({"error": "Failed to update job"})
        response.status_code = 500
    return response




# ------------------------------------------------------------



# Delete a specific job by ID
@jobs.route('/deletebyid', methods=['DELETE'])
def delete_specific_job():
    try:
        the_data = request.json
        current_app.logger.info(f"Received data: {the_data}")

        # Extract job ID
        job_id = the_data.get('job_id')
        if not job_id:
            return jsonify({"error": "Job ID is required"}), 400

        # Prepare and execute the SQL query
        query = "DELETE FROM Job WHERE JobID = %s"
        cursor = db.get_db().cursor()
        cursor.execute(query, (job_id,))  # Use a tuple for single parameters
        db.get_db().commit()

        # Check if a row was deleted
        if cursor.rowcount == 0:
            current_app.logger.warning(f"No job found with job_id: {job_id}")
            return jsonify({"error": "Job not found"}), 404

        current_app.logger.info(f"Successfully deleted job with job_id: {job_id}")
        return jsonify({"message": "Successfully deleted the job"}), 200

    except Exception as e:
        current_app.logger.error(f"Error deleting job: {e}")
        return jsonify({"error": "Failed to delete job"}), 500