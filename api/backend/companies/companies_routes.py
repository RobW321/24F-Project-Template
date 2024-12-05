from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

companies = Blueprint('companies', __name__)

# ------------------------------------------------------------
# Route to view all tickets or filter by status/priority
@companies.route('/companies', methods=['GET'])
# Get all the products from the database, package them up,
# and return them to the client
def get_tickets():
    query = '''
        SELECT CompanyName,
        SponsorshipHistory
        FROM Company
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

@companies.route('/company', methods=['GET'])
# Get all the products from the database, package them up,
# and return them to the client
def get_company():
    query = '''
        SELECT *
        FROM Company
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

@companies.route('/sponsorships', methods=['GET'])
def get_companies_sponsorships():
    query = '''
        SELECT CompanyName, SponsorshipPercentage, VisaType
        FROM Company
        JOIN VisaSponsor ON Company.SponsorID = VisaSponsor.SponsorID
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return jsonify(data)

@companies.route('/deletebycompid', methods=['DELETE'])
def delete_specific_tickets():
    the_data = request.json
    current_app.logger.info(the_data)
    companyID = the_data['CompanyID']

    

    query = "DELETE FROM Company WHERE CompanyID = %s"
    
    current_app.logger.info(query)
    data = (companyID)
    


        # Execute the query with the parameter
    cursor = db.get_db().cursor()
    cursor.execute(query, data)  # Tuple is used even for a single parameter
    
    db.get_db().commit()
    response = make_response("Successfully deleted specific ticket")
    response.status_code = 200
    return response
    

@companies.route('/add', methods=['POST'])
def add_company():
    try:
        # Collect data from the request
        the_data = request.json
        current_app.logger.info(the_data)

        # Extract variables from request
        company_id = the_data['CompanyID']
        company_name = the_data['CompanyName']
        sponsor_id = the_data['SponsorID']
        industry = the_data['Industry']
        location = the_data['Location']

        # SQL query with placeholders
        query = '''
            INSERT INTO Company (CompanyID, CompanyName, Industry, Location, SponsorID)
            VALUES (%s, %s, %s, %s, %s)
        '''

        # Log query for debugging
        current_app.logger.info(f"Executing query: {query}")

        # Execute and commit the query
        cursor = db.get_db().cursor()
        cursor.execute(query, (company_id, company_name, industry, location, sponsor_id))
        db.get_db().commit()

        # Return a success response
        response = make_response(jsonify({"message": "Company added successfully"}))
        response.status_code = 201
        return response

    except Exception as e:
        current_app.logger.error(f"Error adding Company: {e}")
        return jsonify({"error": "Failed to add company"}), 500
    

@companies.route('/edit', methods=['PUT'])
def update_company():
    try:
        # Collect data from the request
        the_data = request.json
        current_app.logger.info(the_data)

        # Extract variables from the request
        company_name = the_data['CompanyName']
        industry = the_data['Industry']
        location = the_data['Location']
        companyID = the_data['CompanyID']


        # Construct the SQL query for updating the company
        query = '''
        UPDATE Company
        SET CompanyName = %s,
            Industry = %s,
            Location = %s
        WHERE CompanyID = %s
        '''

        # Log the query for debugging
        current_app.logger.info(f"Executing query: {query}")

        # Execute the query with parameters
        cursor = db.get_db().cursor()
        cursor.execute(query, (company_name, industry, location, companyID))
        db.get_db().commit()

        # Return a success response
        response = make_response(jsonify({"message": "Company updated successfully"}))
        response.status_code = 200
        return response

    except Exception as e:
        current_app.logger.error(f"Error updating company: {e}")
        return jsonify({"error": f"Failed to update company: {e}"}), 500
