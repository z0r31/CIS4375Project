import flask
from flask import jsonify
from flask import request, make_response

from sql import create_connection
from sql import execute_query
from sql import execute_read_query
from sql import get_connection

from datetime import date


# setting up an application name
app = flask.Flask(__name__) # sets up the application
app.config["DEBUG"] = True # allows to show errors in browser

# default url without any routing as GET request
@app.route('/', methods=['GET']) 
def home():
    return "<h1> WELCOME! </h1>"



# route to read all data from Customer table
@app.route('/api/customer', methods=['GET'])
def get_customer():
    # create connection to DB and execute read query
    connection = get_connection()
    # read request return as a dictionary
    cursor = connection.cursor(dictionary=True)

    select_query = 'SELECT * FROM Customer'
 
    # execute read query and save to result variable
    cursor.execute(select_query)
    result = cursor.fetchall()
 
    # append all results to result_json list
    results_json = []
    for row in result:
        results_json.append(row)

    return jsonify(results_json)

# this endpoint adds a new customer to the database table 
# using POST as the method type
@app.route('/api/customer/add', methods=['POST'])
def add_customer():
    # using the get_json function to request data
    request_data = request.get_json()
    CountryID =             request_data['CountryID']
    CustomerFirstName =     request_data['CustomerFirstName']
    CustomerLastName =      request_data['CustomerLastName']
    CustomerAddress =       request_data['CustomerAddress']
    CustomerPhoneNumber =   request_data['CustomerPhoneNumber']
    CustomerEmail =         request_data['CustomerEmail']
    conn = create_connection("database-2.cg9pywfjykka.us-east-2.rds.amazonaws.com", "admin", "FutureTechnologySolutionsGroup9", "KPJDB")
    # this sql query was created to add the new customer
    sql = "INSERT INTO Customer(CountryID, CustomerFirstName, CustomerLastName, CustomerAddress, CustomerPhoneNumber, CustomerEmail) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (CountryID, CustomerFirstName, CustomerLastName, CustomerAddress, CustomerPhoneNumber, CustomerEmail)
    execute_query(conn, sql)
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



# route to read all data from Employee table
@app.route('/api/employee', methods=['GET'])
def get_employee():
    # create connection to DB and execute read query
    connection = get_connection()
    # read request return as a dictionary
    cursor = connection.cursor(dictionary=True)

    select_query = 'SELECT * FROM Employee'
 
    # execute read query and save to result variable
    cursor.execute(select_query)
    result = cursor.fetchall()
 
    # append all results to result_json list
    results_json = []
    for row in result:
        results_json.append(row)

    return jsonify(results_json)

# route to add new record to EMPLOYEE table
@app.route('/api/employee/add', methods=['POST'])
def add_employee():
    # send POST request in json format
    request_data = request.get_json()

    # information to get from payload
    new_CountryID =             request_data['CountryID']
    new_EmployeeAddress =       request_data['EmployeeAddress']
    new_EmployeeEmail =         request_data['EmployeeEmail']
    new_EmployeeFirstName =     request_data['EmployeeFirstName']
    new_EmployeeLastName =      request_data['EmployeeLastName']
    new_EmployeePhoneNumber =   request_data['EmployeePhoneNumber']
    new_HireDate =              request_data['HireDate']

    # establish connection to DB
    connection = get_connection()

    # query to add new record to table
    add_query = "INSERT INTO Employee (CountryID, EmployeeAddress, EmployeeEmail, EmployeeFirstName, EmployeeLastName, EmployeePhoneNumber, HireDate)" \
    "VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(new_CountryID, new_EmployeeAddress, new_EmployeeEmail, new_EmployeeFirstName, new_EmployeeLastName, new_EmployeePhoneNumber, new_HireDate)
    execute_query(connection, add_query)

    return "Employee added to database"

