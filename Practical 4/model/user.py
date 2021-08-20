from model.DatabasePool import DatabasePool


class User:

    @classmethod
    def

    def getUsers(cls):
        dbConn = DatabasePool.getConnection()
        cursor = dbConn.cursor(dictionary=True)

        sql = "select * from user"
        cursor.execute(sql)
        users = cursor.fetchall()
        return users

    @classmethod
    def getUsersByUserid(cls, userid):
        dbConn = DatabasePool.getConnection()
        cursor = dbConn.cursor(dictionary=True)

        sql = "select * from user where userid = ?"
        cursor.execute(sql)
        users = cursor.fetchall()
        return users
