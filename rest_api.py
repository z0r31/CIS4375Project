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
    return 'POST REQUEST WORKED'


app.run()
