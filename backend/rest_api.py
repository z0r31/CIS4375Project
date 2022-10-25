import flask
from flask import jsonify
from flask import request, make_response
from sql import create_connection
from sql import execute_query
from sql import execute_read_query

# setting up an application name
app = flask.Flask(__name__) # sets up the application
app.config["DEBUG"] = True # allows to show errors in browser

# default url without any routing as GET request
@app.route('/', methods=['GET']) 
def home():
    return "<h1> WELCOME! </h1>"

# this endpoint adds a new customer to the database table 
# using POST as the method type
@app.route('/api/addcustomer', methods=['POST'])
def add_customer():
    # using the get_json function to request data
    request_data = request.get_json()
    CountryID = request_data['CountryID']
    CustomerFirstName = request_data['CustomerFirstName']
    CustomerLastName = request_data['CustomerLastName']
    CustomerAddress = request_data['CustomerAddress']
    CustomerPhoneNumber = request_data['CustomerPhoneNumber']
    CustomerEmail = request_data['CustomerEmail']
    conn = create_connection("database-2.cg9pywfjykka.us-east-2.rds.amazonaws.com", "admin", "FutureTechnologySolutionsGroup9", "KPJDB")
    # this sql query was created to add the new customer
    sql = "INSERT INTO Customer(CountryID, CustomerFirstName, CustomerLastName, CustomerAddress, CustomerPhoneNumber, CustomerEmail) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (CountryID, CustomerFirstName, CustomerLastName, CustomerAddress, CustomerPhoneNumber, CustomerEmail)
    execute_query(conn, sql)
<<<<<<< Updated upstream
    return 'POST REQUEST WORKED'
=======
    return 'POST successful'


# route to manually update record to customer table
@app.route('/api/customer/update', methods=['PUT'])
def update_customer():
    # send PUT request in json format
    request_data = request.get_json()

    # information to get from payload
    new_CountryID =             request_data['CountryID']
    new_CustomerFirstName =     request_data['CustomerFirstName']
    new_CustomerLastName =      request_data['CustomerLastName']
    new_CustomerAddress =       request_data['CustomerAddress']
    new_CustomerPhoneNumber =   request_data['CustomerPhoneNumber']
    new_CustomerEmail =         request_data['CustomerEmail']
    new_CustomerID =            request_data['CustomerID']

    # establish connection to DB
    connection = get_connection()

    # query to add new record to table
    update_query = "UPDATE Customer SET CountryID = '{}', CustomerFirstName = '{}', CustomerLastName = '{}' " \
        "CustomerAddress = '{}', CustomerPhoneNumber = '{}', CustomerEmail = '{}' " \
        "WHERE CustomerID = '{}'".format(new_CountryID, new_CustomerFirstName, new_CustomerLastName, new_CustomerAddress, new_CustomerPhoneNumber, new_CustomerEmail, new_CustomerID)
    execute_query(connection, update_query)

    return "Update successful"



# route to read all data from country table
@app.route('/api/country', methods=['GET'])
def get_country():
    # create connection to DB and execute read query
    connection = get_connection()
    # read request return as a dictionary
    cursor = connection.cursor(dictionary=True)

    select_query = 'SELECT * FROM Country'
 
    # execute read query and save to result variable
    cursor.execute(select_query)
    result = cursor.fetchall()
 
    # append all results to result_json list
    results_json = []
    for row in result:
        results_json.append(row)

    return jsonify(results_json)



# route to add new record to return table
@app.route('/api/return/add', methods=['POST'])
def add_return():
    # send POST request in json format
    request_data = request.get_json()

    # information to get from payload
    # the date is handled automatically by the datetime function
    new_ReturnReason = request_data['ReturnReason']

    # establish connection to DB
    connection = get_connection()

    # query to add new record to table
    add_query = "INSERT INTO ReturnTable (ReturnDate, ReturnReason) VALUES ('{}','{}')".format(date.today(), new_ReturnReason)
    execute_query(connection, add_query)

    return "POST successful"

# route to read all data from ReturnTable table
@app.route('/api/return', methods=['GET'])
def get_return():
    # create connection to DB and execute read query
    connection = get_connection()
    # read request return as a dictionary
    cursor = connection.cursor(dictionary=True)

    select_query = 'SELECT * FROM ReturnTable'
 
    # execute read query and save to result variable
    cursor.execute(select_query)
    result = cursor.fetchall()
 
    # append all results to result_json list
    results_json = []
    for row in result:
        results_json.append(row)

    return jsonify(results_json)

# route to manually update record to return table
@app.route('/api/return/update', methods=['PUT'])
def update_return():
    # send PUT request in json format
    request_data = request.get_json()

    # information to get from payload
    new_ReturnReason =  request_data['ReturnReason']
    new_ReturnID =      request_data['ReturnID']

    # establish connection to DB
    connection = get_connection()

    # query to add new record to table
    update_query = "UPDATE ReturnTable SET ReturnReason = '{}' WHERE ReturnID = '{}'".format(new_ReturnReason,new_ReturnID)
    execute_query(connection, update_query)

    return "Update successful"


>>>>>>> Stashed changes

# this endpoint adds a new employee to the database table 
# using POST as the method type
@app.route('/api/addemployee', methods=['POST'])
def add_employee():
    # using the get_json function to request data
    request_data = request.get_json()
    CountryID = request_data['CountryID']
    EmployeeFirstName = request_data['EmployeeFirstName']
    EmployeeLastName = request_data['EmployeeLastName']
    EmployeeAddress = request_data['EmployeeAddress']
    EmployeePhoneNumber = request_data['EmployeePhoneNumber']
    EmployeeEmail = request_data['EmployeeEmail']
    HireDate = request_data['HireDate']
    conn = create_connection("database-2.cg9pywfjykka.us-east-2.rds.amazonaws.com", "admin", "FutureTechnologySolutionsGroup9", "KPJDB")
    # this sql query was created to add the new employee
    sql = "INSERT INTO Employee(CountryID, EmployeeFirstName, EmployeeLastName, EmployeeAddress, EmployeePhoneNumber, EmployeeEmail, HireDate) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (CountryID, EmployeeFirstName, EmployeeLastName, EmployeeAddress, EmployeePhoneNumber, EmployeeEmail, HireDate)
    execute_query(conn, sql)
    return 'POST REQUEST WORKED'

app.run()