# route to manually update record to employee table
@app.route('/api/employee/update', methods=['PUT'])
def update_employee():
    # send PUT request in json format
    request_data = request.get_json()

    # information to get from payload
    new_CountryID =             request_data['CountryID']
    new_EmployeeAddress =       request_data['EmployeeAddress']
    new_EmployeeEmail =         request_data['EmployeeEmail']
    new_EmployeeFirstName =     request_data['EmployeeFirstName']
    new_EmployeeLastName =      request_data['EmployeeLastName']
    new_EmployeePhoneNumber =   request_data['EmployeePhoneNumber']
    new_HireDate =              request_data['HireDate']
    new_EmployeeID =            request_data['EmployeeID']

    # establish connection to DB
    connection = get_connection()

    # query to add new record to table
    update_query = "UPDATE Employee SET CountryID = '{}', EmployeeAddress = '{}', EmployeeEmail = '{}', " \
        "EmployeeFirstName = '{}', EmployeeLastName = '{}', EmployeePhoneNumber = '{}', HireDate = '{}' " \
        "WHERE EmployeeID = '{}'".format(new_CountryID, new_EmployeeAddress, new_EmployeeEmail, new_EmployeeFirstName, new_EmployeeLastName, new_EmployeePhoneNumber, new_HireDate, new_EmployeeID)
    execute_query(connection, update_query)

    return "Update successful"



# route to read all data from Invoice table
@app.route('/api/invoice', methods=['GET'])
def get_invoice():
    # create connection to DB and execute read query
    connection = get_connection()
    # read request return as a dictionary
    cursor = connection.cursor(dictionary=True)

    select_query = 'SELECT * FROM Invoice'
 
    # execute read query and save to result variable
    cursor.execute(select_query)
    result = cursor.fetchall()
 
    # append all results to result_json list
    results_json = []
    for row in result:
        results_json.append(row)

    return jsonify(results_json)

# route to add new record to Invoice table
@app.route('/api/invoice/add', methods=['POST'])
def add_invoice():
    # send POST request in json format
    request_data = request.get_json()

    # information to get from payload
    new_CustomerID =            request_data['CustomerID']
    new_EmployeeID =            request_data['EmployeeID']
    new_ShipToAddress =         request_data['ShipToAddress']
    new_DateToShip =            request_data['DateToShip']
    new_StoreName =             request_data['StoreName']
    new_PaymentType =           request_data['PaymentType']
    new_InvoiceDate =           request_data['InvoiceDate']
    new_InvoiceAmount =         request_data['InvoiceAmount']
    new_Tax =                   request_data['Tax']
    new_ShippingTotal =         request_data['ShippingTotal']
    new_TrackingID =            request_data['TrackingID']

    # establish connection to DB
    connection = get_connection()

    # query to add new record to table
    add_query = "INSERT INTO Invoice (CustomerID, EmployeeID, ShipToAddress, DateToShip, StoreName, PaymentType, InvoiceDate, InvoiceAmount, Tax, ShippingTotal, TrackingID)" \
    "VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(new_CustomerID, new_EmployeeID, new_ShipToAddress, new_DateToShip, new_StoreName, new_PaymentType, \
        new_InvoiceDate, new_InvoiceAmount, new_Tax, new_ShippingTotal, new_TrackingID)
    execute_query(connection, add_query)

    return "Invoice added to database"

# route to manually update record to Invoice table
@app.route('/api/invoice/update', methods=['PUT'])
def update_invoice():
    # send PUT request in json format
    request_data = request.get_json()

    # information to get from payload
    new_CustomerID =            request_data['CustomerID']
    new_EmployeeID =            request_data['EmployeeID']
    new_ShipToAddress =         request_data['ShipToAddress']
    new_DateToShip =            request_data['DateToShip']
    new_StoreName =             request_data['StoreName']
    new_PaymentType =           request_data['PaymentType']
    new_InvoiceDate =           request_data['InvoiceDate']
    new_InvoiceAmount =         request_data['InvoiceAmount']
    new_Tax =                   request_data['Tax']
    new_ShippingTotal =         request_data['ShippingTotal']
    new_TrackingID =            request_data['TrackingID']
    new_InvoiceID =             request_data['InvoiceID']

    # establish connection to DB
    connection = get_connection()

    # query to add new record to table
    update_query = "UPDATE Invoice SET CustomerID = '{}', EmployeeID = '{}', ShipToAddress = '{}', " \
        "DateToShip = '{}', StoreName = '{}', PaymentType = '{}', InvoiceDate = '{}', " \
        "InvoiceAmount = '{}',  Tax ='{}', ShippingTotal = '{}', TrackingID = '{}' " \
        "WHERE InvoiceID = '{}'".format(new_CustomerID, new_EmployeeID, new_ShipToAddress, new_DateToShip, new_StoreName, new_PaymentType, new_InvoiceDate, \
        new_InvoiceAmount, new_Tax, new_ShippingTotal, new_TrackingID, new_InvoiceID)
    execute_query(connection, update_query)

    return "Update successful"



