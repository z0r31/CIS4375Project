#import flask library from Python 
from http.client import OK
import logging
import flask
#Import jsonify to make crud operation in JSON format
from flask import jsonify
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS, cross_origin
from flask import request, make_response

#Import mysql from python to connect vscode to mysql server
from mysql.connector import connect
#Import three sql pre-made functions from sql.py file to establish connection, and execute queries.
from sql import create_connection
from sql import execute_query
from sql import execute_read_query
import random

from datetime import date

#setting up an application name
app = flask.Flask(__name__) #sets up the application
app.config["DEBUG"] = True #allow to show errors in browser
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

#creating connection to Database stored in AWS using AWS credentials.
connection = create_connection("database-2.cg9pywfjykka.us-east-2.rds.amazonaws.com", "admin", "FutureTechnologySolutionsGroup9", "KPJDB")



# default url without any routing as GET request
@app.route('/', methods=['GET']) 
def home():
    return "<h1> WELCOME! </h1>"



# route to read all data from Customer table
@app.route('/api/customer', methods=['GET'])
def get_customer():
    # create connection to DB and execute read query
    
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
@cross_origin(origin='*')
def add_customer():

    # using the get_json function to request data
    request_data = request.get_json()

    CountryID =             request_data['CountryID']
    CustomerFirstName =     request_data['CustomerFirstName']
    CustomerLastName =      request_data['CustomerLastName']
    CustomerAddress =       request_data['CustomerAddress']
    CustomerPhoneNumber =   request_data['CustomerPhoneNumber']
    CustomerEmail =         request_data['CustomerEmail']

    # this sql query was created to add the new customer
    sql = "INSERT INTO Customer(CountryID, CustomerFirstName, CustomerLastName, CustomerAddress, CustomerPhoneNumber, CustomerEmail) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (CountryID, CustomerFirstName, CustomerLastName, CustomerAddress, CustomerPhoneNumber, CustomerEmail)
    
    execute_query(connection, sql)

    return jsonify({'status':200})



# route to manually update record to customer table
@app.route('/api/customer/update', methods=['PUT'])
@cross_origin(origin='*')
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
    

    # query to add new record to table
    update_query = "UPDATE Customer SET CountryID = '{}', CustomerFirstName = '{}', CustomerLastName = '{}' " \
        ", CustomerAddress = '{}', CustomerPhoneNumber = '{}', CustomerEmail = '{}' " \
        "WHERE CustomerID = '{}'".format(new_CountryID, new_CustomerFirstName, new_CustomerLastName, new_CustomerAddress, new_CustomerPhoneNumber, new_CustomerEmail, new_CustomerID)
    print(update_query)
    execute_query(connection, update_query)

    return jsonify({'status':200})

@app.route('/api/getcustomer', methods=['GET'])
def allcustomer():
    usersql = "SELECT * FROM Customer"
    allcustomers = execute_read_query(connection, usersql) 
    return jsonify(allcustomers)

@app.route('/token', methods=['POST'])
@cross_origin(origin='*')
def getToken():
     return jsonify({'data': '5befc834-62f4-4281-a71b-35c9067d8686','status':200})

@app.route('/auth', methods=['POST'])
@cross_origin(origin='*')
def auth():
    request_data = request.get_json()
    email = request_data['username']
    password = request_data['password']
    usersql = "SELECT *,'5befc834-62f4-4281-a71b-35c9067d8686' as TOKEN FROM Customer where CustomerEmail='%s' and password='%s'" % (email,password)
    allcustomers = execute_read_query(connection, usersql) 
    return jsonify({'result': allcustomers,'status':200})


# Category Section
@app.route('/createCategory', methods=['POST'])
@cross_origin(origin='*')
def createCategory():
    request_data = request.get_json()
    categoryName = request_data['category']
    usersql = "INSERT INTO ProductCategory(ProductDescription) values ('%s')" % (categoryName)
    execute_query(connection, usersql)
    return jsonify({'status':200})

@app.route('/updateCategory', methods=['POST'])
@cross_origin(origin='*')
def updateCategory():
    request_data = request.get_json()
    categoryName = request_data['category']
    id = request_data['id_category']
    usersql = "UPDATE ProductCategory SET ProductDescription = '%s' WHERE ProductCategoryID = '%s'" % (categoryName,id)
    execute_query(connection, usersql)
    return jsonify({'status':200})

