import functools
from flask import Flask, jsonify, request, g
from config.Settings import Settings

import jwt
import re


def validateRegister2(func):
    @functools.wraps(func)
    def validate2(*args, **kwargs):
        print("validate register 2")
        username = request.json['username']
        email = request.json['email']
        role = request.json['role']
        password = request.json['password']

        patternUsername = re.compile('^[a-zA-Z0-9]+$')

        # simple email check
        # justin.monreal@sp.edu
        # justin_monreal@sp.edu
        patternEmail = re.compile('^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+@\w+\.\w+$')
        patternPassword = re.compile('^[a-zA-Z0-9]{8,}$')

        if(patternUsername.match(username) and patternEmail.match(email) and patternPassword.match(password) and (role.lower() == "admin" or role.lower() == "member" or role.lower() == "user")):
            print("Correct")
            return func(*args, **kwargs)

        else:
            # return response
            return jsonify({"Message": "Validation Failed!"}), 403

    return validate2


def login_required(func):
    @functools.wraps(func)
    def secure_login(*args, **kwargs):
        auth = True

        # retrieve authorization bearer token
        auth_header = request.headers.get('Authorization')
        if auth_header:
            # retrieve the JWT value without the Bearer
            auth_token = auth_header.split(" ")[1]
        else:
            auth_token = ''
            auth = False  # Failed check
        if auth_token:
            try:
                payload = jwt.decode(
                    auth_token, Settings.secretKey, algorithms=['HS256'])
                # print(payload)
                # update info in flask application context's g which lasts for one req/res cyycle
                g.userid = payload['userid']
                g.role = payload['role']

            except jwt.exceptions.InvalidSignatureError as err:
                print(err)
                auth = False  # Failed check

        if auth == False:
            # return response
            return jsonify({"Message": "Not Authorized!"}), 403

        return func(*args, **kwargs)

    return secure_login


def validateRegister(func):
    @functools.wraps(func)
    def validate(*args, **kwargs):
        return func(*args, **kwargs)
        print("old validateregister")

    return validate


def validateNumber(num):
    @functools.wraps(num)
    def numonly(*args, **kwargs):
        username = request.json['username']
        email = request.json['email']
        role = request.json['role']
        password = request.json['password']

        # patternUsername=re.compile('^[a-zA-Z0-9]+$')

        # simple email check
        # justin.monreal@sp.edu
        # justin_monreal@sp.edu
        #patternEmail = re.compile('^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+@\w+\.\w+$')
        patternPassword = re.compile('^[0-9]{8,}$')

        if(patternPassword.match(password) and (role.lower() == "admin" or role.lower() == "member" or role.lower() == "user")):
            print("Correct")
            return num(*args, **kwargs)

        else:
            # return response
            return jsonify({"Message": "Validation Failed!"}), 403

    return numonly
