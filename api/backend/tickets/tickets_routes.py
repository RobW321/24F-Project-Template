from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

tickets = Blueprint('tickets', __name__)

# ------------------------------------------------------------
# Route to view all tickets or filter by status/priority
@tickets.route('/tickets', methods=['GET'])
# Get all the products from the database, package them up,
# and return them to the client
def get_tickets():
    query = '''
        SELECT 
            *
        FROM Ticket
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


#------------------------------------------------------------
# Update customer info for customer with particular userID
#   Notice the manner of constructing the query.
@tickets.route('/tickets/edit', methods=['PUT'])
def update_tickets():
    current_app.logger.info('PUT /tickets route')
    ticket_info = request.json
    cust_id = cust_info['id']
    first = cust_info['first_name']
    last = cust_info['last_name']
    company = cust_info['company']

    query = 'UPDATE customers SET first_name = %s, last_name = %s, company = %s where id = %s'
    data = (first, last, company, cust_id)
    cursor = db.get_db().cursor()
    r = cursor.execute(query, data)
    db.get_db().commit()
    return 'customer updated!'