@app.route('/deleteCategory', methods=['DELETE'])
@cross_origin(origin='*')
def deleteCategory():
    request_data = request.get_json()
    id = request_data['id_category']
    usersql = "Delete From ProductCategory  WHERE ProductCategoryID = '%s'" % (id)
    execute_query(connection, usersql)
    return jsonify({'status':200})


@app.route('/categorys', methods=['GET'])
@cross_origin(origin='*')
def categorys():
    usersql = "SELECT * FROM ProductCategory"
    allCategories = execute_read_query(connection, usersql) 
    return jsonify({'results': allCategories,'status':200})

# End Category Section

#Materials
@app.route('/materials', methods=['GET'])
@cross_origin(origin='*')
def materials():
    usersql = "SELECT * FROM Material"
    materials = execute_read_query(connection, usersql) 
    return jsonify({'results': materials,'status':200})


#materials END

# Products CRUD
@app.route('/upload', methods = ['GET', 'POST'])
@cross_origin(origin='*')
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(f.filename)
      return jsonify({'status':200})
# END Products CRUD


# route to read all data from country table
@app.route('/api/country', methods=['GET'])
@cross_origin(origin='*')
def get_country():
  
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
    

    # query to add new record to table
    add_query = "INSERT INTO ReturnTable (ReturnDate, ReturnReason) VALUES ('{}','{}')".format(date.today(), new_ReturnReason)
    execute_query(connection, add_query)

    return "POST successful"

# route to read all data from ReturnTable table
@app.route('/api/return', methods=['GET'])
def get_return():
    # create connection to DB and execute read query
    
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

   

    # query to add new record to table
    update_query = "UPDATE ReturnTable SET ReturnReason = '{}' WHERE ReturnID = '{}'".format(new_ReturnReason,new_ReturnID)
    execute_query(connection, update_query)

    return "Update successful"



# route to read all data from Employee table
@app.route('/api/employee', methods=['GET'])
def get_employee():
  
    
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

   

    # query to add new record to table
    update_query = "UPDATE Employee SET CountryID = '{}', EmployeeAddress = '{}', EmployeeEmail = '{}', " \
        "EmployeeFirstName = '{}', EmployeeLastName = '{}', EmployeePhoneNumber = '{}', HireDate = '{}' " \
        "WHERE EmployeeID = '{}'".format(new_CountryID, new_EmployeeAddress, new_EmployeeEmail, new_EmployeeFirstName, new_EmployeeLastName, new_EmployeePhoneNumber, new_HireDate, new_EmployeeID)
    execute_query(connection, update_query)

    return "Update successful"



# route to read all data from Invoice table
@app.route('/api/invoice', methods=['GET'])
def get_invoice():
  
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


    # query to add new record to table
    update_query = "UPDATE CustomerOrder SET CustomerID = '{}' " \
        "WHERE CustomerOrderID = '{}'".format(new_CustomerID, new_CustomerOrderID)
    execute_query(connection, update_query)

    return "Update successful"



# route to read all data from OrderInvoice table
@app.route('/api/orderinvoice', methods=['GET'])
def get_orderInvoice():
   
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

  

    # query to add new record to table
    update_query = "UPDATE OrderInvoice SET InvoiceID = '{}', CustomerOrderID = '{}', " \
        "ProductInventoryID = '{}', OrderPrice = '{}', OrderNotes = '{}' " \
        "WHERE OrderInvoiceID = '{}'".format(new_InvoiceID, new_CustomerOrderID, new_ProductInventoryID, new_OrderPrice, new_OrderNotes, new_OrderInvoiceID)
    execute_query(connection, update_query)

    return "Update successful"



# route to read all data from ProductInventory table
@app.route('/api/productinventory', methods=['GET'])
def get_productInventory():

    # read request return as a dictionary
    cursor = connection.cursor(dictionary=True)

    select_query = 'SELECT ProductInventoryID, ProductCategoryID, MaterialID, ProductName, ProductDescription, Quantity, UnitPrice FROM ProductInventory'
 
    # execute read query and save to result variable
    cursor.execute(select_query)
    result = cursor.fetchall()
 
    # append all results to result_json list
    results_json = []
    for row in result:
        results_json.append(row)

    return jsonify(results_json)

