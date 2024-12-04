from flask import Blueprint
from flask import jsonify
from flask import make_response
from backend.db_connection import db

tickets = Blueprint('companies', __name__)

# ------------------------------------------------------------
# Route to view all tickets or filter by status/priority
@tickets.route('/companies', methods=['GET'])
# Get all the products from the database, package them up,
# and return them to the client
def get_tickets():
    query = '''
        
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


