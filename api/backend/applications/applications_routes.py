from flask import Blueprint, jsonify, current_app
from backend.db_connection import db

applications = Blueprint('applications', __name__)
@applications.route('/applications/<int:nuid>', methods=['GET'])
def get_user_applications(nuid):
    try:
        # SQL query to fetch applications for the given NUID
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
            WHERE a.StudentNUID = {nuid}
            ORDER BY a.DateSubmitted DESC
        '''
        # Execute query
        cursor = db.get_db().cursor()
        cursor.execute(query)
        applications = cursor.fetchall()

        current_app.logger.info(f"Applications fetched for NUID {nuid}: {applications}")

        return jsonify(applications), 200

    except Exception as e:
        current_app.logger.error(f"Error fetching applications for NUID {nuid}: {e}")
        return jsonify({"error": "Could not fetch applications"}), 500
