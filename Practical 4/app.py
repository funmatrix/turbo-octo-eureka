from mysql.connector import pooling
from model.User import


@app.route('/users', methods=['GET'])
def getUsers():
    try:
        users = User.getUsers()

        output = {"Users": users}
        return jsonify(output), 200
    except Exception as err:
        print(err)
        output = {"Message": "Error occured."}
        return jsonify(output), 500
