from flask import Flask, jsonify, render_template, request
from model.User import User
from model.Category import Category
from model.Furniture import Furniture
app = Flask(__name__)


# GET all users
@app.route('/users', methods=['GET'])
def getUsers():
    try:
        users = User.getUsers()

        output = {"Users": users}
        return jsonify(output), 200
    except Exception as err:
        print(err)
        output = {"Message": "Error occurred."}
        return jsonify(output), 500

# Get 1 User based on userid supplied


@app.route('/users/<int:userid>', methods=['GET'])
def getOneUser(userid):
    try:
        users = User.getUserByUserid(userid)

        if len(users) > 0:
            output = {"Users": users}
            return jsonify(output), 200
        else:
            output = {"Users": ""}
            return jsonify(output), 404
    except Exception as err:
        print(err)
        output = {"Message": "Error occurred."}
        return jsonify(output), 500


# POST 1 new user - Insert
@app.route('/users', methods=['POST'])
def insertUser():
    try:
        # extract the incoming request data from user
        userData = request.json  # request.form.to_dict() ->if using html forms
        print(userData)
        # userid=userData['userid']
        username = userData['username']
        email = userData['email']
        role = userData['role']
        password = userData['password']

        # call the model to insert
        count = User.insertUser(username, email, role, password)

        output = {"Rows Inserted": count}
        return jsonify(output), 201
    except Exception as err:
        print(err)
        output = {"Message": "Error occurred."}
        return jsonify(output), 500


@app.route('/users/<int:userid>', methods=['PUT'])
def updateUser(userid):
    jsonBody = request.json
    print(jsonBody)

    count = User.updateUser(userid, jsonBody['email'], jsonBody['password'])

    if(count == 1):
        return '{"message": "User with id '+str(userid) + ' has been successfully updated!"}', 200
    else:
        return '{"message": "User with id '+str(userid) + ' does not exist!"}', 404


@app.route('/users/<int:userid>', methods=['DELETE'])
def deleteUser(userid):
    try:

        count = User.deleteUser(userid)
        output = {"Rows Affected": count}
        return jsonify(output), 200

    except Exception as err:
        print(err)
        output = {"Message": "Error occurred."}
        return jsonify(output), 500

# WS 1 - Get All Categories

# WS 2- Get furniture by categoryid
# Select * from furniture f,category c where ....


@app.route('/category')  # define the api route
def getAllCategory():
    try:
        jsonCat = Category.getAllCategory()
        jsonCat = {"Category": jsonCat}
        return jsonify(jsonCat), 200
    except Exception as err:
        print(err)
        return{}, 500


@app.route('/category/<int:catid>/furniture')  # define the api route
def getFurnitureByCat(catid):
    try:
        jsonCat = Furniture.getFurnitureByCat(catid)
        jsonCat = {"Furniture": jsonCat[(catid)-1]}
        return jsonify(jsonCat), 200

    except Exception as err:
        print(err)
        return{}, 500


if __name__ == '__main__':
    app.run(debug=True)  # start the flask app with default port 5000
