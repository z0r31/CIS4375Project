import flask
from flask import jsonify
from flask import request, make_response
from sql import create_connection
from sql import execute_query
from sql import execute_read_query
from sql import get_connection

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
    return 'POST REQUEST WORKED'

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
    new_ReturnDate = request_data['ReturnDate']
    new_ReturnReason = request_data['ReturnReason']

    # establish connection to DB
    connection = get_connection()

    # query to add new record to table
    add_query = "INSERT INTO ReturnTable (ReturnDate, ReturnReason) VALUES ('{}','{}')".format(new_ReturnDate, new_ReturnReason)
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

app.run()