# route to add new record to ProductInventory table
@app.route('/api/productinventory/add', methods=['POST'])
def add_productInventory():
    # send POST request in json format
    request_data = request.get_json()

    # information to get from payload
    new_ProductCategoryID =     request_data['ProductCategoryID']
    new_MaterialID =            request_data['MaterialID']
    new_ProductName =           request_data['ProductName']
    new_ProductDescription =    request_data['ProductDescription']
    new_Quantity =              request_data['Quantity']
    new_UnitPrice =             request_data['UnitPrice']


    # query to add new record to table
    add_query = "INSERT INTO ProductInventory (ProductCategoryID, MaterialID, ProductName, ProductDescription, " \
        "Quantity, UnitPrice) " \
    "VALUES ('{}','{}','{}','{}','{}','{}')".format(new_ProductCategoryID, new_MaterialID, new_ProductName, new_ProductDescription, new_Quantity, new_UnitPrice)
    execute_query(connection, add_query)

    return "Product added to database"

# route to manually update record to ProductInventory table
@app.route('/api/productinventory/update', methods=['PUT'])
def update_productInventory():
    # send PUT request in json format
    request_data = request.get_json()

    # information to get from payload
    new_ProductInventoryID =    request_data['ProductInventoryID']
    new_ProductCategoryID =     request_data['ProductCategoryID']
    new_MaterialID =            request_data['MaterialID']
    new_ProductName =           request_data['ProductName']
    new_ProductDescription =    request_data['ProductDescription']
    new_Quantity =              request_data['Quantity']
    new_UnitPrice =             request_data['UnitPrice']


    # query to add new record to table
    update_query = "UPDATE ProductInventory SET ProductCategoryID = '{}', " \
        "MaterialID = '{}', ProductName = '{}', ProductDescription = '{}',  Quantity = '{}', UnitPrice = '{}' " \
        "WHERE ProductInventoryID = '{}'".format(new_ProductCategoryID, new_MaterialID, new_ProductName, new_ProductDescription, new_Quantity, new_UnitPrice, new_ProductInventoryID)
    execute_query(connection, update_query)

    return "Update successful"



# route to read all data from Importing table
@app.route('/api/importing', methods=['GET'])
def get_importing():

    # read request return as a dictionary
    cursor = connection.cursor(dictionary=True)

    select_query = 'SELECT * FROM Importing'
 
    # execute read query and save to result variable
    cursor.execute(select_query)
    result = cursor.fetchall()
 
    # append all results to result_json list
    results_json = []
    for row in result:
        results_json.append(row)

    return jsonify(results_json)

# route to add new record to Importing table
@app.route('/api/importing/add', methods=['POST'])
def add_importing():
    # send POST request in json format
    request_data = request.get_json()

    # information to get from payload
    # checking for ProductInventoryID in the request
    if 'ProductInventoryID' in request_data:
        new_ProductInventoryID =    request_data['ProductInventoryID']

    # checking for OrderInvoice_ReturnID in the request
    if 'OrderInvoice_ReturnID' in request_data:
        new_OrderInvoice_ReturnID = request_data['OrderInvoice_ReturnID']

    new_ProductCategoryID =         request_data['ProductCategoryID']
    new_MaterialID =                request_data['MaterialID']
    new_Weight =                    request_data['Weight']
    new_ProductName =               request_data['ProductName']
    new_Description =               request_data['Description']
    new_ReworkStatus =              request_data['ReworkStatus']
    new_Notes =                     request_data['Notes']


    # query to add new record to table without ProductInventoryID and OrderInvoice_ReturnID
    if 'ProductInventoryID' not in request_data and 'OrderInvoice_ReturnID' not in request_data:
        add_query = "INSERT INTO Importing (ProductCategoryID, MaterialID, " \
            "Weight, ProductName, Description, ReworkStatus, Notes) " \
            "VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(new_ProductCategoryID, new_MaterialID, new_Weight, new_ProductName, new_Description, new_ReworkStatus, new_Notes)

    # query to add new record to table without OrderInvoice_ReturnID
    elif 'ProductInventoryID' in request_data and 'OrderInvoice_ReturnID' not in request_data:
        add_query = "INSERT INTO Importing (ProductInventoryID, ProductCategoryID, MaterialID, " \
            "Weight, ProductName, Description, ReworkStatus, Notes) " \
            "VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(new_ProductInventoryID, new_ProductCategoryID, new_MaterialID, new_Weight, new_ProductName, new_Description, new_ReworkStatus, new_Notes)
    
    # query to add new record to table without ProductInventoryID
    elif 'ProductInventoryID' not in request_data and 'OrderInvoice_ReturnID' in request_data:
        add_query = "INSERT INTO Importing (OrderInvoice_ReturnID, ProductCategoryID, MaterialID, " \
            "Weight, ProductName, Description, ReworkStatus, Notes) " \
            "VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(new_OrderInvoice_ReturnID, new_ProductCategoryID, new_MaterialID, new_Weight, new_ProductName, new_Description, new_ReworkStatus, new_Notes)
    
    # query to add new record to table with all fields
    else:
        add_query = "INSERT INTO Importing (ProductInventoryID, OrderInvoice_ReturnID, ProductCategoryID, MaterialID, " \
            "Weight, ProductName, Description, ReworkStatus, Notes) " \
            "VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(new_ProductInventoryID, new_OrderInvoice_ReturnID, new_ProductCategoryID, new_MaterialID, new_Weight, new_ProductName, new_Description, new_ReworkStatus, new_Notes)
    
    execute_query(connection, add_query)

    return "Product added to database"

