from model.DatabasePool import DatabasePool
from config.Settings import Settings
import jwt
import datetime


class User:

    @classmethod
    def getUsers(cls):
        try:
            dbConn = DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)

            sql = "select * from user"
            cursor.execute(sql)
            users = cursor.fetchall()
            return users
        finally:
            dbConn.close()

    @classmethod
    def getUserByUserid(cls, userid):
        try:
            dbConn = DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)

            sql = "select * from user where userid=%s"
            cursor.execute(sql, (userid,))
            users = cursor.fetchall()
            return users
        finally:
            dbConn.close()

    @classmethod
    def insertUser(cls, username, email, role, password):
        try:
            dbConn = DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)

            sql = "insert into user(username,email,role,password) values(%s,%s,%s,%s)"
            cursor.execute(sql, (username, email, role, password))
            dbConn.commit()

            count = cursor.rowcount
            print(cursor.lastrowid)

            return count
        finally:
            dbConn.close()

    @classmethod
    def updateUser(cls, userid, email, password):
        try:
            dbConn = DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)

            sql = "update user set email=%s,password=%s where userid=%s"
            cursor.execute(sql, (email, password, userid))
            dbConn.commit()
            count = cursor.rowcount

            return count
        finally:
            dbConn.close()

    @classmethod
    def deleteUser(cls, userid):
        try:
            dbConn = DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)

            sql = "delete from user where userid=%s"
            cursor.execute(sql, (userid,))
            dbConn.commit()
            count = cursor.rowcount

            return count
        finally:
            dbConn.close()

    @classmethod
    def loginUser(cls, email, password):
        try:
            dbConn = DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)

            sql = "select * from user where email=%s and password=%s"
            cursor.execute(sql, (email, password))
            users = cursor.fetchone()

            # ---jwt encode to generate a token----
            if users == None:
                return ""
            else:
                role = users['role']
                userid = users['userid']
                username = users['username']
                jwtToken = jwt.encode({"role": role, "userid": userid, "username": username, "exp": datetime.datetime.utcnow(
                ) + datetime.timedelta(seconds=7200)}, Settings.secretKey, "HS256")

                print(jwtToken)
                return jwtToken

        finally:
            dbConn.close()

    @classmethod
    def AdminUser(cls, email, password, role):
        try:
            dbConn = DatabasePool.getConnection()
            cursor = dbConn.cursor(dictionary=True)

            sql = "select * from user where email=%s and password=%s and role = %s"
            cursor.execute(sql, (email, password, role))
            users = cursor.fetchone()

            # ---jwt encode to generate a token----
            if users == None:
                return ""
            else:
                role = users['role']
                userid = users['userid']
                username = users['username']
                jwtToken = jwt.encode({"role": role, "userid": userid, "username": username, "exp": datetime.datetime.utcnow(
                ) + datetime.timedelta(seconds=7200)}, Settings.secretKey, "HS256")

                print(jwtToken)
                return jwtToken
        finally:
            dbConn.close()