# route to read all data from CustomerOrder table
@app.route('/api/customerorder', methods=['GET'])
def get_customerOrder():
    # create connection to DB and execute read query
    connection = get_connection()
    # read request return as a dictionary
    cursor = connection.cursor(dictionary=True)

    select_query = 'SELECT * FROM CustomerOrder'
 
    # execute read query and save to result variable
    cursor.execute(select_query)
    result = cursor.fetchall()
 
    # append all results to result_json list
    results_json = []
    for row in result:
        results_json.append(row)

    return jsonify(results_json)

# route to add new record to CustomerOrder table
@app.route('/api/customerorder/add', methods=['POST'])
def add_customerOrder():
    # send POST request in json format
    request_data = request.get_json()

    # information to get from payload
    new_CustomerID =                request_data['CustomerID']

    # establish connection to DB
    connection = get_connection()

    # query to add new record to table
    add_query = "INSERT INTO CustomerOrder (CustomerID, OrderDate)" \
    "VALUES ('{}','{}')".format(new_CustomerID, date.today())
    execute_query(connection, add_query)

    return "Order added to database"

# route to manually update record to CustomerOrder table
@app.route('/api/customerorder/update', methods=['PUT'])
def update_customerOrder():
    # send PUT request in json format
    request_data = request.get_json()

    # information to get from payload
    new_CustomerID =           request_data['CustomerID']
    new_CustomerOrderID =      request_data['CustomerOrderID']

    # establish connection to DB
    connection = get_connection()

    # query to add new record to table
    update_query = "UPDATE CustomerOrder SET CustomerID = '{}' " \
        "WHERE CustomerOrderID = '{}'".format(new_CustomerID, new_CustomerOrderID)
    execute_query(connection, update_query)

    return "Update successful"



# route to read all data from OrderInvoice table
@app.route('/api/orderinvoice', methods=['GET'])
def get_orderInvoice():
    # create connection to DB and execute read query
    connection = get_connection()
    # read request return as a dictionary
    cursor = connection.cursor(dictionary=True)

    select_query = 'SELECT * FROM OrderInvoice'
 
    # execute read query and save to result variable
    cursor.execute(select_query)
    result = cursor.fetchall()
 
    # append all results to result_json list
    results_json = []
    for row in result:
        results_json.append(row)

    return jsonify(results_json)

# route to add new record to OrderInvoice table
@app.route('/api/orderinvoice/add', methods=['POST'])
def add_orderInvoice():
    # send POST request in json format
    request_data = request.get_json()

    # information to get from payload
    new_InvoiceID =                request_data['InvoiceID']
    new_CustomerOrderID =          request_data['CustomerOrderID']
    new_ProductInventoryID =       request_data['ProductInventoryID']
    new_OrderPrice =               request_data['OrderPrice']
    new_OrderNotes =               request_data['OrderNotes']

    # establish connection to DB
    connection = get_connection()

    # query to add new record to table
    add_query = "INSERT INTO OrderInvoice (InvoiceID, CustomerOrderID, ProductInventoryID, OrderPrice, OrderNotes)" \
    "VALUES ('{}','{}','{}','{}','{}')".format(new_InvoiceID, new_CustomerOrderID, new_ProductInventoryID, new_OrderPrice, new_OrderNotes)
    execute_query(connection, add_query)

    return "Order line added to database"

# route to manually update record to OrderInvoice table
@app.route('/api/orderinvoice/update', methods=['PUT'])
def update_orderInvoice():
    # send PUT request in json format
    request_data = request.get_json()

    # information to get from payload
    new_OrderInvoiceID =           request_data['OrderInvoiceID']
    new_InvoiceID =                request_data['InvoiceID']
    new_CustomerOrderID =          request_data['CustomerOrderID']
    new_ProductInventoryID =       request_data['ProductInventoryID']
    new_OrderPrice =               request_data['OrderPrice']
    new_OrderNotes =               request_data['OrderNotes']

    # establish connection to DB
    connection = get_connection()

    # query to add new record to table
    update_query = "UPDATE OrderInvoice SET InvoiceID = '{}', CustomerOrderID = '{}', " \
        "ProductInventoryID = '{}', OrderPrice = '{}', OrderNotes = '{}' " \
        "WHERE OrderInvoiceID = '{}'".format(new_InvoiceID, new_CustomerOrderID, new_ProductInventoryID, new_OrderPrice, new_OrderNotes, new_OrderInvoiceID)
    execute_query(connection, update_query)

    return "Update successful"

app.run()
