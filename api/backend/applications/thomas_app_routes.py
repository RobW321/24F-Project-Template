from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

applications = Blueprint('applications', __name__)

@applications.route('/applications/thomas', methods=['GET'])
def get_thomas_applications():
        query = '''
            SELECT *
            FROM Application
            WHERE StudentNUID = 1003
            ORDER BY Priority DESC
        '''
        # get a cursor object from the database
        cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
        cursor.execute(query)

    # fetch all the data from the cursor
    # The cursor will return the data as a 
    # Python Dictionary
        theData = cursor.fetchall()

    # Create a HTTP Response object and add results of the query to it
    # after "jasonify"-ing it.
        response = make_response(jsonify(theData))
    # set the proper HTTP Status code of 200 (meaning all good)
        response.status_code = 200
    # send the response back to the client
        return response