# route to manually update record to Importing table
@app.route('/api/importing/update', methods=['PUT'])
def update_importing():
    # send PUT request in json format
    request_data = request.get_json()

    # information to get from payload
    # checking for ProductInventoryID in the request
    if 'ProductInventoryID' in request_data:
        new_ProductInventoryID =    request_data['ProductInventoryID']

    # checking for OrderInvoice_ReturnID in the request
    if 'OrderInvoice_ReturnID' in request_data:
        new_OrderInvoice_ReturnID = request_data['OrderInvoice_ReturnID']

    new_ProductCategoryID =         request_data['ProductCategoryID']
    new_MaterialID =                request_data['MaterialID']
    new_Weight =                    request_data['Weight']
    new_ProductName =               request_data['ProductName']
    new_Description =               request_data['Description']
    new_ReworkStatus =              request_data['ReworkStatus']
    new_Notes =                     request_data['Notes']
    new_ImportID =                  request_data['ImportID']

    # query to add new record to table without ProductInventoryID and OrderInvoice_ReturnID
    if 'ProductInventoryID' not in request_data and 'OrderInvoice_ReturnID' not in request_data:
        update_query = "UPDATE Importing SET ProductCategoryID = '{}', MaterialID = '{}',  Weight = '{}', ProductName = '{}', " \
            "Description = '{}', ReworkStatus = '{}', Notes = '{}' " \
            "WHERE ImportID = '{}'".format(new_ProductCategoryID, new_MaterialID, new_Weight, new_ProductName, new_Description, new_ReworkStatus, new_Notes, new_ImportID)

    # query to add new record to table without OrderInvoice_ReturnID
    elif 'ProductInventoryID' in request_data and 'OrderInvoice_ReturnID' not in request_data:
        update_query = "UPDATE Importing SET ProductInventoryID = '{}', ProductCategoryID = '{}', MaterialID = '{}',  Weight = '{}', ProductName = '{}', " \
            "Description = '{}', ReworkStatus = '{}', Notes = '{}' " \
            "WHERE ImportID = '{}'".format(new_ProductInventoryID, new_ProductCategoryID, new_MaterialID, new_Weight, new_ProductName, new_Description, new_ReworkStatus, new_Notes, new_ImportID)

    # query to add new record to table without ProductInventoryID
    elif 'ProductInventoryID' not in request_data and 'OrderInvoice_ReturnID' in request_data:
        update_query = "UPDATE Importing SET OrderInvoice_ReturnID = '{}', ProductCategoryID = '{}', MaterialID = '{}',  Weight = '{}', ProductName = '{}', " \
            "Description = '{}', ReworkStatus = '{}', Notes = '{}' " \
            "WHERE ImportID = '{}'".format(new_OrderInvoice_ReturnID, new_ProductCategoryID, new_MaterialID, new_Weight, new_ProductName, new_Description, new_ReworkStatus, new_Notes, new_ImportID)
    
    # query to add new record to table
    else:
        update_query = "UPDATE Importing SET ProductInventoryID = '{}', OrderInvoice_ReturnID = '{}', ProductCategoryID = '{}', MaterialID = '{}',  Weight = '{}', ProductName = '{}', " \
                "Description = '{}', ReworkStatus = '{}', Notes = '{}' " \
                "WHERE ImportID = '{}'".format(new_ProductInventoryID, new_OrderInvoice_ReturnID, new_ProductCategoryID, new_MaterialID, new_Weight, new_ProductName, new_Description, new_ReworkStatus, new_Notes, new_ImportID)    
   
    execute_query(connection, update_query)

    return "Update successful"



