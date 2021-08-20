from flask import Flask, jsonify, render_template, request, g
from config.Settings import Settings
import functools
import jwt


def login_required(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        token = request.headers.get('Authorization')
        print(token)

        auth = True
        # print(token.index("Bearer"))
        if token and token.index("Bearer") == 0:
            token = token.split(" ")[1]
        else:
            auth = False

        if auth:
            try:

                # decode
                payload = jwt.decode(token, Settings.secretKey, 'HS256')
                g.role = payload['role']
                g.userid = payload['userid']
            except Exception as err:
                print(err)
                auth = False

        if auth == False:
            output = {"Message": "Error JWT"}
            return jsonify(output), 403

        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator


def admin_required(func):
    @functools.wraps(func)
    def admin_decorator(*args, **kwargs):
        # Do something before
        # Apply your own code to do the necessary checks

        token = request.headers.get('Authorization')
        print(token)

        auth = True
        # print(token.index("Bearer"))
        if token and token.index("Bearer") == 0:
            token = token.split(" ")[1]
        else:
            auth = False
            output = {"Message": "False"}
            return jsonify(output), 403
        if auth:
            try:

                # decode
                payload = jwt.decode(token, Settings.secretKey, 'HS256')
                print(payload)
                if payload['role'] == "admin":

                    g.role = payload['role']
                    g.userid = payload['userid']
                else:

                    output = {"Message": "Error JWT"}
                    return jsonify(output), 403

            except Exception as err:
                print(err)
                auth = False

        if auth == False:
            output = {"Message": "Error JWT"}
            return jsonify(output), 403

        value = func(*args, **kwargs)
        # Do something after
        return value
    return admin_decorator
