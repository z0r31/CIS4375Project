
#import flask library from Python 
import flask
#Import jsonify to make crud operation in JSON format
from flask import jsonify
from flask import request, make_response
#Import mysql from python to connect vscode to mysql server
from mysql.connector import connect
#Import three sql pre-made functions from sql.py file to establish connection, and execute queries.
from sql import create_connection
from sql import execute_query
from sql import execute_read_query
import random

#setting up an application name
app = flask.Flask(__name__) #sets up the application
app.config["DEBUG"] = True #allow to show errors in browser

#creating connection to Database stored in AWS using AWS credentials.
connection = create_connection("database-2.cg9pywfjykka.us-east-2.rds.amazonaws.com", "admin", "FutureTechnologySolutionsGroup9", "KPJDB")

@app.route('/customer', methods=['POST'])
def user():
    request_data = request.get_json()
    country_id = request_data['CountryID']
    new_Fname = request_data['CustomerFirstName']
    new_Lname = request_data['CustomerLastName']
    address = request_data['CustomerAddress']
    phonenumber = request_data['CustomerPhoneNumber']
    email = request_data['CustomerEmail']

    user_query = "INSERT INTO Customer(CountryID, CustomerFirstName, CustomerLastName, CustomerAddress, CustomerPhoneNumber, CustomerEmail ) values ('%s', '%s', '%s', '%s', '%s', '%s')" % (country_id, new_Fname, new_Lname, address, phonenumber, email)

    execute_query(connection, user_query)
    return 'Given Profile Successfully Created!!!'

'''
@app.route('/', methods=['GET'])
def home():
    return "<h1> Deciding Diner!!! </h1>"


@app.route('/getcustomer', methods=['GET'])
def alluser():
    request_data = request.get_json()
    usersql = "SELECT * FROM Customer"
    allusers = execute_read_query(connection, usersql) 
    return jsonify(allusers)

@app.route('/api/restaurant/all', methods=['GET'])
def allrestaurant():
    request_data = request.get_json()
    restaurantsql = "SELECT * FROM restaurant ORDER BY user_id"
    allrestaurants = execute_read_query(connection, restaurantsql)
    return jsonify(allrestaurants)


@app.route('/api/userrestaurant', methods=['GET'])
def userrestaurant_no_user_id():
    return 'Enter User ID'


@app.route('/api/userrestaurant/<user_id>', methods=['GET'])
def userrestaurant(user_id):
    request_data = request.get_json()
    usersql = "SELECT * FROM restaurant WHERE user_id=" + user_id
    alluserrestaurants = execute_read_query(connection, usersql) 
    count = len(alluserrestaurants)
    
    if count > 10:
        return "User have " + str(count) + " restaurants. Max limit is 10."
    elif count < 5:
        return "User have " + str(count) + " restaurants. Add at least 5."
    else:
        return jsonify(alluserrestaurants)

@app.route('/api/restaurant', methods=['POST'])
def restaurant():
    request_data = request.get_json()
    new_Rname = request_data['restaurant_name']
    new_Id = request_data['user_id']

    restaurant_query = "INSERT INTO restaurant(restaurant_name, user_id) values ('%s', '%s')" % (new_Rname, new_Id)

    execute_query(connection, restaurant_query)
    return 'Given Restaurant Successfully Added!!!'


@app.route('/api/deleteuser', methods=['DELETE'])
def deluser():
    request_data = request.get_json()
    user_ID = request_data['id']

    del_user_query = "DELETE FROM user WHERE id = '%s'" % (user_ID)
    execute_query(connection, del_user_query)
    return "Selected Profile Successfully Deleted!!!"

@app.route('/api/deleterestaurant', methods=['DELETE'])
def delrestaurant():
    request_data = request.get_json()
    restaurantid = request_data['restaurant_id']

    del_rest_query = "DELETE FROM restaurant WHERE restaurant_id = '%s'" % (restaurantid)
    execute_query(connection, del_rest_query)
    return "Selected Restaurant Successfully Deleted!!!"


@app.route('/api/userupdate', methods=['PATCH'])
def userupdate():
    request_data = request.get_json()
    updated_fname = request_data['first_name']
    updated_lname = request_data['last_name']
    user_ID = request_data['id']
    userupdate = "UPDATE user SET first_name = '%s', last_name = '%s' WHERE id = '%s'" % (updated_fname, updated_lname, user_ID)
    execute_query(connection, userupdate)
    return "Selected User Successfully Updated!!!"


@app.route('/api/restaurantupdate', methods=['PATCH'])
def restaurantupdate():
    request_data = request.get_json()
    updated_restaurantname = request_data['restaurant_name']
    restaurant_ID = request_data["restaurant_id"]
    restaurantupdate = "UPDATE restaurant SET restaurant_name = '%s' WHERE restaurant_id = '%s'" % (updated_restaurantname, restaurant_ID)
    execute_query(connection, restaurantupdate)
    return "Selected Restaurant Successfully Updated!!!"


@app.route('/api/random', methods=['GET'])
def randomrestaurant():
    request_data = request.get_json()
    randomInt=random.randint(1, 3)
    random_sql = """ select Restaurant.restaurant_name,GROUP_CONCAT(user.first_name) as  first_name
                     from 
                     (SELECT  restaurant_name
                     from 
                     restaurant
                     ORDER BY RAND() limit 1) as Restaurant,
                     (select first_name from user ORDER BY RAND() limit %s) as user """ %(randomInt)
    random_query = execute_read_query(connection, random_sql)
    return jsonify(random_query) 
    

'''
app.run()