# route to read all data from OrderInvoice_Return table
@app.route('/api/orderinvoicereturn', methods=['GET'])
def get_orderInvoiceReturn():

    # read request return as a dictionary
    cursor = connection.cursor(dictionary=True)

    select_query = 'SELECT * FROM OrderInvoice_Return'
 
    # execute read query and save to result variable
    cursor.execute(select_query)
    result = cursor.fetchall()
 
    # append all results to result_json list
    results_json = []
    for row in result:
        results_json.append(row)

    return jsonify(results_json)

# route to add new record to OrderInvoice_Return table
@app.route('/api/orderinvoicereturn/add', methods=['POST'])
def add_orderInvoiceReturn():
    # send POST request in json format
    request_data = request.get_json()

    # information to get from payload
    new_ReturnID =          request_data['ReturnID']
    new_OrderInvoiceID =    request_data['OrderInvoiceID']

    # query to add new record to table
    add_query = "INSERT INTO OrderInvoice_Return (ReturnID, OrderInvoiceID) VALUES ('{}','{}')".format(new_ReturnID, new_OrderInvoiceID)
    
    execute_query(connection, add_query)

    return "Return added to database"

# route to manually update record to OrderInvoice_Return table
@app.route('/api/orderinvoicereturn/update', methods=['PUT'])
def update_orderInvoiceReturn():
    # send PUT request in json format
    request_data = request.get_json()

    # information to get from payload
    new_ReturnID =              request_data['ReturnID']
    new_OrderInvoiceID =        request_data['OrderInvoiceID']
    new_OrderInvoice_ReturnID = request_data['OrderInvoice_ReturnID']


    # query to add new record to table
    update_query = "UPDATE OrderInvoice_Return SET ReturnID = '{}', OrderInvoiceID = '{}' WHERE OrderInvoice_ReturnID = '{}'".format(new_ReturnID, new_OrderInvoiceID, new_OrderInvoice_ReturnID)
    
    execute_query(connection, update_query)

    return "Update successful"

# Products CRUD


@app.route('/products', methods=['GET'])
@cross_origin(origin='*')
def products():
    if (connection.is_connected()):
        print("Connected")
    else:
        connection.reconnect()
        print("Not connected")
    usersql = "SELECT ProductInventoryID,ProductCategoryID,MaterialID,ProductName,ProductDescription,Quantity,UnitPrice FROM ProductInventory"
    allproducts = execute_read_query(connection, usersql)
    return jsonify({'results': allproducts, 'status': 200})

@app.route('/search/<ProductCategoryID>', methods=['GET'])
@cross_origin(origin='*')
def search(ProductCategoryID):
    if (connection.is_connected()):
        print("Connected")
    else:
        connection.reconnect()
    usersql = "SELECT ProductInventoryID,ProductCategoryID,MaterialID,ProductName,ProductDescription,Quantity,UnitPrice FROM ProductInventory WHERE ProductCategoryID=" + ProductCategoryID
    allproducts = execute_read_query(connection, usersql)
    return jsonify({'results': allproducts, 'status': 200})


@app.route('/createProduct', methods=['POST'])
@cross_origin(origin='*')
def createProduct():
    request_data = request.get_json()

    # information to get from payload
    MaterialID = request_data['MaterialID']
    category_productId = request_data['category_productId']
    image_product = request_data['image_product']
    price_product = request_data['price_product']
    product_description = request_data['product_description']
    product_name = request_data['product_name']
    quantity = request_data['quantity']

    usersql = "INSERT INTO ProductInventory(ProductCategoryID,MaterialID,ProductName,ProductDescription,Quantity,UnitPrice)"\
        "VALUES ('{}','{}','{}','{}','{}','{}')".format(category_productId,
                                                        MaterialID, product_name, product_description, quantity, price_product)
    execute_query(connection, usersql)
    return jsonify({'status': 200})

# END Products CRUD

@app.route('/api/deleteCustomer', methods=['DELETE'])
@cross_origin(origin='*')
def deleteCustomer():
    request_data = request.get_json()
    id = request_data['CustomerID']
    usersql = "Delete From Customer  WHERE CustomerID = '%s'" % (id)
    execute_query(connection, usersql)
    return jsonify({'status':200})

app.run()
