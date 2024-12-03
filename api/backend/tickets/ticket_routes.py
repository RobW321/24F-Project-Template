from flask import Blueprint, request, jsonify, make_response, current_app
from backend.db_connection import db

ticket_management = Blueprint('ticket_management', __name__)

# ------------------------------------------------------------
# Route to view all tickets or filter by status/priority
@ticket_management.route('/tickets', methods=['GET'])
def view_tickets():
    status = request.args.get('status')
    priority = request.args.get('priority')

    query = 'SELECT * FROM Ticket'
    filters = []

    if status:
        filters.append(f"Status = '{status}'")
    if priority:
        filters.append(f"Priority = {priority}")

    if filters:
        query += ' WHERE ' + ' AND '.join(filters)

    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    tickets = cursor.fetchall()

    response = jsonify(tickets)
    response.status_code = 200
    return response


# ------------------------------------------------------------
# Route to reassign a ticket to a different employee
@ticket_management.route('/tickets/<int:ticket_id>/reassign', methods=['PUT'])
def reassign_ticket(ticket_id):
    data = request.json
    new_employee_id = data['employee_id']

    query = f'''
        UPDATE Ticket
        SET EmployeeID = {new_employee_id}
        WHERE TicketID = {ticket_id}
    '''
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response(f"Ticket {ticket_id} reassigned to employee {new_employee_id} successfully")
    response.status_code = 200
    return response


# ------------------------------------------------------------
# Route to edit a ticket's details
@ticket_management.route('/tickets/<int:ticket_id>', methods=['PUT'])
def edit_ticket(ticket_id):
    data = request.json
    fields = []

    # Optional fields to update
    if 'description' in data:
        fields.append(f"Description = '{data['description']}'")
    if 'status' in data:
        fields.append(f"Status = '{data['status']}'")
    if 'priority' in data:
        fields.append(f"Priority = {data['priority']}")
    if 'ticket_type' in data:
        fields.append(f"TicketType = '{data['ticket_type']}'")
    if 'student_nuid' in data:
        fields.append(f"StudentNUID = {data['student_nuid']}")

    if not fields:
        response = make_response("No fields provided to update")
        response.status_code = 400
        return response

    query = f'''
        UPDATE Ticket
        SET {', '.join(fields)}
        WHERE TicketID = {ticket_id}
    '''
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response(f"Ticket {ticket_id} updated successfully")
    response.status_code = 200
    return response
